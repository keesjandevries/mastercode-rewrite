#! /usr/bin/env python

from ctypes import cdll, c_int, c_double, c_char_p, byref, Structure

from modules import mcoutput

FHlib = cdll.LoadLibrary('./libs/libmcfeynhiggs.so')

mssmpart = 4
fieldren = 0
tanbren = 0
higgsmix = 2
p2approx = 0
looplevel = 2
Tl_mt = 1
tl_bot_resum = 1

class FeynHiggsPrecObs(Structure):
    _fields_ = [('DeltaRho', c_double), ('MWMSSM', c_double),
            ('MWSM', c_double), ('SW2effMSSM', c_double),
            ('SW2effSM', c_double), ('gminus2mu', c_double),
            ('EDMeTh', c_double), ('EDMn', c_double), ('EDMHg', c_double),
            ('bsgammaMSSM', c_double), ('bsgammaSM', c_double),
            ('DeltaMsMSSM', c_double), ('DeltaMsSM', c_double),
            ('BsmumuMSSM', c_double), ('BsmumuSM', c_double)]



def run(filename) :
    mcoutput.header('feynhiggs')
    FHout = FeynHiggsPrecObs()
    FHlib.run_feynhiggs(filename, mssmpart, fieldren, tanbren, higgsmix,
            p2approx, looplevel, Tl_mt, tl_bot_resum, byref(FHout))
    print dir(FHout)
    exit()
