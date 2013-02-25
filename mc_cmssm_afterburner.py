#! /usr/bin/env python
import os, sys, select, argparse, pprint, json
from collections import OrderedDict

#from ObsCalculator import point
from ObsCalculator import point
from tools import  pickle_object

from PointAnalyser import Analyse
from PointAnalyser import Constraints_list

#storage
import Storage.interfaces.ROOT_ab_out as ab_root
import Storage.interfaces.ROOT_read as rread
from Storage import old_mc_rootstorage 

def parse_args():
    # WARNING: this code was written in a result oriented fashion
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--observables', '-o', dest='obs'      , action='store_true', help='print observables')
    parser.add_argument('--breakdown'  , '-b', dest='breakdown', action='store_true', help='print X^2 breakdonw')
    parser.add_argument('--verbose'    , '-v', dest='verbose'  , action='store', nargs="+", help='verbosity')
    parser.add_argument('--in_file', '-i', dest='in_file', action='store', type=str,
            default='temp/test.root', help='output in file')
    parser.add_argument('--root_file', '-r', dest='root_file', action='store', type=str,
            default='temp/test_ab.root', help='output root file')
    parser.add_argument('--input_pars', '-p', dest='input_pars', action='store', type=str,
            default=None, help='override all_params')
    parser.add_argument('--nstart', '-B', dest='begin', action='store', type=int,
            default=0, help='start entry')
    parser.add_argument('--npoints', '-N', dest='end', action='store', type=int,
            default=10, help='number of entries')
    parser.add_argument('--njump', '-J', dest='njump', action='store', type=int,
            default=1, help='number of entries to jump after sampling')
    return parser.parse_args()

if __name__=="__main__" :
    args = parse_args()
    # open root files
    rread.root_open(args.in_file)
    ab_root.root_open(args.root_file)

    model = 'cMSSM' 
    
    begin=args.begin
    step=args.njump
    end=args.end*step
    if end > rread.root_get_entries():
        end= rread.root_get_entries()
    # WARNING: this code was written in a result oriented fashion
    for entry in range(begin,end,step):
        if 'n' in args.verbose: print("Entry number: {0}, ({1} out of {2})".format( entry, int((entry-begin)/step)+1, int((end-begin)/step)))
        VARS=rread.root_read(entry)
        m0, m12, A0, tanb, mt, mz, Delta_alpha_had = [VARS[i] for i in [1,2,3,4,6,7,9]]
        all_params={
                'SoftSUSY':{
                    ('MINPAR', 'M0'):       m0,
                    ('MINPAR', 'M12'):      m12,
                    ('MINPAR', 'TB'):       tanb,
                    ('MINPAR', 'signMUE'):  1,
                    ('MINPAR', 'A'):        A0,
                    ('SMINPUTS', 'Mt') :    mt,
                    },
                'mc_slha_update':{
                    ('SMINPUTS','MZ')   : mz, 
                    },
                'SUSY-POPE':{
                    'non_slha_inputs':{
                        'DeltaAlfa5had' : Delta_alpha_had,
                        }
                    }
                }
        #check for command line input parameters
        if args.input_pars:
            all_params.update(eval(args.input_pars))
            
        #check verbosity
        if args.verbose:
            all_params['verbose']=args.verbose
        try:
            slha_obj, observations,stdouts = point.run_point(model=model, **all_params)
        except TypeError:
            print("ERROR: Point failed to run")
            continue



        slha_file=slha_obj.process()
        combined_obs = OrderedDict(list(slha_file.items()) + list(observations.items()))

        all_constraints=Constraints_list.constraints
        #mc8 data set
        data_set= [ 'Al(SLD)', 'Ab', 'Ac', 'Oh^2_mc8', 'Higgs125', 'BR(Bd->ll)',  
                'Gamma_Z', 'GZ_in', 'R(B->Xsll)', 'Al(P_tau)', 'MZ', 'R(D_ms)', 'MW', 'Afb_l', 
                'xenon100', 'DAlpha_had', 'R(Delta_mk)',  'sigma_had^0', 'Afb(c)', 
                'atlas5_m0_m12', 'Afb(b)',  'R(b->sg)', 'R(Dms)/R(Dmd)', 'R(B->taunu)', 
                'Rc', 'Rb',  'Rl', 'mc8_bsmm', 'sintheta_eff', 'Mt', 'R(K->lnu)', 'R(Kp->pinn)', 'gminus2mu', 'MATANB' ]
        constraints={name: all_constraints[name] for name in data_set}
        #pass this constraints list to the chi2 function
        total, breakdown = Analyse.chi2(combined_obs,constraints)

        bpp = pprint.PrettyPrinter(indent=4, depth=3)

        # optional printing
        if args.obs:
            bpp.pprint(combined_obs)
        if args.breakdown:
            bpp.pprint(breakdown)
            print('Total chi2:',total)

        # save to root
        combined_obs[('tot_X2','all')]=total
        #WARNING: the following is extremetly result oriented
        VARS=VARS[:74]+VARS[-34:]
        old_mc_rootstorage.write_in_out_to_ab_root(VARS,combined_obs)

    # close root files after for loop
    rread.root_close()
    ab_root.root_close()


