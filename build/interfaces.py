import os
import subprocess

softsusy = {

INTERFACES = [ softsusy, slha, softsusy_slha, feynhiggs ]

function compile_softsusy_interfaces {
    g++ -c -fPIC -o obj/softsusy.o interfaces/softsusy.cc \
        -I${MAINDIR}/packages/include/softsusy/ \
        -L${MAINDIR}/packages/lib -lsoft
    g++ -shared -Wl,-soname,libmcsoftsusy.so \
        -Wl,-rpath,${MAINDIR}/packages/lib -o libs/libmcsoftsusy.so \
       obj/softsusy.o -L${MAINDIR}/packages/lib -lsoft
}

function compile_slha_interfaces {
    g++ -c -fPIC -o obj/slha.o interfaces/slha.cc \
        -I${MAINDIR}/SLHA/inc/ -L${MAINDIR}/SLHA/libs -lSLHAfile \
        ${RFLAGS}
    g++ -shared -Wl,-soname,libmcslha.so \
        -Wl,-rpath,${MAINDIR}/SLHA/libs -o libs/libmcslha.so \
        obj/slha.o -L${MAINDIR}/SLHA/libs -lSLHAfile \
        ${RFLAGS}
}


function compile_joint_interfaces {
    g++ -c -fPIC -o obj/softsusy_slha.o interfaces/softsusy_slha.cc \
        -I${MAINDIR}/SLHA/inc/ -L${MAINDIR}/SLHA/libs -lSLHAfile \
        -I${MAINDIR}/packages/include/softsusy \
        -L${MAINDIR}/packages/lib -lsoft \
        ${RFLAGS}

    g++ -shared -Wl,-soname,libmcsoftsusyslha.so \
        -Wl,-rpath,${MAINDIR}/SLHA/libs:${MAINDIR}/packages/lib  \
        -o libs/libmcsoftsusyslha.so obj/softsusy_slha.o \
        -L${MAINDIR}/SLHA/libs -lSLHAfile -L${MAINDIR}/packages/lib -lsoft \
        ${RFLAGS}
}


function compile_feynhiggs_interfaces {
    g++ -c -fPIC -o obj/feynhiggs.o interfaces/feynhiggs.cc \
        -I${MAINDIR}/packages/include/ -L${MAINDIR}/packages/lib64 -lFH \
         -lgfortran
    g++ -shared -Wl,-soname,libmcfeynhiggs.so -o libs/libmcfeynhiggs.so \
        obj/feynhiggs.o -L${MAINDIR}/packages/lib64 -lFH \
        -lgfortran
}
