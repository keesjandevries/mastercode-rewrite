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

from User.data_sets import data_sets

def parse_args():
    #WARNING: this option list is rather ad hoc
    # feel free to ammend it!
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--tmp_dir', '-T', dest='tmp_dir', action='store', type=str,
            default=None, help='directory where temporary files get stored')
    parser.add_argument('--verbose'    , '-v', dest='verbose'  , action='store', 
            nargs="+", help='verbosity', default=[])
    parser.add_argument('--output-root' , '-o', dest='root_out', action='store', 
            default='temp/test_mn.root',  help='output root file')
    parser.add_argument('--multinest-dir'    , '-m', dest='multinest_dir'  , action='store', 
            default="chains", help='mulitnest parameter: directory for storing mulinest parameters ')
    parser.add_argument('--dataset'    , '-d', dest='data_set'  , action='store', 
            default="mc8", help='data set for X^2 calculation')
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
    parser.add_argument('--boxes', dest='boxes', action='store_true', 
            default=False,  help='RESULT ORIENTED: extract box number N from subdir_N and assign box')
    parser.add_argument('--multinest-para-scan', dest='multinest_para_scan', action='store_true', 
            default=False,  help='RESULT ORIENTED: test the various multinest parameters')
    return parser.parse_args()
##################################################
# WARNING: RESULT ORIENTED boxes study
##################################################
#args=parse_args()
#
def get_param_ranges():
    par_range=dict([
    ('m0',(0.,4000.)),
    ('m12',(0.,4000.)),
    ('A0',(-5000.,5000.)),
    ('tanb',(1.,65.)),]) # softsusy only takes tanb>=1.
    
    if args.boxes:
        m0N, m12N, A0N, tanbN = 3,3,3,3
    
        interval_integers=[]
        for m0i in range(m0N):
            for m12i in range(m12N):
                for A0i in range(A0N):
                    for tanbi in range(tanbN):
                        interval_integers.append({'m0':m0i,'m12':m12i,'A0':A0i,'tanb':tanbi,})
        
        n_box=0 # RESULT ORIENTED subdir looks like subdir_N
        for v in args.multinest_dir.split('/'):
            if 'subdir' in v:
                n_box=int(v.split('_')[-1])
        
        range_ints=interval_integers[n_box-1]
        for var in par_range.keys():
            min_par=par_range[var][0]+range_ints[var]*(par_range[var][1]-par_range[var][0])/3.
            max_par=par_range[var][0]+(range_ints[var]+1)*(par_range[var][1]-par_range[var][0])/3.
            par_range[var]=(min_par,max_par)
        print("BOX RANGES: ",par_range)
    return OrderedDict([
            ('m0',  par_range['m0']),
            ('m12', par_range['m12']),
            ('A0',  par_range['A0']),
            ('tanb',par_range['tanb']),
            ('mt',(171.4,175)),
            ('mz',(91.1833,91.1917)),
            ('Delta_alpha_had',(0.02729,0.02769))
           ] )
##################################################
# WARNING: RESULT ORIENTED multinest parameters study
##################################################
#args=parse_args()
#
def get_multinest_parameters():
    samplingefficiency=0.3 #DEFAULT from multinest api, tuned for 
    nlive=args.nlive
    tolerance=args.tolerance
    multinest_pars=[]
    if args.multinest_para_scan:
        #make list of parameters
        for eff in [0.8,0.5,0.3,0.1]:
            for n in [100,500,100,5000,10000]:
                for t in [0.5,0.1,0.01,0.001,0.0001]:
                    multinest_pars.append((eff,n,t))
        #get subdir number to select parameters from list
        n_param=1000 # RESULT ORIENTED: Out of range!!
        for v in args.multinest_dir.split('/'):
            if 'subdir' in v:
                n_param=int(v.split('_')[-1])
        samplingefficiency, nlive, tolerance= multinest_pars[n_param]
    return samplingefficiency, nlive , tolerance
##################################################
# DEFINITIONS NEEDED inside myprior, and myloglike 
##################################################
args = parse_args()
param_ranges=get_param_ranges()


default_chi=1e9

lookup=SLHA().get_lookup()

all_constraints=Constraints_list.constraints

bpp = pprint.PrettyPrinter(indent=4, depth=3)

data_set=data_sets[args.data_set]

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

    if args.tmp_dir:
        all_params.update({'tmp_dir':args.tmp_dir})

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
#    args = parse_args()
    my_seed=args.seed
    if args.boxes:
        for v in args.multinest_dir.split('/'):
            if 'subdir' in v:
                my_seed=int(v.split('_')[-1])

    if not os.path.exists(args.multinest_dir): os.mkdir(args.multinest_dir)
    samplingefficiency, nlive , tolerance = get_multinest_parameters()
    
    print(args.verbose)
    # this is where multinest is actually run
    root.root_open(args.root_out)
    multinest.run(myloglike, 
            myprior, 
            n_dims                  = len(param_ranges),
            resume                  = args.resume, 
            verbose                 = ('multinest' in args.verbose), 
            sampling_efficiency     = samplingefficiency, 
            n_live_points           = nlive , 
            max_iter                = args.max_iter,
            seed                    = my_seed,
            outputfiles_basename    = '{}/'.format(args.multinest_dir),
            evidence_tolerance      = tolerance)
    root.root_close()
    
