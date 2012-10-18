#include <iostream>
#include <complex>
#include <string>
#include <fstream>
#include <stdlib.h>

#include "CFeynHiggs.h"
#include "CSLHA.h"
#include "SLHADefs.h"

const bool write_fh_slha = false;

struct FeynHiggsPrecObs {
    double DeltaRho, MWMSSM, MWSM, SW2effMSSM, SW2effSM, gminus2mu, EDMeTh,
           EDMn, EDMHg, bsgammaMSSM, bsgammaSM, DeltaMsMSSM, DeltaMsSM,
           BsmumuMSSM, BsmumuSM;
};

extern "C" {
    void run_feynhiggs(const char slhafilename [], int mssmpart, int fieldren,
            int tanbren, int higgsmix, int p2approx, int looplevel,
            int tl_running_mt, int tl_bot_resum, FeynHiggsPrecObs* out) {

        COMPLEX slhadata[nslhadata]; // stupid typedefs: not a true constructor
        int error;
        const int abort(0);
        FHSetDebug(0);

        FHSetFlags(&error, mssmpart, fieldren, tanbren, higgsmix, p2approx,
                looplevel, tl_running_mt, tl_bot_resum, 0);

        SLHARead(&error, slhadata, slhafilename, abort);
        if(error) {
            exit(error);
        }
        FHSetSLHA(&error, slhadata);
        if(error) {
            exit(error);
        }

        double mhiggs[4];
        ComplexType SAeff;
        ComplexType UHiggs[3][3];
        ComplexType ZHiggs[3][3];
        FHHiggsCorr(&error, mhiggs, &SAeff, UHiggs, ZHiggs);

        double gm2, Deltarho, MWMSSM, MWSM, SW2MSSM, SW2SM, edmeTh, edmn,
               edmHg;
        int ccb;

        FHConstraints(&error, &gm2, &Deltarho, &MWMSSM, &MWSM, &SW2MSSM,
                &SW2SM, &edmeTh, &edmn, &edmHg, &ccb);
        
        if(error != 0) {
            std::cout << "FH FAILED" << std::endl;
            // FH has failed
        }
        else {
            std::cout << "FH SUCCESS" << std::endl;
            if( write_fh_slha ) {
                const char fh_slha_name[] = "feyn_out.slha";
                std::cout << "Writing FH SLHA" << std::endl;
                SLHAWrite(&error, slhadata, fh_slha_name);
                std::cout << "Wrote FH SLHA" << std::endl;
            }
            out->DeltaRho = PrecObs_DeltaRho.re;
            out->MWMSSM = PrecObs_MWMSSM.re;
            out->MWSM = PrecObs_MWSM.re;
            out->SW2effMSSM = PrecObs_SW2effMSSM.re;
            out->SW2effSM = PrecObs_SW2effSM.re;
            out->gminus2mu = PrecObs_gminus2mu.re;
            out->EDMeTh = PrecObs_EDMeTh.re;
            out->EDMn = PrecObs_EDMn.re;
            out->EDMHg = PrecObs_EDMHg.re;
            out->bsgammaMSSM = PrecObs_bsgammaMSSM.re;
            out->bsgammaSM = PrecObs_bsgammaSM.re;
            out->DeltaMsMSSM = PrecObs_DeltaMsMSSM.re;
            out->DeltaMsSM = PrecObs_DeltaMsSM.re;
            out->BsmumuMSSM = PrecObs_BsmumuMSSM.re;
            out->BsmumuSM = PrecObs_BsmumuSM.re;
        }
    }
}
