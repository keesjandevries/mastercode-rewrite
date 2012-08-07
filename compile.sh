#! /bin/bash
MAINDIR=`pwd`  
SOFTSUSY_VERSION="3.3.1"
SOFTSUSY_BASE="softsusy-${SOFTSUSY_VERSION}"
SOFTSUSY_TARGET="http://www.hepforge.org/archive/softsusy/\
${SOFTSUSY_BASE}.tar.gz"
SOFTSUSY_LIB="packages/lib/libsoft.so"

FEYNHIGGS_VERSION="2.9.1"
FEYNHIGGS_BASE="FeynHiggs-${FEYNHIGGS_VERSION}"
FEYNHIGGS_TARGET="http://wwwth.mpp.mpg.de/members/heinemey/feynhiggs/\
newversion/${FEYNHIGGS_BASE}.tar.gz"
FEYNHIGGS_LIB="packages/lib64/libFH.a"

RFLAGS=`root-config --cflags --libs`


function compile_softsusy {
    echo -n "Compiling softsusy... "
    if [[ ! -h ${SOFTSUSY_LIB} ]] || \
       [[ `strings ${SOFTSUSY_LIB} | grep "${SOFTSUSY_VERSION}"` ]]; then
        if [[ ! -f tars/${SOFTSUSY_BASE}.tar.gz ]]; then
            wget -P tars/ ${SOFTUSY_TARGET}
        fi
        if [[ ! -d ${SOFTSUSY_BASE} ]]; then
            tar zxf tars/${SOFTSUSY_BASE}.tar.gz
        fi
        cd ${SOFTSUSY_BASE}
        ./configure --prefix=${MAINDIR}/packages
        make
        make install
        cd ${MAINDIR}
    fi
    echo "Done"
}


function compile_feynhiggs {
    echo "==================="
    echo "Compiling feynhiggs"
    echo "==================="
    if [[ ! -h ${FEYNHIGGS_LIB} ]] || \
       [[ `strings ${FEYNHIGGS_LIB} | grep "${FEYNHIGGS_VERSION}"` ]]; then
        if [[ ! -f tars/${FEYNHIGGS_BASE}.tar.gz ]]; then
            wget -P tars/ ${FEYNHIGGS_TARGET}
        fi
        if [[ ! -d ${FEYNHIGGS_BASE} ]]; then
            tar zxf tars/${FEYNHIGGS_BASE}.tar.gz
            patch -p1 < patches/FH.patch
        fi
        cd ${FEYNHIGGS_BASE}
        ./configure --prefix=${MAINDIR}/packages
        make
        make install
        cd ${MAINDIR}
    fi
    echo "Done"
}

function compile_feynhiggs_interfaces {
    echo "======================="
    echo "Compiling FH Interfaces"
    echo "======================="
    g++ -c -fPIC -o obj/feynhiggs.o interfaces/feynhiggs.cc \
        -I${MAINDIR}/packages/include/ -L${MAINDIR}/packages/lib64 -lFH \
         -lgfortran
    g++ -shared -Wl,-soname,libmcfeynhiggs.so -o libs/libmcfeynhiggs.so \
        obj/feynhiggs.o -L${MAINDIR}/packages/lib64 -lFH \
        -lgfortran
    echo "Done"
}


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
    # softsusy & slha join interface
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


#compile_softsusy
#compile_softsusy_interfaces
compile_slha_interfaces
#compile_joint_interfaces

#compile_feynhiggs
#compile_feynhiggs_interfaces
