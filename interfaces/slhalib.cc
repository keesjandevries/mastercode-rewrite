#include <cstdlib>
#include <complex>
#include <iostream>
#include "CSLHA.h"

extern "C" {
    int get_nslhadata() {
        return nslhadata;
    }
    void read_slha(const char slhafilename [], std::complex<double>* slhadata){
        int error;
        const int abort(0);
        SLHARead(&error, slhadata, slhafilename, abort);
        //for(int i=0; i<nslhadata; ++i) {
            //std::cout << slhadata[i] << std::endl;
            //}
        if(error) {
            exit(error);
        }
    }
}
