#! /usr/bin/env python

from ctypes import cdll, c_double, byref, Structure

name = "ROOT reading module"
ROOT_readlib = cdll.LoadLibrary('packages/lib/libmcROOT_read.so')


def root_open(filename):
    ROOT_readlib.rootopen(filename.encode('ascii'))

def root_close():
    ROOT_readlib.rootclose()

def root_get_n_vars():
    return ROOT_readlib.getNvars()

def root_read(entry):
    nvars=root_get_n_vars()
    double_array=c_double*nvars
    l=[0.]*nvars
    VARS=double_array(*l)
    ROOT_readlib.rootread(VARS,entry)
    return [v for v in VARS]
