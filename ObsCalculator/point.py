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

    obj, stdout = tools.get_ctypes_streams(func=slha_generator.run,
            args=[model], kwargs=input_pars[slha_generator.name])

    stdouts.update({slhamodule.name: stdout})
    slhafile = SLHA(obj)

    predictor_output = OrderedDict()
    for predictor in predictors:
        is_modifier = predictor in slha_modifiers
        result, stdout = tools.get_ctypes_streams(
                func=slhamodule.send_to_predictor,
                args=[slhafile,input_pars.get(predictor.name),predictor, is_modifier])
        predictor_output.update(result)
        stdouts.update({predictor.name: stdout})

    return slhafile, predictor_output , stdouts
