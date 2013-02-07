#! /usr/bin/env python
import os, pprint
from collections import OrderedDict

from Samplers.interfaces import multinest
from ObsCalculator import point

from PointAnalyser import Analyse
from PointAnalyser import Constraints_list

if not os.path.exists("chains"): os.mkdir("chains")

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
        ('tanb',(0,65)),
       ] )

set_global_lookup(None)

default_chi=1e9

all_constraints=Constraints_list.constraints

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
    input_vars = {
     'm0': m0, 'm12': m12, 'A0': A0 , 'tanb': tanb, 'sgnMu': 1 #MC8 bf
                }
    print(input_vars)
    other_vars = {
            'mt': 173.2,
            'mgut': {'cMSSM': 2e16, 'pMSSM': 1.0e3}[model]
            }
    m_vars = dict(list(input_vars.items()) + list(other_vars.items()))
    input_pars={'SoftSUSY':m_vars}
    input_pars['mc_slha_update']=True
    input_pars['lookup']=slha_lookup
#    input_pars['verbose']=True
    try:
        slha_obj, observations , stdouts = point.run_point(model=model, **input_pars)
    except TypeError:
        return None

    bpp = pprint.PrettyPrinter(indent=4, depth=3)
    bpp.pprint(stdouts)

    slha_file=slha_obj.process()
    if slha_lookup is None:
        set_global_lookup(slha_obj.get_lookup())
        print( "saved slhalookup")

    combined_obs = dict(list(slha_file.items()) + list(observations.items()))
    return combined_obs

def get_chi2(obs):
    data_set=['xenon100']
#    constraints={name: all_constraints[name] for name in data_set}
    constraints=all_constraints.copy()
    total, breakdown = Analyse.chi2(obs,constraints)
    print("Done this, chi2: ",total)
    return total


def myloglike(cube, ndim, nparams):
    chi2=default_chi
    obs=get_obs(cube,ndim)
    if obs: chi2=get_chi2(obs)
    else: print("ERROR: in one of the programs")
    return -chi2

n_params = len(param_ranges)

multinest.run(myloglike, myprior, n_params, resume =False, verbose = True, sampling_efficiency = 0.3, n_live_points=5, max_iter=1)
