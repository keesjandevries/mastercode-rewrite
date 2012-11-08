#include<iostream>
#include<complex>

#include "CSLHA.h"



struct BPhysicsObs {
        double BRbsg, BRKpnn , RDMb , RDMs, RDMK, BRXsll, BRbtn, BRKl2 ,Psll, Pdll, Pllsapx;
};

extern "C"{
    void bphysicsinterface_(  int &,  double_complex*,  double&, double &,  double&,  double&, double&, double&,
           double&, double&, double&, double&, double& );

    void run_bphysics(char slhafilename[], BPhysicsObs * out){
        int ERROR=0;
        double_complex  slhadata[nslhadata];
        const int abort(0);

        SLHARead(&ERROR, slhadata, slhafilename , abort);

        bphysicsinterface_( ERROR,    slhadata,   out->BRbsg,   out->BRKpnn,   out->RDMb,   out->RDMs,   
                        out->RDMK,   out->BRXsll,   out->BRbtn,   out->BRKl2,   out->Psll,   out->Pdll,   out->Pllsapx );
    }
}

                                          
int main(){
        BPhysicsObs  obs; 
        BPhysicsObs * pobs = &obs;

        char slhaname[]="000547-slha.out";

        run_bphysics(slhaname,pobs);

        std::cout << "Bs->mu mu: " << pobs->Psll << std::endl;
        return 0;
}

