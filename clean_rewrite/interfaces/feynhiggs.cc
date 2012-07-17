#include <iostream>
#include <complex>
#include <string>

#include "CFeynHiggs.h"
#include "CSLHA.h"

const int fh_interface_nslhadata = 5558;

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

        //for(int p=0; p<fh_interface_nslhadata; ++p) {
            //if(slhadata[p].re != -999) {
                //std::cout << slhadata[p].re << ", " << slhadata[p].im <<
                    //std::endl;
            //}
        //}

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
        std::cout << gm2 << std::endl;
        
        if(error != 0) {
            // FH has failed
        }

        const char lulz[] = "feyn_out.slha";
        SLHAWrite(&error, slhadata, lulz);
    }

}
     /* PREDICTIONS FROM  FEYN HIGGS */
      //PREDICT(7)  = gm2         ! FeynHiggs
      //PREDICT(19) = MHiggs(1)   ! FeynHiggs
      //PREDICT(33) = HMix_MUE    ! Mu
      //PREDICT(35) = Alpha_Alpha ! Alpha_effective
      
      //PREDICT(36) = HMix_MA02   ! MA0^2(Q)

      //PREDICT(37) = NMix_ZNeu(1,1) ! neu mix matrix
      //PREDICT(38) = NMix_ZNeu(1,2) ! neu mix matrix
      //PREDICT(39) = NMix_ZNeu(1,3) ! neu mix matrix
      //PREDICT(40) = NMix_ZNeu(1,4) ! neu mix matrix
      //PREDICT(41) = NMix_ZNeu(2,1) ! neu mix matrix
      //PREDICT(42) = NMix_ZNeu(2,2) ! neu mix matrix
      //PREDICT(43) = NMix_ZNeu(2,3) ! neu mix matrix
      //PREDICT(44) = NMix_ZNeu(2,4) ! neu mix matrix
      //PREDICT(45) = NMix_ZNeu(3,1) ! neu mix matrix
      //PREDICT(46) = NMix_ZNeu(3,2) ! neu mix matrix
      //PREDICT(47) = NMix_ZNeu(3,3) ! neu mix matrix
      //PREDICT(48) = NMix_ZNeu(3,4) ! neu mix matrix
      //PREDICT(49) = NMix_ZNeu(4,1) ! neu mix matrix
      //PREDICT(50) = NMix_ZNeu(4,2) ! neu mix matrix
      //PREDICT(51) = NMix_ZNeu(4,3) ! neu mix matrix
      //PREDICT(52) = NMix_ZNeu(4,4) ! neu mix matrix

      //PREDICT(53) = Mass_MSf(1,3,1) ! muL
      //PREDICT(54) = Mass_MSf(2,3,1) ! muR
      //PREDICT(55) = Mass_MSf(1,4,1) ! mdL
      //PREDICT(56) = Mass_MSf(2,4,1) ! mdR

      //PREDICT(57) = StopMix_USf(1,1)
      //PREDICT(58) = StopMix_USf(1,2)
      //PREDICT(59) = StopMix_USf(2,1)
      //PREDICT(60) = StopMix_USf(2,2)

      //PREDICT(61) = SbotMix_USf(1,1)
      //PREDICT(62) = SbotMix_USf(1,2)
      //PREDICT(63) = SbotMix_USf(2,1)
      //PREDICT(64) = SbotMix_USf(2,2)
