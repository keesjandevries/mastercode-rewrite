MAINDIR=`pwd`  
# using -L isn't really necessary here once we've set the run path
g++ -c -fPIC -o softsusy_interface.o softsusy_interface.cc -L${MAINDIR}/softsusy-3.3.1/.libs -lsoft
g++ -shared -Wl,-soname,libmcsoftsusy.so -Wl,-rpath,${MAINDIR}/softsusy-3.3.1/.libs -o libmcsoftsusy.so softsusy_interface.o -L${MAINDIR}/softsusy-3.3.1/.libs
