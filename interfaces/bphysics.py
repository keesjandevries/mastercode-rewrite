#! /usr/bin/env python

from ctypes import cdll, c_double, byref, Structure
from collections import OrderedDict

name = "BPhysics"
BPlib = cdll.LoadLibrary('packages/lib/libmcbphysics.so')

class BPhysicsPrecObs(Structure):
    _fields_= [('BRbsg', c_double), ('BRKpnn', c_double), ('RDMb', c_double),
            ('RDMs', c_double), ('RDMK', c_double), ('BRXsll', c_double),
            ('BRbtn', c_double), ('BRKl2', c_double), ('Psll', c_double),
            ('Pdll', c_double), ('Pllsapx', c_double)]

def get_values(output):
    d = OrderedDict([(attr, getattr(output,attr)) for (attr, a_type) in
        output._fields_])
    return {name: d}

def run(slhadata, update=False):
    BPout = BPhysicsPrecObs()
    BPlib.run_bphysics(byref(slhadata.data), byref(BPout))
    return get_values(BPout)
