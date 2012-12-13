#! /usr/bin/env python2
import os, sys, select, argparse

from mcrw import point


def parse_args():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--debug', dest='debug', action='store_true',
            help='Print debugging information (e.g. stdout from predictors')
    parser.add_argument('--model', '-m', dest='model', action='store', type=str,
            default='cMSSM', help='override model')

    return parser.parse_args()

if __name__=="__main__" :
    args = parse_args()
    DEBUG = args.debug

    model = args.model
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
    point.run_point(model=model, **m_vars)
