from ctypes import cdll, c_int, c_double, c_char_p, byref, Structure

from modules import mcoutput, utils

SIlib = cdll.LoadLibrary('./libs/libmcsuperiso.so')

class SuperISOPrecObs(Structure):
    _fields_ = [('SIbsg', c_double), ('SId0', c_double), ('SIgm2', c_double)]

def get_values(output):
    d = dict([(attr, getattr(output,attr)) for (attr, a_type) in
        output._fields_])
    return d

def run(filename, make_perm=True) :
    mcoutput.header('superiso')
    SIout = SuperISOPrecObs()
    # FIXME: to be honest this is stupid: we send our slhafile obj itno a pipe,
    # read it out and onto a tmp file -> maybe feature request in superiso?
    if make_perm:
        filename = utils.make_file_from_pipe(filename)
    SIlib.run_superiso(filename, byref(SIout))
    utils.rm(filename)
    return SIout
