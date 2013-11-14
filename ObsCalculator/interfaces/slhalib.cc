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
    int write_slha(const char slhafilename [],
            std::complex<double>* slhadata){
        int error;
        SLHAWrite(&error, slhadata, slhafilename);
        return error;
    }

    int read_slha(const char slhafilename [], std::complex<double>* slhadata){
        int error;
        const int abort(0);
        SLHARead(&error, slhadata, slhafilename, abort);
        return error;
    }
}
