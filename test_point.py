#! /usr/bin/env python
import os, sys, select, argparse, pprint
from collections import OrderedDict

#from ObsCalculator import point
from ObsCalculator import point
from tools import ansi_bold

from PointAnalyser import Analyse
from PointAnalyser import Constraints_list

def parse_args():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--model', '-m', dest='model', action='store', type=str,
            default='cMSSM', help='override model')
    parser.add_argument('--input_pars', '-p', dest='input_pars', action='store', type=str,
            default=None, help='override model')

    return parser.parse_args()

if __name__=="__main__" :
    args = parse_args()

    model = args.model
    
    if args.input_pars is None:
        input_vars = {
            'cMSSM': {
                'm0': 300.53, 'm12': 905.0, 'A0': -1323.97 , 'tanb': 16.26, 'sgnMu': 1 #MC8 bf
                #'m0': 100, 'm12': 270, 'A0': 0, 'tanb': 10., 'sgnMu': 1
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
    else:
        input_vars=eval(args.input_pars)
    other_vars = {
            'mt': 173.2,
            'mgut': {'cMSSM': 2e16, 'pMSSM': 1.0e3}[model]
            }
    m_vars = dict(list(input_vars.items()) + list(other_vars.items()))
    all_params={'SoftSUSY':m_vars}
#    all_params['mc_slha_update']={('SMINPUTS','MZ'):90.}
    all_params['mc_slha_update']=True
    all_params['verbose']=True
    

    try:
        slha_obj, observations,stdouts = point.run_point(model=model, **all_params)
    except TypeError:
        print("ERROR: Point failed to run")
        exit()

    slha_file=slha_obj.process()
    combined_obs = OrderedDict(list(slha_file.items()) + list(observations.items()))

    # I think this is the way to do it:
    # initialise all constraints
    all_constraints=Constraints_list.constraints
    # make a dictionary that only contains the constraints you want (e.g. just define on the spot, or read in from a file)
#       data_set=['xenon100']
#    data_set=all_constraints.keys()
    data_set=['Al(SLD)', 'sintheta_eff', 'Gamma_Z', 'MZ',  'Rl', 'Afb(b)',  'Afb(c)',   'DAlpha_had', 'sigma_had^0', 'Al(P_tau)', 'Ac17', 'Rb', 'Rc', 'Ab16',  'Al_fb',  'MW', ]
#    print(data_set)
    constraints={name: all_constraints[name] for name in data_set}
    #pass this constraints list to the chi2 function
    total, breakdown = Analyse.chi2(combined_obs,constraints)

    bpp = pprint.PrettyPrinter(indent=4, depth=3)
#    bpp.pprint(combined_obs)
    susypope_obs={oid:val for oid, val in combined_obs.items() if oid[0]=='SUSY-POPE'}
    bpp.pprint(susypope_obs)
    bpp.pprint(breakdown)
#    print('Total chi2:',total)

