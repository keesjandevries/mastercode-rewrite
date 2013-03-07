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
    parser.add_argument('--verbose'    , '-v', dest='verbose'  , action='store', nargs="+", help='verbosity')
    parser.add_argument('--input_pars', '-p', dest='input_pars', action='store', type=str,
            default=None, help='override all_params')
    return parser.parse_args()

if __name__=="__main__" :
    args = parse_args()

    model = 'cMSSM' 

    all_params={
            'SoftSUSY':{
                ('SMINPUTS', 'invAlfaMZ'): 127.934,
                ('SMINPUTS', 'GF'): 1.16637e-05,
                ('SMINPUTS', 'AlfasMZ'): 0.1172,
                ('SMINPUTS', 'MZ'): 91.1876,
                ('SMINPUTS', 'Mtau'): 1.777,
                ('SMINPUTS', 'Mt'): 173.3,
                ('SMINPUTS', 'Mb'): 4.25,
                ('MINPAR', 'TB'): 10.0,
                ('EXTPAR', 'Q'): -1.0,
                ('EXTPAR', 'M1'): 300.0,
                ('EXTPAR', 'M2'): 2500.0,
                ('EXTPAR', 'M3'): 360.0,
                ('EXTPAR', 'Atau'): 0.0,
                ('EXTPAR', 'At'): 0.0,
                ('EXTPAR', 'Ab'): 0.0,
                ('EXTPAR', 'MUE'): 2500.0,
                ('EXTPAR', 'MA0'): 2500.0,
                ('EXTPAR', 'MSL(1)'): 2500.0,
                ('EXTPAR', 'MSL(2)'): 2500.0,
                ('EXTPAR', 'MSL(3)'): 2500.0,
                ('EXTPAR', 'MSE(1)'): 2500.0,
                ('EXTPAR', 'MSE(2)'): 2500.0,
                ('EXTPAR', 'MSE(3)'): 2500.0,
                ('EXTPAR', 'MSQ(1)'): 360.0,
                ('EXTPAR', 'MSQ(2)'): 360.0,
                ('EXTPAR', 'MSQ(3)'): 2500.0,
                ('EXTPAR', 'MSU(1)'): 360.0,
                ('EXTPAR', 'MSU(2)'): 360.0,
                ('EXTPAR', 'MSU(3)'): 2500.0,
                ('EXTPAR', 'MSD(1)'): 360.0,
                ('EXTPAR', 'MSD(2)'): 360.0,
                ('EXTPAR', 'MSD(3)'): 2500.0
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
    #check for command line input parameters
    if args.input_pars:
        all_params.update(eval(args.input_pars))
        
    #check verbosity
    if args.verbose:
        all_params['verbose']=args.verbose
    try:
        slha_obj, combined_obs ,stdouts = point.run_point(model=model, **all_params)
    except TypeError:
        print("ERROR: Point failed to run")
        exit()


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

