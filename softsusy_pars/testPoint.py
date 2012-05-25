from softsusy import (DoubleVector, MssmSoftsusy, QedQcd)

#! /usr/bin/env python
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
