#include <iostream>
#include <complex>
#include <string>
#include <fstream>

#include "CFeynHiggs.h"
#include "CSLHA.h"
#include "SLHADefs.h"

const int fh_interface_nslhadata = 5558;

const bool WRITE_SLHA = false;

extern "C" {
    void run_feynhiggs(const char slhafilename [], int mssmpart, int fieldren,
            int tanbren, int higgsmix, int p2approx, int looplevel,
            int tl_running_mt, int tl_bot_resum) {

        COMPLEX slhadata[fh_interface_nslhadata]; // stupid typedefs: not a true constructor
        int error;
        const int abort(0);
        FHSetDebug(0);

        FHSetFlags(&error, mssmpart, fieldren, tanbren, higgsmix, p2approx, looplevel,
                tl_running_mt, tl_bot_resum, 0);

        SLHARead(&error, slhadata, slhafilename, abort);
        FHSetSLHA(&error, slhadata);

        double mhiggs[4];
        Complex SAeff;
        Complex UHiggs[3][3];
        Complex ZHiggs[3][3];
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
            if( WRITE_SLHA ) {
                const char slha_name[] = "feyn_out.slha";
                std::cout << "Writing FH SLHA" << std::endl;
                SLHAWrite(&error, slhadata, slha_name);
                std::cout << "Wrote FH SLHA" << std::endl;
            }
            //prec_obs_array[0] = PrecObs_DeltaRho;
            //prec_obs_array[1] = PrecObs_MWMSSM;
            //prec_obs_array[2] = PrecObs_MWSM;
            //prec_obs_array[3] = PrecObs_SW2effMSSM;
            //prec_obs_array[4] = PrecObs_SW2effSM;
            //prec_obs_array[5] = PrecObs_gminus2mu;
            //prec_obs_array[6] = PrecObs_EDMeTh;
            //prec_obs_array[7] = PrecObs_EDMn;
            //prec_obs_array[8] = PrecObs_EDMHg;
            //prec_obs_array[9] = PrecObs_bsgammaMSSM;
            //prec_obs_array[10] = PrecObs_bsgammaSM;
            //prec_obs_array[11] = PrecObs_DeltaMsMSSM;
            //prec_obs_array[12] = PrecObs_DeltaMsSM;
            //prec_obs_array[13] = PrecObs_BsmumuMSSM;
            //prec_obs_array[14] = PrecObs_BsmumuSM;
        }
    }
}
