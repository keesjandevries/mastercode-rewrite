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
    obj, stdout = tools.get_ctypes_streams(func=slha_generator.run,
            args=[model], kwargs=input_pars[slha_generator.name])

    stdouts.update({slhamodule.name: stdout})
    slhafile = SLHA(obj)

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
        result, stdout = tools.get_ctypes_streams(
                func=slhamodule.send_to_predictor,
                args=[slhafile,input_pars.get(predictor.name),predictor, is_modifier])
        predictor_output.update(result)
        stdouts.update({predictor.name: stdout})

    return slhafile.process(), predictor_output , stdouts
