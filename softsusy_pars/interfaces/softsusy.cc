#include "linalg.h"
#include "softsusy.h"
#include "lowe.h"
#include <iostream>

/*--------------------*/
/* BoundaryConditions */
/*--------------------*/
void (*boundaryCondition( int cond ))( MssmSoftsusy &, const DoubleVector &) {
    void (*retval)(MssmSoftsusy &, const DoubleVector &);
    switch (cond) {
        case 0 :
            retval = &sugraBcs;
            break;
        case 1 :
            retval = &extendedSugraBcs;
            break;
        case 2 :
            retval = &generalBcs;
            break;
        case 3 :
            retval = &generalBcs2;
            break;
        case 4 :
            retval = &amsbBcs;
            break;
        case 5 :
            retval = &gmsbBcs;
            break;
        case 6 :
            retval = &splitGmsb;
            break;
        case 7 :
            retval = &lvsBcs;
            break;
        case 8 :
            retval = &nonUniGauginos;
            break;
        case 9 :
            retval = &userDefinedBcs;
            break;
        case 10 :
            retval = &nonUniGauginos;
            break;
        default : 
            std::cout << "Defaulting to sugra boundary conditions" << 
                std::endl;
            retval = &sugraBcs;
    }
    return retval;
}

extern "C" 
{
    /*--------------*/
    /* DoubleVector */
    /*--------------*/
    DoubleVector* DoubleVector_new( int sz ) {
        return new DoubleVector(sz);
    }
    double DoubleVector_display( DoubleVector* dv, int pos )  { 
        return dv->display(pos+1); 
    }
    void DoubleVector_set( DoubleVector* dv, int pos, double val )  { 
        (*dv)(pos+1) = val;
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

    void MssmSoftsusy_lowOrg( MssmSoftsusy* mss, int bCond, double mxGuess,
                              DoubleVector *pars, int sgnMu, double tanb,
                              QedQcd *oneset, bool gaugeUnification,
                              bool ewsbBCscale = false) {
        void (*bC)( MssmSoftsusy &, const DoubleVector &) = 
            boundaryCondition( bCond );
        mss->lowOrg(bC, mxGuess, *pars, sgnMu, tanb, *oneset, 
                    gaugeUnification, ewsbBCscale);
    }

    void MssmSoftsusy_lesHouchesAccordOutput( MssmSoftsusy* mss, const char model[], 
					  DoubleVector *pars, int sgnMu, double tanb, double qMax, 
					  int numPoints, double mgut, bool altEwsb ) {
        mss->lesHouchesAccordOutput( std::cout, model, *pars, sgnMu, tanb, qMax,
                                     numPoints, mgut, altEwsb );
    }
} 
