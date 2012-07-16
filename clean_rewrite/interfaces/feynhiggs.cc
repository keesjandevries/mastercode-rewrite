#include <iostream>

#include "CFeynHiggs.h"
#include "CSLHA.h"

extern "C" {
    void new_COMPLEX(double re, double im) {
       return new COMPLEX(re,im); 
    }

    void slharead(int *error, COMPLEX *slhadata, const char *filename, const int abort){
        SLHARead(error,slhadata,filename,abort)
    {
}
