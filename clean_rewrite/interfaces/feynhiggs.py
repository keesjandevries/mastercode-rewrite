#! /usr/bin/env python

from ctypes import cdll, c_int, c_double, c_char_p, byref

FHlib = cdll.LoadLibrary('./libs/libmcfeynhiggs.so')

FHlib.foo()

#! /usr/bin/env python

# constant stolen from FeynHiggs... fortran wow...
nslhadata = c_int(5426)

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

(int *error, COMPLEX *slhadata, const char *filename, const int abort)
