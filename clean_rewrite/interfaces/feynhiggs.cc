#include <iostream>
#include <complex>
#include <string>

#include "CFeynHiggs.h"
#include "CSLHA.h"

extern "C" {
    void initFH(const char slhafilename [], int* mssmpart, int fieldren,
            int tanbren, int higgsmix, int p2approx, int looplevel,
            int tl_running_mt, int tl_bot_resum) {
        std::cout << mssmpart << std::endl;

        COMPLEX slhadata[5558]; // stupid typedefs: not a true constructor
        int error;
        const int abort(0);
        FHSetDebug(0);

        //CALL FHSETFLAGS( ERROR, MSSMPART_IN, FIELDREN_IN, TANBREN_IN,
        //&     HIGGSMIX_IN, P2APPROX_IN, LOOPLEVEL_IN, TL_RUNNING_MT_IN, 
        //&     TL_BOT_RESUM_IN, 0 )
        FHSetFlags(&error, mssmpart, fieldren, tanbren, higgsmix, p2approx, looplevel,
                tl_running_mt, tl_bot_resum, 0);

        //CALL SLHAREAD(ERROR, SLHADATA, SLHAFILENAME, 1)
        SLHARead(&error, slhadata, slhafilename, abort);

        //call FHSetSLHA( error, slhadata )
        FHSetSLHA(&error, slhadata);

        //call FHHiggsCorr(error, MHiggs, SAeff, UHiggs, ZHiggs)
        double mhiggs[4];
        Complex SAeff;
        Complex UHiggs[3][3];
        Complex ZHiggs[3][3];
        FHHiggsCorr(&error, mhiggs, &SAeff, UHiggs, ZHiggs);

        //SPECTRUM(31) = Mass_Mh0
        //SPECTRUM(32) = Mass_MHH
        //SPECTRUM(33) = Mass_MA0
        //SPECTRUM(34) = Mass_MHp
        
        //CALL FHConstraints(error, gm2, Deltarho, MWMSSM, MWSM, SW2MSSM, 
        //&     SW2SM, edmeTh, edmn, edmHg )
        //FHConstraints(...);
        
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
