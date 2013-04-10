#! /usr/bin/env python

from ctypes import cdll, c_int, c_double, byref, Structure

from tools import ctypes_field_values
from tools import set_obj_inputs_and_defaults

name = "SUSY-POPE"
SPlib = cdll.LoadLibrary('packages/lib/libmcsusypope.so')

default_inputs={   
    'flags': 
     {  'LoopOption'    : 5,
        'IterOpt'       : 1,
        'Observables'   : 1,
        'HiggsOpt'      : 1,
        'Verbose'       : 1,
        'SMObsOpt'      : 1
     },
     'non_slha_inputs' : 
     {  'DeltaAlfa5had' : 0.02749,
        'DeltaAlfaQED'  : 0.031497637,
        'ZWidthexp'     : 2.4952,
        'MB'            : 4.8,
        'M2phase'       : 0.,
        'M1phase'       : 0., 
        'MUEPhase'      : 0.,
        'Atphase'       : 0., 
        'Abphase'       : 0.,
        'Atauphase'     : 0., 
     },
}

class susypopeFlags(Structure):
    _fields_ = [('LoopOption', c_int), ('IterOpt', c_int),
            ('Observables', c_int), ('HiggsOpt', c_int), ('Verbose', c_int),
            ('SMObsOpt', c_int)]
    def __init__(self,  defaults, inputs={}):
        set_obj_inputs_and_defaults(self,inputs,defaults)

class susypopeNoneSLHA(Structure):
    _fields_ = [('DeltaAlfa5had', c_double), ('DeltaAlfaQED', c_double),
            ('ZWidthexp', c_double), ('M2phase', c_double),
            ('M1phase', c_double), ('MUEPhase', c_double),
            ('Atphase', c_double), ('Abphase', c_double),
            ('Atauphase', c_double), ('MB', c_double)]
    def __init__(self,  defaults, inputs={}):
        set_obj_inputs_and_defaults(self,inputs,defaults)

# output
class susypopeObs(Structure):
    _fields_ = [('MSSMObs', c_double*35), ('SMObs', c_double*35)]

def get_relevant_observables(all_obs):
    all_obs_d=ctypes_field_values(all_obs, name)
    d={
        'MW'             :  all_obs_d[(name,'MSSMObs')][0 ],
        'sin_theta_eff'  :  all_obs_d[(name,'MSSMObs')][26],
        'Gamma_z'        :  all_obs_d[(name,'MSSMObs')][10],
        'Rl'             :  all_obs_d[(name,'MSSMObs')][21],
        'sigma_had'      :  all_obs_d[(name,'MSSMObs')][20],
        'Rb'             :  all_obs_d[(name,'MSSMObs')][25],
        'Rc'             :  all_obs_d[(name,'MSSMObs')][24],
        'Al'             :  all_obs_d[(name,'MSSMObs')][29],
        'Ab'             :  all_obs_d[(name,'MSSMObs')][30],
        'Ac'             :  all_obs_d[(name,'MSSMObs')][31],
        'Afb_l'          :  all_obs_d[(name,'MSSMObs')][32],
        'Afb_b'          :  all_obs_d[(name,'MSSMObs')][33],
        'Afb_c'          :  all_obs_d[(name,'MSSMObs')][34],}
    return {(name,obs):val for obs,val in d.items()}

def run(slhadata, inputs=None, update=False):
    #FIXME: not entirely sure if this is the most elegant way of doing it.
    # We somehow need to set the defaults for the susypope flags and none-slhainputs
    if inputs is None:
        inputs={}
    verbose = inputs.get('verbose',False)
    flags  = susypopeFlags(default_inputs['flags'],inputs.get('flags'))
    n_slha = susypopeNoneSLHA(default_inputs['non_slha_inputs'],inputs.get('non_slha_inputs'))

    spout = susypopeObs()
    error=SPlib.run_susypope(byref(slhadata.data), byref(n_slha), byref(flags),
            byref(spout),verbose)
#    susypope_outputs=ctypes_field_values(spout, name)
    susypope_outputs=get_relevant_observables(spout)
    susypope_outputs[(name,'GZ_in')]=n_slha.ZWidthexp
    susypope_outputs[(name,'DAlpha_had_in')]=n_slha.DeltaAlfa5had
    susypope_outputs[(name,'error')]=error
    return susypope_outputs
