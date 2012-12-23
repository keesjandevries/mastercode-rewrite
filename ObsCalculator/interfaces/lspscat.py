#! /usr/bin/env python

from ctypes import cdll, c_double, byref, Structure

from mcrw.utils import ctypes_field_values

name = "LSP scattering"
LSPlib = cdll.LoadLibrary('packages/lib/libmclspscat.so')

class lspscatObs(Structure):
    _fields_ = [('s2out', c_double), ('ss2out', c_double), ('s3out', c_double),
            ('ss3out', c_double)]

class lspscatInputs(Structure):
    _fields_ = [('SigmaPiN', c_double), ('SigmaPiNerr', c_double)]
    def __init__(self, SigmaPiN, SigmaPiNerr):
        self.SigmaPiN = SigmaPiN
        self.SigmaPiNerr = SigmaPiNerr

def run(slhadata, update=False):
    LSPout = lspscatObs()
    LSPin = lspscatInputs(50,14)
    LSPlib.run_lspscat(byref(slhadata.data), byref(LSPin), byref(LSPout))
    return ctypes_field_values(LSPout, name)
