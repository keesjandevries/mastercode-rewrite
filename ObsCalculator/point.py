from collections import OrderedDict

import tools

# slha represntation
from ObsCalculator.interfaces import slhalib as slhamodule
from ObsCalculator.interfaces.slhalib import SLHA

# spectrum calculator
from ObsCalculator.interfaces import softsusy
from ObsCalculator.interfaces import feynhiggs, micromegas, superiso, bphysics, lspscat
from ObsCalculator.interfaces import susypope

default_slha_generator = softsusy
default_slha_modifiers = [feynhiggs]
default_predictors = default_slha_modifiers + [micromegas, superiso, bphysics, lspscat,#]
            susypope]


def run_point(model, **input_pars):
    #==================================
    # define predictors
    #==================================
    slha_generator  =default_slha_generator
    slha_modifiers  =default_slha_modifiers
    predictors      =default_predictors

    #define standard outs dict
    stdouts = OrderedDict()
    
    #==============================================================
    # handle verbosity like this 'verbose': ['softsusy', 'FH', ...]
    # verbosity helps with debugging
    #==============================================================
    if not input_pars.get('verbose'): input_pars['verbose']=[]
    #make an option to select all verbosity
    if 'all' in input_pars['verbose']:
        input_pars['verbose']=[pred.name for pred in predictors]
        input_pars['verbose'].append(slha_generator.name)
        input_pars['verbose'].append('slha')

    if input_pars.get('spectrumfile'):
        #=============================================================
        # if an slhafile is given, the spectrum generation is skipped
        # the slhafile also does not get modified
        #=============================================================
        slha_modifiers=[]
        slhafile = SLHA()
        slhafile.read(input_pars['spectrumfile'])
        print("NOTE: Running on spectrum file {0}.".format(input_pars['spectrumfile'])) 
        print('      Spectrum is not modified.')
    else:
        # ======================
        # run spectrum generator
        # ======================

        # check for verbosity
        slha_gen_verbose=slha_generator.name in input_pars['verbose']
        # run the spectrum calculator
        (obj,err), stdout = tools.get_ctypes_streams(func=slha_generator.run,
                args=[model,input_pars[slha_generator.name]], kwargs={'verbose':slha_gen_verbose})
        # print standard out 
        if slha_gen_verbose:
            print(stdout)
        #error handling for slha generator    
        if err: print("ERROR: spectrum calculator")
        
        # If the spectrum calculater fails then there is no hope to calculate anything else.
        # Hence, return None is appropriate
        if(err): return None

        stdouts.update({slhamodule.name: stdout})

        # if you want to see the slha file from the specturm generator, put 'verbose' in the 
        if 'slha' in input_pars['verbose']:
            print(obj)

        # make slha object 
        slhafile = SLHA(obj,input_pars.get('lookup'))

    # =====================================================
    # WARNING: here is a functionality needed by mastercode
    #          it is not generic
    # "Manually" setting MW and MZ in the slha file object
    # if 'mc_slha_update' is in input_vars
    # this hack should not escape from this file
    # =====================================================
    if input_pars.get('mc_slha_update'):
        # by default, use these values
        values={('MASS','MW') : 80.4,('SMINPUTS','MZ') : 91.1875}
        # someone may define 'mc_slha_updata : True'
        try:
            values.update([(oid,val ) for oid,val in input_pars['mc_slha_update'].items() if oid in values.keys()])
        except AttributeError:
            pass
        for oid, val in values.items():
            slhafile[oid]=val

    # predictions start here
    predictor_output = OrderedDict()
    # FIXME: this should be done less arbitrarily: Save softsusy-Higgs sector
    predictor_output[(softsusy.name,'Mh0')]=slhafile[('MASS', 'Mh0')]
    predictor_output[(softsusy.name,'MHH')]=slhafile[('MASS', 'MHH')]
    predictor_output[(softsusy.name,'MA0')]=slhafile[('MASS', 'MA0')]
    predictor_output[(softsusy.name,'MHp')]=slhafile[('MASS', 'MHp')]

    # ===========================
    # run predictors on slha file
    # ===========================
    for predictor in predictors:
        is_modifier = predictor in slha_modifiers
        #FIXME: needs to get something like: pred_verbose=  predictor.name in input_pars['verbose']
        # and pred_verbose as one of tdhe options, 
        pred_verbose=(predictor.name in input_pars['verbose'])
        result, stdout = tools.get_ctypes_streams(
                func=slhamodule.send_to_predictor,
                args=[slhafile,input_pars.get(predictor.name),predictor, is_modifier])
        #FIXME: if pred_verbose: print
        if pred_verbose:  print(stdout)
        predictor_output.update(result)
        stdouts.update({predictor.name: stdout})


    return slhafile, predictor_output , stdouts
