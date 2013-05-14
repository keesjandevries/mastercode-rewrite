#! /usr/bin/env python
import os, pprint, argparse, sys,pickle ,re
from collections import OrderedDict

#FIXME: use interface from github though check performance!!!!
from Samplers.interfaces import multinest
from ObsCalculator import point, inputs
from Storage import old_mc_rootstorage as rootstore

from PointAnalyser import Analyse
from PointAnalyser import Constraints_list

import Storage.interfaces.ROOT as root
from ObsCalculator.interfaces.slhalib import SLHA

from tools import unique_str

from User.data_sets import data_sets

def parse_args():
    # feel free to ammend it!
    parser = argparse.ArgumentParser(
            description='''Run mcpp with multinest.
            Note you can set using files like this: "./test_multinest.py @command_line_options.txt".
            For more info see the documentation on python's argparse function.
            ''',
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
            fromfile_prefix_chars='@') #FIXME: I'm not happy yet with how files are read in
    mcpp = parser.add_argument_group('mcpp arguments')
    multinest = parser.add_argument_group('multinest settings','For more info see README of Multinest')
    #mastercode specific arguments
    mcpp.add_argument('--tmp-dir',  dest='tmp_dir', action='store', type=str,
            default=None, help='directory where temporary files get stored')
    mcpp.add_argument('--verbose'    , '-v', dest='verbose'  , action='store', 
            nargs="+", help='verbosity, e.g. parameters, X, errors, multinest, or mcpp verbosity',default=[])
    mcpp.add_argument('--output-root' , '-o', dest='root_out', action='store', 
            default='chains/',  help='output root directory ')
    mcpp.add_argument('--root-prefix' ,  action='store', 
            default='cmssm-multinest-step-',  help='output root file prefix ')
    mcpp.add_argument('--suppress-mc-info', dest='suppress_info', action='store_true', 
            default=False,  help='suppress dumping the multinest parameters. Not recommended')
    mcpp.add_argument('--pickle-out', dest='pickle_out', action='store_true', 
            default=False,  help='This is what we want. Store points to pickled dictionaries: unique_string.pkl')
    mcpp.add_argument('--data-set'  ,  dest='data_set'  , action='store', 
            default="mc8", help='data set for X^2 calculation')
    mcpp.add_argument('--model', default='cMSSM', help='Model that SoftSUSY takes', choices=['cMSSM','NUHM1'])
    mcpp.add_argument('--m0-range', action='store', nargs=2, type=float,
            default=[0.,4000.], help='parameter range: m0')
    mcpp.add_argument('--m12-range', action='store', nargs=2, type=float,
            default=[0.,4000.], help='parameter range: m12')
    mcpp.add_argument('--A0-range', action='store', nargs=2, type=float,
            default=[-5000.,5000.], help='parameter range: A0')
    mcpp.add_argument('--tanb-range', action='store', nargs=2, type=float,
            default=[1.,62.], help='parameter range: tanb')
    mcpp.add_argument('--mt-range', action='store', nargs=2, type=float,
            default=[171.4,175], help='parameter range: mt')
    mcpp.add_argument('--mz-range', action='store', nargs=2, type=float,
            default=[91.1833,91.1917], help='parameter range: mz')
    mcpp.add_argument('--delta-alpha-had-range', action='store', nargs=2, type=float,
            default=[0.02729,0.02769], help='parameter range: delta_alpha_had')
    mcpp.add_argument('--mh2-range', action='store', nargs=2, type=float,
            default=[-2e7,2e7], help='parameter range: mh2 (when model=NUHM1),note: further than ever')
    #multinest specific arguments
    multinest.add_argument('--multinest-dir' ,     action='store', 
            default="chains", help='directory for storing mulinest parameters ')
    multinest.add_argument('--evidence-tolerance' ,'--tol' , '-t',  action='store', type=float,
            default=0.5, help='evidence tolerance')
    multinest.add_argument('--sampling-efficiency',  action='store', type=float,
            default=0.8, help='0.8 and 0.3 are recommended for parameter estimation & evidence evalutaion respectively.')
    multinest.add_argument('--null-log-evidence',  action='store', type=float,
            default=-1e90, help='do not change, see README')
    multinest.add_argument('--log-zero',  action='store', type=float,
            default=-1e100, help='do not change, see README')
    multinest.add_argument('--n-live-points', '-l',  action='store', type=int,
            default=10, help='very important setting: the number of living points ')
    multinest.add_argument('--max-iter', '-i',  action='store', type=int,
            default=1,  help='maximum number of iterations')
    multinest.add_argument('--context',   action='store', type=int,
            default=0,  help='the user can pass info using context, probably not needed')
    multinest.add_argument('--max-modes',   action='store', type=int,
            default=100,  help='maximum number of modes, to do with memory; see README')
    multinest.add_argument('--n-iter-before-update',  action='store', type=int,
            default=100,  help='n_iter_before_update')
    multinest.add_argument('--seed', '-s',  action='store', type=int,
            default=-1, help='seed (negative for seed from sys clock) ')
    multinest.add_argument('--resume','-R', dest='resume', action='store_true', 
            default=False,  help=' resume existing jobs using parameters from multinest dir')
    multinest.add_argument('--multimodal',  action='store',type=bool, default=True,
            help='do mode separation? Usually want this on.')
    multinest.add_argument('--const-efficiency-mode',  action='store',type=bool, default=False,
            help='Constant efficientcy mode; see README')
    multinest.add_argument('--write-output',  action='store',type=bool, default=True,
            help='write output files? Probably yes')
    multinest.add_argument('--init-MPI',  action='store',type=bool, default=False,
            help='relevant only if compiling with MPI')
    return parser.parse_args()

def get_root_file_name(output_dir):
    root_file_step_numbers=[ int(re.search(r'\d+', f).group()) for f in os.listdir(output_dir) if args.root_prefix in f]
    if not len(root_file_step_numbers) == 0: 
        current_step=max(root_file_step_numbers)+1
    else: 
        current_step=1
    return '{}/{}{}.root'.format(output_dir,args.root_prefix,current_step)

def get_param_ranges():
    param_ranges= OrderedDict([
    ('m0',  tuple(args.m0_range)),
    ('m12', tuple(args.m12_range)),
    ('A0',  tuple(args.A0_range)),
    ('tanb',tuple(args.tanb_range)), # softsusy only takes tanb>=1.
    ('mt',  tuple(args.mt_range)),
    ('mz',  tuple(args.mz_range)),
    ('Delta_alpha_had',tuple(args.delta_alpha_had_range))
    ])
    if args.model == 'NUHM1':
        param_ranges['mh2']=tuple(args.mh2_range)
    return param_ranges
##################################################
# DEFINITIONS NEEDED inside myprior, and myloglike 
##################################################
#arguments from command line
args = parse_args()
#parameter ranges
param_ranges=get_param_ranges()
#default X^2 penalty in case of errors
default_chi=1e9
#lookup dictionary for initiating SLHA() objects
lookup=SLHA().get_lookup()
#constraint objects
all_constraints=Constraints_list.constraints
#pretty printer
my_pprint = pprint.PrettyPrinter(indent=4, depth=3)
#constraints list
data_set=data_sets[args.data_set]
###############################################

def myprior(cube, ndim, nparams):
    for i, (name,(low,high)) in enumerate(param_ranges.items()):
        cube[i]=(high-low)*cube[i]+low

def get_obs(cube,ndim):
    #FIXME: 
    m0=cube[0]
    m12=cube[1]
    A0=cube[2]
    tanb=cube[3]
    mt=cube[4]
    mz=cube[5]
    Delta_alpha_had=cube[6]
    if args.model == 'NUHM1':
        mh2=cube[7]

    # Get formatted input, Feel free to have a look !!!
    if args.model == 'cMSSM':
        all_params= inputs.get_mc_cmssm_inputs(m0,m12,tanb,A0    ,mt,mz,Delta_alpha_had)
    if args.model == 'NUHM1':
        all_params= inputs.get_mc_nuhm1_inputs(m0,m12,tanb,A0,mh2,mt,mz,Delta_alpha_had)

    if 'parameters' in args.verbose : 
        print(all_params)

    if args.tmp_dir:
        all_params.update({'tmp_dir':args.tmp_dir})

    all_params['lookup']=lookup
    all_params['verbose']=args.verbose
    try:
        slha_obj, combined_obs, stdouts = point.run_point( **all_params)
    except TypeError:
        return None
    #WARNING: this if for debugging: 
    # give parameters to the place where a problem occurs and trow it in stderr
    del all_params['lookup']
    del all_params['verbose']
    if ('errors' in args.verbose) : 
        any_error=False
        if not combined_obs:
            print("ERROR: in Spectrum Calculator",file=sys.stderr)
            any_error=True
        else:
            for name in ['FeynHiggs','Micromegas','BPhysics','SUSY-POPE']:
                if combined_obs[(name,'error')]:
                    print('ERROR: in {}'.format(name),file=sys.stderr)
                    any_error=True
        if any_error:
            print('\nParameters are: {}\n'.format(all_params),file=sys.stderr)
    return combined_obs, all_params 

def get_chi2(obs):
    constraints={name: all_constraints[name] for name in data_set}
    total, breakdown = Analyse.chi2(obs,constraints)
    return total


def myloglike(cube, ndim, nparams):
    obs,params=get_obs(cube,ndim)
            
    if obs: 
        chi2=get_chi2(obs)
        #RESULT ORIENTED: for sampling set error to default if error in one of the predictors  
        for name in ['FeynHiggs','Micromegas','BPhysics','SUSY-POPE']:
            if obs[(name,'error')]:
                chi2=default_chi
        obs[('tot_X2', 'all')]=chi2
    else:
        chi2=default_chi
        obs=params
    # write everything to root files
    if args.root_out:
        rootstore.write_point_to_root(obs)
    if args.pickle_out:
        with open('{}/{}.pkl'.format(args.multinest_dir, unique_str()),'wb') as pickle_file:
            pickle.dump(obs,pickle_file)
    if 'X' in args.verbose: 
        print("X^2={}".format(chi2))
    return -chi2


if __name__=="__main__" :

    if not os.path.exists(args.multinest_dir): os.mkdir(args.multinest_dir)

    #print whith verbosity options were selected
    print('SELECTED VERBOSITY OPTIONS:')
    print(args.verbose)

   #dump sampling info in the sampling file
    if not args.suppress_info:
        info=my_pprint.pformat(vars(args))
        fname='{}/mc_mn_info.txt'.format(args.multinest_dir)
        with open(fname,'w') as info_file:
            info_file.write(info)

    #open root file before calling the sampling algorithm
    if args.root_out:
        if not os.path.exists(args.root_out): os.makedirs(args.root_out)
        root.root_open(get_root_file_name(args.root_out))

    #run multinest
    multinest.run(LogLikelihood     = myloglike,
	        Prior                   = myprior,
            n_dims                  = len(param_ranges),
	        n_params                = None, 
	        n_clustering_params     = None, 
            wrapped_params          = None, 
	        multimodal              = args.multimodal, 
            const_efficiency_mode   = args.const_efficiency_mode, 
            n_live_points           = args.n_live_points , 
            evidence_tolerance      = args.evidence_tolerance,
            sampling_efficiency     = args.sampling_efficiency, 
	        n_iter_before_update    = args.n_iter_before_update, 
            null_log_evidence       = args.null_log_evidence,    #-1e90,
	        max_modes               = args.max_modes,
            outputfiles_basename    = '{}/root-'.format(args.multinest_dir), # 'root-' to get root-.txt
            seed                    = args.seed,
            verbose                 = ('multinest' in args.verbose), 
            resume                  = args.resume, 
            context                 = args.context,         #0, 
            write_output            = args.write_output ,    #True, 
            log_zero                = args.log_zero,         #-1e100, 
            max_iter                = args.max_iter,
            init_MPI                = args.init_MPI,        #False, 
            dump_callback           = None)
    #close root file after sampling
    if args.root_out:
        root.root_close()
    
