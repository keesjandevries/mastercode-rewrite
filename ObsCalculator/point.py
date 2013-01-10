from collections import OrderedDict

import tools

# slha represntation
from ObsCalculator.interfaces import slhalib as slhamodule
from ObsCalculator.interfaces.slhalib import SLHA

# spectrum calculator
from ObsCalculator.interfaces import softsusy
from ObsCalculator.interfaces import feynhiggs, micromegas, superiso, bphysics, lspscat
from ObsCalculator.interfaces import susypope

# defaults settings all defined in one place
from ObsCalculator import defaults

slha_generator = softsusy
slha_modifiers = [feynhiggs]
predictors = slha_modifiers + [micromegas, superiso, bphysics, lspscat,#]
        susypope]

def run_point(model, **input_pars):
    stdouts = OrderedDict()

    inputs=defaults.predictor_defaults
    for pred, dic in input_pars.items():
        inputs[pred].update(dic)

    obj, stdout = tools.get_ctypes_streams(func=slha_generator.run,
            args=[model], kwargs=inputs[slha_generator.name])
    stdouts.update({slhamodule.name: stdout})
    slhafile = SLHA(obj)

    predictor_output = OrderedDict()
    for predictor in predictors:
        is_modifier = predictor in slha_modifiers
        result, stdout = tools.get_ctypes_streams(
                func=slhamodule.send_to_predictor,
                args=[slhafile,inputs.get(predictor.name),predictor, is_modifier])
        predictor_output.update(result)
        stdouts.update({predictor.name: stdout})

    return slhafile.process(), predictor_output , stdouts
