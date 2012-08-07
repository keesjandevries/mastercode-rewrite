#! /usr/bin/env python

_SLHAfile__MAX_SLHA_SIZE = 10000

from ctypes import cdll, create_string_buffer
SLHAlib = cdll.LoadLibrary('./libs/libmcslha.so')

class SLHAfile(object):
    def __init__(self):
        self.obj = SLHAlib.SLHAfile_new()
    def __str__(self):
        slha_str = create_string_buffer(__MAX_SLHA_SIZE)
        sz = SLHAlib.SLHAfile_getstr(self.obj, slha_str, __MAX_SLHA_SIZE)
        if sz >= __MAX_SLHA_SIZE:
            print "*** WARNING: SLHA file may be truncated"
        return slha_str.value
    def ReadFile(self, filename):
        SLHAlib.SLHAfile_ReadFile(self.obj, str(filename))

class SLHAblock(object):
    def __init__(self, name):
        self.obj = SLHAlib.SLHAblock_new(str(name))
    def __str__(self):
        block_str = create_string_buffer(__MAX_SLHA_SIZE)
        sz = SLHAlib.SLHAblock_getstr(self.obj, block_Str, __MAX_SLHA_SIZE)
        if sz >= __MAX_SLHA_SIZE:
            print "*** WARNING: SLHA block may be truncated"
        return block_str.value
