#! /usr/bin/env python
import os, sys, select, argparse, pprint, json, pickle
from collections import OrderedDict

#from ObsCalculator import point
from ObsCalculator import point, inputs
from tools import  pickle_object

from PointAnalyser import Analyse
from PointAnalyser import Constraints_list

#storage
import Storage.interfaces.ROOT_ab_out as ab_root
import Storage.interfaces.ROOT_read as rread
from Storage import old_mc_rootstorage 

#data set
from User.data_sets import data_sets

def parse_args():
    # WARNING: this code was written in a result oriented fashion
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--observables', '-o', dest='obs'      , action='store_true', help='print observables')
    parser.add_argument('--breakdown'  , '-b', dest='breakdown', action='store_true', help='print X^2 breakdonw')
    parser.add_argument('--verbose'    , '-v', dest='verbose'  , action='store', nargs="+", help='verbosity',default=[])
    parser.add_argument('--in_file', '-i', dest='in_file', action='store', type=str,
            default='temp/test.root', help='output in file')
    parser.add_argument('--root_file', '-r', dest='root_file', action='store', type=str,
            default='temp/test_ab.root', help='output root file')
    parser.add_argument('--input_pars', '-p', dest='input_pars', action='store', type=str,
            default=None, help='override all_params')
    parser.add_argument('--nstart', '-B', dest='begin', action='store', type=int,
            default=0, help='start entry')
    parser.add_argument('--npoints', '-N', dest='tot_points', action='store', type=int,
            default=10, help='number of entries')
    parser.add_argument('--njump', '-J', dest='njump', action='store', type=int,
            default=1, help='number of entries to jump after sampling')
    parser.add_argument('--dataset'    , '-d', dest='data_set'  , action='store', 
            default="mc8", help='data set for X^2 calculation')
    parser.add_argument('--pickle-in',dest='pickle_in', action='store', 
            default=None,  help='Name of pickled file containing entry numbers')
    parser.add_argument('--model', default='cMSSM', help='Model that SoftSUSY takes', choices=['cMSSM','NUHM1','pMSSM8'])
    return parser.parse_args()

if __name__=="__main__" :
    args = parse_args()
    # open root files
    rread.root_open(args.in_file)
    ab_root.root_open(args.root_file)

    model = 'cMSSM' 
    
    begin=args.begin
    step=args.njump
    end=begin+args.tot_points*step
    if end > rread.root_get_entries():
        end= rread.root_get_entries()
    # WARNING: this code was written in a result oriented fashion
    entry_range=range(begin,end,step)

    #allow that the entries come from a piclked file 
    if args.pickle_in:
        with open(args.pickle_in,'rb') as pickle_file:
            entry_range=pickle.load(pickle_file)
            if args.tot_points < len(entry_range):
                entry_range=entry_range[:args.tot_points]
    
    number_points=len(entry_range)
    for nth_entry, entry in enumerate(entry_range):
        if 'n' in args.verbose: print("Entry number: {0}, ({1} out of {2})".format( entry, nth_entry+1, number_points))
        VARS=rread.root_read(entry)
        m0, m12, A0, tanb, mt, mz, Delta_alpha_had = [VARS[i] for i in [1,2,3,4,6,7,9]]
        if args.model == 'cMSSM':
            all_params=inputs.get_mc_cmssm_inputs(m0,m12,tanb,A0,mt,mz,Delta_alpha_had )
        #check for command line input parameters
        if args.input_pars:
            all_params.update(eval(args.input_pars))
            
        #check verbosity
        if args.verbose:
            all_params['verbose']=args.verbose
        try:
            slha_obj, point ,stdouts = point.run_point(model=model, **all_params)
        except TypeError:
            print("ERROR: Point failed to run")
            continue

        all_constraints=Constraints_list.constraints
        #mc8 data set
        try:
            data_set=data_sets[args.data_set]
        except KeyError:
            print("WARNING: \"{}\" invalid data set. No X^2 is calculated".format(args.data_set))
            data_set=[]
        constraints={name: all_constraints[name] for name in data_set}
        #pass this constraints list to the chi2 function
        total, breakdown = Analyse.chi2(point,constraints)

        bpp = pprint.PrettyPrinter(indent=4, depth=3)

        # optional printing
        if args.obs:
            bpp.pprint(point)
        if args.breakdown:
            bpp.pprint(breakdown)
            print('Total chi2:',total)

        # save to root
        point[('tot_X2','all')]=total
        #WARNING: the following is extremetly result oriented
        VARS=VARS[:74]+VARS[-35:]
        VARSOUT=old_mc_rootstorage.get_VARS(point,point[('m', 'in_o')])
        ab_root.root_write(VARS,VARSOUT)

    # close root files after for loop
    rread.root_close()
    ab_root.root_close()


