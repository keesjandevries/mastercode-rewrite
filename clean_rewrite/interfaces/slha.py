#! /usr/bin/env python

_SLHAfile__MAX_SLHA_SIZE = 10000

from ctypes import cdll, create_string_buffer
SLHAlib = cdll.LoadLibrary('./libs/libmcslha.so')

class SLHAfile(object):
    def __init__(self) :
        self.obj = SLHAlib.SLHAfile_new()
    def __str__(self) :
        str = create_string_buffer(__MAX_SLHA_SIZE)
        sz = SLHAlib.SLHAfile_getstr(self.obj, str, __MAX_SLHA_SIZE)
        if sz >= __MAX_SLHA_SIZE:
            print "*** WARNING: SLHA may be truncated"
        return str.value
    def ReadFile(self, filename):
        SLHAlib.SLHAfile_ReadFile(self.obj, str(filename))
