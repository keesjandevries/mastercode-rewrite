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

def run(filename, file_is_pipe=True) :
    utils.show_header(name)
    SIout = SuperISOPrecObs()
    # FIXME: to be honest this is stupid: we send our slhafile obj itno a pipe,
    # read it out and onto a tmp file -> maybe feature request in superiso?
    if file_is_pipe:
        filename = utils.make_file_from_pipe(filename)
    SIlib.run_superiso(filename, byref(SIout))
    utils.rm(filename)
    return get_values(SIout)
