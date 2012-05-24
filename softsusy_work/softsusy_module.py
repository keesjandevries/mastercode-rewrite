#! /usr/bin/env python

from ctypes import cdll, c_int

SPlib = cdll.LoadLibrary('./libmcsoftsusy.so')

class ss_DoubleVector(object):
    def __init__(self, size) :
        self.obj = SPlib.DoubleVector_new( c_int(size) )

test = ss_DoubleVector(3)
