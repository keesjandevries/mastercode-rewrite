#! /usr/bin/env python

from ctypes import cdll, c_int, c_double, c_char_p, byref

FHlib = cdll.LoadLibrary('./libs/libmcfeynhiggs.so')
# const from FeynHiggs FIXME (src/inclue/SLHADefs.h)

def slharead(filename) :

    print "lulz interface"
    FHlib.initFH(filename) # c_char_p...
    #FHlib.null_op()
    print "HNNNNN"

filename = "post_ss.slha"
slharead(filename)
