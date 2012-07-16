#! /usr/bin/env python

from ctypes import cdll, c_double, c_char_p, c_int, byref, POINTER
from array import array
FHlib = cdll.LoadLibrary('./libs/libFH.so')
#FHlib = cdll.LoadLibrary('./libtest.so')

# constant stolen from FeynHiggs... fortran wow...
nslhadata = c_int(5558)

def slharead( filename ) :
    filename = "post_ss.slha"

    error = c_int(0)
    slhadata = (c_double*nslhadata.value)()
    f_filename = c_char_p(filename)
    abort = c_int(1)

    f_len = c_int( len(filename) )

    # hidden argument at end fo len(f_filename)
    print "going to read this shit"
    FHlib.slharead_( byref(error), slhadata, f_filename, byref(abort), f_len )
    print "HNNNNN"
