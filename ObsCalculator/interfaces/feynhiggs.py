#! /usr/bin/env python

from ctypes import cdll, c_int, c_double, byref, Structure

from tools import ctypes_field_values
from tools import set_obj_inputs_and_defaults

from ObsCalculator.interfaces.slhalib import  invalid

name = "FeynHiggs"
default_version='2.9.5'
versions={
    '2.8.6': 'packages/lib/libmcfeynhiggs2.8.6.so',
    '2.8.7': 'packages/lib/libmcfeynhiggs2.8.7.so',
    '2.9.5': 'packages/lib/libmcfeynhiggs2.9.5.so',
    '2.9.5.r3456': 'packages/lib/libmcfeynhiggs2.9.5.r3456.so',
    '2.9.5.r3456v2': 'packages/lib/libmcfeynhiggs2.9.5.r3456v2.so',
    '2.9.5.r3456v3': 'packages/lib/libmcfeynhiggs2.9.5.r3456v3.so',
}

#want to be able to use various libraries without everything in need of compiling
FHlibs={}
for version, lib in versions.items():
#    try:
    FHlibs[version]=cdll.LoadLibrary(lib)
#    except OSError:
#        print('WARNING: could not find FeynHiggs library: \"{}\"'.format(lib))

nslhadata ={version: lib.get_nslhadata() for version,lib in FHlibs.items()}

default_inputs={
    'mssmpart'      :4, 
    'fieldren'      :0, 
    'tanbren'       :0, 
    'higgsmix'      :2,
    'p2approx'      :0, 
    'looplevel'     :2, 
    'tl_running_mt' :1, 
    'tl_bot_resum'  :1,
        }

class FeynHiggsOpts(Structure):
    _fields_ = [('mssmpart', c_int), ('fieldren', c_int), ('tanbren', c_int),
            ('higgsmix', c_int), ('p2approx', c_int), ('looplevel', c_int),
            ('tl_running_mt', c_int), ('tl_bot_resum', c_int)]
    def __init__(self,  defaults, inputs={}):
        set_obj_inputs_and_defaults(self,inputs,defaults)

class FeynHiggsPrecObs(Structure):
    _fields_ = [('gm2', c_double), ('DeltaRho', c_double),
            ('MWMSSM', c_double), ('MWSM', c_double), ('SW2effMSSM', c_double),
            ('SW2effSM', c_double), ('EDMeTh', c_double), ('EDMn', c_double),
            ('EDMHg', c_double), 
            ('mh', c_double), ('mH', c_double), ('mA', c_double), ('mHpm', c_double),
            ('Dmh', c_double), ('DmH', c_double), ('DmA', c_double), ('DmHpm', c_double)
            ]

# For NUHM1 and NUHM2, BLOCK EXTPAR had to be ignored by FeynHiggs
# Previously, this was accomplished with a hack in FeynHiggs-2.8.7/src/SLHA/SLHARead.F
# but we now parse the slhadata directly, so we have to set these to "invalid"
def drop_extpar(slhafile):
    oids=[oid for oid in slhafile.get_lookup().keys() if isinstance(oid,tuple)]
    extpars=([oid for oid in oids if oid[0]=='EXTPAR'])
    recovery={}
    for extpar in extpars:
        recovery[extpar]=slhafile[extpar]
        slhafile[extpar]=invalid
    return slhafile, recovery

def run(slhafile, inputs=None, update=False) :
    print(inputs)
    if inputs is None:
        inputs={}
    fhopts = FeynHiggsOpts(default_inputs,inputs)
    recovery={}
    if inputs:
        if inputs.get('drop_extpar'):
            slhafile, recovery=drop_extpar(slhafile)
    if inputs.get('versions') is not None:
        return_value={}
        for version in inputs['versions']:
            FHout = FeynHiggsPrecObs()
            assert len(slhafile) == nslhadata[version]
            error = FHlibs[version].run_feynhiggs(byref(FHout), byref(fhopts), byref(slhafile.data),
                    update)
            return_value.update(ctypes_field_values(FHout, name+version, error))
    #130806 KJ NOTE: in case of no 'versions' specified, the outputs will look like e.g. ('FeynHigs','mh' )
    #instead of ('FeynHiggs2.8.7','mh'), for downward compatiblility. This may change in the future
    else:
        FHout = FeynHiggsPrecObs()
        assert len(slhafile) == nslhadata[default_version]
        error = FHlibs[default_version].run_feynhiggs(byref(FHout), byref(fhopts), byref(slhafile.data),
                update)
        return_value=ctypes_field_values(FHout, name, error)
    #If (!) extpar is dropped for running FH it has to be put back
    for key, value in recovery.items():
        slhafile[key]=value
#    if error: print("ERROR: FH")
    return return_value
