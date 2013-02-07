from collections import OrderedDict

import tools

# slha represntation
from ObsCalculator.interfaces import slhalib as slhamodule
from ObsCalculator.interfaces.slhalib import SLHA

# spectrum calculator
from ObsCalculator.interfaces import softsusy
from ObsCalculator.interfaces import feynhiggs, micromegas, superiso, bphysics, lspscat
from ObsCalculator.interfaces import susypope

slha_generator = softsusy
slha_modifiers = [feynhiggs]
predictors = slha_modifiers + [micromegas, superiso, bphysics, lspscat,#]
        susypope]


def run_point(model, **input_pars):
    stdouts = OrderedDict()

    # spectrum generation
    (obj,err), stdout = tools.get_ctypes_streams(func=slha_generator.run,
            args=[model], kwargs=input_pars[slha_generator.name])
    # verbosity can be set as an input, useful for debugging
    if input_pars.get('verbose'):
        #FIXME: maybe specify verbose like 'verbose':['spectrum_calculator','feynhiggs',..] 
        print("slhafile:")
        print(obj)
        print("stdout:")
        print(stdout)
        if err: print("ERROR: spectrum calculator")
    
    # If the spectrum calculater fails then there is no hope to calculate anything else.
    # Hence, return None is appropriate
    if(err): return None

    stdouts.update({slhamodule.name: stdout})
    slhafile = SLHA(obj,input_pars.get('lookup'))

    # "Manually" setting MW and MZ in the slha file object
    # if 'mc_slha_update' is in input_vars
    # this hack should not escape from this file
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


    # send slha file to predictors
    predictor_output = OrderedDict()
    for predictor in predictors:
        is_modifier = predictor in slha_modifiers
        #FIXME: the other predictors don't have error handling yet
        result, stdout = tools.get_ctypes_streams(
                func=slhamodule.send_to_predictor,
                args=[slhafile,input_pars.get(predictor.name),predictor, is_modifier])
        if input_pars.get('verbose'):  print(stdout)
        predictor_output.update(result)
        stdouts.update({predictor.name: stdout})


    return slhafile, predictor_output , stdouts
