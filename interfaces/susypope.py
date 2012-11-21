#! /usr/bin/env python

from ctypes import cdll, c_int, c_double, c_char_p, byref, Structure
from collections import OrderedDict

from modules.utils import c_complex

name = "SUSY-POPE"
SPlib = cdll.LoadLibrary('packages/lib/libmcsusypope.so')

default_gammaZ = 2.4952
default_alphaHad = 0.02749

    # DEFAULTS
    #susypopeFlags opts(5,1,1,1,1,1);
    #inp.flags=opts;
    #inp.n_slha.DeltaAlfa5had = 0.02749;
    #inp.n_slha.DeltaAlfaQED  = 0.031497637;
    #inp.n_slha.ZWidthexp     = 2.4952;

class SUSYPOPEOpts(Structure):
    _fields_ = [('gammaZ', c_double), ('alphaHad', c_double)]
    def __init__(self, gammaZ, alphaHad):
        self.gammaZ = gammaZ
        self.alphaHad = alphaHad

class susypopeFlags(Structure):
    _fields_ = [('LoopOption', c_int), ('IterOpt', c_int),
            ('Observables', c_int), ('HiggsOpt', c_int), ('Verbose', c_int),
            ('SMObsOpt', c_int)]

class susypopeNoneSLHA(Structure):
    _fields_ = [('DeltaAlfa5had', c_double), ('DeltaAlfaQED', c_double),
            ('ZWidthexp', c_double), ('M2phase', c_double),
            ('M1phase', c_double), ('MUEPhase', c_double),
            ('Atphase', c_double), ('Abphase', c_double),
            ('Atauphase', c_double), ('MB', c_double)]

class susypopeIn(Structure):
    _fields_ = [('n_slha', susypopeNoneSLHA), ('flags', susypopeFlags)]


class susypopeObs(Structure):
    _fields_ = [('MSSMObs', c_double*35), ('SMObs', c_double*35),
        ('MW', c_double), ('sin_theta_eff', c_double), ('Gamma_z', c_double),
        ('Rl', c_double), ('Rb', c_double), ('Rc', c_double),
        ('Afb_b', c_double), ('Afb_c', c_double), ('Ab_16', c_double),
        ('Ac_17', c_double), ('Al', c_double), ('Al_fb', c_double),
        ('sigma_had', c_double)]

class SUSYPOPEObs(Structure):
    _fields_ = [('MSSMObs', c_double*35), ('SMObs', c_double*35),
            ('MW', c_double), ('sin_theta_eff', c_double),
            ('Gamma_z', c_double), ('Rl', c_double), ('Rb', c_double),
            ('Rc', c_double), ('Afb_b', c_double), ('Afb_c', c_double),
            ('Ab_16', c_double), ('Ac_17', c_double), ('Al', c_double),
            ('Al_fb', c_double), ('sigma_had', c_double)]

def run(slhadata, update, spopts=None):
    if spopts is None:
        spopts = SUSYPOPEOpts(gammaZ=2.4952, alphaHad=0.02749)

    spout = SUSYPOPEObs()
    SPlib.run_susypope(byref(slhadata.data), byref(spopts), byref(SPout))
