#! /usr/bin/env python

from ctypes import cdll, c_double, byref, Structure

from tools import ctypes_field_values
from tools import set_obj_inputs_and_defaults

name = "LSP scattering"
LSPlib = cdll.LoadLibrary('packages/lib/libmclspscat.so')

default_inputs={
    'SigmaPiN'      : 50. ,
    'SigmaPiNerr'   : 7. ,
    }

class lspscatObs(Structure):
    _fields_ = [('s2out', c_double), ('ss2out', c_double), ('s3out', c_double),
            ('ss3out', c_double)]

class lspscatInputs(Structure):
    _fields_ = [('SigmaPiN', c_double), ('SigmaPiNerr', c_double)]
    def __init__(self,  defaults, inputs={}):
        set_obj_inputs_and_defaults(self,inputs,defaults)

def run(slhadata, inputs=None, update=False):
    LSPout = lspscatObs()
    LSPin  = lspscatInputs(default_inputs,inputs)
    LSPlib.run_lspscat(byref(slhadata.data), byref(LSPin), byref(LSPout))
    #FIXME: lspscat has no error handling that I know of, maybe should fix this later
    return ctypes_field_values(LSPout, name)
