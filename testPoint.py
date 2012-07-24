#! /usr/bin/env python
import os

from socket import gethostname
from time import gmtime, strftime

from interfaces.softsusy import (DoubleVector, MssmSoftsusy, QedQcd)
from interfaces.slha import SLHAfile
from interfaces.feynhiggs import run_feynhiggs
from modules import mcoutput
from modules import utils

def softsusy(tanb, sgnMu, mgut, mt, boundary_condition, vars):
    mcoutput.header('softsusy')
    inputs = DoubleVector(len(vars))
    for pos in range(len(vars)):
        inputs[pos] = vars[pos]
    r = MssmSoftsusy()

    oneset = QedQcd()
    oneset.setPoleMt(mt)
    oneset.setMass(3,mt)

    r.lowOrg( boundary_condition, mgut, inputs, sgnMu, tanb, oneset, False )

    slhafile = SLHAfile()
    slhafile.ReadFile("")

    r.lesHouchesAccordOutputStream( "sugra", inputs, sgnMu, tanb, 91.1875,
            1, mgut, False, slhafile.obj )

    return slhafile


def feynhiggs(filename):
    mcoutput.header('feynhiggs')
    run_feynhiggs(filename)
    return


def run_point(tanb, sgnMu, mgut, mt, boundary_condition, vars) :
    slhafile = softsusy(tanb, sgnMu, mgut, mt, boundary_condition, vars)

    t_now = strftime('%Y_%m_%d_%H_%M_%S', gmtime() )
    pipe_name = "/tmp/mc-{host}-{pid}-{time}".format(host=gethostname(),
            pid=os.getpid(), time=t_now)

    utils.pipe_to_function(pipe_name, slhafile, lambda: feynhiggs(pipe_name))


if __name__=="__main__" :
    vars = [ 100, 200, 0 ]
    boundary_condition = "sugraBcs"
    run_point(tanb=10., sgnMu=1, mgut=2e16, mt=173.2,
            boundary_condition=boundary_condition, vars=vars)
