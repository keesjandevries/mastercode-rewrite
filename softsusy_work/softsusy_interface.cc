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
    void QedQcd_setPoleMt(QedQcd *qq, double mt) { 
        qq->setPoleMt(mt); 
    }
    void QedQcd_setPoleMb(QedQcd *qq, double mb) {
        qq->setPoleMb(mb); 
    }
    void QedQcd_setPoleMtau(QedQcd *qq, double mtau) {
        qq->setPoleMtau(mtau); 
    }
    void QedQcd_setMbMb(QedQcd *qq, double mb)   {
        qq->setMbMb(mb);   
    }
    void QedQcd_setMass(QedQcd *qq, mass mno, double m) {
        qq->setMass(mno,m);
    } 
    void QedQcd_setAlpha(QedQcd *qq, leGauge ai, double ap) {
        //  typedef enum {mUp=1, mCharm, mTop, mDown, mStrange, mBottom, mElectron,
        //            mMuon, mTau} mass;
        //  typedef enum {ALPHA=1, ALPHAS} leGauge;
        qq->setAlpha(ai, ap);
    } 
    void QedQcd_set(QedQcd *qq, DoubleVector *dv) {
        qq->set(*dv);
    }
        
    /*--------------*/
    /* MssmSoftsusy */
    /*--------------*/
    MssmSoftsusy* MssmSoftsusy_new() {
        return new MssmSoftsusy();
    }

//    void MssmSoftsusy_lowOrg( void (*boundaryCondition) 
//                                   (MssmSoftsusy &, const DoubleVector &),
//                              double mxGuess,
//                              const DoubleVector & pars, int sgnMu, double tanb,
//                              const QedQcd & oneset, bool gaugeUnification,
//                              bool ewsbBCscale = false) {
//
//    }
} 
