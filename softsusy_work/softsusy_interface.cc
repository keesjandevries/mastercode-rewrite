#include "softsusy-3.3.1/linalg.h"
#include "softsusy-3.3.1/softsusy.h"
#include "softsusy-3.3.1/lowe.h"
#include <iostream>

extern "C" 
{
    /*--------------*/
    /* DoubleVector */
    /*--------------*/
    DoubleVector* DoubleVector_new( int sz ) {
        return new DoubleVector(sz);
    }
    double DoubleVector_display( DoubleVector* dv, int pos )  { 
        return dv->display(pos); 
    }
    void DoubleVector_set( DoubleVector* dv, int pos, double val )  { 
        std::cout << pos << "," << val<< std::endl;
        (*dv)(pos) = val;
    }
    /*--------*/
    /* QedQcd */
    /*--------*/
    QedQcd* QedQcd_new() {
        return new QedQcd();
    }
    void setPoleMt(double mt) { mtPole = mt; }; ///< set pole top mass
    void setPoleMb(double mb) { mbPole = mb; }; ///< set pole bottom mass
    void setPoleMtau(double mtau) { mtauPole = mtau; }; ///< set pole tau mass
    void setMbMb(double mb)   { mbMb = mb;   }; ///< set mb(mb)
    /// sets a running quark mass
    void setMass(mass mno, double m) { mf(mno) = m; }; 
    /// sets QED or QCD structure constant
    void setAlpha(leGauge ai, double ap) { a(ai) = ap; }; 
    /// For exporting beta functions to Runge-Kutta
    void set(const DoubleVector &); 

    /*--------------*/
    /* MssmSoftsusy */
    /*--------------*/
    MssmSoftsusy* MssmSoftsusy_new() {
        return new MssmSoftsusy();
    }

    void MssmSoftsusy_lowOrg( void (*boundaryCondition) 
                                   (MssmSoftsusy &, const DoubleVector &),
                              double mxGuess,
                              const DoubleVector & pars, int sgnMu, double tanb,
                              const QedQcd & oneset, bool gaugeUnification,
                              bool ewsbBCscale = false) {

    }
} 
