#!/bin/bash

SLHALIB=/home/hep/kjd110/mastercode-rewrite/SLHALib-2.2/x86_64-linux/

#g77 -ffixed-line-length-none -o bphysics.o bphysics.F 
#g77 -ffixed-line-length-none -o main.o main.F 

#g77 -o main.o -ffixed-line-length-none -I$SLHALIB/include main.F  
g77 -c  -o main.o -ffixed-line-length-none -I$SLHALIB/include main.F  
g77 -c  -o bphysics.o -ffixed-line-length-none -I$SLHALIB/include bphysics.F  

g77 -o main -ffixed-line-length-none -I$SLHALIB/include main.o bphysics.o  -L$SLHALIB/lib -lSLHA
