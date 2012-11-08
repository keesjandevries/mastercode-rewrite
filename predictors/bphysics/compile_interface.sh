#!/bin/bash

SLHALIB=/home/hep/kjd110/mastercode-rewrite/SLHALib-2.2/x86_64-linux/
FCC=/home/hep/kjd110/mastercode-rewrite/SLHALib-2.2/x86_64-linux/../build/fcc

g++  -c  -o interface.o  bphysics.cc -I$SLHALIB/include 
gfortran -c  -o bphysics.o  bphysics.F -ffixed-line-length-none -I$SLHALIB/include 

g++ -o interface interface.o bphysics.o 
    -I$SLHALIB/include \
    -L$SLHALIB/lib -lSLHA \
    -lpthread -lfrtbegin -lgfortran -lm -lgcc_s -lgcc_s
