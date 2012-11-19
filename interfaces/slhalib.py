#! /usr/bin/env python

from ctypes import cdll, c_int, c_double, c_char_p, byref, Structure
from collections import OrderedDict
from modules.utils import c_complex
from modules.utils import pipe_object_to_function

name = "FeynHiggs"
SLlib = cdll.LoadLibrary('packages/lib/libmcslhalib.so')
nslhadata = SLlib.get_nslhadata()

# this idea *requires* that the memory allocation of a complex type (C99, c++0x)
# is the same as an array of 2 doubles.  This is in the standard, but mileage
# with different compilers may vary
class SLHAData(Structure):
    _fields_ = [('carray', c_complex * nslhadata)]

class SLHA(object):
    def __init__(self, data=""):
        if data:
            pipe_object_to_function(data, self.read)

    def read(self, filename):
        print "made it into read function"
        self.data = SLHAData()
        SLlib.read_slha(filename, byref(self.data))
