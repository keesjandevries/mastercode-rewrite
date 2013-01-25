#! /usr/bin/env python
import math
import os, threading, subprocess
import sys, select, argparse, pprint
from collections import OrderedDict

from Samplers.interfaces import multinest
from ObsCalculator import point
from tools import ansi_bold

from PointAnalyser import Analyse
from PointAnalyser import Constraints_list

if not os.path.exists("chains"): os.mkdir("chains")

param_ranges=OrderedDict([
        ('m0',(300,310)),
        ('m12',(900,910)),
       ] )

all_constraints=Constraints_list.constraints

def myprior(cube, ndim, nparams):
    for i, (name,(low,high)) in enumerate(param_ranges.items()):
        cube[i]=(high-low)*cube[i]+low

def get_obs(cube,ndim):
    model='cMSSM'
    m0=cube[0]
    m12=cube[1]
    input_vars = {
     'm0': m0, 'm12': m12, 'A0': -1323.97 , 'tanb': 16.26, 'sgnMu': 1 #MC8 bf
                }
    other_vars = {
            'mt': 173.2,
            'mgut': {'cMSSM': 2e16, 'pMSSM': 1.0e3}[model]
            }
    m_vars = dict(list(input_vars.items()) + list(other_vars.items()))
    input_pars={'SoftSUSY':m_vars}
    slha_file, observations , stdouts = point.run_point(model=model, **input_pars)

    combined_obs = dict(list(slha_file.items()) + list(observations.items()))
    return combined_obs

def get_chi2(obs):
    data_set=['xenon100']
#    constraints={name: all_constraints[name] for name in data_set}
    constraints=all_constraints.copy()
    total, breakdown = Analyse.chi2(obs,constraints)
    print(breakdown)

    return total


def myloglike(cube, ndim, nparams):
    obs=get_obs(cube,ndim)
    chi2=get_chi2(obs)
    return -chi2

n_params = len(param_ranges)

multinest.run(myloglike, myprior, n_params, resume =False, verbose = True, sampling_efficiency = 0.3, n_live_points=10, max_iter=2)
