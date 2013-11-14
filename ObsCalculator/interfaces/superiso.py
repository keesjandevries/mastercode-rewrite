#! /usr/bin/env python

from ctypes import cdll, c_int, c_double, c_char_p, byref, Structure

from tools import rm , ctypes_field_values, unique_filename

name = 'SuperISO'
SIlib = cdll.LoadLibrary('packages/lib/libmcsuperiso.so')

class SuperISOPrecObs(Structure):
    _fields_ = [('SIbsg', c_double), ('SId0', c_double), ('SIgm2', c_double)]

def run(slhadata, inputs=None, update=False) :
    if inputs is None: inputs={}
    SIout = SuperISOPrecObs()
    fname=unique_filename(inputs.get('tmp_dir'))
    slhadata.write(fname)
    SIlib.run_superiso(c_char_p(fname.encode('ascii')), byref(SIout))
    rm(fname)
    #FIXME: No error handling yet
    return ctypes_field_values(SIout, name)
