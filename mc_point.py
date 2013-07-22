#! /usr/bin/env python
import os, sys, select, argparse, pprint, json, pickle
from collections import OrderedDict

#tools
from tools import  pickle_object
#point calculator
from ObsCalculator import point, inputs
#chi2 calculation
from PointAnalyser import Analyse, Constraints_list

#data set
from User.data_sets import data_sets

#storage
import Storage.interfaces.ROOT as root
from Storage import old_mc_rootstorage 

#pretty printer
pp = pprint.PrettyPrinter(indent=4)

def parse_args():
    parser = argparse.ArgumentParser(description='Run mastercode for cmssm point')
    parser.add_argument('--observables', '-o', dest='obs'      , action='store_true', help='print observables')
    parser.add_argument('--breakdown'  , '-b', dest='breakdown', action='store_true', help='print X^2 breakdown')
    parser.add_argument('--json-breakdown'  ,  help='provide json file for breakdown')
    parser.add_argument('--suppress-chi2-calc' , dest='suppress_chi2_calc', action='store_true', help='suppress chi2 calculation for testing')
    parser.add_argument('--observable-keys'  , dest='observable_keys', action='store_true', help='print observable keys')
    parser.add_argument('--store-pickle'     , dest='store_pickle', action='store', type=str,
            default=None ,help='store obervables in pickle file')
    parser.add_argument('--root-save'  , '-r',  help='save to root file')
    parser.add_argument('--verbose'    , '-v', dest='verbose'  , default=[], action='store', nargs="+", help='verbosity')
    parser.add_argument('--input_pars', '-p', dest='input_pars', action='store', type=str,
            default=None, help='override all_params')
    parser.add_argument('--tmp_dir', '-t', dest='tmp_dir', action='store', type=str,
            default=None, help='directory where temporary files get stored')
    parser.add_argument('--data-set'    , '-d', dest='data_set'  , action='store', 
            default="generic", help='data set for X^2 calculation')
    parser.add_argument('--run-spectrum', help='run spectrum file through point.py')
    parser.add_argument('--run-softsusy-input-slha', help='run softsusy input slha file through point.py')
    parser.add_argument('--mc-cmssm-default', action='store_true', 
            help="Mastercode cmssm point: m0=271.3,m12=920.3,tanb=14.4,A0=-1193.57,mt=173.47,mz=91.18774,Delta_alpha_had=0.027482")
    parser.add_argument('--mc-cmssm', nargs=7, type=float, 
            help="Run cmssm mc8 best fit point: m0,m12,tanb,A0,mt,mz,Delta_alpha_had") # FIXME: metavariable is stupid
    parser.add_argument('--mc-nuhm1', nargs=8, type=float,
            help="Mastercode nuhm1 point specify: m0,m12,tanb,A0,mh2,mt,mz,Delta_alpha_had")
    parser.add_argument('--mc-nuhm1-default', action='store_true', 
            help="Mastercode nuhm1 point: m0=237.4,m12=968.8,tanb=15.6,A0=-1858.7,mh2=-6499529, mt=173.3,mz=91.1875,Delta_alpha_had=0.0274949")
    parser.add_argument('--mc-pmssm8', nargs=11, type=float,
            help="Mastercode 8d pmssm point specify: msq12,msq3,msl, M1, A, MA,tanb,mu,mt,mz,Delta_alpha_had")
    parser.add_argument('--mc-pmssm10', nargs=13, type=float,
            help="Mastercode 10d pmssm point specify: msq12,msq3,msl, M1,M2,M3, A, MA,tanb,mu,mt,mz,Delta_alpha_had")
    parser.add_argument('--mc-pmssm10-default',action='store_true' ,
            help="Mastercode 10d pmssm point specify: best fit found with minuit")
    return parser.parse_args()

if __name__=="__main__" :
    args = parse_args()

    #Start with clean set of parameters
    all_params={} 

    #this is afterburner style 
    if args.mc_cmssm :
        all_params=inputs.get_mc_cmssm_inputs(*(args.mc_cmssm))
    elif args.mc_cmssm_default:
        all_params=inputs.get_mc_cmssm_inputs(271.378279475, 920.368119935, 14.4499538001, -1193.57068242, 173.474173, 91.1877452551, 0.0274821578423)
    elif args.mc_nuhm1 :
        all_params=inputs.get_mc_nuhm1_inputs(*(args.mc_nuhm1))
    elif args.mc_nuhm1_default :
        all_params=inputs.get_mc_nuhm1_inputs(237.467776964, 968.808711245, 15.649644, -1858.78698798, -6499529.79661,
                173.385870186, 91.1875000682, 0.0274949856504)
    elif args.mc_pmssm8 :
        all_params=inputs.get_mc_pmssm8_inputs(*(args.mc_pmssm8))
    elif args.mc_pmssm10 :
        all_params=inputs.get_mc_pmssm10_inputs(*(args.mc_pmssm10))
    elif args.mc_pmssm10_default :
        all_params=inputs.get_mc_pmssm10_inputs(1663.99,1671.75,414.131,294.935,311.199,1712.73,
                1841.21,718.489,43.4923,775.09,173.233,91.1874,0.0275018)
    elif args.run_softsusy_input_slha:
        all_params={'SoftSUSY':{'file':args.run_softsusy_input_slha}}
    elif args.run_spectrum:
        all_params={'spectrumfile':args.run_spectrum}

    #check for command line input parameters
    elif args.input_pars:
        all_params.update(eval(args.input_pars))

    #check for tmp_dir
    if args.tmp_dir:
        all_params.update({'tmp_dir':args.tmp_dir})
    #print inputs like  
    if 'inputs' in args.verbose : 
        print(all_params)
        
    #check verbosity
    if args.verbose:
        all_params['verbose']=args.verbose
    try:
        slha_obj, point ,stdouts = point.run_point(**all_params)
    except TypeError:
        print("ERROR: Point failed to run")
        exit()

    if slha_obj is None:
        print("Exiting because slha_obj is None")
        exit()

    if not args.suppress_chi2_calc:
        all_constraints=Constraints_list.constraints
        #mc8 data set
        try:
            data_set=data_sets[args.data_set]
        except KeyError:
            print("WARNING: \"{}\" invalid data set. No X^2 is calculated".format(args.data_set))
            data_set=[]
    if not args.suppress_chi2_calc:
        constraints={name: all_constraints[name] for name in data_set}

    #pass this constraints list to the chi2 function
    if not args.suppress_chi2_calc:
        total, breakdown = Analyse.chi2(point,constraints)


    # optional printing
    if args.obs:
        pp.pprint(point)
    if args.breakdown:
        Analyse.print_chi2_breakdown(point, constraints,data_set)

    # save to root
    if args.root_save:
        # NOTE: for old_mc_rootstorage, need X^2 
        point[('tot_X2','all')]=total
        root.root_open(args.root_save)
        VARS=old_mc_rootstorage.get_VARS(point,point[('m','in_o')])
        root.root_write(VARS)
        root.root_close()
    if args.json_breakdown:
        l=[]
        for d in data_set:
            l.append([d,breakdown[d]])
        with open(args.json_breakdown,'w') as f:
            json.dump(l,f)
        

    # print only observable keys
    if args.observable_keys:
        pp.pprint([key for key in point.keys()])

    # store observables to piclked file
    if args.store_pickle:
        with open(args.store_pickle,'wb') as pickle_file:
            pickle.dump(point,pickle_file)

