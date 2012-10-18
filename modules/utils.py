import os
import time
import urllib2
import tarfile

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

def extract_tarfile(file, local_dir):
    output_dir = None
    if tarfile.is_tarfile(file):
        mode = 'r'
        if file.endswith('.gz'):
            mode += ':gz'
        tf = tarfile.open(file,mode)
        test_file = filter(lambda x: '/' in x, tf.getnames())[0]
        test_obj = '{l}/{f}'.format(l=local_dir, f=test_file)
        dir_end_pos = find_nth(test_obj, '/',2)
        output_dir = test_obj[:dir_end_pos]
        try:
            with open(test_obj) as f: pass
        except IOError as e:
            print("Extracting {f} to {p} ...".format(f=file, p=local_dir))
            tf.extractall(local_dir)
            print("  --> Done")
        tf.close()
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
    return output_object

