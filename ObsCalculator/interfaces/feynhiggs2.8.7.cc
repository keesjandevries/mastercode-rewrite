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

#ifndef COMPLEX
#define COMPLEX DOUBLE_COMPLEX
#endif

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
    double Dmh, DmH, DmA, DmHpm;
};

extern "C" {
    int get_nslhadata() {
        return nslhadata;
    }

    int write_slha(const char slhafilename [], COMPLEX* slhadata) {
        int error;
        double_complex mytemp[nslhadata];
        for(int i=0; i<nslhadata; ++i)
            mytemp[i] = ToComplex(slhadata[i]);
        SLHAWrite(&error, mytemp, slhafilename);
        return error;
    }
    int run_feynhiggs(FeynHiggsPrecObs* out, FeynHiggsOpts* opts,
            COMPLEX* slhadata, bool update) {
        int error;
        const int abort(0);
        FHSetDebug(0);

        FHSetFlags(&error, opts->mssmpart, opts->fieldren, opts->tanbren,
                opts->higgsmix, opts->p2approx, opts->looplevel,
                opts->tl_running_mt, opts->tl_bot_resum, 0);

        double_complex mytemp[nslhadata];
        for(int i=0; i<nslhadata; ++i) {
            mytemp[i] = ToComplex((slhadata[i]));
        }
        FHSetSLHA(&error, mytemp);

        if(error) {
            return error;
        }

        double mhiggs[4];
        std::complex<double> SAeff;
        std::complex<double> UHiggs[3][3];
        std::complex<double> ZHiggs[3][3];
        FHHiggsCorr(&error, mhiggs, &SAeff, UHiggs, ZHiggs);

        double Dmhiggs[4];
        std::complex<double> DSAeff;
        std::complex<double> DUHiggs[3][3];
        std::complex<double> DZHiggs[3][3];
        FHUncertainties(&error, Dmhiggs, &DSAeff, DUHiggs, DZHiggs);

        int ccb;

        FHConstraints(&error, &(out->gm2), &(out->DeltaRho),
                &(out->MWMSSM), &(out->MWSM), &(out->SW2MSSM), &(out->SW2SM),
                &(out->edmeTh), &(out->edmn), &(out->edmHg));//, &ccb);
        
        if(error != 0) {
            return error;
            // FH has failed
        }
        else {
            out->mh = mhiggs[0];
            out->mH = mhiggs[1];
            out->mA = mhiggs[2];
            out->mHpm = mhiggs[3];

            out->Dmh = Dmhiggs[0];
            out->DmH = Dmhiggs[1];
            out->DmA = Dmhiggs[2];
            out->DmHpm = Dmhiggs[3];

            if(update) {
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
            }
            return error;
        }
    }
}
