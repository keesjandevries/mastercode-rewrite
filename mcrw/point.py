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

DEBUG = False

def run_point(model, **inputs):
    stdouts = OrderedDict()

    obj, stdout = utils.get_ctypes_streams(func=slha_generator.run,
            args=[model], kwargs=inputs)
    stdouts.update({slhamodule.name: stdout})
    slhafile = SLHA(obj)
    if DEBUG: print(obj)

    predictor_output = OrderedDict()
    for predictor in predictors:
        is_modifier = predictor in slha_modifiers
        result, stdout = utils.get_ctypes_streams(
                func=slhamodule.send_to_predictor,
                args=[slhafile,predictor, is_modifier])
        predictor_output.update(result)
        stdouts.update({predictor.name: stdout})

    if DEBUG:
        for name, stdout in stdouts.items():
            print("="*80)
            print(utils.ansi_bold(name))
            print("-"*80)
            print(stdout)
            print("="*80)
        for predictor, obs in predictor_output.items():
            print('')
            print(utils.ansi_bold(predictor))
            print("="*len(predictor))
            x = max([len(n) for n,_ in obs.items()])
            f_str = "{{n:{x}}} = {{p}}".format(x=x)
            for name,value in obs.items():
                if type(value) is not list:
                    print(f_str.format(n=name, p=value))
                else:
                    print(f_str.format(n=name, p="[{0}, ... , {1}][{2}]".format(
                        value[0],value[-1],len(value))))

    return slhafile.process(), predictor_output
