import os
import time
import urllib2
import tarfile
import pickle
import hashlib

from socket import gethostname
from time import gmtime, strftime

def show_header(header, sub=''):
    print header, sub
    total_len = len(header) + len(sub)
    block = "*"*(total_len+4 if not sub else total_len+6)
    print block
    print "* {h}{s} *".format(h=header, s=(': '+sub if sub else ''))
    print block

def unique_str():
    t_now = strftime('%Y_%m_%d_%H_%M_%S', gmtime() )
    ustr = "{host}-{pid}-{time}".format(host=gethostname(),
            pid=os.getpid(), time=t_now)
    return ustr

def pipe_to_function(pipe_name, obj, function):
    try:
        os.mkfifo(pipe_name)
    except OSError, e:
        print("Failed to create FIFO: %s" % e)
        exit()

    child_pid = os.fork()
    if child_pid == 0 :
    # child process
        pipeout = os.open(pipe_name, os.O_WRONLY)
        os.write(pipeout, str(obj))
        os.close(pipeout)
        os._exit(child_pid)
    else:
    # parent process
        function_out = function()
        os.unlink(pipe_name)
        os.waitpid(child_pid,0)
        return function_out

def make_file_from_pipe(pipe_name):
    pipe_in = open(pipe_name,'r').read()
    new_filename = pipe_name+"_P"
    print>>open(new_filename,'w'), pipe_in
    return new_filename

def rm(filename):
    try:
        with open(filename) as f: pass
        os.remove(filename)
    except IOError as e:
        print "rm: File {0} does not exist"

def fetch_url(target, local_path):
    success = False
    try:
        f = urllib2.urlopen(target)
        print("Downloading {0} ...".format(target))
        local_file = open(local_path,'wb')
        local_file.write(f.read())
        local_file.close()
        print("  --> Done")
        success = True
    except urllib2.HTTPError, e:
        print("HTTP Error:", e.code, target)
    except urllib2.URLError, e:
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
        raise IOError, "{f} is not a tar file".format(f=filename)
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
    f = open(filename, 'w')
    pickle.dump(obj,f)

def open_pickled_file(filename):
    f = open(filename,'r')
    return pickle.load(f)
