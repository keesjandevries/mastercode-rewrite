#! /usr/bin/env python2
import os, sys, select

from collections import OrderedDict
from multiprocessing import Process, get_logger

from interfaces import softsusy
from interfaces import feynhiggs, micromegas, superiso, bphysics, lspscat
from interfaces import susypope
from modules import utils

from interfaces import slhalib as slhamodule
from interfaces.slhalib import SLHA

DEBUG = False

slha_generator = softsusy
slha_modifiers = [feynhiggs]
predictors = slha_modifiers + [micromegas, superiso, bphysics, lspscat,#]
        susypope]

def run_point(model, **inputs):
    stdouts = OrderedDict()

    #print "Generating SLHA file...",
    obj, stdout = utils.get_ctypes_streams(func=slha_generator.run,
            args=[model], kwargs=inputs)
    stdouts.update({slhamodule.name: stdout})
    slhafile = SLHA(obj)
    #print "Done"
    #print>>open('slhas/test.slha','w'), slhafile

    predictor_output = OrderedDict()
    for predictor in predictors:
        #print "Running {n}...".format(n=predictor.name),
        is_modifier = predictor in slha_modifiers
        result, stdout = utils.get_ctypes_streams(
                func=slhamodule.send_to_predictor,
                args=[slhafile,predictor, is_modifier])
        predictor_output.update(result)
        stdouts.update({predictor.name: stdout})
        #print "Done"

    for predictor, obs in predictor_output.iteritems():
        print
        print utils.ansi_bold(predictor)
        print "="*len(predictor)
        x = max([len(n) for n,_ in obs.iteritems()])
        f_str = "{{n:{x}}} = {{p}}".format(x=x)
        for name,value in obs.iteritems():
            if type(value) is not list:
                print f_str.format(n=name, p=value)
            else:
                print f_str.format(n=name, p="[{0}, ... , {1}][{2}]".format(
                    value[0],value[-1],len(value)))

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
