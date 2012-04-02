#! /bin/bash

if [[ -n $ROOTSYS ]]; then
    if [[ ! -d SLHA/libs ]]; then
        mkdir SLHA/libs
    fi
    if [[ ! -d SLHA/exe ]]; then
        mkdir SLHA/exe
    fi
    BASEDIR=~/Projects/mastercode/
    cd $BASEDIR/SLHA
    make
    cd $BASEDIR/py_masterfitter/
    g++ -c -fPIC -o softsusy_interface.o softsusy_interface.cc -I$BASEDIR/softsusy/ -L$BASEDIR/SLHA/libs/ -lSLHAfile -L$BASEDIR/softsusy/.libs/ -lsoft -I$BASEDIR/SLHA/inc/ -lgfortran `root-config --cflags --libs`
    g++ -shared -Wl,-soname,libsoftpoint.so -o libs/libsoftpoint.so softsusy_interface.o -lgfortran -L$BASEDIR/SLHA/libs/ -lSLHAfile -L$BASEDIR/softsusy/.libs/ -lsoft -I$BASEDIR/SLHA/inc/ -I$BASEDIR/softsusy/ `root-config --cflags --libs`
	g++ -shared -Wl,-soname,libSLHAfile.so -o libs/libslhafile.so $BASEDIR/SLHA/obj/*.o `root-config --cflags --libs`
else
    echo Please source ROOT first
fi
