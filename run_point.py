#! /usr/bin/env python2
import os, sys, select, argparse

from collections import OrderedDict
from multiprocessing import Process, get_logger

from interfaces import softsusy
from interfaces import feynhiggs, micromegas, superiso, bphysics, lspscat
from interfaces import susypope
from modules import utils

from interfaces import slhalib as slhamodule
from interfaces.slhalib import SLHA

slha_generator = softsusy
slha_modifiers = [feynhiggs]
predictors = slha_modifiers + [micromegas, superiso, bphysics, lspscat,#]
        susypope]

DEBUG = False

def parse_args():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--debug', dest='debug', action='store_true',
            help='Print debugging information (e.g. stdout from predictors')

    return parser.parse_args()

def run_point(model, **inputs):
    stdouts = OrderedDict()

    #print "Generating SLHA file...",
    obj, stdout = utils.get_ctypes_streams(func=slha_generator.run,
            args=[model], kwargs=inputs)
    stdouts.update({slhamodule.name: stdout})
    slhafile = SLHA(obj)
    if DEBUG: print obj
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
    if DEBUG:
        for name, stdout in stdouts.iteritems():
            print "="*80
            print utils.ansi_bold(name)
            print "-"*80
            print stdout
            print "="*80
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
    args = parse_args()
    DEBUG = args.debug

    model = 'pMSSM'
    input_vars = {
            'cMSSM': {
                'm0': 100, 'm12': 200, 'A0': 0, 'tanb': 10., 'sgnMu': 1
                },
            'pMSSM': { 'tanb' : 10., 'sgnMu': 1, 'M_1': 3.00e+02,
                'M_2': 2.50e+03, 'M_3': 3.60e+02, 'At': 0.00e+00,
                'Ab': 0.00e+00, 'Atau': 0.00e+00, 'mu': 2.50e+03,
                'mA': 2.50e+03, 'meL': 2.50e+03, 'mmuL': 2.50e+03,
                'mtauL': 2.50e+03, 'meR': 2.50e+03, 'mmuR': 2.50e+03,
                'mtauR': 2.50e+03, 'mqL1': 3.60e+02, 'mqL2': 3.60e+02,
                'mqL3': 2.50e+03, 'muR': 3.60e+02, 'mcR': 3.60e+02,
                'mtR': 2.50e+03, 'mdR': 3.60e+02, 'msR': 3.60e+02,
                'mbR': 2.50e+03
                },
            }[model]
    other_vars = {
            'mt': 173.2,
            'mgut': {'cMSSM': 2e16, 'pMSSM': 1.0e3}[model]
            }
    m_vars = dict(input_vars.items() + other_vars.items())
    run_point(model=model, **m_vars)
