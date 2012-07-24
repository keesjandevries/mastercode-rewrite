#! /usr/bin/env python

from ctypes import cdll, c_int, c_double, c_char_p

from modules import mcoutput
from interfaces.slha import SLHAfile

SPlib = cdll.LoadLibrary('./libs/libmcsoftsusy.so')
# set our return types
SPlib.DoubleVector_display.restype = c_double
boundaryConditions = [ "sugraBcs", "extendedSugaBcs", "generalBcs",
                       "generalBcs2", "amsbBcs", "gmsbBcs", "splitGmsb",
                       "lvsBcs", "nonUniGauginos", "userDefinedBcs",
                       "nonUniGauginos", ]

SPSLHAlib = cdll.LoadLibrary('./libs/libmcsoftsusyslha.so')

from interfaces.slha import SLHAfile

class DoubleVector(object) :
    def __init__(self, size = 0) :
        self.obj = SPlib.DoubleVector_new( size )
    def __getitem__( self, i ) :
        return SPlib.DoubleVector_display( self.obj, i )
    def __setitem__( self, index, value ) :
        SPlib.DoubleVector_set( self.obj, index, c_double(value) )

class MssmSoftsusy(object) :
    def __init__(self) :
        self.obj = SPlib.MssmSoftsusy_new()
    def lowOrg(self, bCond, mxGuess, dv_pars, sgnMu, tanb, qq_oneset,
            gaugeUnification, ewsbBCscale = False ) :
        mxGuess = c_double(mxGuess)
        tanb = c_double(tanb)
        bC = boundaryConditions.index( bCond )
        SPlib.MssmSoftsusy_lowOrg( self.obj, bC, mxGuess, dv_pars.obj, sgnMu,
                tanb, qq_oneset.obj, gaugeUnification, ewsbBCscale )
    def lesHouchesAccordOutput( self, model, dv_pars, sgnMu, tanb, qMax,
            numPoints, mgut, altEwsb ) :
        tanb = c_double(tanb)
        qMax = c_double(qMax)
        mgut = c_double(mgut)
        model = c_char_p( model )
        SPlib.MssmSoftsusy_lesHouchesAccordOutput( self.obj, model,
                dv_pars.obj, sgnMu, tanb, qMax, numPoints, mgut, altEwsb )
    def lesHouchesAccordOutputStream( self, model, dv_pars, sgnMu, tanb, qMax,
            numPoints, mgut, altEwsb, slhafile ) :
        tanb = c_double(tanb)
        qMax = c_double(qMax)
        mgut = c_double(mgut)
        model = c_char_p( model )
        SPSLHAlib.MssmSoftsusy_lesHouchesAccordOutputStream( self.obj, model,
                dv_pars.obj, sgnMu, tanb, qMax, numPoints, mgut, altEwsb,
                slhafile )


class QedQcd(object) :
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


def run (tanb, sgnMu, mgut, mt, boundary_condition, vars):
    mcoutput.header('softsusy')
    inputs = DoubleVector(len(vars))
    for pos in range(len(vars)):
        inputs[pos] = vars[pos]
    r = MssmSoftsusy()

    oneset = QedQcd()
    oneset.setPoleMt(mt)
    oneset.setMass(3,mt)

    r.lowOrg( boundary_condition, mgut, inputs, sgnMu, tanb, oneset, False )

    slhafile = SLHAfile()
    slhafile.ReadFile("")

    r.lesHouchesAccordOutputStream( "sugra", inputs, sgnMu, tanb, 91.1875,
            1, mgut, False, slhafile.obj )

    return slhafile
