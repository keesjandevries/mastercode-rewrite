#! /usr/bin/env python

from ctypes import cdll, c_double, byref, Structure
from tools import ctypes_field_values, return_c_double_array

ConstraintsLib = cdll.LoadLibrary('packages/lib/libmcconstraints.so')

#placeholder
def my_func(a,b):
    return a-b

class Constraint(object):
    def __init__(self, oids, data, func):
        self._oids=oids
        # place holders
        c_ints=0
        c_data=return_c_double_array(data)
        func=my_func
        self._obj=ConstraintsLib.new_GaussConstraint(c_ints,c_data,func)

