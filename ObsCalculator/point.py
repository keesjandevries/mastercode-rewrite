from collections import OrderedDict

import tools

# slha represntation
from ObsCalculator.interfaces import slhalib as slhamodule
from ObsCalculator.interfaces.slhalib import SLHA


#FIXME: want to separate input parameters (like m0, m12, Delta_Alpha_had, ... ) from options (like verbose)
def run_point( **input_pars):
    """
    run_point is the core function of MC++
    documentation is needed soon, however, there is extensive commenting already
    """
    #==================
    # define predictors
    #==================
    spectrum_generator=input_pars['spectrum_generator']
    spectrum_modifiers=input_pars['spectrum_modifiers']
    predictors=input_pars['predictors']
    #=====================================
    # define directory for temporary files
    #=====================================
    if 'tmp_dir' in input_pars:
        tmp_dir_input={'tmp_dir':input_pars['tmp_dir']}
        for predictor in [spectrum_generator] + predictors:
            try:
                input_pars[predictor.name].update(tmp_dir_input)
            except:
                input_pars[predictor.name]=tmp_dir_input

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
        input_pars['verbose'].append(slhamodule.name)
        input_pars['verbose'].append('spectrum')
        input_pars['verbose'].append('mcspectrum')
        input_pars['verbose'].append('predspectrum')

    if input_pars.get('spectrumfile'):
        #=============================================================
        # if an slhafile is given, the spectrum generation is skipped
        # the slhafile also does not get modified
        #=============================================================
        spectrum_modifiers=[]
        slhafile = SLHA(input_pars.get('tmp_dir'))
        # make slha object 
        none_return,stdout = tools.get_ctypes_streams(func=slhafile.read,args=[input_pars['spectrumfile']],kwargs={})
        # handle standard outs
        if slhamodule.name in input_pars['verbose']:
            print(stdout)
        stdouts.update({slhamodule.name:stdout})
        # handle spectrum verbosity
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
                args=[input_pars[spectrum_generator.name]], kwargs={'verbose':slha_gen_verbose})
        # print standard out 
        if slha_gen_verbose:
            print(stdout)
        #error handling for slha generator    
        if err: print("ERROR: spectrum calculator")
        
        # If the spectrum calculater fails then there is no hope to calculate anything else.
        # Hence, return None is appropriate
        if(err): return None,None,None

        stdouts.update({slhamodule.name: stdout})

        # if you want to see the slha file from the specturm generator, put 'verbose' in the 
        if 'spectrum' in input_pars['verbose']:
            print(obj)

        # make slha object 
        slhafile,stdout = tools.get_ctypes_streams(func=SLHA,args=[obj,input_pars.get('lookup'),input_pars.get('tmp_dir')],kwargs={})
#        slhafile=SLHA(obj,input_pars.get('lookup'),input_pars.get('tmp_dir'))
        # handle standard outs
        if slhamodule.name in input_pars['verbose']:
            print(stdout)
        stdouts.update({slhamodule.name:stdout})
        
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
    if not 'spectrumfile' in input_pars:
        for key, val in input_pars[spectrum_generator.name].items():
            if not (key=='model'):
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
    # "Manually" setting values in the slha file object
    # if 'mc_slha_update' is in input_vars
    # someone may define 'mc_slha_update : True', 
    # or provide a dictionary 'mc_slha_update':{ ('MASS','MZ') : ... }
    # this hack should not escape from this file
    # =====================================================
    if input_pars.get('mc_slha_update'):
        # by default, use set MW=80.4
        values={('MASS','MW') : 80.4}
        try:
            values.update( input_pars['mc_slha_update'])
        except TypeError:
            pass
        for oid, val in values.items():
            slhafile[oid]=val
            #explicitely save these in predictor_output as modified slha values
            mod_key=(oid[0],'mod_{}'.format(oid[1]))
            predictor_output[mod_key]=val
        if 'mcspectrum' in input_pars['verbose']: 
            print(slhafile)

    # ===========================================
    # run predictors on slha file and save output
    # ===========================================
    for predictor in predictors:
        is_modifier = predictor in spectrum_modifiers
        pred_verbose=(predictor.name in input_pars['verbose'])
        if pred_verbose: 
            verbose_true={'verbose': True }
            if input_pars.get(predictor.name):
                input_pars[predictor.name].update(verbose_true)
            else:
                input_pars[predictor.name]=verbose_true
        result, stdout = tools.get_ctypes_streams(
                func=slhamodule.send_to_predictor,
                args=[slhafile,input_pars.get(predictor.name),predictor, is_modifier])
        if pred_verbose:  print(stdout)
        predictor_output.update(result)
        stdouts.update({predictor.name: stdout})

    
    if 'predspectrum' in input_pars['verbose']: 
        print(slhafile)
    # =====================================================
    # save the modified slha obs as e.g. ('MASS','mod_mh0')
    # =====================================================
    mod_slha_obs=slhafile.process()
    for key, val in mod_slha_obs.items():
        if not predictor_output.get(key)==val:
            mod_key=(key[0],'mod_{}'.format(key[1]))
            predictor_output[mod_key]=val

    return slhafile, predictor_output, stdouts
