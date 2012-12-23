from collections import OrderedDict

# slha represntation
from ObsCalculator.interfaces import slhalib as slhamodule
from ObsCalculator.interfaces.slhalib import SLHA

# spectrum calculator
from ObsCalculator.interfaces import softsusy
from ObsCalculator.interfaces import feynhiggs, micromegas, superiso, bphysics, lspscat
from ObsCalculator.interfaces import susypope

from ObsCalculator import utils

slha_generator = softsusy
slha_modifiers = [feynhiggs]
predictors = slha_modifiers + [micromegas, superiso, bphysics, lspscat,#]
        susypope]

def run_point(model, **inputs):
    stdouts = OrderedDict()

    obj, stdout = utils.get_ctypes_streams(func=slha_generator.run,
            args=[model], kwargs=inputs)
    stdouts.update({slhamodule.name: stdout})
    slhafile = SLHA(obj)

    predictor_output = OrderedDict()
    for predictor in predictors:
        is_modifier = predictor in slha_modifiers
        result, stdout = utils.get_ctypes_streams(
                func=slhamodule.send_to_predictor,
                args=[slhafile,predictor, is_modifier])
        predictor_output.update(result)
        stdouts.update({predictor.name: stdout})

    return slhafile.process(), predictor_output
