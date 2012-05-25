MAINDIR=`pwd`  

if [[ ! -h softsusy-3.3.1/.libs/libsoft.so ]]; then
    if [[ ! -d softsusy-3.3.1 ]]; then
        tar zxf softsusy-3.3.1.tar.gz
    fi
    cd softsusy-3.3.1/
    ./configure
    make
    cd ${MAINDIR}
fi

g++ -c -fPIC -o softsusy_interface.o softsusy_interface.cc \
    -I${MAINDIR}/softsusy-3.3.1/ -L${MAINDIR}/softsusy-3.3.1/.libs -lsoft
g++ -shared -Wl,-soname,libmcsoftsusy.so \
    -Wl,-rpath,${MAINDIR}/softsusy-3.3.1/.libs -o libmcsoftsusy.so \
   softsusy_interface.o -L${MAINDIR}/softsusy-3.3.1/.libs -lsoft
