#! /usr/bin/env python

from ctypes import cdll, c_void_p , c_int, c_double
from tools import ctypes_field_values, return_c_double_array, return_c_int_array

ConstraintsLib = cdll.LoadLibrary('packages/lib/libmcconstraints.so')



class Constraint(object):
    """
This Constraint class uses the constraint interface, which wraps
the c++ classes defined in Constraints.h.

Both GaussConstraint's and ContourConstraint's containt a memberfunction
GetChi2(double *). The argument to this function is a double array, and the 
position of the relevant observables is indicated by integers _internal_oids.

In the implementation here, these _internal_oids will be [0] , [0,1], ... depending
on how many observables are relevant for the calculation of the constraint.

The double array with these observables is obtained like this obs=[point[oid] for oid in self._oids]
where point is a dictionary, which can be accessed by self._oids.

This explanation should suffice to understand the code below.
    """
    def __init__(self, oids, data, func_name):
        self._oids=oids
        int_oids=[i for i in range(len(oids))]
        c_ints=return_c_int_array(int_oids)
        c_data=return_c_double_array(data)
        #FIXME: not sure if c_ints are needed here
        c_ints_len=c_int(len(c_ints))
        c_data_len=c_int(len(c_data))
        self._obj=ConstraintsLib.new_GaussConstraint(c_ints,c_ints_len,c_data,c_data_len,func_name.encode('ascii'))
    
    def get_chi2(self,point):
        obs=[point[oid] for oid in self._oids]
        c_obs=return_c_double_array(obs)
        # very important: set the return type to double
        ConstraintsLib.get_GaussChi2.restype=c_double
        return ConstraintsLib.get_GaussChi2(c_void_p(self._obj), c_obs)

