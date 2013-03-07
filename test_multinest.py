#! /usr/bin/env python
import os, pprint
from collections import OrderedDict

from Samplers.interfaces import multinest
from ObsCalculator import point
from Storage import old_mc_rootstorage as rootstore

from PointAnalyser import Analyse
from PointAnalyser import Constraints_list

import Storage.interfaces.ROOT as root

if not os.path.exists("chains"): os.mkdir("chains")

# WARNING: THIS CODE NEEDS A MASSIVE CLEANUP
#####################!!!!!!!!!!!!!!!!!!###############
# global variable
# DON'T USE THIS OUTSIDE THIS SCRIPT
global g_lookup

def set_global_lookup(val ):
    global g_lookup
    g_lookup=val

def get_global_lookup():
    global g_lookup
    return g_lookup
#####################!!!!!!!!!!!!!!!!!!###############

param_ranges=OrderedDict([
        ('m0',(0,4000)),
        ('m12',(0,4000)),
        ('A0',(-5000,5000)),
        ('tanb',(1,65)), # softsusy only takes tanb>=1.
        ('mt',(171.4,175)),
        ('mz',(91.1833,91.1917)),
        ('Delta_alpha_had',(0.02729,0.02769))
       ] )

set_global_lookup(None)

default_chi=1e9

all_constraints=Constraints_list.constraints
#data_base_file='temp/test.db'
bpp = pprint.PrettyPrinter(indent=4, depth=3)

root.root_open('temp/test.root')

# WARNING: THIS CODE NEEDS A MASSIVE CLEANUP
def myprior(cube, ndim, nparams):
    for i, (name,(low,high)) in enumerate(param_ranges.items()):
        cube[i]=(high-low)*cube[i]+low

def get_obs(cube,ndim):
    slha_lookup=get_global_lookup()
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
#    m_vars = dict(list(input_vars.items()) + list(other_vars.items()))
    all_params['lookup']=slha_lookup
#    input_pars['verbose']=True
    try:
        slha_obj, combined_obs, stdouts = point.run_point(model=model, **all_params)
    except TypeError:
        return None

    if slha_lookup is None:
        set_global_lookup(slha_obj.get_lookup())
        print( "saved slhalookup")

    return combined_obs

def get_chi2(obs):
    data_set= [ 'Al(SLD)', 'Ab', 'Ac', 'Oh^2_mc8', 'Higgs125', 'BR(Bd->ll)',  
           'Gamma_Z', 'GZ_in', 'R(B->Xsll)', 'Al(P_tau)', 'MZ', 'R(D_ms)', 'MW', 'Afb_l', 
           'xenon100', 'DAlpha_had', 'R(Delta_mk)',  'sigma_had^0', 'Afb(c)', 
           'atlas5_m0_m12', 'Afb(b)',  'R(b->sg)', 'R(Dms)/R(Dmd)', 'R(B->taunu)', 
           'Rc', 'Rb',  'Rl', 'mc8_bsmm', 'sintheta_eff', 'Mt', 'R(K->lnu)', 'R(Kp->pinn)', 'gminus2mu', 'MATANB' ]
#    constraints=all_constraints.copy()
    constraints={name: all_constraints[name] for name in data_set}
    total, breakdown = Analyse.chi2(obs,constraints)
    print("Done this, chi2: ",total)
    return total

# WARNING: THIS CODE NEEDS A MASSIVE CLEANUP

def myloglike(cube, ndim, nparams):
    chi2=default_chi
    obs=get_obs(cube,ndim)
    if obs: 
        chi2=get_chi2(obs)
        obs[('tot_X2', 'all')]=chi2
        rootstore.write_point_to_root(obs)
    else: print("ERROR: in one of the programs")
    return -chi2

n_params = len(param_ranges)

multinest.run(myloglike, myprior, n_params, resume =False, verbose = True, sampling_efficiency = 0.3, n_live_points=5, max_iter=1)

# WARNING: THIS CODE NEEDS A MASSIVE CLEANUP
root.root_close()
