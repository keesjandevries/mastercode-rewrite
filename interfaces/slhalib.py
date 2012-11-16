#! /usr/bin/env python

from ctypes import cdll, c_int, c_double, c_char_p, byref, Structure
from collections import OrderedDict

from modules.utils import show_header

name = "FeynHiggs"
SLlib = cdll.LoadLibrary('packages/lib/libmcslhalib.so')
nslhadata = SLlib.get_nslhadata()

# this idea *requires* that the memory allocation of a complex type (C99, c++0x)
# is the same as an array of 2 doubles.  This is in the standard, but mileage
# with different compilers may vary
class Complex(Structure):
    _fields_ = [('re', c_double), ('im', c_double)]

class SLHAData(Structure):
    _fields_ = [('carray', Complex * nslhadata)]

def read(filename):
    data = SLHAData()
    SLlib.read_slha(filename, byref(data))
    return data
