#README for the SLHA I/O class
#Jad Marrouche, September 2011
#jad.marrouche@cern.ch

In order to compile and run:

1. Make sure you have sourced the appropriate root bin/thisroot.sh file to define a $ROOTSYS etc
2. Make sure you have the exe/ obj/ folders
3. Go into the src folder and execute the following line:
rootcint -f output.cc -c -p ../inc/SLHAblock.hh ../inc/SLHAfile.hh ../inc/SLHAline.hh ../Linkdef.h
4. Run make clean followed by make
5. The two sample exe are for reading and writing the SLHA file objects to a ROOT file, themselves instantiated by reading from an SLHA txt file
6. The test.cpp shows off some features
