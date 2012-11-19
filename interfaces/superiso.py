#! /usr/bin/env python

from ctypes import cdll, c_int, c_double, c_char_p, byref, Structure
from collections import OrderedDict

from modules import utils

name = 'SuperISO'
SIlib = cdll.LoadLibrary('packages/lib/libmcsuperiso.so')

class SuperISOPrecObs(Structure):
    _fields_ = [('SIbsg', c_double), ('SId0', c_double), ('SIgm2', c_double)]

def get_values(output):
    d = OrderedDict([(attr, getattr(output,attr)) for (attr, a_type) in
        output._fields_])
    return {name: d}

def run(slhadata, update=False) :
    SIout = SuperISOPrecObs()
    fname = "/tmp/mc-{u}".format(u=utils.unique_str())
    fo = open(fname, 'w')
    fo.write(str(slhadata))
    SIlib.run_superiso(fname, byref(SIout))
    utils.rm(fname)
    return get_values(SIout)
