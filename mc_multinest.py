#! /usr/bin/env python
import os, pprint, argparse, sys,pickle ,re, json, numpy
from collections import OrderedDict

#FIXME: use interface from github though check performance!!!!
from Samplers.interfaces import multinest
from ObsCalculator import point, inputs
from Storage import old_mc_rootstorage as rootstore

from PointAnalyser import Analyse
from PointAnalyser import Constraints_list

import Storage.interfaces.ROOT as root
from ObsCalculator.interfaces.slhalib import SLHA

from tools import unique_str,import_predictor_modules

from User.data_sets import data_sets
import User.predictors

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
    mcpp.add_argument('--predictors',default='default',choices=User.predictors.predictors.keys(),
            help='specify key from \'predictors\' dictionary in User/predictors.py')
    mcpp.add_argument('--tmp-dir',  dest='tmp_dir', action='store', type=str,
            default=None, help='directory where temporary files get stored')
    mcpp.add_argument('--verbose'    , '-v', dest='verbose'  , action='store', 
            nargs="+", help='verbosity, e.g. parameters, X, errors, multinest, or mcpp verbosity',default=[])
    mcpp.add_argument('--output-root' , '-o', dest='root_out', action='store', 
            default='chains/',  help='output root directory ')
#    mcpp.add_argument('--root-prefix' ,  action='store', 
#            default='cmssm-multinest-step-',  help='output root file prefix ')
    mcpp.add_argument('--suppress-mc-info', dest='suppress_info', action='store_true', 
            default=False,  help='suppress dumping the multinest parameters. Not recommended')
    mcpp.add_argument('--pickle-out', dest='pickle_out', action='store_true', 
            default=False,  help='This is what we want. Store points to pickled dictionaries: unique_string.pkl')
    mcpp.add_argument('--data-set'  ,  dest='data_set'  , action='store', 
            default="pmssm_with_Oh2", help='data set for X^2 calculation')
    mcpp.add_argument('--model', default='pMSSM8', help='Model that SoftSUSY takes', choices=['cMSSM','NUHM1','pMSSM8','pMSSM10'])
    mcpp.add_argument('--nuisance-parameter-ranges', default='User/nuisance_parameter_ranges.json', 
            help='json file with parameter ranges for mt,mz,delta_alpha_had')
    mcpp.add_argument('--cmssm-ranges', default='User/cmssm_ranges.json', 
            help='json file with parameter ranges for m0,m12,tanb,A0')
    mcpp.add_argument('--nuhm1-ranges', default='User/nuhm1_ranges.json', 
            help='json file with parameter ranges for m0,m12,tanb,A0,mh2')
    mcpp.add_argument('--pmssm8-ranges', default='User/pmssm8_ranges.json', 
            help='json file with parameter ranges for msq12,msq3,msl,M1,A,MA,tanb,mu')
    mcpp.add_argument('--pmssm10-ranges',  
            help='json file with parameter ranges for msq12,msq3,msl,M1,M2,M3,A,MA,tanb,mu')
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
    root_prefix='{}-mn-step-'.format(args.model)
    root_file_step_numbers=[ int(re.search(r'\d+', f.replace(root_prefix,'')).group()) 
            for f in os.listdir(output_dir) if root_prefix in f]
    if not len(root_file_step_numbers) == 0: 
        current_step=max(root_file_step_numbers)+1
    else: 
        current_step=1
    return '{}/{}{}.root'.format(output_dir,root_prefix,current_step)

def get_param_ranges():
    #FIXME: re-implement cMSSM and NUHM1/2 at some point 
    with open(args.nuisance_parameter_ranges,'r') as f:
        nuisance_parameter_ranges=json.load(f)
    if args.model == 'cMSSM':
        with open(args.cmssm_ranges,'r') as f:
            cmssm_ranges=json.load(f)
        cmssm_ranges.update(nuisance_parameter_ranges)
        #The order here should match that of inputs.get_mc_pmssm8_inputs(... )
        param_ranges= OrderedDict([(name, cmssm_ranges[name]) for name in 
            ['m0','m12','tanb','A0','mt','mz','delta_alpha_had']])
    if args.model == 'NUHM1':
        with open(args.nuhm1_ranges,'r') as f:
            nuhm1_ranges=json.load(f)
        nuhm1_ranges.update(nuisance_parameter_ranges)
        #The order here should match that of inputs.get_mc_pmssm8_inputs(... )
        param_ranges= OrderedDict([(name, nuhm1_ranges[name]) for name in 
            ['m0','m12','tanb','A0','mh2','mt','mz','delta_alpha_had']])
    if args.model == 'pMSSM8':
        with open(args.pmssm8_ranges,'r') as f:
            pmssm8_ranges=json.load(f)
        pmssm8_ranges.update(nuisance_parameter_ranges)
        #The order here should match that of inputs.get_mc_pmssm8_inputs(... )
        param_ranges= OrderedDict([(name, pmssm8_ranges[name]) for name in 
            ['msq12','msq3','msl', 'M1', 'A','MA','tanb','mu','mt','mz','delta_alpha_had']])
    if args.model == 'pMSSM10':
        with open(args.pmssm10_ranges,'r') as f:
            pmssm10_ranges=json.load(f)
        pmssm10_ranges.update(nuisance_parameter_ranges)
        #The order here should match that of inputs.get_mc_pmssm10_inputs(... )
        param_ranges= OrderedDict([(name, pmssm10_ranges[name]) for name in 
            ['msq12','msq3','msl', 'M1','M2','M3', 'A','MA','tanb','mu','mt','mz','delta_alpha_had']])
    return param_ranges

##################################################
# DEFINITIONS NEEDED inside myprior, and myloglike 
##################################################
#arguments from command line
args = parse_args()
#parameter ranges
param_ranges=get_param_ranges()
#default X^2 penalty in case of errors
default_chi=-10*args.log_zero
#lookup dictionary for initiating SLHA() objects
lookup=SLHA().get_lookup()
#constraint objects
all_constraints=Constraints_list.constraints
#pretty printer
my_pprint = pprint.PrettyPrinter(indent=4, depth=3)
#constraints list
data_set=data_sets[args.data_set]
#predictors
predictors=User.predictors.get(args.predictors)
predictor_modules=import_predictor_modules(predictors)
###############################################

def myprior(cube, ndim, nparams):
    for i, (name,(low,high)) in enumerate(param_ranges.items()):
        cube[i]=(high-low)*cube[i]+low

def get_obs(cube,ndim):
    #make a python list out of the cube
    parameters=[cube[i] for i in range(ndim)]
    # start from clean directory as input for run_point
    all_params={}
    all_params.update(predictor_modules)
    # add predictors

    # Get formatted input. See what is looks like with option "-v inputs"  
    if args.model == 'cMSSM':
        all_params.update( inputs.get_mc_cmssm_inputs(*parameters))
    if args.model == 'NUHM1':
        all_params.update( inputs.get_mc_nuhm1_inputs(*parameters))
    if args.model == 'pMSSM8':
        all_params.update( inputs.get_mc_pmssm8_inputs(*parameters))
    if args.model == 'pMSSM10':
        all_params.update( inputs.get_mc_pmssm10_inputs(*parameters))

    if 'parameters' in args.verbose:
        print(*parameters)

    if 'inputs' in args.verbose : 
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
        if not combined_obs:
            print("ERROR: in Spectrum Calculator",file=sys.stderr)
        else:
            for name in ['FeynHiggs','Micromegas','BPhysics','SUSY-POPE']:
                if combined_obs[(name,'error')]:
                    print('ERROR: in {}'.format(name),file=sys.stderr)
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
        #FIXME: consider to not set Micromegas error to infinity, since it crashes on neutralino!=lsp
        for name in ['FeynHiggs','Micromegas','BPhysics','SUSY-POPE']:
            if obs[(name,'error')]:
                chi2=default_chi
        if numpy.isnan(chi2):
            chi2=default_chi
        obs[('tot_X2', 'all')]=chi2
    else:
        chi2=default_chi
        obs=params
    # write everything to root files
    if args.root_out:
        VARS=rootstore.get_VARS(obs, args.model)
        root.root_write(VARS)
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
    
