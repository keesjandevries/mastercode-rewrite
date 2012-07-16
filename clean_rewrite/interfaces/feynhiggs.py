#! /usr/bin/env python

from ctypes import cdll, c_int, c_double, c_char_p

FHlib = cdll.LoadLibrary('./libs/libmcfeynhiggs.so')

FHlib.foo()
