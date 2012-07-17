#! /usr/bin/env python

from ctypes import cdll, c_int, c_double, c_char_p, byref

FHlib = cdll.LoadLibrary('./libs/libmcfeynhiggs.so')
# const from FeynHiggs FIXME (src/inclue/SLHADefs.h)

mssmpart = 4
fieldren = 0
tanbren = 0
higgsmix = 2
p2approx = 0
looplevel = 2
Tl_mt = 1
tl_bot_resum = 1


def run_feynhiggs(filename) :
    FHlib.run_feynhiggs(filename, mssmpart, fieldren, tanbren, higgsmix,
            p2approx, looplevel, Tl_mt, tl_bot_resum)
    return

if __name__=='__main__':
    run_feynhiggs('post_ss.slha')
