#! /usr/bin/env python

from ctypes import cdll, c_int, c_double, byref, Structure

from modules.utils import ctypes_field_values

name = "FeynHiggs"
FHlib = cdll.LoadLibrary('packages/lib/libmcfeynhiggs.so')

nslhadata = FHlib.get_nslhadata()

class FeynHiggsOpts(Structure):
    _fields_ = [('mssmpart', c_int), ('fieldren', c_int), ('tanbren', c_int),
            ('higgsmix', c_int), ('p2approx', c_int), ('looplevel', c_int),
            ('tl_running_mt', c_int), ('tl_bot_resum', c_int)]
    def __init__(self, mssmpart, fieldren, tanbren, higgsmix, p2approx,
            looplevel, tl_running_mt, tl_bot_resum):
            self.mssmpart = mssmpart
            self.fieldren = fieldren
            self.tanbren = tanbren
            self.higgsmix = higgsmix
            self.p2approx = p2approx
            self.looplevel = looplevel
            self.tl_running_mt = tl_running_mt
            self.tl_bot_resum = tl_bot_resum

class FeynHiggsPrecObs(Structure):
    _fields_ = [('gm2', c_double), ('DeltaRho', c_double),
            ('MWMSSM', c_double), ('MWSM', c_double), ('SW2effMSSM', c_double),
            ('SW2effSM', c_double), ('EDMeTh', c_double), ('EDMn', c_double),
            ('EDMHg', c_double), ('mh', c_double), ('mH', c_double),
            ('mA', c_double), ('mHpm', c_double)]

def run(slhadata, update=False, fhopts=None) :
    assert len(slhadata) == nslhadata
    if fhopts is None:
        fhopts = FeynHiggsOpts(mssmpart=4, fieldren=0, tanbren=0, higgsmix=2,
                p2approx=0, looplevel=2, tl_running_mt=1, tl_bot_resum=1)

    FHout = FeynHiggsPrecObs()
    FHlib.run_feynhiggs(byref(FHout), byref(fhopts), byref(slhadata.data),
            update)
    return ctypes_field_values(FHout, name)
