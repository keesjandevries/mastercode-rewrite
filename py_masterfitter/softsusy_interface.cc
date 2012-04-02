//    Soft-SUSY front-end to be called by MasterCode
//    INPUT: SLHA file name (file containing SMInputs, MINPAR,...)
//       
//    OUTPUT: SLHA file (file is overwritten)
//
//    $Id: slha_interface.cc,v 1.1 2008/04/01 11:37:32 fronga Exp $

#include <iostream> 
#include <sstream>
#include <algorithm>

#include <softpoint.h>
#include <SLHAfile.hh>

/// global variable declaration 
/// no quark mixing (dominant third family approx), and no verbose output 
int MIXING = -1, PRINTOUT = 0; 
/// fractional accuracy required 
double TOLERANCE = 1.0e-3; 
/// decay constant of muon 
double GMU = 1.16637e-5; 
/// M_{SUSY}/root(mstop1 mstop2). The default value is 1 
double QEWSB = 1.0; 
/// Do we include 2-loop RGEs of *all* scalar masses and A-terms, or only the 
/// scalar mass Higgs parameters? (Other quantities all 2-loop anyway): the 
/// default in SOFTSUSY 2.x is to include all 2-loop terms 
bool INCLUDE_2_LOOP_SCALAR_CORRECTIONS = true; 
/// number of loops used to calculate Higgs mass and tadpoles. They should be 
/// identical for a consistent calculation 
int numHiggsMassLoops = 2, numRewsbLoops = 2; 
/// Number of scan points
int numPoints = 10;
/// global pole mass of MZ in GeV MZCENT is defined in def.h
double MZ = MZCENT;
/// ICs mSUGRA mode debay
bool MSUGRADBG = false;
/// To save slha files (pre post softsusy)
bool SAVESLHA = false;
/// end of global variable declaration 


// Returns a string with all characters in upper case: very handy
struct to_upper {
    int operator() ( int ch ) { return std::toupper( ch ); }
};
string ToUpper(const string & s) {
    string result(s);
    std::transform(result.begin(), result.end(), result.begin(), to_upper());
    return result;
}

void extendedSugraBcs2(MssmSoftsusy & m, 
        const DoubleVector & inputParameters) {
    int i;
    for (i=1; i<=3; i++) m.setGauginoMass(i, inputParameters.display(i));
    m.setTrilinearElement(UA, 1, 1, m.displayYukawaElement(YU, 1, 1) * 
            inputParameters.display(11));
    m.setTrilinearElement(UA, 2, 2, m.displayYukawaElement(YU, 2, 2) * 
            inputParameters.display(11));
    m.setTrilinearElement(UA, 3, 3, m.displayYukawaElement(YU, 3, 3) * 
            inputParameters.display(11));
    m.setTrilinearElement(DA, 1, 1, m.displayYukawaElement(YD, 1, 1) * 
            inputParameters.display(12));
    m.setTrilinearElement(DA, 2, 2, m.displayYukawaElement(YD, 2, 2) * 
            inputParameters.display(12));
    m.setTrilinearElement(DA, 3, 3, m.displayYukawaElement(YD, 3, 3) * 
            inputParameters.display(12));
    m.setTrilinearElement(EA, 1, 1, m.displayYukawaElement(YE, 1, 1) * 
            inputParameters.display(13));
    m.setTrilinearElement(EA, 2, 2, m.displayYukawaElement(YE, 2, 2) * 
            inputParameters.display(13));
    m.setTrilinearElement(EA, 3, 3, m.displayYukawaElement(YE, 3, 3) * 
            inputParameters.display(13));
    m.setSoftMassElement(mLl, 1, 1, sqr(inputParameters.display(31)));
    m.setSoftMassElement(mLl, 2, 2, sqr(inputParameters.display(32)));
    m.setSoftMassElement(mLl, 3, 3, sqr(inputParameters.display(33)));
    m.setSoftMassElement(mEr, 1, 1, sqr(inputParameters.display(34)));
    m.setSoftMassElement(mEr, 2, 2, sqr(inputParameters.display(35)));
    m.setSoftMassElement(mEr, 3, 3, sqr(inputParameters.display(36)));
    m.setSoftMassElement(mQl, 1, 1, sqr(inputParameters.display(41)));
    m.setSoftMassElement(mQl, 2, 2, sqr(inputParameters.display(42)));
    m.setSoftMassElement(mQl, 3, 3, sqr(inputParameters.display(43)));
    m.setSoftMassElement(mUr, 1, 1, sqr(inputParameters.display(44)));
    m.setSoftMassElement(mUr, 2, 2, sqr(inputParameters.display(45)));
    m.setSoftMassElement(mUr, 3, 3, sqr(inputParameters.display(46)));
    m.setSoftMassElement(mDr, 1, 1, sqr(inputParameters.display(47)));
    m.setSoftMassElement(mDr, 2, 2, sqr(inputParameters.display(48)));
    m.setSoftMassElement(mDr, 3, 3, sqr(inputParameters.display(49)));
}

bool softpoint_istream_api_( std::istream* inf, std::ostream* buf = NULL ) 
{ 

    using namespace std;

    //--- Copied from softpoint.cpp ---//
    void (*boundaryCondition)(MssmSoftsusy &, const DoubleVector &)=sugraBcs;
    char * modelIdent = "";
    DoubleVector pars(3); 

    double lambda = 0., aCkm = 0., rhobar = 0., etabar = 0.;

    bool flavourViolation = false;
    bool quarkFlavourViolation = false;
    bool leptonFlavourViolation = false;

    double mgutGuess = 2.0e16, tanb = 10., mbmb = MBOTTOM, mtau = MTAU;
    int sgnMu = 1;
    bool gaugeUnification = true, ewsbBCscale = false, altEwsb = false;
    QedQcd oneset;
    MssmSoftsusy m; MssmSoftsusyAltEwsb l; FlavourMssmSoftsusy k;
    MssmSoftsusy * r = &m; 
    RpvSoftsusy kw; bool RPVflag = false;

    string line, block;
    int model;

    numPoints = 1;
    double qMax = 0.;
    bool flag = false;

    bool error = false;

    try {
        int magicline = 0;
        while (getline(*inf,line)) {
            magicline++;
            istringstream input(line);
            string word1, word2;
            input >> word1;

            if (word1.find("#") == string::npos) { 
                // read in another word if there's no comment
                input >> word2; 

                if (ToUpper(word1) == "BLOCK")  { 
                    block = ToUpper(word2);

                } else { // ought to be data
                    istringstream kk(line);
                    if (block == "MODSEL") {
                        int i; kk >> i; 

                        switch(i) {
                            case 1: kk >> model; 
                                    switch(model) {
                                        case 0: boundaryCondition = &extendedSugraBcs;
                                                modelIdent = "nonUniversal"; r=&m;
                                                break;
                                        case 1: boundaryCondition = &sugraBcs; pars.setEnd(3); 
                                                modelIdent = "sugra"; r=&m; 
                                                break;
                                        case 2: boundaryCondition = &gmsbBcs; pars.setEnd(4); r=&m;
                                                modelIdent = "gmsb"; r=&m;
                                                break;
                                        case 3: boundaryCondition = &amsbBcs; pars.setEnd(2); r=&m; 
                                                modelIdent = "amsb"; r=&m;
                                                break;
                                        case 4: boundaryCondition = &realmsugraBcs;
                                                modelIdent = "rmsugra"; r=&m;
                                                QEWSB = 100.; // better convergence
                                                break;
                                        case 5: boundaryCondition = &realmsugraBcs;
                                                modelIdent = "vcmssm"; r=&m;
                                                QEWSB = 100.; // better convergence
                                                break;
                                        default: 
                                                ostringstream ii;
                                                ii << "SOFTSUSY" << SOFTSUSY_VERSION << " cannot yet do model " 
                                                    << model << ": terminal error\n";
                                                throw ii.str();
                                    }
                                    break;
                            case 4: kk >> i;
                                    switch ( i )
                                    {   case 0: RPVflag = false;
                                        break;
                                        case 1: RPVflag = true;
                                                break;
                                        default:
                                                ostringstream ii;
                                                ii << "MODSEL 4 choosing silly RPV switch \n"
                                                    << "(" << i << ") not a valid switch" << endl;
                                                throw ii.str();
                                    }
                                    break;
                            case 6: int j; kk >> j;
                                    switch ( j )
                                    {   case 0: flavourViolation = false;
                                        break;
                                        case 1: quarkFlavourViolation =true; r=&k;
                                                flavourViolation = true; k.numFV = 1;
                                                if (boundaryCondition != & amsbBcs) {
                                                    pars.setEnd(64); boundaryCondition = &flavourBcs2;
                                                }
                                                break;
                                        case 2: leptonFlavourViolation = true; r=&k;
                                                flavourViolation = true; k.numFV=2;
                                                if (boundaryCondition != & amsbBcs) {
                                                    pars.setEnd(64); boundaryCondition = &flavourBcs2;
                                                }
                                        case 3: quarkFlavourViolation = true; r=&k;
                                                leptonFlavourViolation = true; k.numFV = 3;
                                                flavourViolation = true;
                                                if (boundaryCondition != & amsbBcs) {
                                                    pars.setEnd(64); boundaryCondition = &flavourBcs2;
                                                }
                                                break;
                                        default:
                                                ostringstream ii;
                                                cout << "WARNING: MODEL 6 " << j
                                                    << " not recognised. Ignoring." << endl;
                                                break;
                                    }
                            case 11: kk >> numPoints;
                                     if (numPoints < 1) {
                                         ostringstream ii;
                                         ii << "MODEL 10 selecting silly number of points"
                                             << "(" << numPoints << ") to output" << endl;
                                         throw ii.str();
                                     }
                                     break;
                            case 12: double d; kk >> d;
                                     if (d < MZ) {
                                         ostringstream ii;
                                         ii << "MODSEL 12 selecting silly scale Qmax"
                                             << "(" << d << ") < MZ to output" << endl;
                                         throw ii.str();
                                     }
                                     qMax = d; break;
                            default:
                                     ostringstream ii;
                                     ii << "# WARNING: don't understand first integer " << word1 
                                         << " " << word2 << " in block " << block
                                         << ": ignoring it\n";
                                     throw ii.str();
                                     break;
                        }
                    }
                    else if (block == "MINPAR") {
                        int i; double d; kk >> i >> d; 
                        switch (i) {
                            case 3: tanb = d; break;
                            case 4: sgnMu = int(d); break;
                            default: 
                                    switch(model) {
                                        case 0:
                                            // SUGRA inputs to fill out the pheno MSSM case
                                            switch(i) {
                                                case 1: pars(1) = d; break;
                                                case 2: pars(2) = d; break;
                                                case 5: pars(3) = d; break;
                                                default: 
                                                        ostringstream ii;
                                                        ii << "Didn't understand pheno MSSM input " << i << endl;
                                                        break;
                                            }
                                            break;
                                        case 1:  //SUGRA inputs
                                            switch( i ) {
                                                case 1:
                                                    if (flavourViolation) {
                                                        double d2 = sqr(d);
                                                        pars(4) = d2; pars(7) = d2; pars(9) = d2;
                                                        pars(10) = d2; pars(13) = d2; pars(15) = d2;
                                                        pars(16) = d2; pars(19) = d2; pars(21) = d2;
                                                        pars(22) = d2; pars(25) = d2; pars(27) = d2;
                                                        pars(28) = d2; pars(31) = d2; pars(33) = d2;
                                                        pars(63) = d2; pars(64) = d2;
                                                    } else pars(1)=d;
                                                    break;
                                                case 2:
                                                    if (flavourViolation) {
                                                        pars(1) = d; pars(2) = d; pars(3) = d;
                                                    }
                                                    else pars(2) = d;
                                                    break;
                                                case 5:
                                                    if (flavourViolation) pars(62) = d;
                                                    else pars(3) = d;
                                                    break;
                                                default:
                                                    ostringstream ii;
                                                    ii << "Didn't understand SUGRA input " << i << endl;
                                                    break;
                                            }
                                            break;
                                        case 2: // GMSB inputs
                                            switch(i) {
                                                case 1: pars(3) = d; break;
                                                case 2: pars(2) = d; mgutGuess = d;
                                                        gaugeUnification = false; break;
                                                case 5: pars(1) = d; break;
                                                case 6: pars(4) = d; break;
                                                default: 
                                                        ostringstream ii;
                                                        ii << "Didn't understand GMSB input " << i << endl;
                                                        break;
                                            } break;
                                        case 3: // AMSB inputs
                                            switch(i) {
                                                case 1: pars(2) = d; break;
                                                case 2: pars(1) = d; break;
                                                default: 
                                                        ostringstream ii;
                                                        ii << "Didn't understand AMSB input " << i << endl;
                                                        break;
                                            } break;
                                        case 4:  //real mSugra inputs
                                            switch ( i ) {   
                                                case 1:
                                                    if (flavourViolation) {
                                                        double d2 = sqr(d);
                                                        pars(4) = d2; pars(7) = d2; pars(9) = d2;
                                                        pars(10) = d2; pars(13) = d2; pars(15) = d2;
                                                        pars(16) = d2; pars(19) = d2; pars(21) = d2;
                                                        pars(22) = d2; pars(25) = d2; pars(27) = d2;
                                                        pars(28) = d2; pars(31) = d2; pars(33) = d2;
                                                        pars(63) = d2; pars(64) = d2;
                                                    } else pars(1)=d;
                                                    break;
                                                case 2:
                                                    if ( flavourViolation ) {
                                                        pars(1) = d; pars(2) = d; pars(3) = d;
                                                    }
                                                    else pars(2) = d;
                                                    break;
                                                case 5:
                                                    if (flavourViolation) pars(62) = d;
                                                    else pars(3) = d;
                                                    break;
                                                default:
                                                    ostringstream ii;
                                                    ii << "Didn't understand rSUGRA input " << i << endl;
                                                    break;
                                            }
                                            break;
                                        case 5:  //real mSugra inputs
                                            switch ( i ) {   
                                                case 1:
                                                    if (flavourViolation) {
                                                        double d2 = sqr(d);
                                                        pars(4) = d2; pars(7) = d2; pars(9) = d2;
                                                        pars(10) = d2; pars(13) = d2; pars(15) = d2;
                                                        pars(16) = d2; pars(19) = d2; pars(21) = d2;
                                                        pars(22) = d2; pars(25) = d2; pars(27) = d2;
                                                        pars(28) = d2; pars(31) = d2; pars(33) = d2;
                                                        pars(63) = d2; pars(64) = d2;
                                                    } else pars(1)=d;
                                                    break;
                                                case 2:
                                                    if ( flavourViolation ) {
                                                        pars(1) = d; pars(2) = d; pars(3) = d;
                                                    }
                                                    else pars(2) = d;
                                                    break;
                                                case 5:
                                                    if (flavourViolation) pars(62) = d;
                                                    else pars(3) = d;
                                                    break;
                                                default:
                                                    ostringstream ii;
                                                    ii << "Didn't understand rSUGRA input " << i << endl;
                                                    break;
                                            }
                                            break;
                                        default: 
                                            ostringstream ii;
                                            ii << "Didn't understand model input " << model << endl;
                                            break;
                                    }
                                    break;
                        }
                    }
                    // Adding non-minimal options. However, mA and mu option is not
                    // yet supported. Also, we assume the initial model was mSUGRA
                    // (for now).
                    else if (block == "EXTPAR") {
                        if (modelIdent == "sugra" || modelIdent == "nonUniversal"||
                                modelIdent == "rmsugra" || modelIdent == "vcmssm") {
                            if (pars.displayEnd() != 49) { // initialise vector
                                modelIdent = "nonUniversal"; r=&m; 
                                boundaryCondition = &extendedSugraBcs;
                                double m0 = pars(1), m12 = pars(2), a0 = pars(3);
                                pars.setEnd(49);
                                int i; for (i=1; i<=3; i++) pars(i) = m12;
                                for (i=11; i<=13; i++) pars(i) = a0;
                                pars(21) = m0 * m0; pars(22) = m0 * m0;
                                for (i=31; i<=36; i++) pars(i) = m0;		    
                                for (i=41; i<=49; i++) pars(i) = m0;		    
                            }
                            int i; double d; kk >> i >> d;  
                            if ((i > 0 && i <=  3) || (i >= 11 && i <= 13) || 
                                    (i >= 21 && i <= 23) || (i == 26) 
                                    || (i >= 31 && i <= 36) || 
                                    (i >= 41 && i <= 49)) {
                                if (!flavourViolation) pars(i) = d;
                                else {
                                    if (i == 21) pars(63) = d;
                                    if (i == 22) pars(64) = d;
                                }
                            }
                            if (i == 0) { 
                                mgutGuess = d;
                                gaugeUnification = false;
                                // setting Minput=-1 should yield MSSM BCs at MSUSY
                                if ((d - 1.0) < EPSTOL) {
                                    mgutGuess = 1.0e3;
                                    ewsbBCscale = true;
                                    QEWSB = 1.0;
                                    if (gaugeUnification) 
                                        cout << "# Gauge unification ignored since pheno MSSM"
                                            << " assumes BC set at QEWSB\n"; 
                                    gaugeUnification = false;
                                }
                            }
                            if (i == 23 || i == 26) altEwsb = true; 
                            if (!((i >= -1 && i <=  3) || (i >= 11 && i <= 13) || 
                                        (i >= 21 && i <= 23) || (i == 26)
                                        || (i >= 31 && i <= 36) || 
                                        (i >= 41 && i <= 49)))		  
                                cout << "# Didn't understand extra parameter " << i 
                                    << " - ignoring it" << endl;
                        }
                        else cout << "# Can't yet handle extra parameters in " 
                            << modelIdent << ": ignoring them" << endl;
                    }

                    else if (block == "VCKMIN") {
                        int i; double d; kk >> i >> d;
                        switch ( i )
                        {   case 1: lambda = d; break;
                            case 2: aCkm = d; break;
                            case 3: rhobar = d; break;
                            case 4: etabar = d; break;
                            default:
                                    cout << "# WARNING: Don't understand data input " << i
                                        << " " << d << " in block "
                                        << block << ": ignoring it\n";
                                    break;
                        }
                    }

                    else if (block == "UMNSIN") {
                        int i; double d; kk >> i >> d;
                        switch ( i )
                        {   case 1: k.setThetaB12(asin(d)); break;
                            case 2: k.setThetaB23(asin(d)); break;
                            case 3: k.setThetaB13(asin(d)); break;
                            case 4: 
                                    cout << "# Cannot yet do complex phases: "
                                        << "setting it to zero" << endl;
                                    break;
                            case 5:
                                    cout << "# Cannot yet do complex phases: "
                                        << "setting it to zero" << endl;
                                    break;
                            case 6:
                                    cout << "#Cannot yet do complex phases: "
                                        << "setting it to zero" << endl;
                                    break;
                            default:
                                    cout << "# WARNING: Don't understand data input " << i
                                        << " " << d << " in block "
                                        << block << ": ignoring it\n";
                                    break;
                        }
                    }

                    else if (block == "SMINPUTS") {
                        int i; double d; kk >> i >> d; 
                        switch (i) {
                            case 1: oneset.setAlpha(ALPHA, 1.0 / d); break;
                            case 2: GMU = d; break;
                            case 3: oneset.setAlpha(ALPHAS, d); break; 
                            case 4: oneset.setMu(d); m.setData(oneset); MZ = d; break;
                            case 5: oneset.setMass(mBottom, d); mbmb = d; flag = true; 
                                    break;
                            case 6: oneset.setPoleMt(d); break;
                            case 7: oneset.setMass(mTau, d); mtau = d; break;
                            case 8: k.setMnuTau(d); break;
                            case 11: oneset.setMass(mElectron, d); break;
                            case 12: k.setMnuMu(d); break;
                            case 13: oneset.setMass(mMuon, d); break;
                            case 14: k.setMnuTau(d); break;
                            case 21: oneset.setMass(mDown, d); break;
                            case 22: oneset.setMass(mUp, d); break;
                            case 23: oneset.setMass(mStrange, d); break;
                            case 24: oneset.setMass(mCharm, d); break;
                            default: 
                                     ostringstream ii;
                                     ii << "# WARNING: Don't understand data input " << i 
                                         << " " << d << " in block "
                                         << block << ": ignoring it\n"; break;
                                     throw ii.str();
                        }
                    }

                    else if (block == "SOFTSUSY") {
                        int i; double d; kk >> i >> d;
                        switch(i) {
                            case 1: TOLERANCE = d; break;
                            case 2: 
                                    MIXING = int(d);
                                    if (MIXING > 0) flavourViolation = true;
                                    break;
                            case 3: PRINTOUT = int(d); break;
                            case 4: QEWSB = d; break;
                            case 5: INCLUDE_2_LOOP_SCALAR_CORRECTIONS = bool(int(d+EPSTOL)); 
                                    break;  
                            default:
                                    ostringstream ii;
                                    ii << "# WARNING: Don't understand data input " << i 
                                        << " " << d << " in block "
                                        << block << ": ignoring it\n"; break;
                                    throw ii.str();
                        }
                    }

                    else {
                        ostringstream ii;
                        ii << "# WARNING: don't recognise block " << block 
                            << ": ignoring all data in it" << endl;
                        throw ii.str();
                    }
                    // end if blocks

                } // end of data
            } // end of no-comment

        } // end of file

        if (flavourViolation) k.setAngles(lambda, aCkm, rhobar, etabar);

        if (altEwsb) {
            boundaryCondition = &extendedSugraBcs2;
            l.setAltEwsb(pars(26), pars(23));
            l.setSusyMu(pars(23));
            sgnMu = 0; // Flags different BCs
            r = &l; 
        }

        if (RPVflag) {
            if (boundaryCondition == &sugraBcs) {
                boundaryCondition = &rpvSugraBcs;
            }
            else if (boundaryCondition == &amsbBcs) {
                boundaryCondition = &rpvAmsbBcs;
            }
            else if (boundaryCondition == &gmsbBcs) {
                boundaryCondition = &rpvGmsbBcs;
            }
            else {
                cout << "# WARNING: there is no RPV version for selected "
                    << "boundary condition!" << endl;
            }
            kw.rpvDisplay(pars);
            r=&kw;
        }
        // input error checking  
        if (sgnMu != 1 && sgnMu != -1 && sgnMu != 0) {
            ostringstream ii;
            ii << "Incorrect input for sign(mu)=" << sgnMu <<endl;
            error = true;
            throw ii.str();
        }

        QedQcd twoset(oneset); //save a copy of input parameters

        if (flag) oneset.calcPoleMb();
        oneset.toMz();

        double mgut;

        mgut = r->lowOrg(boundaryCondition, mgutGuess, pars, sgnMu,
                tanb, oneset, gaugeUnification, ewsbBCscale);
        if( !buf ) {
            fstream fout("ss.out", ios::out);
            fout.setf(ios::scientific, ios::floatfield);
            fout.precision(9);
            r->lesHouchesAccordOutput(fout,modelIdent,pars,sgnMu,tanb,qMax,numPoints,
                    mgut,twoset,altEwsb);
        }
        else {
            r->lesHouchesAccordOutput(*buf,modelIdent,pars,sgnMu,tanb,qMax,numPoints,
                    mgut,twoset,altEwsb);
        }
    }

    catch(const string & a) {
        cout << a;
    }

    // Check if problem
    if (r->displayProblem().test())
    {
        cout << "# SOFTSUSY problem with point: " << r->displayProblem() << endl;
    }
    if (r->displayProblem().testSeriousProblem()) error = true;
}

extern "C" 
{
    void softpoint_slhafile_api_( SLHAfile* sf )
    {
        std::stringstream ss( std::stringstream::in | std::stringstream::out );        
        // read the file SLHAfile in ss
        sf->streamer(ss);
        // create input stream for the file
        std::istream is( ss.rdbuf() );
        std::stringstream ss_out( std::stringstream::in | std::stringstream::out );
        softpoint_istream_api_( &is, &ss_out );
        std::istream iss( ss_out.rdbuf() );
        iss >> (*sf);
    }
} 
