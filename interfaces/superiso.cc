extern "C" {
#include <include.h>
}
#include <iostream>

struct SuperISOPrecObs {
      double SIbsg, SId0, SIgm2;
};

extern "C" {
    void run_superiso(char slhafilename [], SuperISOPrecObs* out) {
        out->SId0 = delta0_calculator(slhafilename);
        out->SIbsg = bsgamma_calculator(slhafilename); 
        out->SIgm2 = muon_gm2_calculator(slhafilename);
    }
}

int main() {
    SuperISOPrecObs out;
    char fname [] = "slhas/test.slha";
    run_superiso(fname, &out);
    std::cout << "bsg" << out.SIbsg << std::endl;
    std::cout << "d0" << out.SId0 << std::endl;
    std::cout << "gm2" << out.SIgm2 << std::endl;
}
