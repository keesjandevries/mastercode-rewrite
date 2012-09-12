#include "SLHAfile.hh"

struct feynhiggs_prec_obs;

void write_prec_obs(SLHAfile& sf, feynhiggs_prec_obs& fhp) {
    //sf.AddBlock();
    std::cout << fhp.gm2 << std::endl;
}
