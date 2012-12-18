from collections import OrderedDict

# slha represntation
from mcrw.interfaces import slhalib as slhamodule
from mcrw.interfaces.slhalib import SLHA

# spectrum calculator
from mcrw.interfaces import softsusy
from mcrw.interfaces import feynhiggs, micromegas, superiso, bphysics, lspscat
from mcrw.interfaces import susypope

from mcrw import utils

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
