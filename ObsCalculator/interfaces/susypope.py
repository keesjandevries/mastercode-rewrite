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
    _fields_ = [('MSSMObs', c_double*35), ('SMObs', c_double*35),
            ('MW', c_double), ('sin_theta_eff', c_double),
            ('Gamma_z', c_double), ('Rl', c_double), ('Rb', c_double),
            ('Rc', c_double), ('Afb_b', c_double), ('Afb_c', c_double),
            ('Ab_16', c_double), ('Ac_17', c_double), ('Al', c_double),
            ('Al_fb', c_double), ('sigma_had', c_double)]

def run(slhadata, inputs=None, update=False):
    #FIXME: not entirely sure if this is the most elegant way of doing it.
    # We somehow need to set the defaults for the susypope flags and none-slhainputs
    if inputs is None:
        inputs={}
    flags  = susypopeFlags(default_inputs['flags'],inputs.get('flags'))
    n_slha = susypopeNoneSLHA(default_inputs['non_slha_inputs'],inputs.get('non_slha_inputs'))

    spout = susypopeObs()
    SPlib.run_susypope(byref(slhadata.data), byref(n_slha), byref(flags),
            byref(spout))
    susypope_outputs=ctypes_field_values(spout, name)
    susypope_outputs[(name,'GZ_in')]=n_slha.ZWidthexp
    del susypope_outputs[(name,'MSSMObs')]
    del susypope_outputs[(name,'SMObs')]
    return susypope_outputs
