#! /usr/bin/env python

from socket import gethostname
from os import getpid
import pipes

import SLHA_module
import softsusy_module
import feynhiggs_module

from ctypes import cdll, c_int, byref

def main( argv=None ) :

    # read our SLHA input file
    slha_file = SLHA_module.SLHAfile()
    slha_file.ReadFile("cmssm_in.slha")

    # run RGE
    softsusy_module.SPlib.softpoint_slhafile_api_( slha_file.obj )

    # open a pipe and write out processed SLHA file to it
    pipe_name = "/tmp/.mc-%s-%d" % ( gethostname(), getpid() )
    print pipe_name
    slha_pipe = pipes.Template()
    f = slha_pipe.open(pipe_name,'w')
    f.write( str(slha_file) )
    f.close()

    # print slha_file
    open( pipe_name ).read()


    y = c_int(0)
    feynhiggs_module.FHlib.fhsetdebug_(byref(y))
    feynhiggs_module.slharead( pipe_name )
    print "lololol3"
    

    return 0

if __name__ == "__main__":
    main()
