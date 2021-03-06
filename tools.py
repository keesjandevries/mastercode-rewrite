import os
import sys
import time
import select
import urllib.request
import urllib.error
import tarfile
import pickle
import hashlib
import importlib

from socket import gethostname
from time import gmtime, strftime
from ctypes import Structure, c_double
from collections import OrderedDict

class c_complex(Structure):
    _fields_ = [('re', c_double), ('im', c_double)]

def ctypes_field_values(obj, title,error=None):
    d = OrderedDict([(attr, getattr(obj,attr)) for (attr, a_type) in
        obj._fields_])
    for (attr, a_type) in obj._fields_:
        if 'ctypes' in str(a_type._type_):
            c_obj = getattr(obj, attr)
            d[attr] = c_obj[:]
    if error is not None:
        d['error']=error
    return {(title,key):val for (key,val) in d.items() }

def import_predictor_modules(predictors):
    # FIXME: secure with "try: " statements
    predictor_modules={}
    predictor_modules['spectrum_generator']=importlib.import_module(predictors['spectrum_generator'])
    predictor_modules['spectrum_modifiers']=[]
    for modifier in predictors['spectrum_modifiers']:
        predictor_modules['spectrum_modifiers'].append(importlib.import_module(modifier))
    predictor_modules['predictors']=[]
    for predictor in predictors['predictors']:
        predictor_modules['predictors'].append(importlib.import_module(predictor))
    return predictor_modules

def is_int(s):
    try:
        i = int(s)
    except ValueError:
        return False
    else:
        return True

def ansi_bold(s):
    return "\033[1m{0}\033[0m".format(s)

def show_header(header, sub=''):
    total_len = len(header) + len(sub)
    block = "*"*(total_len+4 if not sub else total_len+6)
    print(block)
    print("* {h}{s} *".format(h=header, s=(': '+sub if sub else '')))
    print(block)

def unique_filename(dir_name=None):
    unique_string=unique_str(2)
    if not dir_name:
        dir_name='/tmp/'
    unq_filename= '{}/mc-{}'.format(dir_name,unique_string)
    return unq_filename

def unique_str(depth=1):
    t_now = strftime('%Y_%m_%d_%H_%M_%S', gmtime() )
    function_name=os.path.splitext(os.path.split(sys._getframe(depth).f_code.co_filename)[1])[0] # to only keep the name without .py
    ustr = "{host}-{pid}-{time}-{fname}".format(host=gethostname(),
            pid=os.getpid(), time=t_now,fname=function_name)
    return ustr

#def setup_pipe(reader, writer, pipe_name=None):
#    if pipe_name is None:
#        pipe_name = "/tmp/mc-{u}".format(u=unique_str())
#    try:
#        os.mkfifo(pipe_name)
#    except OSError as e:
#        print("Failed to create FIFO: %s" % e)
#        exit()
#
#    child_pid = os.fork()
#    if child_pid == 0 :
#    # child process
#        reader(pipe_name)
#        os._exit(child_pid)
#    else:
#    # parent process
#        output = writer(pipe_name)
#        os.unlink(pipe_name)
#        os.waitpid(child_pid,0)
#        return output


def pipe_object_to_function(pipe_name,obj, function, args=[], kwargs={} ):
    #We should not use hard coded directories
#    if pipe_name is None:
#        pipe_name = "/tmp/mc-{u}".format(u=unique_str())
    args.insert(0,pipe_name)
    try:
        os.mkfifo(pipe_name)
    except OSError as e:
        print("Failed to create FIFO: {e}".format(e=e))
        exit()

    child_pid = os.fork()
    if child_pid == 0 :
    # child process
        pipeout = os.open(pipe_name, os.O_WRONLY | os.O_CREAT)
        os.write(pipeout, bytes(str(obj), 'ascii'))
        os.close(pipeout)
        os._exit(child_pid)
    else:
    # parent process
        function_out = function(*args,**kwargs)
        os.unlink(pipe_name)
        os.waitpid(child_pid,0)
        return function_out

def check_pipe(pipe):
    r, _, _ = select.select([pipe], [], [], 0)
    return bool(r)

def read_pipe(pipe):
    out = ''
    while check_pipe(pipe):
        out += os.read(pipe, 1024).decode('utf-8')
    return out

def make_file_from_pipe(pipe_name):
    pipe_in = open(pipe_name,'r').read()
    new_filename = pipe_name+"_P"
    with open(new_filename,'w') as f:
        f.write(pipe_in)
    return new_filename

def rm(filename):
    try:
        with open(filename) as f: pass
        os.remove(filename)
    except IOError as e:
        print("rm: File {0} does not exist")

def fetch_url(target, local_path):
    success = False
    try:
        f = urllib.request.urlopen(target)
        print("Downloading {0} ...".format(target))
        local_file = open(local_path,'wb')
        local_file.write(f.read())
        local_file.close()
        print("  --> Done")
        success = True
    except urllib.error.HTTPError as e:
        print("HTTP Error:", e.code, target)
    except urllib.error.URLError as e:
        print("URL Error:", e.reason, target)
    return success

def md5_matches(filename, checksum):
    checker = hashlib.md5()
    checker.update(open(filename,'r').read())
    return checker.hexdigest() == checksum

def extract_tarfile(filename, local_dir):
    output_dir = None
    if tarfile.is_tarfile(filename):
        mode = 'r'
        if filename.endswith('gz'):
            mode += ':gz'
        tf = tarfile.open(filename,mode)
        test_file = filter(lambda x: '/' in x, tf.getnames())[0]
        test_obj = '{l}/{f}'.format(l=local_dir, f=test_file)
        dir_end_pos = find_nth(test_obj, '/',2)
        output_dir = test_obj[:dir_end_pos]
        try:
            with open(test_obj) as f: pass
        except IOError as e:
            print("Extracting {f} to {p} ...".format(f=filename, p=local_dir))
            tf.extractall(local_dir)
            print("  --> Done")
        tf.close()
    else:
        raise IOError("{f} is not a tar file".format(f=filename))
    return output_dir

def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start

def extract_values(output_object):
    values = {}
    for name in dir(output_object):
        if name[0] != "_":
            values[name] = getattr(output_object,name)
    return values

def pickle_object(obj, filename):
    f = open(filename, 'wb')
    pickle.dump(obj,f)
    f.close()
    print('File saved to :' , filename)

def open_pickled_file(filename):
    f = open(filename,'r')
    return pickle.load(f)

def get_ctypes_streams(func, args=[], kwargs={}):
    sys.stdout.write(' \b')
    sys.stdout.flush()
    pipe_out, pipe_in = os.pipe()
    stdout = os.dup(1)
    os.dup2(pipe_in, 1)
    ret = func(*args, **kwargs)
    os.dup2(stdout, 1)
    p_stdout = read_pipe(pipe_out)
    os.close(pipe_out)
    os.close(pipe_in)
    os.close(stdout)
    return (ret, p_stdout)

class RedirectStdStreams(object):
    def __init__(self, stdout=None, stderr=None):
        self._stdout = stdout or sys.stdout
        self._stderr = stderr or sys.stderr

    def __enter__(self):
        self.old_stdout, self.old_stderr = os.dup(1), os.dup(2)
        self.old_stdout.flush(); self.old_stderr.flush()
        sys.stdout, sys.stderr = self._stdout, self._stderr

    def __exit__(self, exc_type, exc_value, traceback):
        self._stdout.flush(); self._stderr.flush()
        sys.stdout = self.old_stdout
        sys.stderr = self.old_stderr

def set_obj_inputs_and_defaults(obj,inputs={},defaults={}):
    #FIXME: this could be improved: not sure if we need to copy 
    # and we may want to check for fields in the structure
    if inputs is None:
        inputs={}
    values=defaults.copy()
    values.update(inputs)
    for attr, value in values.items():
        setattr(obj,attr,value)

