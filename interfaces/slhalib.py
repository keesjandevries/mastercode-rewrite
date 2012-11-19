#! /usr/bin/env python

from ctypes import cdll, c_int, c_double, c_char_p, byref, Structure
from collections import OrderedDict
from modules.utils import c_complex, pipe_object_to_function, unique_str

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

    def __str__(self):
        tmp_name = "/tmp/mc-{u}".format(u=unique_str())
        SLlib.write_slha(tmp_name, byref(self.data))
        return open(tmp_name).read()
# FIXME: this needs to use pipe to function but at the moment fortran doesnt
# work with writing to pipes

    def read(self, filename):
        self.data = SLHAData()
        SLlib.read_slha(filename, byref(self.data))

def send_to_predictor(slhadata, predictor, update=False):
    return predictor.run(slhadata, update)
