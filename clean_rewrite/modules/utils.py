import os
import time

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
    os.waitpid(child_pid,0)
