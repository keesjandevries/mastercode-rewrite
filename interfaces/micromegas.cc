#include <iostream>
#include "sources/micromegas.h"
#include "MSSM/lib/pmodel.h"

struct MicromegasPrecObs {
    double  Omega, Bll, Bsg, SMbsg;
};

const int fast = 1;
const double Beps = 1e-5;

extern "C" {
    void run_micromegas(char slhafilename[], MicromegasPrecObs* out) {
        double omegaMu,bsg, bll, sigppMu;
        // need to check this argument, seems to not do anything anymore
        int error = readLesH(slhafilename,2);
        if (error != 0) {
            std::cout << "*** Error: micromegas fail to open " <<
                slhafilename << std::endl;//SLHAFILE
        }

        //To include threshold corrections to H-b-B vertex  
        //micromegas_2.2/MSSM/lib/bsg_nlo.c:double deltaMb(void)
        char dMb_s [] = "dMb";
        assignValW(dMb_s,deltaMb());
        
        char mess[20];
        // micromegas_2.2/sources/omega.c:int sortOddParticles(char * lsp)
        error = sortOddParticles(mess);
        if(error != 0) {
                std::cout << "Can not calculate " << mess << std::endl;
                return;
        }

        char lsp_label [] = "~o1";
        if(strcmp(mess,lsp_label) != 0) {
            std::cout << "~o1 is not LSP" << std::endl;
            //ERROR = -10
            //IF (PENALTY(8).LE.0) PENALTY(8) = 10.
            return;
        }

        double Xf;
        out->Omega = darkOmega(&Xf,fast,Beps);
        out->Bll = bsmumu();
        out->Bsg = bsgnlo(&(out->SMbsg));

        //Copied from micromegas_2.2/MSSM/main.F, l. 419 sqq
        //ERROR = nucleonAmplitudes( FeScLoop, pA0, pA5, nA0, nA5 )
        //Nmass=0.939d0 ! Nucleon mass
        //SCcoeff=4/M_PI*3.8937966E8*(Nmass*lopmass()/(Nmass+ lopmass()))**2
        //sigpSI = SCcoeff*pA0(1)**2
        
        if(error != 0) {
            std::cout << "! Calculation failed: no point in continuing" <<
                std::endl;
        }
    }
}

//int main() {
    //MicromegasPrecObs mo_out;
    //char filename [] = "test.slha";
    //run_micromegas(filename, &mo_out);
    //std::cout << mo_out.Omega << std::endl;
//}
    
        //- chargino
        //SPECTRUM(1)=findValW("MC1")
        //SPECTRUM(2)=findValW("MC2") 
        //- neutralino
        //SPECTRUM(3)=findValW("MNE1") 
        //SPECTRUM(4)=findValW("MNE2")       
        //SPECTRUM(5)=findValW("MNE3") 
        //SPECTRUM(6)=findValW("MNE4")
        //- sleptons
        //SPECTRUM(7)=findValW("MSeR") 
        //SPECTRUM(8)=findValW("MSeL") 
        //SPECTRUM(9)=findValW("MSne") 
        //SPECTRUM(10)=findValW("MSmR") 
        //SPECTRUM(11)=findValW("MSmL") 
        //SPECTRUM(12)=findValW("MSnm") 
        //SPECTRUM(13)=findValW("MSl1") 
        //SPECTRUM(14)=findValW("MSl2") 
        //SPECTRUM(15)=findValW("MSnl") 
        
        //- squarks - LHC cannot identify flavour
        
        //SPECTRUM(16)=findValW("MSdR") 
        //SPECTRUM(16)=SPECTRUM(16)+findValW("MSuR") 
        //SPECTRUM(16)=SPECTRUM(16)+findValW("MSsR") 
        //SPECTRUM(16)=SPECTRUM(16)+findValW("MScR")
        //SPECTRUM(16)=SPECTRUM(16)/4D0
        
        //SPECTRUM(17)=findValW("MSdL") 
        //SPECTRUM(17)=SPECTRUM(17)+findValW("MSuL") 
        //SPECTRUM(17)=SPECTRUM(17)+findValW("MSsL") 
        //SPECTRUM(17)=SPECTRUM(17)+findValW("MScL")
        //SPECTRUM(17)=SPECTRUM(17)/4D0    
        
        //SPECTRUM(18)=findValW("MSt1") 
        //SPECTRUM(19)=findValW("MSt2")
        //SPECTRUM(20)=findValW("MSb1") 
        //SPECTRUM(21)=findValW("MSb2") 
        
        //- Gluino
        //SPECTRUM(22)=findValW("MSG")
        //- Higgs sector
        //SPECTRUM(23)=findValW("Mh") 
        //SPECTRUM(24)=findValW("MHH" ) 
        //SPECTRUM(25)=findValW("MH3" ) 
        //SPECTRUM(26)=findValW("MHc" ) 
        
        //- Edge measurements
        //-- mll max
        //SPECTRUM(27)=DSQRT((SPECTRUM(4)**2-SPECTRUM(10)**2)
             //*(SPECTRUM(10)**2-SPECTRUM(3)**2)/
             //SPECTRUM(10)**2)
        
        //-- mqll max
        //SPECTRUM(28)=DSQRT((SPECTRUM(17)**2-SPECTRUM(4)**2)
             //*(SPECTRUM(4)**2-SPECTRUM(3)**2)/
         //SPECTRUM(4)**2)
        
        //mql(mu) min
        //SPECTRUM(29)=DSQRT((SPECTRUM(17)**2-SPECTRUM(4)**2)
             //*(SPECTRUM(4)**2-SPECTRUM(10)**2)/
             //SPECTRUM(4)**2)
        
        //Mtb^max edge (for SPS5)
        //mtop  = findValW("Mtp")
        //mstop1 = findValW("MSt1")
        //mchi1 = findValW("MC1")
        //mgluino = findValW("MSG")
        //SPECTRUM(30) = 
             //DSQRT( Mtop**2 + (mstop1**2-mchi1**2)/2D0/(mstop1**2)
                              //* ((mgluino**2-mstop1**2-mtop**2)
                                 //+ DSQRT((mgluino**2-(mstop1-mtop)**2)
                                          //*(mgluino**2-(mstop1+mtop)**2))) )
        
        
        //IF (ICALL.EQ.0.AND.NSPCON.GT.0) THEN
           //PRINT*,'START VALUES' 
        //Use predicted spectrum for the moment 
           //PRINT*,'------------------------'
           //Shift=5.0
           //DO I=1,NSPCON
              //PRINT*,ID_SPC(I),REAL(SPECTRUM(I)),  SHIFT, SHIFT
           //ENDDO
           //ICALL=1
        //ENDIF
        
