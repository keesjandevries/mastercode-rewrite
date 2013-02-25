#! /usr/bin/env python
import argparse, pprint, sys

from tools import pickle_object
# slha represntation
from ObsCalculator.interfaces.slhalib import SLHA

# spectrum calculator
from ObsCalculator.interfaces import softsusy
from ObsCalculator.interfaces import feynhiggs, micromegas, superiso, bphysics, lspscat
from ObsCalculator.interfaces import susypope

# X^2 calculator
from PointAnalyser import Constraints_list
from PointAnalyser import Analyse

#def parse_args():
#    parser = argparse.ArgumentParser(description='Process some integers.')
#    parser.add_argument('--save', '-s', dest='save', action='store', type=bool,
#            default=False, help='slha file name')
#
#    return parser.parse_args()
#def ouput_obj_to_pickle(d,filename):
#    file=open(filename,'wb')
#    pickle.dump(d,file)
#    print( "Object written to picled file",filename)
#    file.close()


if __name__=="__main__" :
    filenames=sys.argv[1:]
    l=[]
    slha_lookup=None
    for filename in filenames:
        slhafile=SLHA(lookup=slha_lookup)
        slhafile.read(filename)
        bpp = pprint.PrettyPrinter(indent=4, depth=5)
        kwargs={'verbose':False}
        predictions=susypope.run(slhafile,inputs=kwargs)
#        predictions=lspscat.run(slhafile)
        bpp.pprint(predictions)
        
        if True :
            all_constraints=Constraints_list.constraints
        #    data_set=all_constraints.keys()
            data_set=['Al(SLD)', 'sintheta_eff', 'Gamma_Z',  'Rl', 'Afb(b)',  'Afb(c)',    
                    'sigma_had^0', 'Al(P_tau)', 'Ac', 'Rb', 'Rc', 'Ab',  'Afb_l',  'MW-mc-old', ]
        #    print(data_set)
            constraints={name: all_constraints[name] for name in data_set}
            #pass this constraints list to the chi2 function
            total, breakdown = Analyse.chi2(predictions,constraints)
            print('Total is:',total)
            bpp.pprint(breakdown)
            l.append((breakdown,predictions,filename,total))

