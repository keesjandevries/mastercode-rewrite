#! /usr/bin/env python
import os

from socket import gethostname
from time import gmtime, strftime

from interfaces.softsusy import (DoubleVector, MssmSoftsusy, QedQcd)
from interfaces.slha import SLHAfile
from interfaces.feynhiggs import run_feynhiggs
from modules import mcoutput
from modules import utils

def softsusy(m0, m12, A0, tanb, sgnMu, mgut):
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

    slhafile = SLHAfile()
    slhafile.ReadFile("")

    r.lesHouchesAccordOutputStream( "sugra", inputs, sgnMu, tanb, 91.1875,
            1, mgut, False, slhafile.obj )

    return slhafile


def feynhiggs(filename):
    mcoutput.header('feynhiggs')
    print "Fh looking for", filename
    run_feynhiggs(filename)
    return


def testPoint() :
    slhafile = softsusy(m0=100, m12=200, A0=0., tanb=10., sgnMu=1, mgut=2e16)

    t_now = strftime('%Y_%m_%d_%H_%M_%S', gmtime() )
    pipe_name = "/tmp/mc-{host}-{pid}-{time}".format(host=gethostname(),
            pid=os.getpid(), time=t_now)
    utils.pipe_to_function(pipe_name, slhafile, lambda: feynhiggs(pipe_name))


if __name__=="__main__" :
    testPoint()
