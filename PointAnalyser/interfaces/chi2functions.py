#! /usr/bin/env python

from ctypes import cdll, c_void_p

Chi2Lib = cdll.LoadLibrary('packages/lib/libmcchi2functions.so')

def get_chi2_functions(l):
    function_map_pointer=Chi2Lib.get_new_GaussFunc_map()
    d={}
    for func in l:
        d[func]=Chi2Lib.get_GaussFunc(c_void_p(function_map_pointer),func.encode('ascii'))
    return d
