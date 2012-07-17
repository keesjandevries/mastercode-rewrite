#! /usr/bin/env python
import os

from socket import gethostname
from time import gmtime, strftime

from interfaces.softsusy import (DoubleVector, MssmSoftsusy, QedQcd)
from interfaces.slha import SLHAfile
from interfaces.feynhiggs import run_feynhiggs
from modules import mcoutput

def softsusy(m0, m12, A0, tanb, sgnMu, mgut, outputfile=None):
    mcoutput.header('softsusy')
    inputs = DoubleVector(3)
    inputs[0] = m0
    inputs[1] = m12
    inputs[2] = A0

    r = MssmSoftsusy()

    oneset = QedQcd()
    oneset.setPoleMt(173.2)
    oneset.setMass(3,173.2)

    r.lowOrg( "sugraBcs", mgut, inputs, sgnMu, tanb, oneset, False )
    if outputfile is None:
        print "Printing to stdout"
        r.lesHouchesAccordOutput( "sugra", inputs, sgnMu, tanb, 91.1875, 1,
                mgut, False )
    else:
        print "Printing to slhafile"
        slhafile = SLHAfile()
        slhafile.ReadFile("")

        r.lesHouchesAccordOutputStream( "sugra", inputs, sgnMu, tanb, 91.1875,
                1, mgut, False, slhafile.obj )

        f = open(outputfile,'w')
        f.write(str(slhafile))
        #print >> f, str(slhafile)
        f.close()


def feynhiggs(filename):
    mcoutput.header('feynhiggs')
    run_feynhiggs(filename)


def testPoint() :
    t_now = strftime('%Y_%m_%d_%H_%M_%S', gmtime() )
    pipe_name = "/tmp/mc-{host}-{pid}-{time}".format(host=gethostname(),
            pid=os.getpid(), time=t_now)
    try:
        os.mkfifo(pipe_name)
    except OSError, e:
        print "Failed to create FIFO: %s" % e
    else:
        pid = os.fork()
        if pid != 0:
            softsusy(m0=100, m12=200, A0=0., tanb=10., sgnMu=1, mgut=2e16,
                    outputfile=pipe_name)
        else:
            import sys
            so = open("fh.stdout", 'w', 0)
            se = open("fh.stderr", 'w', 0)
            sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
            sys.stderr = os.fdopen(sys.stderr.fileno(), 'w', 0)
            os.dup2(so.fileno(), sys.stdout.fileno())
            os.dup2(se.fileno(), sys.stderr.fileno())

            # this code does get executed but FH seems to die (imagine related to pipes)
            run_feynhiggs(pipe_name)

        os.unlink(pipe_name)

if __name__=="__main__" :
    testPoint()
