#! /bin/bash

LOG_FILE="build/build.log"

MAINDIR=`pwd`  
PREDICTOR_DIR="predictors"

SOFTSUSY_VERSION="3.3.4"
SOFTSUSY_BASE="softsusy-${SOFTSUSY_VERSION}"
SOFTSUSY_TARGET="http://www.hepforge.org/archive/softsusy/\
${SOFTSUSY_BASE}.tar.gz"
SOFTSUSY_LIB="packages/lib/libsoft.so"

FEYNHIGGS_VERSION="2.9.4"
FEYNHIGGS_BASE="FeynHiggs-${FEYNHIGGS_VERSION}"
FEYNHIGGS_TARGET="http://wwwth.mpp.mpg.de/members/heinemey/feynhiggs/\
newversion/${FEYNHIGGS_BASE}.tar.gz"
FEYNHIGGS_LIB="packages/lib/libFH.a"

MICROMEGAS_VERSION="2.4.5"
MICROMEGAS_BASE="micromegas_${MICROMEGAS_VERSION}"
MICROMEGAS_TARGET="http://lapth.in2p3.fr/micromegas/downloadarea/code/\
${MICROMEGAS_BASE}.tgz"

SLHA_DIR="SLHA"

RFLAGS=`root-config --cflags --libs`

border="============================"


function compile_softsusy {
    echo ${border}
    echo "  Compiling softsusy"
    echo ${border}
    if [[ ! -h ${SOFTSUSY_LIB} ]] || \
       [[ `strings ${SOFTSUSY_LIB} | grep "${SOFTSUSY_VERSION}"` ]]; then
        if [[ ! -f tars/${SOFTSUSY_BASE}.tar.gz ]]; then
            wget -P tars/ ${SOFTSUSY_TARGET}
        fi
        if [[ ! -d ${PREDICTOR_DIR}/${SOFTSUSY_BASE} ]]; then
            tar -zxf tars/${SOFTSUSY_BASE}.tar.gz -C ${PREDICTOR_DIR}
        fi
        cd  ${PREDICTOR_DIR}/${SOFTSUSY_BASE}
        ./configure --prefix=${MAINDIR}/packages
        make
        make install
        cd ${MAINDIR}
    fi
    echo "Done"
}


function compile_feynhiggs {
    echo ${border}
    echo "  Compiling feynhiggs..."
    echo ${border}
    if [[ ! -h ${FEYNHIGGS_LIB} ]] || \
       [[ `strings ${FEYNHIGGS_LIB} | grep "${FEYNHIGGS_VERSION}"` ]]; then
        if [[ ! -f tars/${FEYNHIGGS_BASE}.tar.gz ]]; then
            wget -P tars/ ${FEYNHIGGS_TARGET}
        fi
        if [[ ! -d ${PREDICTOR_DIR}/${FEYNHIGGS_BASE} ]]; then
            tar -zxf tars/${FEYNHIGGS_BASE}.tar.gz -C ${PREDICTOR_DIR}
            patch -p1 < patches/FH.patch
        fi
        cd ${PREDICTOR_DIR}/${FEYNHIGGS_BASE}
        ./configure --prefix=${MAINDIR}/packages
        make
        make install
        cd ${MAINDIR}
    fi
    echo "Done"
}

function compile_micromegas {
}


function compile_slha {
    echo ${border}
    echo "  Compiling SLHA classes"
    echo ${border}
    cd ${SLHA_DIR}
    make
    cd ${MAINDIR}
}

function compile_feynhiggs_interfaces {
    echo ${border}
    echo "  Compiling FH Interfaces"
    echo ${border}
    g++ -c -fPIC -o obj/feynhiggs.o interfaces/feynhiggs.cc \
        -I${MAINDIR}/packages/include/ -L${MAINDIR}/packages/lib64 -lFH \
         -lgfortran
    g++ -shared -Wl,-soname,libmcfeynhiggs.so -o libs/libmcfeynhiggs.so \
        obj/feynhiggs.o -L${MAINDIR}/packages/lib64 -lFH \
        -lgfortran
    echo "Done"
}


function compile_softsusy_interfaces {
    echo ${border}
    echo "  Compiling SS Interfaces"
    echo ${border}
    g++ -c -fPIC -o obj/softsusy.o interfaces/softsusy.cc \
        -I${MAINDIR}/packages/include/softsusy/ \
        -L${MAINDIR}/packages/lib -lsoft
    g++ -shared -Wl,-soname,libmcsoftsusy.so \
        -Wl,-rpath,${MAINDIR}/packages/lib -o libs/libmcsoftsusy.so \
       obj/softsusy.o -L${MAINDIR}/packages/lib -lsoft
}


function compile_slha_interfaces {
    echo ${border}
    echo "  Compiling SLHA Interfaces"
    echo ${border}
    g++ -c -fPIC -o obj/slha.o interfaces/slha.cc \
        -I${MAINDIR}/SLHA/inc/ -L${MAINDIR}/SLHA/libs -lSLHAfile \
        ${RFLAGS}
    g++ -shared -Wl,-soname,libmcslha.so \
        -Wl,-rpath,${MAINDIR}/SLHA/libs -o libs/libmcslha.so \
        obj/slha.o -L${MAINDIR}/SLHA/libs -lSLHAfile \
        ${RFLAGS}
}


function compile_joint_interfaces {
    echo ${border}
    echo "  Compiling Joint Interfaces"
    echo ${border}
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

cat /dev/null > ${LOG_FILE}
#tailf ${LOG_FILE} &

#compile_slha >> ${LOG_FILE}
#compile_softsusy >> ${LOG_FILE}
#compile_feynhiggs >> ${LOG_FILE}
#compile_micromegas >> ${LOG_FILE}

compile_softsusy_interfaces >> ${LOG_FILE}
compile_slha_interfaces >> ${LOG_FILE}
compile_joint_interfaces >> ${LOG_FILE}
compile_feynhiggs_interfaces >> ${LOG_FILE}

