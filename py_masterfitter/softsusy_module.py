#! /usr/bin/env python

from ctypes import cdll
import SLHA_module

SPlib = cdll.LoadLibrary('./libs/libsoftpoint.so')
