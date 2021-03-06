//g++ -o susypope.x susypope.cc -I../packages/include/SLHALib -L../packages/lib -lSLHA -L../predictors/private/SUSY-POPE-0.1/ -lAMWObs -lgfortran
#include <iostream>
#include <iomanip>
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
//    double MW, sin_theta_eff, Gamma_z, Rl, Rb, Rc, Afb_b, Afb_c, Ab, Ac,
//           Al, Afb_l, sigma_had;
};

extern "C" {
// functions from SUSY-POPE (Fortran)
// set flags
    void setflags_amw_( int&, int&, int&, int&, int&, int&, int&);
// set paramters from slha and non-slha data
    void setpara_amw_(int&, 
            double&, double&, double&, double&, double&,
            double&, double&, double&, 
            double&, double&, double&, 
            double&, double&, std::complex<double>&, 
            double*, std::complex<double> a[][3], 
            double&, double&, double&, double&, double&, 
            double&, double&, double&, double&, double&, 
            double&, double&, double&, double&, double&, 
            std::complex<double>&, double&, 
            std::complex<double>&, std::complex<double>&, std::complex<double>&, std::complex<double>&, 
                std::complex<double>&, std::complex<double>&,std::complex<double>&, std::complex<double>&, 
                std::complex<double>&, 
            double&, double&, double &, 
            std::complex<double>&, std::complex<double>&, std::complex<double>&, 
            double&, double&, 
            double&, double&,double&);
// calculate the observables
    void calcobs_amw_(int&, double*, double*);
}


int set_parameters(std::complex<double>* slhadata, susypopeNoneSLHA* n_slha, bool verbose=false){
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
      std::complex<double> UHiggs[3][3];


      for (int I=0; I<3 ; I++){
        for (int J=0; J<3 ; J++){
            UHiggs[I][J] = CVHMix_UH(I+1,J+1); // FIXME: now sure if the matrix is transposed here...
        }
      }

      if (verbose){
        std::cout << "=============SUSY-POPE-INPUTS============" << std::endl;
        std::cout << " MT, MB, ML, MW, MZ" << std::setprecision(9) 
              <<"  "<< MT <<"  "<<  MB <<"  "<<  MTAU <<"  "<<  MW <<"  "<<  Zmass <<"  "<<  std::endl ;
        std::cout <<  " DeltaAlfa5had, DeltaAlfaQED, ZWidthexp" 
              <<"  "<<   DeltaAlfa5had <<"  "<<  DeltaAlfaQED <<"  "<<  ZWidthexp <<"  "<<  std::endl ;
        std::cout << " TB, MA0, MHp, Mh0, MHH, SA" 
              <<"  "<< TB <<"  "<<  MA0 <<"  "<<  MHp <<"  "<<  Mh0 << std::endl;
        std::cout << "  "<<   MHH <<"  "<<  SAeff <<"  "<<  std::endl ;
        std::cout << " M3SL, M3SE, M3SQ, M3SU, M3SD" 
              <<"  "<< M3SL <<"  "<<  M3SE <<"  "<<  M3SQ <<"  "<<   M3SU << std::endl;
        std::cout << "  "<<  M3SD << std::endl ;
        std::cout <<  " M2SL, M2SE, M2SQ, M2SU, M2SD" 
              <<"  "<< M2SL <<"  "<<  M2SE <<"  "<<  M2SQ <<"  "<<   M2SU << std::endl;
        std::cout << "  "<<  M2SD <<  std::endl ;
        std::cout <<  " M1SL, M1SE, M1SQ, M1SU, M1SD" 
              <<"  "<< M1SL <<"  "<<  M1SE <<"  "<<  M1SQ <<"  "<<   M1SU << std::endl;
        std::cout << "  "<<  M1SD <<"  "<<  std::endl ;
        std::cout <<  " MUE, MUEPhase" 
              <<" "<< MUE <<"  "<<  MUEPhase <<"  "<<  std::endl ;
        std::cout <<  " Atau, At, Ab, Amu, Ac, As, Ae, Au, Ad"
              <<" "<< Atau <<"  "<<  At << std::endl; 
        std::cout <<  " "<<  Ab <<"  "<<  Amu <<"  "<<  Ac <<"  "<<  As <<"  "<<  Ae << std::endl;
        std::cout <<  " "<<  Au <<"  "<<  Ad <<"  "<<  std::endl ;
        std::cout << " Atphase, Abphase, Atauphase"
              <<"  "<< Atphase <<"  "<<  Abphase <<"  "<< Atauphase <<"  "<<  std::endl ;
        std::cout <<  " M_1, M_2, M_3" 
              <<"  "<< M_1 <<"  "<<  M_2 <<"  "<<  M_3 <<"  "<<  std::endl ;
        std::cout <<  " M2phase, M1phase"
              <<"  "<< M2phase <<"  "<<  M1phase <<"  "<<  std::endl ;
        std::cout <<  " Qtau, Qt, Qb" 
              <<"  "<< Qtau <<"  "<<  Qt <<"  "<<  Qb <<"  "<<  std::endl ;
        std::cout << "=============SUSY-POPE-INPUTS============" << std::endl;
      }

      setpara_amw_(error, 
              MT, MB, MTAU, MW, Zmass, 
              DeltaAlfa5had, DeltaAlfaQED, ZWidthexp, 
              TB, MA0, MHp, 
              Mh0, MHH, SAeff, 
              MHiggs, UHiggs, 
              M3SL, M3SE, M3SQ, M3SU, M3SD, 
              M2SL, M2SE, M2SQ, M2SU, M2SD, 
              M1SL, M1SE, M1SQ, M1SU, M1SD, 
              MUE, MUEPhase, 
              Atau, At, Ab, Amu, Ac, As, Ae, Au, Ad, 
              Atphase, Abphase, Atauphase, 
              M_1, M_2, M_3, 
              M2phase, M1phase, 
              Qtau, Qt, Qb);
      return error;
}

int set_flags(susypopeFlags * flags){
    int error;
    setflags_amw_(error,flags->LoopOption, flags->IterOpt, flags->Observables, 
              flags->SMObsOpt , flags->HiggsOpt, flags->Verbose );
    return error;
}

extern "C" {

    int run_susypope(std::complex<double>* slhadata, susypopeNoneSLHA* n_slha,
        susypopeFlags* flags, susypopeObs* out, bool verbose=false) {
        int error(0);
        error = set_flags(flags);
        if (error) {
            std::cout << "set flags failed" << std::endl;
            return error;
        }
        error = set_parameters(slhadata, n_slha, verbose);
        if (error) {
            std::cout << "set parameters failed" << std::endl;
            return error;
        }
        calcobs_amw_(error, out->MSSMObs, out->SMObs);
        if (error){ 
            std::cout << "calcobs failed" << std::endl;
            return error;
        }
        return 0;
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

    std::cout <<  "MW           : " <<  obs.MSSMObs[0 ] << std::endl ;
    std::cout <<  "sin_theta_eff: " <<  obs.MSSMObs[26] << std::endl ;
    std::cout <<  "Gamma_z      : " <<  obs.MSSMObs[10] << std::endl ;
    std::cout <<  "Rl           : " <<  obs.MSSMObs[21] << std::endl ;
    std::cout <<  "Rb           : " <<  obs.MSSMObs[25] << std::endl ;
    std::cout <<  "Rc           : " <<  obs.MSSMObs[24] << std::endl ;
    std::cout <<  "Afb_b        : " <<  obs.MSSMObs[33] << std::endl ;
    std::cout <<  "Afb_c        : " <<  obs.MSSMObs[34] << std::endl ;
    std::cout <<  "Ab           : " <<  obs.MSSMObs[30] << std::endl ;
    std::cout <<  "Ac           : " <<  obs.MSSMObs[31] << std::endl ;
    std::cout <<  "Al           : " <<  obs.MSSMObs[29] << std::endl ;
    std::cout <<  "Afb_l        : " <<  obs.MSSMObs[33] << std::endl ;
    std::cout <<  "sigma_had    : " <<  obs.MSSMObs[20] << std::endl ;

}
