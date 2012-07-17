#include <iostream>
#include <complex>
#include <string>

#include "CFeynHiggs.h"
#include "CSLHA.h"

extern "C" {
    void initFH(const char slhafilename []) {
        // FHSetDebug(0)
        // FHSetFlags / FHSetFlagString
        // Check new interfaces in 2.9.1
        //COMPLEX slhadata();

        COMPLEX* slhadata = new COMPLEX[5558]; // stupid typedefs: not a true constructor
        int error;
        const int abort(0);
        std::cout << slhafilename << std::endl;
        slhafilename = "post_ss.slha";
        std::cout << slhafilename << std::endl;

        //std::string sfn(slhafilename);
        //const char* lol = sfn.c_str();

        //std::cout << lol << std::endl;
        SLHARead( &error, slhadata, slhafilename, abort);
    }

}
