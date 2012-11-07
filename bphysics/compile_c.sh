#!/bin/bash

SLHALIB=/home/hep/kjd110/mastercode-rewrite/SLHALib-2.2/x86_64-linux/
FCC=/home/hep/kjd110/mastercode-rewrite/SLHALib-2.2/x86_64-linux/../build/fcc
#g77 -ffixed-line-length-none -o bphysics.o bphysics.F 
#g77 -ffixed-line-length-none -o main.o main.F 

#g77 -o main.o -ffixed-line-length-none -I$SLHALIB/include main.F  
#g77 -c  -o main.o -ffixed-line-length-none -I$SLHALIB/include main.F  
g++  -c  -o main.o  main.cpp -I$SLHALIB/include 
g77 -c  -o bphysics.o  bphysics.F -ffixed-line-length-none -I$SLHALIB/include 

g++ -o main  -I$SLHALIB/include main.o bphysics.o     -L$SLHALIB/lib -lSLHA   -lpthread -L/usr/lib/gcc/x86_64-redhat-linux/3.4.6 -L/usr/lib/gcc/x86_64-redhat-linux/3.4.6 -L/usr/lib/gcc/x86_64-redhat-linux/3.4.6/../../../../lib64 -L/usr/lib/gcc/x86_64-redhat-linux/3.4.6/../../.. -L/lib/../lib64 -L/usr/lib/../lib64 -lfrtbegin -lg2c -lm -lgcc_s -lgcc_s
