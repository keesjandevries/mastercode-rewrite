import os

def pipe_to_function(pipe_name, obj, function, debug=True):
    try:
        os.mkfifo(pipe_name)
    except OSError, e:
        print "Failed to create FIFO: %s" % e
        exit()

    child_pid = os.fork()
    if child_pid != 0 :
        f = open(pipe_name,'w')
        f.write(str(obj))
        f.close()
        os.waitpid(child_pid,0)
    else:
        if debug:
            import sys
            so = open("fh.stdout", 'w', 0)
            se = open("fh.stderr", 'w', 0)
            sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
            sys.stderr = os.fdopen(sys.stderr.fileno(), 'w', 0)
            os.dup2(so.fileno(), sys.stdout.fileno())
            os.dup2(se.fileno(), sys.stderr.fileno())
        function()
        os._exit(0)
