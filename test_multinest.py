#! /usr/bin/env python
import os, pprint, argparse, sys
from collections import OrderedDict

from Samplers.interfaces import multinest
from ObsCalculator import point
from Storage import old_mc_rootstorage as rootstore

from PointAnalyser import Analyse
from PointAnalyser import Constraints_list

import Storage.interfaces.ROOT as root
from ObsCalculator.interfaces.slhalib import SLHA

def parse_args():
    #WARNING: this option list is rather ad hoc
    # feel free to ammend it!
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--verbose'    , '-v', dest='verbose'  , action='store', 
            nargs="+", help='verbosity', default=[])
    parser.add_argument('--output-root' , '-o', dest='root_out', action='store', 
            default='temp/test_mn.root',  help='output root file')
    parser.add_argument('--multinest-dir'    , '-m', dest='multinest_dir'  , action='store', 
            default="chains", help='mulitnest parameter: directory for storing mulinest parameters ')
    parser.add_argument('--tolerance'    , '-t', dest='tolerance'  , action='store', type=float,
            default=0.5, help='multinest parameter: evidence tolerance')
    parser.add_argument('--nlive', '-l', dest='nlive'  , action='store', type=int,
            default=10, help='multinest parameter: nlive')
    parser.add_argument('--max_iter', '-i', dest='max_iter' , action='store', type=int,
            default=1,  help='multinest parameter: max_iter')
    parser.add_argument('--seed', '-s', dest='seed' , action='store', type=int,
            default=-1, help='multinest parameter: seed (negative for seed from sys clock) ')
    parser.add_argument('--resume','-R', dest='resume', action='store_true', 
            default=False,  help='multinest parameter: resume existing jobs using parameters from multinest dir')
    return parser.parse_args()

##################################################
# DEFINITIONS NEEDED inside myprior, and myloglike 
##################################################
param_ranges=OrderedDict([
            ('m0',(0,4000)),
            ('m12',(0,4000)),
            ('A0',(-5000,5000)),
            ('tanb',(1,65)), # softsusy only takes tanb>=1.
            ('mt',(171.4,175)),
            ('mz',(91.1833,91.1917)),
            ('Delta_alpha_had',(0.02729,0.02769))
           ] )

default_chi=1e9

lookup=SLHA().get_lookup()

all_constraints=Constraints_list.constraints

bpp = pprint.PrettyPrinter(indent=4, depth=3)

data_set= [ 'Al(SLD)', 'Ab', 'Ac', 'Oh^2_mc8', 'Higgs125', 'BR(Bd->ll)',  
            'Gamma_Z', 'GZ_in', 'R(B->Xsll)', 'Al(P_tau)', 'MZ', 'R(D_ms)', 'MW', 'Afb_l', 
            'xenon100', 'DAlpha_had', 'R(Delta_mk)',  'sigma_had^0', 'Afb(c)', 
            'atlas5_m0_m12', 'Afb(b)',  'R(b->sg)', 'R(Dms)/R(Dmd)', 'R(B->taunu)', 
            'Rc', 'Rb',  'Rl', 'mc8_bsmm', 'sintheta_eff', 'Mt', 'R(K->lnu)', 'R(Kp->pinn)', 'gminus2mu', 'MATANB' ]

###############################################

def myprior(cube, ndim, nparams):
    for i, (name,(low,high)) in enumerate(param_ranges.items()):
        cube[i]=(high-low)*cube[i]+low

def get_obs(cube,ndim):
    model='cMSSM'
    m0=cube[0]
    m12=cube[1]
    A0=cube[2]
    tanb=cube[3]
    mt=cube[4]
    mz=cube[5]
    Delta_alpha_had=cube[6]

    model = 'cMSSM' 

    all_params={
            'SoftSUSY':{
                ('MINPAR', 'M0'):       m0,
                ('MINPAR', 'M12'):      m12,
                ('MINPAR', 'TB'):       tanb,
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
    if 'parameters' in args.verbose : 
        print(all_params)

    all_params['lookup']=lookup
    all_params['verbose']=args.verbose
    try:
        slha_obj, combined_obs, stdouts = point.run_point(model=model, **all_params)
    except TypeError:
        return None
    #WARNING: this if for debugging: 
    # give parameters to the place where a problem occurs and trow it in stderr
    del all_params['lookup']
    del all_params['verbose']
    if (not combined_obs) and ('errors' in args.verbose) : 
        print("ERROR: error in some of the predictors")
        print(all_params,file=sys.stderr)
    return combined_obs, all_params 

def get_chi2(obs):
    constraints={name: all_constraints[name] for name in data_set}
    total, breakdown = Analyse.chi2(obs,constraints)
    return total


def myloglike(cube, ndim, nparams):
    chi2=default_chi
    obs,params=get_obs(cube,ndim)
    if obs: 
        chi2=get_chi2(obs)
        obs[('tot_X2', 'all')]=chi2
        rootstore.write_point_to_root(obs,params)
    print("X^2={}".format(chi2))
    print()
#    else: print("ERROR: in one of the programs")
    return -chi2


if __name__=="__main__" :
    args = parse_args()

    if not os.path.exists(args.multinest_dir): os.mkdir(args.multinest_dir)
    
    print(args.verbose)
    # this is where multinest is actually run
    root.root_open(args.root_out)
    multinest.run(myloglike, 
            myprior, 
            n_dims                  = len(param_ranges),
            resume                  = args.resume, 
            verbose                 = ('multinest' in args.verbose), 
            sampling_efficiency     = 0.3, 
            n_live_points           = args.nlive , 
            max_iter                = args.max_iter,
            seed                    = args.seed,
            outputfiles_basename    = '{}/'.format(args.multinest_dir),
            evidence_tolerance      = args.tolerance)
    root.root_close()
    
