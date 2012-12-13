#! /usr/bin/env python

from ctypes import cdll, c_int, c_double, c_char_p, byref, Structure

from mcrw.utils import setup_pipe, unique_str, ctypes_field_values

name = "Micromegas"
MOlib = cdll.LoadLibrary('packages/lib/libmcmicromegas.so')

class MicromegasPrecObs(Structure):
    _fields_ = [('Omega', c_double), ('Bll', c_double), ('Bsg', c_double),
            ('SMbsg', c_double)]

def run(slhadata, update=False) :
    MOout = MicromegasPrecObs()
    reader = lambda f: MOlib.run_micromegas(f, byref(MOout))
    writer = lambda f: slhadata.write(f)

    fname = "/tmp/mc-{u}".format(u=unique_str())
    writer(fname)
    reader(fname)
    return ctypes_field_values(MOout, name)
