#! /usr/bin/env python2
import os

from collections import OrderedDict

from interfaces import softsusy
from interfaces import feynhiggs, micromegas, superiso, bphysics, lspscat
from modules import utils

from interfaces import slhalib as slhamodule
from interfaces.slhalib import SLHA

slha_generator = softsusy
slha_modifiers = [feynhiggs]
predictors = slha_modifiers + [micromegas, superiso, bphysics, lspscat]

def run_point(model, **inputs):
    utils.show_header(slha_generator.name)
    slhafile = SLHA(slha_generator.run(model, **inputs))

    predictor_output = OrderedDict()
    for predictor in predictors:
        utils.show_header(predictor.name)
        predictor_output.update(slhamodule.send_to_predictor(slhafile,
            predictor, True if predictor in slha_modifiers else False))

    for predictor, obs in predictor_output.iteritems():
        print
        print predictor
        print "="*len(predictor)
        x = max([len(n) for n,_ in obs.iteritems()])
        f_str = "{{n:{x}}} = {{p}}".format(x=x)
        for name,value in obs.iteritems():
            print f_str.format(n=name, p=value)

    #print slhafile

    #print>>open('slhas/testPoint_output_fh.slha','w'), slhafile
    #utils.pickle_object(slhafile, 'slhas/testPoint_output.pickled')
    #unpickled = utils.open_pickled_file('slhas/testPoint_output.pickled')
    #print unpickled


if __name__=="__main__" :
    model = 'cMSSM'
    input_vars = { 'm0': 100, 'm12': 200, 'A0': 0, 'tanb':10., 'sgnMu':1 }
    other_vars = { 'mt': 173.2, 'mgut': 2e16, }
    m_vars = dict(input_vars.items() + other_vars.items())
    run_point(model=model, **m_vars)
