#!/bin/bash

SLHALIB=/home/hep/kjd110/mastercode-rewrite/SLHALib-2.2/x86_64-linux/
FCC=/home/hep/kjd110/mastercode-rewrite/SLHALib-2.2/x86_64-linux/../build/fcc

g++  -c  -o interface.o  bphysics.cc -I$SLHALIB/include 
g77 -c  -o bphysics.o  bphysics.F -ffixed-line-length-none -I$SLHALIB/include 

g++ -o interface  -I$SLHALIB/include interface.o bphysics.o     -L$SLHALIB/lib -lSLHA   -lpthread -L/usr/lib/gcc/x86_64-redhat-linux/3.4.6 -L/usr/lib/gcc/x86_64-redhat-linux/3.4.6 -L/usr/lib/gcc/x86_64-redhat-linux/3.4.6/../../../../lib64 -L/usr/lib/gcc/x86_64-redhat-linux/3.4.6/../../.. -L/lib/../lib64 -L/usr/lib/../lib64 -lfrtbegin -lg2c -lm -lgcc_s -lgcc_s
