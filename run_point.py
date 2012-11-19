#! /usr/bin/env python2
import os

from collections import OrderedDict

from interfaces import softsusy
from interfaces import feynhiggs, micromegas, superiso
from modules import utils

from interfaces import slhaclass as slhamodule
from interfaces.slhaclass import SLHAfile as slhaobj

slha_generator = softsusy
slha_modifiers = [feynhiggs]
predictors = [feynhiggs, micromegas, superiso]

def run_point(model, **inputs):
    utils.show_header(slha_generator.name)
    slhafile = slhaobj(slha_generator.run(model, **inputs))
    #slha.process_slhafile(slhafile)

    predictor_output = OrderedDict()
    for predictor in predictors:
        utils.show_header(predictor.name)
        predictor_output.update(slhamodule.send_to_predictor(slhafile,
            predictor))
            #predictor, True if predictor in slha_modifiers else False))

    for block_name, values in predictor_output.iteritems():
        slhafile.add_values(block_name, values)

    #print>>open('slhas/testPoint_output.slha','w'), slhafile
    #utils.pickle_object(slhafile, 'slhas/testPoint_output.pickled')
    #unpickled = utils.open_pickled_file('slhas/testPoint_output.pickled')
    #print unpickled


if __name__=="__main__" :
    model = 'cMSSM'
    input_vars = { 'm0': 100, 'm12': 200, 'A0': 0, 'tanb':10., 'sgnMu':1 }
    other_vars = { 'mt': 173.2, 'mgut': 2e16, }
    m_vars = dict(input_vars.items() + other_vars.items())
    run_point(model=model, **m_vars)
