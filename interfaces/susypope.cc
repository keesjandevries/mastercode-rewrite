//g++ -o susypope.x susypope.cc -I../packages/include/SLHALib -L../packages/lib -lSLHA -L../predictors/private/SUSY-POPE-0.1/ -lAMWObs -lgfortran
#include <iostream>
#include <complex>
#include <cmath>

#include "CSLHA.h"

// struct that contains the flags for susypope
//      LoopOption  : 5 only:
//      IterOpt     : 1 = Standard iteration, 2 = Iteration optimised for speed (almost perfect accuracy),
//                           3 = very fast iteration (good accuracy for well chosen starting value of iteration)
//      Observables : 1 = all the Z Observables, 2 = Sin^2(theta)_eff only, 3 = MW only
//      HiggsOpt    : 1 = directly insert Higgs masses, 2 = born Higgs, 3 = FH
//      Verbose     : 1 = no information printed to screen, 2 = some information, 3 = lots of information)
//      SMObsOpt    : ??????????????
struct susypopeFlags{
    int LoopOption, IterOpt, Observables, HiggsOpt, Verbose,  SMObsOpt;
    // constructors
    susypopeFlags(int lOpt, int iOpt, int obs, int hOpt, int v, int smOpt):
        LoopOption(lOpt), IterOpt(iOpt), Observables(obs), HiggsOpt(hOpt),
        Verbose(v), SMObsOpt(smOpt){}
};

// some of the imput parameters are not contained in the slha file 
// this struct collects all of them
struct susypopeNoneSLHA {
    double DeltaAlfa5had, DeltaAlfaQED, ZWidthexp, M2phase, M1phase, MUEPhase,
           Atphase, Abphase, Atauphase, MB; 
};

// combination of flags and non-slha inputs
// output
struct susypopeObs {
    double MSSMObs[35], SMObs[35];
    double MW, sin_theta_eff, Gamma_z, Rl, Rb, Rc, Afb_b, Afb_c, Ab_16, Ac_17,
           Al, Al_fb, sigma_had;
};

extern "C" {
// functions from SUSY-POPE (Fortran)
// set flags
    void setflags_amw_( int&, int&, int&, int&, int&, int&, int&);
// set paramters from slha and non-slha data
    void setpara_amw_(int&, double&, double&, double&, double&, double&,
            double&, double&, double&, double&, double&, double&, double&,
            double&, std::complex<double>&, double*,
            std::complex<double> a[][4], double&, double&, double&, double&,
            double&, double&, double&, double&, double&, double&, double&,
            double&, double&, double&, double&, std::complex<double>&, double&, 
            std::complex<double>&, std::complex<double>&,
            std::complex<double>&, std::complex<double>&,
            std::complex<double>&, std::complex<double>&,
            std::complex<double>&, std::complex<double>&,
            std::complex<double>&, double&, double&, double &, 
            std::complex<double>&, std::complex<double>&,
            std::complex<double>&, double&, double&, double&, double&,
            double&);
// calculate the observables
    void calcobs_amw_(int&, double*, double*);
}


int set_parameters(std::complex<double>* slhadata, susypopeNoneSLHA* n_slha){
      int error=0;
      double DeltaAlfa5had = n_slha->DeltaAlfa5had;
      double DeltaAlfaQED  = n_slha->DeltaAlfaQED ;
      double ZWidthexp     = n_slha->ZWidthexp    ;

      double M2phase       = n_slha->M2phase      ;
      double M1phase       = n_slha->M1phase      ;
      double MUEPhase      = n_slha->MUEPhase     ;
      double Atphase       = n_slha->Atphase      ;
      double Abphase       = n_slha->Abphase      ;
      double Atauphase     = n_slha->Atauphase    ;

      double MB            = n_slha->MB           ;

// inputs from slha 
      double Zmass=std::real( SMInputs_MZ);
      double MT   =std::real( SMInputs_Mt);
      double MTAU =std::real( SMInputs_Mtau);
      double MW   =std::real( Mass_MW);
      double TB   =std::real( MinPar_TB);

      double Mh0  =std::real( Mass_Mh0 );
      double MHH  =std::real( Mass_MHH);
      double MA0  =std::real( Mass_MA0);
      double MHp  =std::real( Mass_MHp);
      std::complex<double> SAeff( sin( std::real(Alpha_Alpha )), 0.0 ) ;

      double M1SL =std::real( MSoft_MSL(1));
      double M2SL =std::real( MSoft_MSL(2));
      double M3SL =std::real( MSoft_MSL(3));
      double M1SE =std::real( MSoft_MSE(1));
      double M2SE =std::real( MSoft_MSE(2));
      double M3SE =std::real( MSoft_MSE(3));
      double M1SQ =std::real( MSoft_MSQ(1));
      double M2SQ =std::real( MSoft_MSQ(2));
      double M3SQ =std::real( MSoft_MSQ(3));
      double M1SU =std::real( MSoft_MSU(1));
      double M2SU =std::real( MSoft_MSU(2));
      double M3SU =std::real( MSoft_MSU(3));
      double M1SD =std::real( MSoft_MSD(1));
      double M2SD =std::real( MSoft_MSD(2));
      double M3SD =std::real( MSoft_MSD(3));
      std::complex<double> MUE  = HMix_MUE;
      std::complex<double> Atau = Ae_Atau;
      std::complex<double> At   = Au_At;
      std::complex<double> Ab   = Ad_Ab;
      std::complex<double> Amu  = Ae_Atau;
      std::complex<double> Ac   = Au_At;
      std::complex<double> As   = Ad_Ab;
      std::complex<double> Ae   = Ae_Atau;
      std::complex<double> Au   = Au_At;
      std::complex<double> Ad   = Ad_Ab;
      std::complex<double> M_1  = MSoft_M1;
      std::complex<double> M_2  = MSoft_M2;
      std::complex<double> M_3  = MSoft_M3;
      double Qtau =std::real( HMix_Q);
      double Qt   =std::real( HMix_Q);
      double Qb   =std::real( HMix_Q);
      
      double MHiggs[]={0.,0.,0.,0.}; // yes hard coded, could be promoted to non-slha inputs
      std::complex<double> UHiggs[4][4];


      for (int I=0; I<4 ; I++){
        for (int J=0; J<4 ; J++){
            UHiggs[I][J] = CVHMix_UH(I+1,J+1); // FIXME: now sure if the matrix is transposed here...
        }
      }

      setpara_amw_(error, MT, MB, MTAU, MW, Zmass, DeltaAlfa5had, DeltaAlfaQED,
              ZWidthexp, TB, MA0, MHp, Mh0, MHH, SAeff, MHiggs, UHiggs, M3SL,
              M3SE, M3SQ, M3SU, M3SD, M2SL, M2SE, M2SQ, M2SU, M2SD, M1SL, M1SE,
              M1SQ, M1SU, M1SD, MUE, MUEPhase, Atau, At, Ab, Amu, Ac, As, Ae,
              Au, Ad, Atphase, Abphase, Atauphase, M_1, M_2, M_3, M2phase,
              M1phase, Qtau, Qt, Qb);
      return error;
}

int set_flags(susypopeFlags * flags){
    int error;
    setflags_amw_(error,flags->LoopOption, flags->IterOpt, flags->Observables, 
              flags->SMObsOpt , flags->HiggsOpt, flags->Verbose );
    return error;
}

extern "C" {

    void run_susypope(std::complex<double>* slhadata, susypopeNoneSLHA* n_slha,
        susypopeFlags* flags, susypopeObs* out) {
        int error(0);
        error = set_flags(flags);
        if (error) std::cout << "set flags failed" << std::endl;
        error = set_parameters(slhadata, n_slha);
        if (error) std::cout << "set parameters failed" << std::endl;
        calcobs_amw_(error, out->MSSMObs, out->SMObs);
        if (error) std::cout << "calcobs failed" << std::endl;

        // extract observables in more readable terms
        out->MW             =  out->SMObs[0 ];
        out->sin_theta_eff  =  out->SMObs[26];
        out->Gamma_z        =  out->SMObs[10];
        out->Rl             =  out->SMObs[21];
        out->Rb             =  out->SMObs[25];
        out->Rc             =  out->SMObs[24];
        out->Afb_b          =  out->SMObs[33];
        out->Afb_c          =  out->SMObs[34];
        out->Ab_16          =  out->SMObs[30];
        out->Ac_17          =  out->SMObs[31];
        out->Al             =  out->SMObs[29];
        out->Al_fb          =  out->SMObs[33];
        out->sigma_had      =  out->SMObs[20];

    }
}



int main() {
    susypopeObs obs; 
    susypopeFlags flags(5,1,1,1,1,1);
    susypopeNoneSLHA n_slha;

    n_slha.DeltaAlfa5had = 0.02749;
    n_slha.DeltaAlfaQED  = 0.031497637;
    n_slha.ZWidthexp     = 2.4952;

    n_slha.M2phase   = 0.0;
    n_slha.M1phase   = 0.0;
    n_slha.MUEPhase  = 0.0;
    n_slha.Atphase   = 0.0;
    n_slha.Abphase   = 0.0;
    n_slha.Atauphase = 0.0;

    n_slha.MB   = 4.8;

    char slhaname[]="slhas/sp_test.slha";
    // read the slha file
    int error=0;
    std::complex<double>  slhadata[nslhadata];
    const int abort(0);
    SLHARead(&error, slhadata, slhaname , abort);

    run_susypope(slhadata,&n_slha,&flags,&obs);
    //C0i = Ccache(cgetr + id)
    // cgetr
    // -----
    // Correct =  5379
    // Error Causing = 8928284
    // Getting different memory address styles between the susypope executable
    // that is tied up against libAMWObs and hte one that uses libmcsoftsusy

    std::cout <<  "MW           : " <<  obs.SMObs[0]      << std::endl ;
    std::cout <<  "sin_theta_eff: " <<  obs.sin_theta_eff << std::endl ;
    std::cout <<  "Gamma_z      : " <<  obs.Gamma_z       << std::endl ;
    std::cout <<  "Rl           : " <<  obs.Rl            << std::endl ;
    std::cout <<  "Rb           : " <<  obs.Rb            << std::endl ;
    std::cout <<  "Rc           : " <<  obs.Rc            << std::endl ;
    std::cout <<  "Afb_b        : " <<  obs.Afb_b         << std::endl ;
    std::cout <<  "Afb_c        : " <<  obs.Afb_c         << std::endl ;
    std::cout <<  "Ab_16        : " <<  obs.Ab_16         << std::endl ;
    std::cout <<  "Ac_17        : " <<  obs.Ac_17         << std::endl ;
    std::cout <<  "Al           : " <<  obs.Al            << std::endl ;
    std::cout <<  "Al_fb        : " <<  obs.Al_fb         << std::endl ;
    std::cout <<  "sigma_had    : " <<  obs.sigma_had     << std::endl ;

}

//      std::cout << "Zmass" << Zmass << std::endl;
//      std::cout << "MT   " << MT    << std::endl;
//      std::cout << "MTAU " << MTAU  << std::endl;
//      std::cout << "MW   " << MW    << std::endl;
//      std::cout << "TB   " << TB    << std::endl;
//      std::cout << "Mh0  " << Mh0   << std::endl;
//      std::cout << "MHH  " << MHH   << std::endl;
//      std::cout << "MA0  " << MA0   << std::endl;
//      std::cout << "MHp  " << MHp   << std::endl;
//      std::cout << "SAeff" << SAeff << std::endl;
//      std::cout << "M1SL " << M1SL  << std::endl;
//      std::cout << "M2SL " << M2SL  << std::endl;
//      std::cout << "M3SL " << M3SL  << std::endl;
//      std::cout << "M1SE " << M1SE  << std::endl;
//      std::cout << "M2SE " << M2SE  << std::endl;
//      std::cout << "M3SE " << M3SE  << std::endl;
//      std::cout << "M1SQ " << M1SQ  << std::endl;
//      std::cout << "M2SQ " << M2SQ  << std::endl;
//      std::cout << "M3SQ " << M3SQ  << std::endl;
//      std::cout << "M1SU " << M1SU  << std::endl;
//      std::cout << "M2SU " << M2SU  << std::endl;
//      std::cout << "M3SU " << M3SU  << std::endl;
//      std::cout << "M1SD " << M1SD  << std::endl;
//      std::cout << "M2SD " << M2SD  << std::endl;
//      std::cout << "M3SD " << M3SD  << std::endl;
//      std::cout << "MUE  " << MUE   << std::endl;
//      std::cout << "Atau " << Atau  << std::endl;
//      std::cout << "At   " << At    << std::endl;
//      std::cout << "Ab   " << Ab    << std::endl;
//      std::cout << "Amu  " << Amu   << std::endl;
//      std::cout << "Ac   " << Ac    << std::endl;
//      std::cout << "As   " << As    << std::endl;
//      std::cout << "Ae   " << Ae    << std::endl;
//      std::cout << "Au   " << Au    << std::endl;
//      std::cout << "Ad   " << Ad    << std::endl;
//      std::cout << "M_1  " << M_1   << std::endl;
//      std::cout << "M_2  " << M_2   << std::endl;
//      std::cout << "M_3  " << M_3   << std::endl;
//      std::cout << "Qtau " << Qtau  << std::endl;
//      std::cout << "Qt   " << Qt    << std::endl;
//      std::cout << "Qb   " << Qb    << std::endl;
