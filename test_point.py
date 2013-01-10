#! /usr/bin/env python
import os, sys, select, argparse, pprint

#from ObsCalculator import point
from ObsCalculator import point
from tools import ansi_bold

from PointAnalyser import Analyse

def parse_args():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--model', '-m', dest='model', action='store', type=str,
            default='cMSSM', help='override model')

    return parser.parse_args()

if __name__=="__main__" :
    args = parse_args()

    model = args.model
    input_vars = {
            'cMSSM': {
                'm0': 300.53, 'm12': 905.0, 'A0': -1323.97 , 'tanb': 16.26, 'sgnMu': 1 #MC8 bf
                #'m0': 100, 'm12': 200, 'A0': 0, 'tanb': 10., 'sgnMu': 1
                #'m0': 389.50582, 'm12': 853.0322, 'A0': 2664.7922,
                #'tanb': 14.59729, 'sgnMu': 1
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
    m_vars = dict(list(input_vars.items()) + list(other_vars.items()))
    slha_file, observations = point.run_point(model=model, **m_vars)

    combined_obs = dict(list(slha_file.items()) + list(observations.items()))


    total, breakdown = Analyse.chi2(combined_obs)

    bpp = pprint.PrettyPrinter(indent=4, depth=3)
    bpp.pprint(breakdown)

    ## test code for Contour analyser
    #from PointAnalyser import Contours
    #from PointAnalyser import LikelihoodFunctions
    #testf = LikelihoodFunctions.power_4_scaling
    #point = (1,300)
    #contour = Contours.Contour(filename='PointAnalyser/test.txt', mode='radial',
            #pval=0.95, dim=2)
    #print(Contours.chi2_from_contour(contour, point, testf))
