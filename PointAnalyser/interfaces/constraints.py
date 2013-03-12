#! /usr/bin/env python

from ctypes import cdll, c_void_p , c_int
from tools import ctypes_field_values, return_c_double_array, return_c_int_array

ConstraintsLib = cdll.LoadLibrary('packages/lib/libmcconstraints.so')

#placeholder
def my_func(a,b):
    return a-b

class Constraint(object):
    def __init__(self, oids, data, func):
        self._oids=oids
        int_oids=[i for i in range(len(oids))]
        c_ints=return_c_int_array(int_oids)
        c_data=return_c_double_array(data)
        #FIXME: not sure if c_ints are needed here
        c_ints_len=c_int(len(c_ints))
        c_data_len=c_int(len(c_data))
        self._obj=ConstraintsLib.new_GaussConstraint(c_ints,c_ints_len,c_data,c_data_len,c_void_p(func))
    
    def get_chi2(self,point):
        obs=[point[oid] for oid in self._oids]
        c_obs=return_c_double_array(obs)
        return ConstraintsLib.get_GaussChi2(c_void_p(self._obj), c_obs)

