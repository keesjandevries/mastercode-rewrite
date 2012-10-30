#! /usr/bin/env python

from ctypes import cdll, c_int, c_double, c_char_p, byref, Structure

from modules import mcoutput

MOlib = cdll.LoadLibrary('./libs/libmcmicromegas.so')

class MicromegasPrecObs(Structure):
    _fields_ = [('Omega', c_double), ('Bll', c_double), ('Bsg', c_double),
            ('SMbsg', c_double)]

def get_values(output):
    d = dict([(attr, getattr(output,attr)) for (attr, a_type) in
        output._fields_])
    return d

def run(filename) :
    mcoutput.header('micromegas')
    MOout = MicromegasPrecObs()
    MOlib.run_micromegas(filename, byref(MOout))
    return get_values(MOout)
