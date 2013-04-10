#include <iostream>
#include "sources/micromegas.h"
#include "MSSM/lib/pmodel.h"

struct MicromegasPrecObs {
    double  Omega, Bll, Bsg, SMbsg, sigma_p_si;
};

const int fast = 1;
const double Beps = 1e-5;

// NOTE: $MICROMEGAS/MSSM/main.c contains all the info you need to understand
// or modify this module

extern "C" {
    int run_micromegas(char slhafilename[], MicromegasPrecObs* out) {
        double omegaMu,bsg, bll, sigppMu;

        // get slha file
        int error = lesHinput(slhafilename);
        if (error != 0) {
            std::cout << "*** Error: micromegas fail to open " <<
                slhafilename << std::endl;//SLHAFILE
            return error;
        }

        //calculate relic density
        char dMb_s [] = "dMb";
        assignValW(dMb_s,deltaMb());
        
        char mess[20];

        error = sortOddParticles(mess);
        if(error != 0) {
                std::cout << "Can not calculate " << mess << std::endl;
                return error;
        }

        char lsp_label [] = "~o1";
        if(strcmp(mess,lsp_label) != 0) {
            std::cout << "~o1 is not LSP" << std::endl;
            return error;
        }

        double Xf;
        out->Omega = darkOmega(&Xf,fast,Beps);
        out->Bll = bsmumu();
        out->Bsg = bsgnlo(&(out->SMbsg));

        
        if(error != 0) {
            std::cout << "! Calculation failed: no point in continuing" <<
                std::endl;
            return error;
        }
        // calculate sigma_p_si
        double pA0[2],pA5[2],nA0[2],nA5[2];
        double Nmass=0.939; /*nucleon mass*/
        double SCcoeff;        
        nucleonAmplitudes(FeScLoop, pA0,pA5,nA0,nA5);
        SCcoeff=4/M_PI*3.8937966E8*pow(Nmass*Mcdm/(Nmass+ Mcdm),2.);
        out->sigma_p_si=SCcoeff*pA0[0]*pA0[0];
        return 0;
    }
}
