#! /usr/bin/env python

from ctypes import cdll, c_int, c_double, c_char_p, byref, Structure

from tools import  ctypes_field_values, rm, unique_filename

name = "Micromegas"
MOlib = cdll.LoadLibrary('packages/lib/libmcmicromegas.so')

class MicromegasPrecObs(Structure):
    _fields_ = [('Omega', c_double), ('Bll', c_double), ('Bsg', c_double),
            ('SMbsg', c_double),('sigma_p_si',c_double)]

def run(slhadata, inputs=None, update=False) :
    if inputs is None: inputs={}

    MOout = MicromegasPrecObs()
    reader = lambda f: MOlib.run_micromegas(c_char_p(f.encode('ascii')), byref(MOout))
    writer = lambda f: slhadata.write(f)

    fname=unique_filename(inputs.get('tmp_dir'))
    writer(fname)
    reader(fname)
    rm(fname)
    return ctypes_field_values(MOout, name)
