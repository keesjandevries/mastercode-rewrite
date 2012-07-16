#include <iostream>
#include <complex>

#include "CFeynHiggs.h"
#include "CSLHA.h"

extern "C" {
    // this needs to be a c-interface that hides all of the implementation from python
    // which sucks, can't pass out from the .a file so this is literally just
    // going to have to be a "RUN", "GET VALUES" where it copies out hte values
    // to we don't get relocate errors

    //std::complex<double>* COMPLEX_new(double re, double im) {
       //return new std::complex<double>(re,im);
    //}

    //void slharead(int error, COMPLEX slhadata, const char filename,
            //const int abort){
        //SLHARead(&error,&slhadata,&filename,abort);
    //}

    void initFH(std::string slhafilename) {
    }
}
