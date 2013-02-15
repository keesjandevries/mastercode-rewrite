#! /usr/bin/env python

from ctypes import cdll, c_double, byref, Structure

#from tools import ctypes_field_values
#from tools import set_obj_inputs_and_defaults

name = "ROOT module"
ROOTlib = cdll.LoadLibrary('packages/lib/libmcROOT.so')


#class lspscatObs(Structure):
#    _fields_ = [('s2out', c_double), ('ss2out', c_double), ('s3out', c_double),
#            ('ss3out', c_double)]


#def run(slhadata, inputs=None, update=False):
#    LSPout = lspscatObs()
#    LSPin  = lspscatInputs(default_inputs,inputs)
#    LSPlib.run_lspscat(byref(slhadata.data), byref(LSPin), byref(LSPout))
#    return ctypes_field_values(LSPout, name)

def root_open(filename):
    ROOTlib.rootopen(filename.encode('ascii'))

def root_close():
    ROOTlib.rootclose()

def root_write(l):
    double_array=c_double*len(l)
    vars=double_array(*l)
    ROOTlib.rootwrite(vars,len(l))
