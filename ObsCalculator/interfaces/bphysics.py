#! /usr/bin/env python

from ctypes import cdll, c_double, byref, Structure
from tools import ctypes_field_values

name = "BPhysics"
BPlib = cdll.LoadLibrary('packages/lib/libmcbphysics.so')

class BPhysicsPrecObs(Structure):
    _fields_= [('BRbsg', c_double), ('BRKpnn', c_double), ('RDMb', c_double),
            ('RDMs', c_double), ('RDMK', c_double), ('BRXsll', c_double),
            ('BRbtn', c_double), ('BRKl2', c_double), ('Psll', c_double),
            ('Pdll', c_double), ('Pllsapx', c_double)]

def run(slhadata, inputs=None, update=False):
    BPout = BPhysicsPrecObs()
    error=BPlib.run_bphysics(byref(slhadata.data), byref(BPout))
    if error: print('ERROR: Bphysics') 
    return ctypes_field_values(BPout, name,error)
