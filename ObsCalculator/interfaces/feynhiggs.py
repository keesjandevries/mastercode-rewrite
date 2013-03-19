#! /usr/bin/env python

from ctypes import cdll, c_int, c_double, byref, Structure

from tools import ctypes_field_values
from tools import set_obj_inputs_and_defaults

name = "FeynHiggs"
FHlib = cdll.LoadLibrary('packages/lib/libmcfeynhiggs.so')

nslhadata = FHlib.get_nslhadata()


default_inputs={
    'mssmpart'      :4, 
    'fieldren'      :0, 
    'tanbren'       :0, 
    'higgsmix'      :2,
    'p2approx'      :0, 
    'looplevel'     :2, 
    'tl_running_mt' :1, 
    'tl_bot_resum'  :1,
        }

class FeynHiggsOpts(Structure):
    _fields_ = [('mssmpart', c_int), ('fieldren', c_int), ('tanbren', c_int),
            ('higgsmix', c_int), ('p2approx', c_int), ('looplevel', c_int),
            ('tl_running_mt', c_int), ('tl_bot_resum', c_int)]
    def __init__(self,  defaults, inputs={}):
        set_obj_inputs_and_defaults(self,inputs,defaults)

class FeynHiggsPrecObs(Structure):
    _fields_ = [('gm2', c_double), ('DeltaRho', c_double),
            ('MWMSSM', c_double), ('MWSM', c_double), ('SW2effMSSM', c_double),
            ('SW2effSM', c_double), ('EDMeTh', c_double), ('EDMn', c_double),
            ('EDMHg', c_double), ('mh', c_double), ('mH', c_double),
            ('mA', c_double), ('mHpm', c_double)]

def run(slhadata, inputs=None, update=False) :
    assert len(slhadata) == nslhadata
    fhopts = FeynHiggsOpts(default_inputs,inputs)

    FHout = FeynHiggsPrecObs()
    error = FHlib.run_feynhiggs(byref(FHout), byref(fhopts), byref(slhadata.data),
            update)
    if error: print("ERROR: FH")
    return ctypes_field_values(FHout, name)
