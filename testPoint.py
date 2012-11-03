#! /usr/bin/env python
import os

from collections import OrderedDict

from interfaces import softsusy as rge_calc
from interfaces import feynhiggs, micromegas, superiso
from modules import utils

from interfaces import slha

models = {
        'cMSSM': {
            'generator': ['softsusy'][0],
            'inputs': ['m0', 'm12', 'a0', 'tanb', 'sgnMu'],
            'fixed_vars': ['mgut', 'mt'],
            }
        }

predictors = [feynhiggs, micromegas, superiso]

def run_point(tanb, sgnMu, mgut, mt, model, i_vars) :
    slhafile = rge_calc.run(tanb, sgnMu, mgut, mt, model, i_vars)
    #slha.process_slhafile(slhafile)
    pipe_name = "/tmp/mc-{u}".format(u=utils.unique_str())

    predictor_output = OrderedDict()
    for predictor in predictors:
        predictor_output.update(utils.pipe_to_function(pipe_name, slhafile,
                lambda: predictor.run([pipe_name, "slha/test.slha"][0])))

    for block_name, values in predictor_output.iteritems():
        slhafile.add_values(block_name, values)

    print>>open('slhas/testPoint_output.slha','w'), slhafile
    utils.pickle_object(slhafile, 'slhas/testPoint_output.pickled')
    unpickled = utils.open_pickled_file('slhas/testPoint_output.pickled')
    print unpickled


if __name__=="__main__" :
    model = 'cMSSM'
    i_vars = [ 100, 200, 0 ]
    boundary_condition = "sugraBcs"
    run_point(tanb=10., sgnMu=1, mgut=2e16, mt=173.2,
            model=model, i_vars=i_vars)
