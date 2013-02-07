#! /usr/bin/env python
import argparse, pprint

# slha represntation
from ObsCalculator.interfaces.slhalib import SLHA

# spectrum calculator
from ObsCalculator.interfaces import softsusy
from ObsCalculator.interfaces import feynhiggs, micromegas, superiso, bphysics, lspscat
from ObsCalculator.interfaces import susypope

# X^2 calculator
from PointAnalyser import Constraints_list
from PointAnalyser import Analyse

def parse_args():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--filename', '-f', dest='filename', action='store', type=str,
            default='slhas/test.slha', help='slha file name')

    return parser.parse_args()

if __name__=="__main__" :
    args=parse_args()
    filename=args.filename
    slhafile=SLHA()
    slhafile.read(filename)

    
    bpp = pprint.PrettyPrinter(indent=4, depth=5)
    predictions=susypope.run(slhafile)
#    predictions=lspscat.run(slhafile)
    bpp.pprint(predictions)
    
    if True:
        all_constraints=Constraints_list.constraints
    #    data_set=all_constraints.keys()
        data_set=['Al(SLD)', 'sintheta_eff', 'Gamma_Z',  'Rl', 'Afb(b)',  'Afb(c)',   'DAlpha_had', 
                'sigma_had^0', 'Al(P_tau)', 'Ac', 'Rb', 'Rc', 'Ab',  'Al_fb',  'MW-mc-old', ]
    #    print(data_set)
        constraints={name: all_constraints[name] for name in data_set}
        #pass this constraints list to the chi2 function
        total, breakdown = Analyse.chi2(predictions,constraints)
        bpp.pprint(breakdown)
