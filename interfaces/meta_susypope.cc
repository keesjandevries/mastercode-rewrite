//g++ -o test.x -Wl,-rpath,packages/lib interfaces/meta_susypope.cc
//-Lpackages/lib/ -lmcsusypope -Lpackages/lib/ -lSLHA
//-Ipackages/include/SLHALib
#include <iostream>
#include <complex>
#include <cmath>
#include "CSLHA.h"

extern "C" {
    struct susypopeFlags{
        int LoopOption, IterOpt, Observables, HiggsOpt, Verbose,  SMObsOpt;
        susypopeFlags(int lOpt, int iOpt, int obs, int hOpt, int v, int smOpt);//:
            //LoopOption(lOpt), IterOpt(iOpt), Observables(obs), HiggsOpt(hOpt),
            //Verbose(v), SMObsOpt(smOpt){}
    };

    struct susypopeNoneSLHA {
        double DeltaAlfa5had, DeltaAlfaQED, ZWidthexp, M2phase, M1phase, MUEPhase,
               Atphase, Abphase, Atauphase, MB; 
    };

    struct susypopeObs {
        double MSSMObs[35], SMObs[35];
        double MW, sin_theta_eff, Gamma_z, Rl, Rb, Rc, Afb_b, Afb_c, Ab_16, Ac_17,
               Al, Al_fb, sigma_had;
    };

    void run_susypope(std::complex<double>*, susypopeNoneSLHA*,
            susypopeFlags*, susypopeObs*);

    double cachelookup_(double *inputs, void (*)(double *, double *),
            int &, int &, int &);
}

void my_fill(double *inputs, double *outputs) {
    for(int i=0; i<6; ++i) {
        outputs[i] = i;
    }
    return;
}

int main() {
    double* inputs = new double[6];
    for(int i=0; i < 6; ++i) {
        inputs[i] = 2*i+6;
    }
    int n_inputs(6), n_outputs(6), pos(3);
    double x;
    for(int i=0; i<1; ++i) {
        for(int i=0; i < 6; ++i) {
            inputs[i] = 6-i;
        }
        x = cachelookup_(inputs, &my_fill, n_inputs, n_outputs, pos);
        std::cout << x << std::endl;
        for(int i=0; i < 6; ++i) {
            inputs[i] = i+1;
        }
        x = cachelookup_(inputs, &my_fill, n_inputs, n_outputs, ++pos);
        std::cout << x << std::endl;
    }
}
//int main() {
    //susypopeObs obs; 
    //susypopeFlags flags(5,1,1,1,1,1);
    //susypopeNoneSLHA n_slha;

    //n_slha.DeltaAlfa5had = 0.02749;
    //n_slha.DeltaAlfaQED  = 0.031497637;
    //n_slha.ZWidthexp     = 2.4952;

    //n_slha.M2phase   = 0.0;
    //n_slha.M1phase   = 0.0;
    //n_slha.MUEPhase  = 0.0;
    //n_slha.Atphase   = 0.0;
    //n_slha.Abphase   = 0.0;
    //n_slha.Atauphase = 0.0;

    //n_slha.MB   = 4.8;

    //char slhaname[]="slhas/sp_test.slha";
    //// read the slha file
    //int error=0;
    //std::complex<double>  slhadata[nslhadata];
    //const int abort(0);
    //SLHARead(&error, slhadata, slhaname , abort);

    //run_susypope(slhadata,&n_slha,&flags,&obs);

    //std::cout <<  "MW           : " <<  obs.SMObs[0]      << std::endl ;
    //std::cout <<  "sin_theta_eff: " <<  obs.sin_theta_eff << std::endl ;
    //std::cout <<  "Gamma_z      : " <<  obs.Gamma_z       << std::endl ;
    //std::cout <<  "Rl           : " <<  obs.Rl            << std::endl ;
    //std::cout <<  "Rb           : " <<  obs.Rb            << std::endl ;
    //std::cout <<  "Rc           : " <<  obs.Rc            << std::endl ;
    //std::cout <<  "Afb_b        : " <<  obs.Afb_b         << std::endl ;
    //std::cout <<  "Afb_c        : " <<  obs.Afb_c         << std::endl ;
    //std::cout <<  "Ab_16        : " <<  obs.Ab_16         << std::endl ;
    //std::cout <<  "Ac_17        : " <<  obs.Ac_17         << std::endl ;
    //std::cout <<  "Al           : " <<  obs.Al            << std::endl ;
    //std::cout <<  "Al_fb        : " <<  obs.Al_fb         << std::endl ;
    //std::cout <<  "sigma_had    : " <<  obs.sigma_had     << std::endl ;
//}
