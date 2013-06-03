#! /usr/bin/env python
import argparse, minuit2


#point calculator
from ObsCalculator import point, inputs
#chi2 calculation
from PointAnalyser import Analyse, Constraints_list
from User.data_sets import data_sets

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data-set' , default="mc8", help='data set for X^2 calculation')
    return parser.parse_args()

def cmssm_chi2(parameters):
    input_pars=inputs.get_mc_cmssm_inputs(*parameters)
    slha_obj, observables ,stdouts= point.run_point(**input_pars)
    #pass this constraints list to the chi2 function
    total, breakdown = Analyse.chi2(observables,constraints)
    return total
    
if __name__ == '__main__':
    args=parse_args()
    all_constraints=Constraints_list.constraints
    #mc8 data set
    try:
        data_set=data_sets[args.data_set]
    except KeyError:
        print("WARNING: \"{}\" invalid data set. No X^2 is calculated".format(args.data_set))
        data_set=[]
    constraints={name: all_constraints[name] for name in data_set}


    print(cmssm_chi2([271.378279475, 920.368119935, 14.4499538001, -1193.57068242, 173.474173, 91.1877452551, 0.0274821578423]))
