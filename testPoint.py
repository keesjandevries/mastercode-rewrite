#! /usr/bin/env python
import os

from socket import gethostname
from time import gmtime, strftime

from interfaces import softsusy
from interfaces import feynhiggs
from modules import utils


def run_point(tanb, sgnMu, mgut, mt, boundary_condition, vars) :
    slhafile = softsusy.run(tanb, sgnMu, mgut, mt, boundary_condition, vars)

    t_now = strftime('%Y_%m_%d_%H_%M_%S', gmtime() )
    pipe_name = "/tmp/mc-{host}-{pid}-{time}".format(host=gethostname(),
            pid=os.getpid(), time=t_now)

    utils.pipe_to_function(pipe_name, slhafile, lambda: feynhiggs.run(pipe_name))


if __name__=="__main__" :
    vars = [ 100, 200, 0 ]
    boundary_condition = "sugraBcs"
    run_point(tanb=10., sgnMu=1, mgut=2e16, mt=173.2,
            boundary_condition=boundary_condition, vars=vars)
