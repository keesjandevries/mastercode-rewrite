#include <iostream>
#include <complex>
#include <string>
#include <fstream>
#include <cmath>
#include <cstdlib>

#include "CFeynHiggs.h"
#include "CSLHA.h"
#include "SLHADefs.h"

const bool write_fh_slha = false;

struct FeynHiggsOpts {
    int mssmpart, fieldren, tanbren, higgsmix, p2approx, looplevel,
        tl_running_mt, tl_bot_resum;
};

struct FeynHiggsPrecObs {
    //double gm2, DeltaRho, MWMSSM, MWSM, SW2effMSSM, SW2effSM, EDMeTh,
           //EDMn, EDMHg, bsgammaMSSM, bsgammaSM, DeltaMsMSSM, DeltaMsSM,
           //BsmumuMSSM, BsmumuSM;
    double gm2, DeltaRho, MWMSSM, MWSM, SW2MSSM, SW2SM, edmeTh, edmn, edmHg;
    double mh, mH, mA, mHpm;
};

extern "C" {
    int get_nslhadata() {
        return nslhadata;
    }

    int write_slha(const char slhafilename [], COMPLEX* slhadata) {
        int error;
        SLHAWrite(&error, slhadata, slhafilename);
        return error;
    }
    void run_feynhiggs(const char slhafilename [], FeynHiggsPrecObs* out,
            FeynHiggsOpts* opts, COMPLEX* slhadata ) {

        int error;
        const int abort(0);
        FHSetDebug(0);

        FHSetFlags(&error, opts->mssmpart, opts->fieldren, opts->tanbren,
                opts->higgsmix, opts->p2approx, opts->looplevel,
                opts->tl_running_mt, opts->tl_bot_resum, 0);

        SLHARead(&error, slhadata, slhafilename, abort);
        if(error) {
            exit(error);
        }
        FHSetSLHA(&error, slhadata);
        if(error) {
            exit(error);
        }

        double mhiggs[4];
        std::complex<double> SAeff;
        std::complex<double> UHiggs[3][3];
        std::complex<double> ZHiggs[3][3];
        FHHiggsCorr(&error, mhiggs, &SAeff, UHiggs, ZHiggs);

        int ccb;

        FHConstraints(&error, &(out->gm2), &(out->DeltaRho),
                &(out->MWMSSM), &(out->MWSM), &(out->SW2MSSM), &(out->SW2SM),
                &(out->edmeTh), &(out->edmn), &(out->edmHg), &ccb);
        
        if(error != 0) {
            std::cout << "FH FAILED" << std::endl;
            // FH has failed
        }
        else {
            // update higgs values
            out->mh = mhiggs[0];
            out->mH = mhiggs[1];
            out->mA = mhiggs[2];
            out->mHpm = mhiggs[3];

            Mass_Mh0.re = mhiggs[0];
            Mass_MHH.re = mhiggs[1];
            Mass_MA0.re = mhiggs[2];
            Mass_MHp.re = mhiggs[3];
            for(int i=1; i<4; ++i) {
                for( int j=1; j<4; ++j) {
                    CVHMix_UH(i,j).re = std::real(UHiggs[i][j]);
                }
            }
            Alpha_Alpha.re = asin(std::real(SAeff));

            // update precobs
            PrecObs_gminus2mu.re = out->gm2;
            PrecObs_DeltaRho.re  = out->DeltaRho;
            PrecObs_MWSM.re      = out->MWSM;
            PrecObs_SW2effSM.re  = out->SW2SM;
            PrecObs_EDMeTh.re    = out->edmeTh;
            PrecObs_EDMn.re      = out->edmn;
            PrecObs_EDMHg.re     = out->edmHg;
            //PrecObs_MW.re        = out->MWMSSM;
            //PrecObs_SW2eff.re    = out->SW2MSSM;
            //PrecObs_bsgamma.re   = out->bsgammaMSSM;
            //PrecObs_bsgammaSM.re = out->bsgammaSM;

            std::cout << "FH SUCCESS" << std::endl;
            if( write_fh_slha ) {
                const char fh_slha_name[] = "slhas/feyn_out.slha";
                std::cout << "Writing FH SLHA" << std::endl;
                SLHAWrite(&error, slhadata, fh_slha_name);
                std::cout << "Wrote FH SLHA" << std::endl;
            }
        }
    }
}
