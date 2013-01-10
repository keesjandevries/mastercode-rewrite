#! /usr/bin/env python

from ctypes import cdll, c_int, c_double, c_char_p, byref, Structure

import tools

name = 'SuperISO'
SIlib = cdll.LoadLibrary('packages/lib/libmcsuperiso.so')

class SuperISOPrecObs(Structure):
    _fields_ = [('SIbsg', c_double), ('SId0', c_double), ('SIgm2', c_double)]

def run(slhadata, update=False) :
    SIout = SuperISOPrecObs()
    fname = "/tmp/mc-{u}".format(u=tools.unique_str())
    slhadata.write(fname)
    SIlib.run_superiso(c_char_p(fname.encode('ascii')), byref(SIout))
    tools.rm(fname)
    return tools.ctypes_field_values(SIout, name)
