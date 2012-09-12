#include <sstream>

#include "softsusy.h"
#include "SLHAfile.hh"

extern "C" {
    void MssmSoftsusy_lesHouchesAccordOutputStream( MssmSoftsusy* mss, 
                                                    const char model[], 
                                                    DoubleVector *pars,
                                                    int sgnMu, double tanb,
                                                    double qMax, int numPoints,
                                                    double mgut, bool altEwsb,
                                                    SLHAfile *sf) {

        std::stringstream ss_out( std::stringstream::in |
                                  std::stringstream::out );

        mss->lesHouchesAccordOutput( ss_out, model, *pars, sgnMu, tanb, qMax,
                                     numPoints, mgut, altEwsb );
        std::istream iss( ss_out.rdbuf() );

        iss >> (*sf);
    }
}
