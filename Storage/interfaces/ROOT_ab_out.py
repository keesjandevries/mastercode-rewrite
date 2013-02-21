#! /usr/bin/env python

from ctypes import cdll, c_double, byref, Structure

#WARNING: this code is result oriented. 
#No deep thought has gone into this

name = "ROOT_ab_out module"
ROOT_ab_outlib = cdll.LoadLibrary('packages/lib/libmcROOT_ab_out.so')


def root_open(filename):
    ROOT_ab_outlib.rootopen(filename.encode('ascii'))

def root_close():
    ROOT_ab_outlib.rootclose()

def root_write(l_in,l_out):
    n=max(len(l_in),len(l_out))
    double_array_in=c_double*n    
    double_array_out=c_double*n    
    VARS_in=double_array_in(*l_in)
    VARS_out=double_array_out(*l_out)
    ROOT_ab_outlib.rootwrite(VARS_in,VARS_out,n)
