#!/bin/bash

SLHAdir=../packages/

g++  -c  -o interface.o  bphysics.cc \
    -I$SLHAdir/include 

gfortran -c -o bphysics.o bphysics.F \
    -ffixed-line-length-none \
    -I$SLHAdir/include 

g++ -o interface interface.o bphysics.o \
    -I$SLHAdir/include \
    -L$SLHAdir/lib -lSLHA \
    -lpthread -lgfortran -lm -lgcc_s -lgcc_s 
#-lfrtbegin 
