from collections import OrderedDict

# slha represntation
from interfaces import slhalib as slhamodule
from interfaces.slhalib import SLHA

# spectrum calculator
from interfaces import softsusy
from interfaces import feynhiggs, micromegas, superiso, bphysics, lspscat
from interfaces import susypope


import utils

slha_generator = softsusy
slha_modifiers = [feynhiggs]
predictors = slha_modifiers + [micromegas, superiso, bphysics, lspscat,#]
        susypope]

DEBUG = False

def run_point(model, **inputs):
    stdouts = OrderedDict()

    #print "Generating SLHA file...",
    obj, stdout = utils.get_ctypes_streams(func=slha_generator.run,
            args=[model], kwargs=inputs)
    stdouts.update({slhamodule.name: stdout})
    slhafile = SLHA(obj)
    if DEBUG: print obj
    #print "Done"
    #print>>open('slhas/test.slha','w'), slhafile

    predictor_output = OrderedDict()
    for predictor in predictors:
        #print "Running {n}...".format(n=predictor.name),
        is_modifier = predictor in slha_modifiers
        result, stdout = utils.get_ctypes_streams(
                func=slhamodule.send_to_predictor,
                args=[slhafile,predictor, is_modifier])
        predictor_output.update(result)
        stdouts.update({predictor.name: stdout})
    if DEBUG:
        for name, stdout in stdouts.iteritems():
            print "="*80
            print utils.ansi_bold(name)
            print "-"*80
            print stdout
            print "="*80
        #print "Done"

    for predictor, obs in predictor_output.iteritems():
        print
        print utils.ansi_bold(predictor)
        print "="*len(predictor)
        x = max([len(n) for n,_ in obs.iteritems()])
        f_str = "{{n:{x}}} = {{p}}".format(x=x)
        for name,value in obs.iteritems():
            if type(value) is not list:
                print f_str.format(n=name, p=value)
            else:
                print f_str.format(n=name, p="[{0}, ... , {1}][{2}]".format(
                    value[0],value[-1],len(value)))

    #print slhafile

    #print>>open('slhas/testPoint_output_fh.slha','w'), slhafile
    #utils.pickle_object(slhafile, 'slhas/testPoint_output.pickled')
    #unpickled = utils.open_pickled_file('slhas/testPoint_output.pickled')
    #print unpickled


