#! /usr/bin/env python

from ctypes import cdll, c_int, c_double, c_char_p, c_void_p
from ctypes import create_string_buffer

from modules.utils import show_header
from interfaces.slhaclass import SLHAfile

name = "SoftSUSY"
SPlib = cdll.LoadLibrary('packages/lib/libmcsoftsusy.so')
# set our return types
SPlib.DoubleVector_display.restype = c_double
boundaryConditions = [ 'sugraBcs', 'extendedSugraBcs', 'generalBcs',
        'generalBcs2', 'amsbBcs', 'gmsbBcs', 'splitGmsb', 'lvsBcs',
        'nonUniGauginos', 'userDefinedBcs', 'nonUniGauginos', ]

models = {
        'cMSSM': {
            'universals': ['m0', 'm12', 'A0'],
            'fixed_vars': ['tanb', 'sgnMu', 'mgut',],
            'boundary_condition': 'sugraBcs',
            'output': 'sugra',
            'other_vars': { # provide defaults
                'gaugeUnification': False,
                'ewsbBCscale': False,
                },
            }
        }

qed_qcd_funcs = {
        'mt': 'setPoleMt'
        }

output_opts = {
        'qMax': 91.1875,
        'numPoints': 1,
        'altEwsb': False,
        }

#SPSLHAlib = cdll.LoadLibrary('packages/lib/libmcsoftsusy_slha.so')

SLHA_MAX_SIZE = 10000

class DoubleVector(object) :
    def __init__(self, size = 0) :
        self._obj = SPlib.DoubleVector_new( size )
    def __getitem__( self, i ) :
        return SPlib.DoubleVector_display( c_void_p(self._obj), i )
    def __setitem__( self, index, value ) :
        SPlib.DoubleVector_set( c_void_p(self._obj), index, c_double(value) )

class MssmSoftsusy(object) :
    def __init__(self) :
        self._obj = SPlib.MssmSoftsusy_new()
    def lowOrg(self, model, mgut, dv_pars, sgnMu, tanb, qq_oneset,
            gaugeUnification, ewsbBCscale = False ) :
        mgut = c_double(mgut)
        tanb = c_double(tanb)
        bCond = models[model]['boundary_condition']
        bC = boundaryConditions.index(bCond)
        SPlib.MssmSoftsusy_lowOrg(c_void_p(self._obj), bC, mgut,
                c_void_p(dv_pars._obj), sgnMu, tanb, c_void_p(qq_oneset._obj),
                gaugeUnification, ewsbBCscale)
    def lesHouchesAccordOutput(self, model, dv_pars, sgnMu, tanb, qMax,
            numPoints, mgut, altEwsb) :
        tanb = c_double(tanb)
        qMax = c_double(qMax)
        mgut = c_double(mgut)
        model = c_char_p(models[model]['output'])
        SPlib.MssmSoftsusy_lesHouchesAccordOutput( c_void_p(self._obj), model,
                c_void_p(dv_pars._obj), sgnMu, tanb, qMax, numPoints, mgut,
                altEwsb )
    def lesHouchesAccordOutputStream( self, model, dv_pars, sgnMu, tanb, qMax,
            numPoints, mgut, altEwsb ):
        tanb = c_double(tanb)
        qMax = c_double(qMax)
        mgut = c_double(mgut)
        model = c_char_p(models[model]['output'])
        c_str_buf = create_string_buffer(SLHA_MAX_SIZE)
        sz = SPlib.MssmSoftsusy_lesHouchesAccordOutputStream(
                c_void_p(self._obj), model, c_void_p(dv_pars._obj), sgnMu,
                tanb, qMax, numPoints, mgut, altEwsb, c_str_buf, SLHA_MAX_SIZE)
        if sz >= SLHA_MAX_SIZE:
            print "*** WARNING: string access has been truncated in softsusy"
        return c_str_buf.value


class QedQcd(object) :
    def __init__(self) :
        self._obj = SPlib.QedQcd_new()
    def setPoleMt(self,  mt) :
        SPlib.QedQcd_setPoleMt( c_void_p(self._obj), c_double(mt) )
    def setPoleMb(self, mb) :
        SPlib.QedQcd_setPoleMb( c_void_p(self._obj), c_double(mb) )
    def setPoleMtau(self, mtau) :
        SPlib.QedQcd_setPoleMtau( c_void_p(self._obj), c_double(mtau) )
    def setMbMb(self, mb) :
        SPlib.QedQcd_setMbMb( c_void_p(self._obj), c_double(mb) )
    # these need enums equivalents...
    def setMass( self, mno, m) :
        mno = c_int(mno) #enum type
        SPlib.QedQcd_setMass( c_void_p(self._obj), mno, c_double(m) )
    def setAlpha( self, ai, ap) :
        ai = c_int(ai) #enum type
        SPlib.QedQcd_setAlpha( c_void_p(self._obj), ai, c_double(ap))
    def set( self, dv ) :
        SPlib.QedQcd_set( dv )


def run(model, **model_inputs):
    show_header(name, model)
    n_universals = len(models[model]['universals'])
    inputs = DoubleVector(n_universals)
    for pos, var_name in enumerate(models[model]['universals']):
        inputs[pos] = model_inputs[var_name]

    fixed = {}
    for var_name in models[model]['fixed_vars']:
        fixed.update({var_name: model_inputs[var_name]})

    r = MssmSoftsusy()

    oneset = QedQcd()
    for var, func_name in qed_qcd_funcs.iteritems():
        # for example
        #oneset.setPoleMt(mt)
        if var in model_inputs and var in models[model]:
            getattr(oneset,func_name)(model_inputs[var])

    low_args = fixed.copy()
    for var_name, value in models[model]['other_vars'].iteritems():
        low_args[var_name] =  model_inputs.get(var_name, value)

    r.lowOrg(model=model, dv_pars=inputs, qq_oneset=oneset, **low_args)

    output_args = fixed.copy()
    for var_name, value in output_opts.iteritems():
        output_args[var_name] = model_inputs.get(var_name, value)

    slhafile = r.lesHouchesAccordOutputStream(model=model, dv_pars=inputs,
            **output_args)

    return slhafile
