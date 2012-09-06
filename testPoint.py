#! /usr/bin/env python
import os

from socket import gethostname
from time import gmtime, strftime

from interfaces import softsusy as rge_calc
from interfaces import feynhiggs
from modules import utils

from interfaces import slha

def run_point(tanb, sgnMu, mgut, mt, boundary_condition, i_vars) :
    slhafile = rge_calc.run(tanb, sgnMu, mgut, mt, boundary_condition, i_vars)

    t_now = strftime('%Y_%m_%d_%H_%M_%S', gmtime() )
    pipe_name = "/tmp/mc-{host}-{pid}-{time}".format(host=gethostname(),
            pid=os.getpid(), time=t_now)

    utils.pipe_to_function(pipe_name, slhafile,
            lambda: feynhiggs.run(pipe_name))

    line_test = slha.SLHAline()
    line_test.set_index1(2000006)
    line_test.set_index2(5)
    line_test.set_comment('lulz')
    line_test.set_value(123.4)

    block_test = slha.SLHAblock('lol block')
    block_test.add_line(line_test)
    line_test.set_comment('ffff')
    line_test.set_value(567.8)
    block_test.add_line(line_test)
    slhafile.add_block(block_test)
    print slhafile
    print line_test.get_num_indices()
    print line_test.get_index1()
    print line_test.get_index2()
    print line_test.get_full_index()


if __name__=="__main__" :
    i_vars = [ 100, 200, 0 ]
    boundary_condition = "sugraBcs"
    run_point(tanb=10., sgnMu=1, mgut=2e16, mt=173.2,
            boundary_condition=boundary_condition, i_vars=i_vars)
