MAINDIR=`pwd`  

if [[ ! -h softsusy-3.3.1/.libs/libsoft.so ]]; then
    if [[ ! -f softsusy-3.3.1.tar.gz ]]; then
        wget http://www.hepforge.org/archive/softsusy/softsusy-3.3.1.tar.gz
    fi
    if [[ ! -d softsusy-3.3.1 ]]; then
        tar zxf softsusy-3.3.1.tar.gz
    fi
    cd softsusy-3.3.1/
    ./configure
    make
    cd ${MAINDIR}
fi

# softsusy
g++ -c -fPIC -o obj/softsusy.o interfaces/softsusy.cc \
    -I${MAINDIR}/softsusy-3.3.1/ -L${MAINDIR}/softsusy-3.3.1/.libs -lsoft
g++ -shared -Wl,-soname,libmcsoftsusy.so \
    -Wl,-rpath,${MAINDIR}/softsusy-3.3.1/.libs -o libs/libmcsoftsusy.so \
   obj/softsusy.o -L${MAINDIR}/softsusy-3.3.1/.libs -lsoft

RFLAGS=`root-config --cflags --libs`
# slha file
g++ -c -fPIC -o obj/slha.o interfaces/slha.cc \
    -I${MAINDIR}/SLHA/inc/ -L${MAINDIR}/SLHA/libs -lSLHAfile \
    ${RFLAGS}
g++ -shared -Wl,-soname,libmcslha.so \
    -Wl,-rpath,${MAINDIR}/SLHA/libs -o libs/libmcslha.so \
    obj/slha.o -L${MAINDIR}/SLHA/libs -lSLHAfile \
    ${RFLAGS}
