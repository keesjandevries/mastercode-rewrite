from interfaces.softsusy import (DoubleVector, MssmSoftsusy, QedQcd)
from interfaces.slha import SLHAfile

#! /usr/bin/env python
def testPoint() :
    # DoubleVector
    inputs = DoubleVector(3)
    inputs[0] = 100.
    inputs[1] = 200.
    inputs[2] = 0.
    tanb = 10.
    sgnMu = 1
    mgut = 2e16

    # setup MssmSoftusy object
    r = MssmSoftsusy()

    # QedQcd object
    oneset = QedQcd()
    oneset.setPoleMt(173.2)
    oneset.setMass(3,173.2)
    r.lowOrg( "sugraBcs", mgut, inputs, sgnMu, tanb, oneset, False )
    r.lesHouchesAccordOutput( "sugra", inputs, sgnMu, tanb, 91.1875,  1, mgut, False )

    slhafile = SLHAfile()
    slhafile.ReadFile("")
#    r.lesHouchesAccordOutputStream( "sugra", inputs, sgnMu, tanb, 91.1875,  1, mgut, False, slhafile.obj ) # still doesn't work
    #print slhafile
 
if __name__=="__main__" :
    testPoint()