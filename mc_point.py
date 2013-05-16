#! /usr/bin/env python
import os, sys, select, argparse, pprint, json, pickle
from collections import OrderedDict

#from ObsCalculator import point
from ObsCalculator import point, inputs
from tools import  pickle_object

from PointAnalyser import Analyse
from PointAnalyser import Constraints_list

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
    parser.add_argument('--suppress-chi2-calc' , dest='suppress_chi2_calc', action='store_true', help='suppress chi2 calculation for testing')
    parser.add_argument('--observable-keys'  , dest='observable_keys', action='store_true', help='print observable keys')
    parser.add_argument('--store-pickle'     , dest='store_pickle', action='store', type=str,
            default=None ,help='store obervables in pickle file')
    parser.add_argument('--root-save'  , '-r',  help='save to root file')
    parser.add_argument('--verbose'    , '-v', dest='verbose'  , action='store', nargs="+", help='verbosity')
    parser.add_argument('--input_pars', '-p', dest='input_pars', action='store', type=str,
            default=None, help='override all_params')
    parser.add_argument('--tmp_dir', '-t', dest='tmp_dir', action='store', type=str,
            default=None, help='directory where temporary files get stored')
    parser.add_argument('--data-set'    , '-d', dest='data_set'  , action='store', 
            default="mc8", help='data set for X^2 calculation')
    parser.add_argument('--mc-cmssm-default', action='store_true', 
            help="Mastercode cmssm point: m0=271.3,m12=920.3,tanb=14.4,A0=-1193.57,mt=173.47,mz=91.18774,Delta_alpha_had=0.027482")
    parser.add_argument('--mc-cmssm', nargs=7, type=float, metavar=''
            help="Run cmssm mc8 best fit point: m0,m12,tanb,A0,mt,mz,Delta_alpha_had") # FIXME: metavariable is stupid
    parser.add_argument('--mc-nuhm1', nargs=8, type=float,
            help="Mastercode nuhm1 point specify: m0,m12,tanb,A0,mh2,mt,mz,Delta_alpha_had")
    parser.add_argument('--mc-7dpmssm', nargs=8, type=float,
            help="Mastercode 7dpmssm point specify: msq12,msq3,msl, M1, A, MA,tanb,mu")
    return parser.parse_args()

if __name__=="__main__" :
    args = parse_args()

    #FIXME: make option like --default-mc-cmssm
    all_params={
            'SoftSUSY':{
#                'model'         :       'NUHM1',
                'model'         :       'cMSSM',
                ('MINPAR', 'M0'):       300.53,
                ('MINPAR', 'M12'):      905.0,
                ('MINPAR', 'TB'):       16.26,
                ('MINPAR', 'A'):        -1303.97,
                ('SMINPUTS', 'Mt') :    173.2,
#                ('EXTPAR','MH2') :       1,
                },
            'mc_slha_update':{
                ('SMINPUTS','MZ')   : 91.1876, 
                },
            'SUSY-POPE':{
                'non_slha_inputs':{
                    'DeltaAlfa5had' : 0.02759,
                    }
                }
            }

    #this is afterburner style 
    if args.mc_cmssm :
        all_params=inputs.get_mc_cmssm_inputs(*(args.mc_cmssm))
    if args.mc_cmssm_default:
        all_params=inputs.get_mc_cmssm_inputs(271.378279475, 920.368119935, 14.4499538001, -1193.57068242, 173.474173, 91.1877452551, 0.0274821578423)
    if args.mc_nuhm1 :
        all_params=inputs.get_mc_nuhm1_inputs(*(args.mc_nuhm1))
    if args.mc_7dpmssm :
        all_params=inputs.get_mc_7d_pmssm_inputs(*(args.mc_7dpmssm))

    #check for command line input parameters
    if args.input_pars:
        all_params.update(eval(args.input_pars))

    #check for tmp_dir
    if args.tmp_dir:
        all_params.update({'tmp_dir':args.tmp_dir})
        
    #check verbosity
    if args.verbose:
        all_params['verbose']=args.verbose
    try:
        slha_obj, combined_obs ,stdouts = point.run_point(**all_params)
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
        total, breakdown = Analyse.chi2(combined_obs,constraints)


    # optional printing
    if args.obs:
        pp.pprint(combined_obs)
    if args.breakdown:
        Analyse.print_chi2_breakdown(combined_obs, constraints)

    # save to root
    if args.root_save:
        # NOTE: for old_mc_rootstorage, need X^2 
        combined_obs[('tot_X2','all')]=total
        root.root_open(args.root_save)
        old_mc_rootstorage.write_point_to_root(combined_obs)
        root.root_close()

    # print only observable keys
    if args.observable_keys:
        pp.pprint([key for key in combined_obs.keys()])

    # store observables to piclked file
    if args.store_pickle:
        with open(args.store_pickle,'wb') as pickle_file:
            pickle.dump(combined_obs,pickle_file)

