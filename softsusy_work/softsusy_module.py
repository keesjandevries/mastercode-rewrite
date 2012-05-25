#! /usr/bin/env python

from ctypes import cdll, c_int, c_double

SPlib = cdll.LoadLibrary('./libmcsoftsusy.so')
# set our return types
SPlib.DoubleVector_display.restype = c_double

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

# test the DV
test = ss_DoubleVector(3)
print test[1]
test[1] = 5
print test[1]

# test the MSs obj
test_mm = ss_MssmSoftsusy()
test_qq = ss_QedQcd()
test_qq.setPoleMt(173.2)
test_qq.setMass(3,173.2)
