#! /usr/bin/env python

from ctypes import cdll, c_int, c_double, c_char_p, byref

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


def run(filename) :
    mcoutput.header('feynhiggs')
    FHlib.run_feynhiggs(filename, mssmpart, fieldren, tanbren, higgsmix,
            p2approx, looplevel, Tl_mt, tl_bot_resum)
