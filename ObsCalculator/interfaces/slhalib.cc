#include <cstdlib>
#include <complex>
#include <iostream>
#include "CSLHA.h"

extern "C" {
    int get_nslhadata() {
        return nslhadata;
    }
    int get_ofsetspinfo(){
        return OffsetSPInfo;
    }
    void write_slha(const char slhafilename [],
            std::complex<double>* slhadata){
        int error;
        SLHAWrite(&error, slhadata, slhafilename);
        if(error) {
            exit(error);
        }
    }

    void read_slha(const char slhafilename [], std::complex<double>* slhadata){
        int error;
        const int abort(0);
        SLHARead(&error, slhadata, slhafilename, abort);
        if(error) {
            exit(error);
        }
    }
}
