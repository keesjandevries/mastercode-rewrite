#! /usr/bin/env python

from ctypes import cdll, c_int, c_double, c_char_p

SPlib = cdll.LoadLibrary('./libmcsoftsusy.so')
# set our return types
SPlib.DoubleVector_display.restype = c_double
boundaryConditions = [ "sugraBcs", "extendedSugaBcs", "extendedSugraBcs2",
                       "generalBcs", "generalBcs2", "amsbBcs", "gmsbBcs",
                       "splitGmsb", "lvsBcs", "nonUniGauginos", 
                       "userDefinedBcs", "nonUniGauginos", ]

class ss_DoubleVector(object) :
    def __init__(self, size = 0) :
        self.obj = SPlib.DoubleVector_new( size )
    def __getitem__( self, i ) :
        return SPlib.DoubleVector_display( self.obj, i )
    def __setitem__( self, index, value ) :
        SPlib.DoubleVector_set( self.obj, index, c_double(value) )
 
class ss_MssmSoftsusy(object) :
    def __init__(self) :
        self.obj = SPlib.MssmSoftsusy_new()
    def lowOrg(self, bCond, mxGuess, dv_pars, sgnMu, tanb, qq_oneset,
               gaugeUnification, ewsbBCscale = False ) :
        mxGuess = c_double(mxGuess)
        tanb = c_double(tanb)
        bC = boundaryConditions.index( bCond )
        SPlib.MssmSoftsusy_lowOrg( self.obj, bC, mxGuess, dv_pars.obj, sgnMu,
                                   tanb, qq_oneset.obj, gaugeUnification,
                                   ewsbBCscale )
    def lesHouchesAccordOutput( self, model, dv_pars, sgnMu, tanb, qMax, 
                                numPoints, mgut, altEwsb ) :
        tanb = c_double(tanb)
        qMax = c_double(qMax)
        mgut = c_double(mgut)
        model = c_char_p( model )
        SPlib.MssmSoftsusy_lesHouchesAccordOutput( self.obj, model, dv_pars.obj,
                                                   sgnMu, tanb, qMax, numPoints,
                                                   mgut, altEwsb )

class ss_QedQcd(object) :
    def __init__(self) :
        self.obj = SPlib.QedQcd_new()
    def setPoleMt(self,  mt) :
        SPlib.QedQcd_setPoleMt( self.obj, c_double(mt) )
    def setPoleMb(self, mb) :
        SPlib.QedQcd_setPoleMb( self.obj, c_double(mb) )
    def setPoleMtau(self, mtau) :
        SPlib.QedQcd_setPoleMtau( self.obj, c_double(mtau) )
    def setMbMb(self, mb) :
        SPlib.QedQcd_setMbMb( self.obj, c_double(mb) )
    # these need enums equivalents...
    def setMass( self, mno, m) :
        mno = c_int(mno) #enum type
        SPlib.QedQcd_setMass( self.obj, mno, c_double(m) )
    def setAlpha( self, ai, ap) :
        ai = c_int(ai) #enum type
        SPlib.QedQcd_setAlpha( self.obj, ai, c_double(ap))
    def set( self, dv ) :
        SPlib.QedQcd_set( dv )
