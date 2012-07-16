#! /bin/bash

function compile_softsusy {
    if [[ ! -h packages/lib/libsoft.so ]]; then
        if [[ ! -f ${SOFTSUSY_BASE}.tar.gz ]]; then
            wget ${SOFTUSY_TARGET}
        fi
        if [[ ! -d ${SOFTSUSY_BASE} ]]; then
            tar zxf ${SOFTSUSY_BASE}.tar.gz
        fi
        cd ${SOFTSUSY_BASE}
        ./configure --prefix=${MAINDIR}/packages
        make
        make install
        cd ${MAINDIR}
    fi
}

function compile_softsusy_interfaces {
    g++ -c -fPIC -o obj/softsusy.o interfaces/softsusy.cc \
        -I${MAINDIR}/packages/include/softsusy/ -L${MAINDIR}/packages/lib -lsoft
    g++ -shared -Wl,-soname,libmcsoftsusy.so \
        -Wl,-rpath,${MAINDIR}/packages/libs -o libs/libmcsoftsusy.so \
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
    # softsusy & slha join interface
    g++ -c -fPIC -o obj/softsusy_slha.o interfaces/softsusy_slha.cc \
        -I${MAINDIR}/SLHA/inc/ -L${MAINDIR}/SLHA/libs -lSLHAfile \
        -I${MAINDIR}/packages/include/softsusy -L${MAINDIR}/packages/lib -lsoft \
        ${RFLAGS}

    g++ -shared -Wl,-soname,libmcsoftsusyslha.so \
        -Wl,-rpath,${MAINDIR}/SLHA/libs:${MAINDIR}/packages/lib  \
        -o libs/libmcsoftsusyslha.so obj/softsusy_slha.o \
        -L${MAINDIR}/SLHA/libs -lSLHAfile -L${MAINDIR}/packages/lib -lsoft \
        ${RFLAGS}
}

MAINDIR=`pwd`  
SOFTSUSY_VERSION="3.3.1"
SOFTSUSY_TARGET="http://www.hepforge.org/archive/softsusy/\
                 softsusy-${SOFTSUSY_VERSION}.tar.gz"
SOFTSUSY_BASE="softsusy-${SOFTSUSY_VERSION}"
RFLAGS=`root-config --cflags --libs`

compile_softsusy
compile_softsusy_interfaces
compile_slha_interfaces
compile_joint_interfaces
