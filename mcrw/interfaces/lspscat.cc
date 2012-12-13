#include<iostream>
#include<complex>

#include "CSLHA.h"

struct lspscatInputs {
    double SigmaPiN, SigmaPiNerr;
};

struct lspscatObs {
    double s2out, ss2out, s3out, ss3out;
};

// This global variable gets the values from the common block containing the
// values from lspscat

extern "C" { 
    double lspscat_( double&, double&, double&, double&, double&, double&, 
        double&, double&, double&, double&, double&, double&, double&, double&, 
        double&, double&, double&, double&, double&, double&, double&, double&,
        double&, double&, double&, double&, double&, double&, double&, double&,
        double&, double&, double&, double&, double&, double&, double&, double&,
        double&, double&, double&, double&);

    void run_lspscat(std::complex<double>* slhadata, lspscatInputs* in,
            lspscatObs* out ) {
        // cos otherwise wow...
        using std::real;
        // neutralino masses (correct order!)
        double n1(real(Mass_MNeu(1))), n2(real(Mass_MNeu(2))),
               n3(real(Mass_MNeu(4))), n4(real(Mass_MNeu(3)));
        // neutralino mixing matrix
        double nm11(real(NMix_ZNeu(1,1))), nm12(real(NMix_ZNeu(2,1))),
               nm13(real(NMix_ZNeu(4,1))), nm14(real(NMix_ZNeu(3,1)));
        double nm21(real(NMix_ZNeu(1,2))), nm22(real(NMix_ZNeu(2,2))),
               nm23(real(NMix_ZNeu(4,2))), nm24(real(NMix_ZNeu(3,2)));
        double nm31(real(NMix_ZNeu(1,3))), nm32(real(NMix_ZNeu(2,3))),
               nm33(real(NMix_ZNeu(4,3))), nm34(real(NMix_ZNeu(3,3)));
        double nm41(real(NMix_ZNeu(1,4))), nm42(real(NMix_ZNeu(2,4))),
               nm43(real(NMix_ZNeu(4,4))), nm44(real(NMix_ZNeu(3,4)));
        // h0, A0 masses and mixing angle
        double lhiggs(real(Mass_Mh0)), shiggs(real(Mass_MA0)), 
               halpha(real(Alpha_Alpha));
        // sinb, m_top, m_b
        double sbeta(sin(atan(real(MinPar_TB)))),
               mtin(real(SMInputs_Mt)), mbin(4.2);
        // Squark mass squared
        // Mass_MSf({L,R},{1:neutrino, 2:lepton, 3: uptype, 4: downtype},{generation})
        double ul =real(Mass_MSf(1,3,1) )*real(Mass_MSf(1,3,1)); 
        double dl =real(Mass_MSf(1,4,1) )*real(Mass_MSf(1,4,1));
        double ur =real(Mass_MSf(2,3,1) )*real(Mass_MSf(2,3,1));
        double dr =real(Mass_MSf(2,4,1) )*real(Mass_MSf(2,4,1));
        // just to be completely sure:
        double b1 = std::min(real(Mass_MSf(1,4,3)),real(Mass_MSf(2,4,3)));
        double b2 = std::max(real(Mass_MSf(1,4,3)),real(Mass_MSf(2,4,3)));
        double t1 = std::min(real(Mass_MSf(1,3,3)),real(Mass_MSf(2,3,3)));
        double t2 = std::max(real(Mass_MSf(1,3,3)),real(Mass_MSf(2,3,3)));
        double tt(acos(real(StopMix_USf(1,1)))),
               tb(acos(real(SbotMix_USf(1,1))));
        // want squark mass squared
        b1*=b1;
        b2*=b2;
        t1*=t1;
        t2*=t2;

        lspscat_(in->SigmaPiN, in->SigmaPiNerr, n1, n2, n3, n4, nm11, nm12,
                nm13, nm14, nm21, nm22, nm23, nm24, nm31, nm32, nm33, nm34,
                nm41, nm42, nm43, nm44, lhiggs, shiggs, halpha, sbeta, mtin,
                mbin, ul, ur, dl, dr, b1, b2, t1, t2, tt, tb, out->s2out,
                out->ss2out, out->s3out, out->ss3out);

    }
}


int main(){
    lspscatObs obs; 
    lspscatInputs inp;
    inp.SigmaPiN=50.0;
    inp.SigmaPiNerr=14.0;

    char slhaname[]="../slhas/test.slha";
    int error(0), abort(0);
    std::complex<double> slhadata[nslhadata];
    SLHARead(&error, slhadata, slhaname, abort);

    run_lspscat(slhadata,&inp,&obs);

    std::cout << std::scientific << "s2out : " << obs.s2out << std::endl;
    std::cout << std::scientific << "ss2out: " << obs.ss2out << std::endl;
    std::cout << std::scientific << "s3out : " << obs.s3out  << std::endl;
    std::cout << std::scientific << "ss3out: " << obs.ss3out << std::endl;
    return 0;
}
