#! /usr/bin/env python
import os

from socket import gethostname
from time import gmtime, strftime

from interfaces import softsusy as rge_calc
from interfaces import feynhiggs, micromegas, superiso
from modules import utils

from interfaces import slha

def run_point(tanb, sgnMu, mgut, mt, boundary_condition, i_vars) :
    slhafile = rge_calc.run(tanb, sgnMu, mgut, mt, boundary_condition, i_vars)

    t_now = strftime('%Y_%m_%d_%H_%M_%S', gmtime() )
    pipe_name = "/tmp/mc-{host}-{pid}-{time}".format(host=gethostname(),
            pid=os.getpid(), time=t_now)

    predictors = {
            'FeynHiggs': feynhiggs,
            'Micromegas': micromegas,
            'SuperISO': superiso,
            }
    predictor_output = {}
    for name,predictor in predictors.iteritems():
        out = utils.pipe_to_function(pipe_name, slhafile,
                lambda: predictor.run([pipe_name, "slha/test.slha"][0]))
        predictor_output[name] = predictor.get_values(out)

    for block_name, values in predictor_output.iteritems():
        slhafile.add_values(block_name, values)

    print>>open('slhas/testPoint_output.slha','w'), slhafile
    utils.pickle_object(slhafile, 'slhas/testPoint_output.pickled')
    unpickled = utils.open_pickled_file('slhas/testPoint_output.pickled')
    print unpickled


if __name__=="__main__" :
    i_vars = [ 100, 200, 0 ]
    boundary_condition = "sugraBcs"
    run_point(tanb=10., sgnMu=1, mgut=2e16, mt=173.2,
            boundary_condition=boundary_condition, i_vars=i_vars)
