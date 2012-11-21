#include<iostream>
#include<complex>

#include "CSLHA.h"



struct BPhysicsObs {
        double BRbsg, BRKpnn, RDMb, RDMs, RDMK, BRXsll, BRbtn, BRKl2, Psll,
               Pdll, Pllsapx;
};

extern "C"{
    void bphysicsinterface_( int &, double_complex*, double&, double &,
            double&, double&, double&, double&, double&, double&, double&,
            double&, double& );

    void run_bphysics(std::complex<double>* slhadata, BPhysicsObs* out){
        int ERROR=0;
        const int abort(0);

        bphysicsinterface_( ERROR, slhadata, out->BRbsg, out->BRKpnn,
                out->RDMb, out->RDMs, out->RDMK, out->BRXsll, out->BRbtn,
                out->BRKl2, out->Psll, out->Pdll, out->Pllsapx );
    }
}

                                          
int main(){
        BPhysicsObs obs; 

        char slhaname[]="../slhas/test.slha";

        int error(0), abort(0);
        std::complex<double> slhadata[nslhadata];
        SLHARead(&error, slhadata, slhaname, abort);
        run_bphysics(slhadata,&obs);

        std::cout << "Bs->mu mu: " << obs.Psll << std::endl;
        return 0;
}

