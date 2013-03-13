from collections import OrderedDict

import tools

# slha represntation
from ObsCalculator.interfaces import slhalib as slhamodule
from ObsCalculator.interfaces.slhalib import SLHA

# spectrum calculator
from ObsCalculator.interfaces import softsusy
from ObsCalculator.interfaces import feynhiggs, micromegas, superiso, bphysics, lspscat
from ObsCalculator.interfaces import susypope

default_spectrum_generator = softsusy
default_spectrum_modifiers = [feynhiggs]
default_predictors = default_spectrum_modifiers + [micromegas, superiso, bphysics, lspscat,#]
            susypope]


#FIXME: model should not be a neseccarry input, since also able to run on slha
def run_point(model, **input_pars):
    """
    run_point is the core function of MC++
    documentation is needed soon, however, in this file you will find extensive commenting already
    """
    #==================
    # define predictors
    #==================
    spectrum_generator  =default_spectrum_generator
    spectrum_modifiers  =default_spectrum_modifiers
    predictors          =default_predictors

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
        input_pars['verbose'].append(spectrum_generator.name)
        input_pars['verbose'].append('spectrum')

    if input_pars.get('spectrumfile'):
        #=============================================================
        # if an slhafile is given, the spectrum generation is skipped
        # the slhafile also does not get modified
        #=============================================================
        spectrum_modifiers=[]
        slhafile = SLHA()
        slhafile.read(input_pars['spectrumfile'])
        if 'spectrum' in input_pars['verbose']:
            print("NOTE: Running on spectrum file {0}.".format(input_pars['spectrumfile'])) 
            print('      Spectrum is not modified.')
    else:
        # ======================
        # run spectrum generator
        # ======================

        # check for verbosity
        slha_gen_verbose=spectrum_generator.name in input_pars['verbose']
        # run the spectrum calculator
        (obj,err), stdout = tools.get_ctypes_streams(func=spectrum_generator.run,
                args=[model,input_pars[spectrum_generator.name]], kwargs={'verbose':slha_gen_verbose})
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
        if 'spectrum' in input_pars['verbose']:
            print(obj)

        # make slha object 
        slhafile = SLHA(obj,input_pars.get('lookup'))

        
    # ======================
    # predictions start here
    # ======================
    predictor_output = OrderedDict()

    # =============================================================
    # save inputs to spectrum calculater like ('MINPAR','in_M0')
    # Motivation: in NUHM1 and NUHM2, m0, m12 and A0 are translated
    # into EXTPAR parameters. We need this for consistent naming
    # for e.g. constraints
    # =============================================================
    in_dict={}
    for key, val in input_pars[spectrum_generator.name].items():
        in_key =(key[0],'in_{0}'.format(key[1]))
        in_dict[in_key]=val
    predictor_output.update(in_dict)

    # ======================================
    # save spectrum before any modifications
    # ======================================
    predictor_output.update(slhafile.process())

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
            #explicitely save these in predictor_output as modified slha values
            mod_key=(oid[0],'mod_{}'.format(oid[1]))
            predictor_output[mod_key]=val


    # ===========================================
    # run predictors on slha file and save output
    # ===========================================
    for predictor in predictors:
        is_modifier = predictor in spectrum_modifiers
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

    
    
    # =====================================================
    # save the modified slha obs as e.g. ('MASS','mod_mh0')
    # =====================================================
    mod_slha_obs=slhafile.process()
    for key, val in mod_slha_obs.items():
        if not predictor_output.get(key)==val:
            mod_key=(key[0],'mod_{}'.format(key[1]))
            predictor_output[mod_key]=val
    return slhafile, predictor_output, stdouts
