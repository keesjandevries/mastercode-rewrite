#! /usr/bin/env python

from ctypes import cdll, c_double, byref, Structure
from collections import OrderedDict

name = "LSP scattering"
LSPlib = cdll.LoadLibrary('packages/lib/libmclspscat.so')

class lspscatObs(Structure):
    _fields_ = [('s2out', c_double), ('ss2out', c_double), ('s3out', c_double),
            ('ss3out', c_double)]

class lspscatInputs(Structure):
    _fields_ = [('SigmaPiN', c_double), ('SigmaPiNerr', c_double)]

def get_values(output):
    d = OrderedDict([(attr, getattr(output,attr)) for (attr, a_type) in
        output._fields_])
    return {name: d}

def run(slhadata, update=False):
    LSPout = lspscatPrecObs()
    LSPlib.run_lspscat(byref(slhadata.data), byref(LSPout))
    return get_values(LSPout)

