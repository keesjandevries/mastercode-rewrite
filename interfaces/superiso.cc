#include <include.h>

struct SuperISOPrecObs {
      double SIbsg, SId0, SIgm2;
};

extern "C" {
    void run_superiso(char slhafilename [], SuperISOPrecObs* out) {
        out->SId0 = delta0_calculator(slhafilename);
        Bout->SIbsg = Rbsgamma_calculator(slhafilename); 
        out->SIgm2 = muon_gm2_calculator(slhafilename);
    }
}
