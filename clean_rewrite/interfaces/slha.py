#! /usr/bin/env python

from ctypes import cdll
SLHAlib = cdll.LoadLibrary('./libs/libmcslha.so')

class SLHAfile(object):
    def __init__(self) :
        self.obj = SLHAlib.SLHAfile_new()
    def __str__(self) :
       SLHAlib.SLHAfile_print( self.obj ) 
       return ""
    def ReadFile(self, filename):
        SLHAlib.SLHAfile_ReadFile(self.obj, str(filename))
