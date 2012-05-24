#! /usr/bin/env python

from ctypes import cdll, c_int, c_double

SPlib = cdll.LoadLibrary('./libmcsoftsusy.so')
# set our return types
SPlib.DoubleVector_display.restype = c_double

class ss_DoubleVector(object):
    def __init__(self, size = 0) :
        self.obj = SPlib.DoubleVector_new( size )
    def __getitem__( self, i ) :
        return SPlib.DoubleVector_display( self.obj, i )
    def __setitem__( self, index, value ) :
        SPlib.DoubleVector_set( self.obj, index, c_double(value) )
        

test = ss_DoubleVector(3)
print test[1]
test[1] = 5
print test[1]
