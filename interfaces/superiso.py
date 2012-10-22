from ctypes import cdll, c_int, c_double, c_char_p, byref, Structure

from modules import mcoutput

SIlib = cdll.LoadLibrary('./libs/libmcsuperiso.so')

class SuperISOPrecObs(Structure):
    _fields_ = [('SIbsg', c_double), ('SId0', c_double), ('SIgm2', c_double)]

def get_values(output):
    d = dict([(attr, getattr(output,attr)) for (attr, a_type) in
        output._fields_])
    return d

def run(filename) :
    mcoutput.header('superiso')
    SIout = SuperISOPrecObs()
    SIlib.run_superiso(filename, byref(SIout))
    return SIout
