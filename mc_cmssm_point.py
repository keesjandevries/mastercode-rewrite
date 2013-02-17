#! /usr/bin/env python
import os, sys, select, argparse, pprint, json
from collections import OrderedDict

#from ObsCalculator import point
from ObsCalculator import point
from tools import  pickle_object

from PointAnalyser import Analyse
from PointAnalyser import Constraints_list

#storage
import Storage.interfaces.ROOT as root
from Storage import old_mc_rootstorage 

def parse_args():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--observables', '-o', dest='obs'      , action='store_true', help='print observables')
    parser.add_argument('--breakdown'  , '-b', dest='breakdown', action='store_true', help='print X^2 breakdonw')
    parser.add_argument('--root_save'  , '-r', dest='root_save', action='store_true', help='save to root file')
    parser.add_argument('--input_pars', '-p', dest='input_pars', action='store', type=str,
            default=None, help='override all_params')
    return parser.parse_args()

if __name__=="__main__" :
    args = parse_args()

    model = 'cMSSM' 

    all_params={
            'SoftSUSY':{
                'm0'    : 300.53, 
                'm12'   : 905.0, 
                'A0'    : -1303.97 , 
                'tanb'  : 16.26, 
                'sgnMu' : 1,
                'mt'    : 173.2,
                'mgut'  : 2e16,     # FIXME: this should become a default
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
    if args.input_pars:
        all_params.update(eval(args.input_pars))

    try:
        slha_obj, observations,stdouts = point.run_point(model=model, **all_params)
    except TypeError:
        print("ERROR: Point failed to run")
        exit()

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
    if args.root_save:
        # NOTE: for old_mc_rootstorage, need X^2 
        combined_obs[('tot_X2','all')]=total
        root.root_open('temp/test.root')
        old_mc_rootstorage.write_point_to_root(combined_obs)
        root.root_close()



