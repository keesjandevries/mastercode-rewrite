#! /usr/bin/env python

from ctypes import cdll, c_int, c_double, c_char_p, byref

FHlib = cdll.LoadLibrary('./libs/libmcfeynhiggs.so')
# const from FeynHiggs FIXME (src/inclue/SLHADefs.h)

nslhadata = c_int(5558)

class FH_COMPLEX(object):
    def __init__(self, re=0, img=0):
        self.obj = FHlib.COMPLEX_new(c_double(re),c_double(img))


def slharead(filename) :
    filename = "post_ss.slha"

    print "lulz interface"
    FHlib.initFH(filename) # c_char_p...
    print "HNNNNN"
