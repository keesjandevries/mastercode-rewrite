import os
import time
import urllib2
import tarfile

def pipe_to_function(pipe_name, obj, function):
    try:
        os.mkfifo(pipe_name)
    except OSError, e:
        print "Failed to create FIFO: %s" % e
        exit()

    child_pid = os.fork()
    if child_pid == 0 :
    # child process
        function()
    else:
    # parent process
        pipeout = os.open(pipe_name, os.O_WRONLY)
        os.write(pipeout, str(obj))
        os.close(pipeout)
        os.unlink(pipe_name)
        print "CLOSED PIPE"
        os.waitpid(child_pid,0)

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

def extract_tarfile(file, local_path):
    print file, local_path
    success = True
    if tarfile.is_tarfile(file):
        mode = 'r'
        if file.endswith('.gz'):
            mode += ':gz'
        tf = tarfile.open(file,mode)
        tf.extractall(local_path)
        tf.close()
    else:
        success = False
