#include "softsusy-3.3.1/linalg.h"
#include <iostream>

extern "C" 
{
    DoubleVector* DoubleVector_new( int sz ) {
        return new DoubleVector(sz);
    }
    double DoubleVector_display( DoubleVector* dv, int pos )  { 
        return dv->display(pos); 
    }
    void DoubleVector_set( DoubleVector* dv, int pos, double val )  { 
        std::cout << pos << "," << val<< std::endl;
        (*dv)(pos) = val;
    }
} 
