#! /usr/bin/env python

from ctypes import cdll, c_int, c_double, c_char_p, c_void_p
from ctypes import create_string_buffer

name = "SoftSUSY"
SPlib = cdll.LoadLibrary('packages/lib/libmcsoftsusy.so')

default_inputs={
    'alpha_em_inv'  : 1.27908953e2, #MC-old
    'G_Fermi'       : 1.16639e-5,   #MC-old
    'alpha_s'       : 1.187e-01,    #MC-old
    'MZ'            : 9.11876e1,    #MC-old
    'mt'            : 174.3,        #arbitrary, from web
    'mb'            : 4.2,          #MC-old
    'mtau'          : 1.77703,      #MC-old
        }


# set our return types
SPlib.DoubleVector_display.restype = c_double
boundaryConditions = [ 'sugraBcs', 'extendedSugraBcs', 'generalBcs',
        'generalBcs2', 'amsbBcs', 'gmsbBcs', 'splitGmsb', 'lvsBcs',
        'nonUniGauginos', 'userDefinedBcs', 'nonUniGauginos', ]

models = {
        'cMSSM': {
            'universals': [('m0',1), ('m12',2), ('A0',3)],
            'fixed_vars': ['tanb', 'sgnMu', 'mgut',],
            'boundary_condition': 'sugraBcs',
            'output': 'sugra',
            'other_vars': { # provide defaults
                'gaugeUnification':True  ,
                'ewsbBCscale': False,
                },
            'other_setup':  {
                'setMixing': [0],
                }
            },
        'pMSSM': {
            'universals': [('M_1', 1), ('M_2', 2), ('M_3', 3), ('At', 11),
                ('Ab', 12), ('Atau', 13), ('mu', 23),('mA', 26), ('meL', 31),
                ('mmuL', 32),('mtauL', 33),('meR', 34),('mmuR', 35),
                ('mtauR', 36), ('mqL1', 41), ('mqL2', 42), ('mqL3', 43),
                ('muR', 44), ('mcR', 45), ('mtR', 46), ('mdR', 47),
                ('msR', 48), ('mbR', 49)],
            'fixed_vars': ['tanb', 'sgnMu', 'mgut',],
            'boundary_condition': 'extendedSugraBcs',
            'output': 'nonUniversal',
            'other_vars': {
                'gaugeUnification': False,
                'ewsbBCscale': True,
                },
            'other_setup':  {
                #'setSetTbAtMX': [True],
                'setMixing': [0],
                }
            }
        }

#qed_qcd_funcs = {
#        'alpha_em_inv'  : 
#        'G_Fermi'       : 
#        'alpha_s'       : 
#        'MZ'            : 
#        'mt'            : 'setPoleMt',
#        'mb'            : 'setMbMb',
#        'mtau'          : 'setPoleMtau',
#        }

output_opts = {
        'cMSSM': {
            'qMax': 91.1875,
            'numPoints': 1,
            'ewsbBCscale': False,
            },
        'pMSSM':{
            'qMax': 0.0,
            'numPoints': 1,
            'ewsbBCscale': True ,
            }
        }

def setup_mu(r, mu):
    r.useAlternativeEwsb()
    r.setMuCond(mu)
    r.setSusyMu(mu)

def setup_ma(r, mA):
    r.useAlternativeEwsb()
    r.setMaCond(mA)

setup_functions = { # function( MssmSoftSusy, Value )
        'mA': setup_ma,
        'mu': setup_mu,
        }

def setup_SM_values(oneset,r,defaults,inputs):
    values=defaults.copy()
    if inputs is not None:
        values.update(inputs)
    #want to crash if one of the values is not there so just use values['...']
    #copy from softpoint.cpp lines
    num_dict={'ALPHA':1, 'ALPHAS':2,
            'mUp':1, 'mCharm':2, 'mTop':3, 'mDown':4, 'mStrange':5, 'mBottom':6, 'mElectron':7,
            'mMuon':8, 'mTau':9} 
    oneset.setAlpha(num_dict['ALPHA'], (1.0 /values['alpha_em_inv']  ) )
    oneset.setGMU(values['G_Fermi'] )
    oneset.setAlpha(num_dict['ALPHAS'], values['alpha_s'])
    oneset.setMu(values['MZ'])
    r.setData(oneset)
    oneset.setMZ(values['MZ']) 
    oneset.setMass(num_dict['mBottom'],values['mb'] ) 
    oneset.setMbMb(values['mb'])
    oneset.setPoleMt(values['mt'])
    oneset.setMass(num_dict['mTau'], values['mtau']) 
    oneset.setPoleMtau(values['mtau'])


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
    def useAlternativeEwsb(self):
        SPlib.MssmSoftSusy_useAlternativeEwsb(c_void_p(self._obj))
    def setSetTbAtMX(self,b_value):
        SPlib.MssmSoftSusy_setSetTbAtMX(c_void_p(self._obj),b_value)
    def setMuCond(self,value):
        value=c_double(value)
        SPlib.MssmSoftSusy_setMuCond(c_void_p(self._obj),value)
    def setSusyMu(self,value):
        value=c_double(value)
        SPlib.MssmSoftSusy_setSusyMu(c_void_p(self._obj),value)
    def setMaCond(self,value):
        value=c_double(value)
        SPlib.MssmSoftSusy_setMaCond(c_void_p(self._obj),value)
    def setData(self,oneset):
        SPlib.MssmSoftSusy_setData(c_void_p(self._obj),c_void_p(oneset._obj))
    def lowOrg(self, model, mgut, dv_pars, sgnMu, tanb, qq_oneset,
            gaugeUnification, ewsbBCscale = False ) :
        mgut = c_double(mgut)
        tanb = c_double(tanb)
        bCond = models[model]['boundary_condition']
        bC = boundaryConditions.index(bCond)
        return SPlib.MssmSoftsusy_lowOrg(c_void_p(self._obj), bC, mgut,
                c_void_p(dv_pars._obj), sgnMu, tanb, c_void_p(qq_oneset._obj),
                gaugeUnification, ewsbBCscale)
    def lesHouchesAccordOutput(self, model, dv_pars, sgnMu, tanb, qMax,
            numPoints, mgut, ewsbBCscale) :
        tanb = c_double(tanb)
        qMax = c_double(qMax)
        mgut = c_double(mgut)
        model = c_char_p(models[model]['output'].encode('ascii'))
        SPlib.MssmSoftsusy_lesHouchesAccordOutput( c_void_p(self._obj), model,
                c_void_p(dv_pars._obj), sgnMu, tanb, qMax, numPoints, mgut,
                ewsbBCscale )
    def lesHouchesAccordOutputStream( self, model, dv_pars, sgnMu, tanb, qMax,
            numPoints, mgut, ewsbBCscale ):
        tanb = c_double(tanb)
        qMax = c_double(qMax)
        mgut = c_double(mgut)
        model = c_char_p(models[model]['output'].encode('ascii'))
        c_str_buf = create_string_buffer(SLHA_MAX_SIZE)
        sz = SPlib.MssmSoftsusy_lesHouchesAccordOutputStream(
                c_void_p(self._obj), model, c_void_p(dv_pars._obj), sgnMu,
                tanb, qMax, numPoints, mgut, ewsbBCscale, c_str_buf,
                SLHA_MAX_SIZE)
        if sz >= SLHA_MAX_SIZE:
            print("*** WARNING: string access has been truncated in softsusy")
        return c_str_buf.value
    def setMixing(self, mixing):
        # this actually sets a global, but we dont like globals
        SPlib.set_global_MIXING(mixing)

class QedQcd(object) :
    def __init__(self) :
        self._obj = SPlib.QedQcd_new()
    def setMu(self,  mu) :
        SPlib.QedQcd_setMu( c_void_p(self._obj), c_double(mu) )
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
    def setGMU(self, gmu):
        # this actually sets a global, but we dont like globals
        SPlib.set_global_GMU(c_double(gmu))
    def setMZ(self, mz):
        # this actually sets a global, but we dont like globals
        SPlib.set_global_MZ(c_double(mz))


def run(model, **model_inputs):
    n_universals = max([pos for (_, pos) in models[model]['universals']])
    inputs = DoubleVector(n_universals)
    for (var_name, pos) in models[model]['universals']:
        inputs[pos] = model_inputs[var_name]

    fixed = {}
    for var_name in models[model]['fixed_vars']:
        fixed.update({var_name: model_inputs[var_name]})

    r = MssmSoftsusy()

    oneset = QedQcd()
#    if model_inputs.get('SMinputs'):
#    setup_SM_values(oneset,r,default_inputs,model_inputs['SMinputs'])
    setup_SM_values(oneset,r,default_inputs,None)
        
    #for var, func_name in qed_qcd_funcs.items():
    #    # for example
    #    #oneset.setPoleMt(mt)
    #    if var in model_inputs and var in models[model]:
    #        getattr(oneset,func_name)(model_inputs[var])

    low_args = fixed.copy()
    for var_name, value in models[model]['other_vars'].items():
        low_args[var_name] =  model_inputs.get(var_name, value)

    for var in model_inputs:
        if var in setup_functions:
            setup_functions[var](r, model_inputs[var])

    for func_name, args in models[model].get('other_setup',{}).items():
        getattr(r, func_name)(*args)

    fin_mgut = r.lowOrg(model=model, dv_pars=inputs, qq_oneset=oneset, **low_args)


    output_args = fixed.copy()
    #FIXME: this is not giving the correct mgut
    output_args['mgut']=fin_mgut
    for var_name, value in output_opts[model].items():
        output_args[var_name] = model_inputs.get(var_name, value)

    slhafile = r.lesHouchesAccordOutputStream(model=model, dv_pars=inputs,
            **output_args)
    return slhafile.decode('utf-8')
