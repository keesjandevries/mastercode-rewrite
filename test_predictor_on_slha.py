#! /usr/bin/env python

#python modules
import argparse, pprint

#mcpp modules
from ObsCalculator.interfaces import feynhiggs, micromegas, superiso, bphysics, lspscat
from ObsCalculator.interfaces import susypope
from ObsCalculator.interfaces.slhalib import SLHA
from PointAnalyser import Analyse
from PointAnalyser import Constraints_list

predictor_dict={
        'feynhiggs' :feynhiggs, 
        'micromegas':micromegas, 
        'superiso'  :superiso, 
        'bphysics'  :bphysics, 
        'lspscat'   :lspscat,
        'susypope'  :susypope,
        }

pp=pprint.PrettyPrinter(indent=4)

def parse_args():
    parser = argparse.ArgumentParser(description='Run predictor on slha file',
            formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-f', '--filename',required=True,  help='slha file name')
    parser.add_argument('-p', dest='predictor', required=True, 
            choices=predictor_dict.keys(),help='specify predictor',)
    parser.add_argument('-v','--verbose', action='store_true',help='verbosity')
    parser.add_argument('-b','--breakdown', action='store_true',help='give chi2 breakdown')
    parser.add_argument('--other-inputs',help='other inputs, like this: \"{....}\"')
    return parser.parse_args()

if __name__=="__main__" :
    args=parse_args()
    slhafile=SLHA()
    slhafile.read(args.filename)
    inputs={}
    if args.other_inputs:
        inputs.update(eval(args.other_inputs))
    if args.verbose:
        inputs.update({'verbose':True})
    predictor_output=predictor_dict[args.predictor].run(slhafile, inputs , False)
    pp.pprint(predictor_output)

    if args.breakdown:
        #FIXME: use print_chi2_breakdown() 
        header='{:<20}: {:>13} | {:<30} :  {:>10}'.format('Name constraint','Chi2 penalty','Observable','Value')
        print('='*len(header))
        print(header)
        print('='*len(header))
        for name, constraint in Constraints_list.constraints.items(): 
            oids= constraint.get_oids()
            if len(oids) == 1 and oids[0] in predictor_output: 
                chi2=constraint.get_chi2(predictor_output)
                print('{:<20}: {:>13.3f} | {:<30} :  {:>10.4e} '.format(name,chi2,str(oids[0]), predictor_output[oids[0]] ))
