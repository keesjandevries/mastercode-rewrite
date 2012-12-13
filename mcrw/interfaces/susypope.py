#! /usr/bin/env python

from ctypes import cdll, c_int, c_double, byref, Structure

from modules.utils import ctypes_field_values

name = "SUSY-POPE"
SPlib = cdll.LoadLibrary('packages/lib/libmcsusypope.so')

class susypopeFlags(Structure):
    _fields_ = [('LoopOption', c_int), ('IterOpt', c_int),
            ('Observables', c_int), ('HiggsOpt', c_int), ('Verbose', c_int),
            ('SMObsOpt', c_int)]
    def __init__(self, flags=None):
        if flags is None:
            self.LoopOption = 5
            self.IterOpt = 1
            self.Observables = 1
            self.HiggsOpt = 1
            self.Verbose = 1
            self.SMObsOpt = 1
        else:
            for attr, value in flags.iteritems():
                if attr in self.__dict__:
                    setattr(self,attr,value)

class susypopeNoneSLHA(Structure):
    _fields_ = [('DeltaAlfa5had', c_double), ('DeltaAlfaQED', c_double),
            ('ZWidthexp', c_double), ('M2phase', c_double),
            ('M1phase', c_double), ('MUEPhase', c_double),
            ('Atphase', c_double), ('Abphase', c_double),
            ('Atauphase', c_double), ('MB', c_double)]
    def __init__(self, flags=None):
        if flags is None:
            self.DeltaAlfa5had = 0.02749
            self.DeltaAlfaQED = 0.031497637
            self.ZWidthexp = 2.4952
            self.MB = 4.8
        else:
            for attr, value in flags.iteritems():
                if attr in self.__dict__:
                    setattr(self,attr,value)

# output
class susypopeObs(Structure):
    _fields_ = [('MSSMObs', c_double*35), ('SMObs', c_double*35),
            ('MW', c_double), ('sin_theta_eff', c_double),
            ('Gamma_z', c_double), ('Rl', c_double), ('Rb', c_double),
            ('Rc', c_double), ('Afb_b', c_double), ('Afb_c', c_double),
            ('Ab_16', c_double), ('Ac_17', c_double), ('Al', c_double),
            ('Al_fb', c_double), ('sigma_had', c_double)]

def run(slhadata, update=False):
    n_slha = susypopeNoneSLHA()
    flags = susypopeFlags()
    spout = susypopeObs()
    SPlib.run_susypope(byref(slhadata.data), byref(n_slha), byref(flags),
            byref(spout))
    return ctypes_field_values(spout, name)
