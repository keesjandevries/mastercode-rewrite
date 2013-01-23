#! /usr/bin/env python
import argparse, pprint
#import Variables

from ObsCalculator.interfaces.slhalib import SLHA

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
#       print(slhafile.data_to_dict_using_variables())
    bpp = pprint.PrettyPrinter(indent=4, depth=5)
#    slhafile.get_matching_dict(Variables.get_ids(),True)

#    bpp.pprint(slhafile.get_lookup())
#    print(slhafile)

#    slhafile[('MSOFT', 'MHu2')]=90.
    print(slhafile[('MSOFT', 'MHu2')])
#    bpp.pprint(slhafile.process())
#    print(slhafile) 
#    bpp.pprint(slhafile.get_oid_val_dict(Variables.get_ids(),True))
#    bpp.pprint(slhafile.all_unambiguous_suggestions())
    
#    bpp.pprint(slhafile.process_all())



