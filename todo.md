## General

* abstract out our nice "run\_point" app into :
    - [slha\_generator, slha\_modifiers, slha\_additions]
* slha class just used as intermediary: want slha->dict and dict->sql db

## SLHA

* Bug fix cause of MX scale from softsusy
* Bug fix: capitalizing everything: maybe implement in python instead (mH and
  MH)
* Attempt to implement SLHAlib from FeynHiggs:
    - choose to pass around slhadata and then import SLHAdefs.h to access values
      by name.
    - adds depedency of SLHAlib to the project, but this is easily sourced
    - minimizes our file read time.  There are still those that need to read
      files, but that can be done quite easily (SLHAWrite(...))
    - move slha.{py,cc} to slha\_jad.{py,cc} and have slhalib.{py,cc}.
    - We can have a new version of `pipe\_to_\_function` which looks like
        ```python
        def pipe_to_function(reader, writer):
            pid = os.fork()
            if pid == 0: #child
                reader()
                os._exit()
            else:
                writer()
                os.WAIT_PID(pid)
        ```
        here we need to know that the reader and writer and wrapped up properly
        so that they're reading the correct file name e.g.
        ```python
        reader = lambda: SLHARead('example.slha')
        writer = labmda: SLHAWrite('example.slha', slhadata)
        ```
## FeynHiggs

* find out why PrecObs\_\* don't get filled (are these SLHA only: if so how do
  you get bsgamma etc.)

## bphysics and POPE

* write c-fortran interface for these.
