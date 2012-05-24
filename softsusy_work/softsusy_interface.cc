#include "softsusy-3.3.1/linalg.h"

extern "C" 
{
    DoubleVector* DoubleVector_new( int *sz ) {
        return new DoubleVector(*sz);
    }
} 
