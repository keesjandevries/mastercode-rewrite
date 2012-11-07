#include<iostream>
#include<complex>

#include "CSLHA.h"


extern "C"{
    void bphysicsinterface_(  int *,  double_complex*,  double*, double *,  double*,  double*, double*, double*,
           double*, double*, double*, double*, double* );
}

struct BPhysicsObs {
        double BRbsg, BRKpnn , RDMb , RDMs, RDMK, BRXsll, BRbtn, BRKl2 ,Psll, Pdll, Pllsapx;
};
                                          
int main(){
        int ERROR=0;
        double_complex  slhadata[nslhadata];
        const int abort(0);
        SLHARead(&ERROR, slhadata, "ss.slha", abort);
        BPhysicsObs *obs;


        bphysicsinterface_( &ERROR,    slhadata,   &obs->BRbsg,   &obs->BRKpnn,   &obs->RDMb,   &obs->RDMs,   
                        &obs->RDMK,   &obs->BRXsll,   &obs->BRbtn,   &obs->BRKl2,   &obs->Psll,   &obs->Pdll,   &obs->Pllsapx );
        return 0;
}

