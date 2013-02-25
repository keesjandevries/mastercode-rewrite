#! /usr/bin/env python

from ctypes import cdll, c_double, byref, Structure

name = "ROOT module"
ROOTlib = cdll.LoadLibrary('packages/lib/libmcROOT.so')

def root_open(filename):
    ROOTlib.rootopen(filename.encode('ascii'))

def root_close():
    ROOTlib.rootclose()

def root_write(l):
    double_array=c_double*len(l)
    VARS=double_array(*l)
    ROOTlib.rootwrite(VARS,len(l))
