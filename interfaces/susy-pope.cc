#include "SLHA.h"

struct SUSYPOPEOpts {
    int LoopOption, IterOpt, Observables, HiggsOpt, Verbose, HiggsOpt,
        SMObsOpt;
};

struct SUSYPOPEPrecObs {
    double gammaZ, alphaHad
      gammaZ   = EXTPAR(1)
      alphaHad = EXTPAR(2)
};

extern "C" {
    void run_susypope(char slhafilename [], SUSYPOPEOpts* opts,
            SUSYPOPEPrecObs* out) {
        double POPEPRE[50];
        POPE_INTERFACE( ERROR, slhadata, gammaZ, alphaHad, POPEPRE )

    }
}

int main() {
    SUSYPOPEOpts opts(5,1,1,1,1,1,1);
    SUSYPOPEPrecObs obs;
}

/* double precision 
 * MT, MB,MTAU, MW, gammaZ, alphaHad, DeltaAlfa5had, DeltaAlfaQED, ZWidthexp, 
 * Zmass, TB, MA0, MHp, Mh0, MHH, MHiggs(4), M3SL, M3SE, M3SQ, M3SU, M3SD,
 * M2SL, M2SE, M2SQ, M2SU, M2SD, M1SL, M1SE, M1SQ, M1SU, M1SD, Qtau, Qt, Qb,
 * Atphase, Abphase, Atauphase, M2phase, M1phase, MUEphase ,PRE(50),
 * MSSMObs(35), SMObs(35)
 */

/* double complex
 * UHiggs(4,4), SAeff, MUE, M_1, M_2, M_3, At, Ab, Atau, Ac, As,
 * Amu, Au, Ad, Ae, slhadata(nslhadata)
 */
      
/* Integer 
 * error,I,J, LoopOption, IterOpt, Observables,HiggsOpt,Verbose,SMObsOpt,
 * observables
 */

/*
      DO I=8,18
         PRE(I)=-1.
      ENDDO   
      Call SetFlags_AMW(error,LoopOption,IterOpt,Observables,SMObsOpt,HiggsOpt,Verbose)
      IF ( error.NE.0 ) THEN
         PRINT *, '*** Error SetFlags_AMW:',error
         RETURN
      ENDIF

*     - Additional EW parameters
      DeltaAlfa5had = alphaHad
      DeltaAlfaQED  = 0.031497637D0
      ZWidthexp     = gammaZ
      Zmass         = SMInputs_MZ

*     - No phases
      M2phase   = 0D0
      M1phase   = 0D0
      MUEPhase  = 0D0
      Atphase   = 0D0
      Abphase   = 0D0
      Atauphase = 0D0

*     SUSY-POPE needs pole mass
      MB   = 4.8D0
*     - Define all other parameters from SLHA input
      MT   = SMInputs_Mt
      MTAU = SMInputs_Mtau
      MW   = Mass_MW
      TB   = MinPar_TB

      Mh0  = Mass_Mh0 
      MHH  = Mass_MHH
      MA0  = Mass_MA0
      MHp  = Mass_MHp
      SAeff = DSIN( DBLE(Alpha_Alpha) )

      M1SL = MSoft_MSL(1)
      M2SL = MSoft_MSL(2)
      M3SL = MSoft_MSL(3)
      M1SE = MSoft_MSE(1)
      M2SE = MSoft_MSE(2)
      M3SE = MSoft_MSE(3)
      M1SQ = MSoft_MSQ(1)
      M2SQ = MSoft_MSQ(2)
      M3SQ = MSoft_MSQ(3)
      M1SU = MSoft_MSU(1)
      M2SU = MSoft_MSU(2)
      M3SU = MSoft_MSU(3)
      M1SD = MSoft_MSD(1)
      M2SD = MSoft_MSD(2)
      M3SD = MSoft_MSD(3)
      MUE  = HMix_MUE
      Atau = Ae_Atau
      At   = Au_At
      Ab   = Ad_Ab
      Amu  = Ae_Atau
      Ac   = Au_At
      As   = Ad_Ab
      Ae   = Ae_Atau
      Au   = Au_At
      Ad   = Ad_Ab
      M_1  = MSoft_M1
      M_2  = MSoft_M2
      M_3  = MSoft_M3
      Qtau = HMix_Q
      Qt   = HMix_Q
      Qb   = HMix_Q

      DO I=1,4
         DO J=1,4
            UHiggs(I,J) = CVHMix_UH(I,J)
         ENDDO
      ENDDO
      
      CALL SetPara_AMW(error,
     &     MT, MB, MTAU, MW, Zmass,
     &     DeltaAlfa5had, DeltaAlfaQED,ZWidthexp, 
     &     TB, MA0, MHp, 
     &     Mh0, MHH,SAeff,
     &     MHiggs,              ! Note: if MHiggs is 0, MA0, MHp Mh0 and MHH are used instead 
     &     UHiggs,              ! Only used if Mh0<0
     &     M3SL, M3SE, M3SQ, M3SU, M3SD,
     &     M2SL, M2SE, M2SQ, M2SU, M2SD,
     &     M1SL, M1SE, M1SQ, M1SU, M1SD,
     &     MUE, MUEPhase,
     &     Atau, At, Ab, Amu, Ac, As, Ae, Au, Ad, 
     &     Atphase, Abphase, Atauphase,
     &     M_1, M_2, M_3, 
     &     M2phase, M1phase,
     &     Qtau, Qt, Qb)

      IF ( error.NE.0 ) THEN
         PRINT *, '*** Error SetPara_AMW:',error
         RETURN
      ENDIF

      goto 1234
      Print*,'=================================first'
      print*,'MT, MB, ML, MW, MZ',MT, MB, MTAU, MW, Zmass
      print*, 'DeltaAlfa5had, DeltaAlfaQED, ZWidthexp',
     &     DeltaAlfa5had, DeltaAlfaQED, ZWidthexp
      print*, 'TB, MA0, MHp, Mh0, MHH, SA',TB, MA0, MHp, Mh0, 
     &     MHH, SAeff
      print*,'M3SL, M3SE, M3SQ, M3SU, M3SD',M3SL, M3SE, M3SQ, 
     &     M3SU, M3SD
      print*, 'M2SL, M2SE, M2SQ, M2SU, M2SD',M2SL, M2SE, M2SQ, 
     &     M2SU, M2SD
      print*, 'M1SL, M1SE, M1SQ, M1SU, M1SD',M1SL, M1SE, M1SQ, 
     &     M1SU, M1SD
      print*, 'MUE, MUEPhase',MUE, MUEPhase
      print*,  'Atau, At, Ab, Amu, Ac, As, Ae, Au, Ad',
     &     Atau, At, Ab, Amu, Ac, As, Ae, Au, Ad
      print*,'Atphase, Abphase, Atauphase',Atphase, Abphase,Atauphase
      print*, 'M_1, M_2, M_3',M_1, M_2, M_3
      print*, 'M2phase, M1phase',M2phase, M1phase
      print*, 'Qtau, Qt, Qb',Qtau, Qt, Qb
      Print*,'===================================second'
 1234 continue

      Call CalcObs_AMW(error,MSSMObs,SMObs)
      IF (error.EQ.0) THEN
         
         PRE(8) = MSSMObs(1)
         PRE(9) = MSSMObs(27)
         PRE(10) = MSSMObs(11)
         IF (ABS(MSSMObs(11)-MSSMObs(12)).GT.10E-4) THEN
            PRINT*,'Gamma_Z not equal 10E-4', MSSMObs(11),MSSMObs(12)
         ENDIF   
         
         PRE(11) = MSSMObs(22)
         PRE(12) = MSSMObs(26)
         PRE(13) = MSSMObs(25)
         PRE(14) = MSSMObs(34)
         PRE(15) = MSSMObs(35)
         PRE(16) = MSSMObs(31)
         PRE(17) = MSSMObs(32)
         PRE(18) = MSSMObs(30)
         PRE(21) = MSSMObs(30)
         PRE(22) = MSSMObs(33)
         PRE(23) = MSSMObs(21)

      ELSE
         DO I=8,18
            PRE(I)=-1.
         ENDDO   
      ENDIF
      
      RETURN
      END
*/      

