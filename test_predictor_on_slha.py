#! /usr/bin/env python
import argparse, pprint

# slha represntation
from ObsCalculator.interfaces.slhalib import SLHA

# spectrum calculator
from ObsCalculator.interfaces import softsusy
from ObsCalculator.interfaces import feynhiggs, micromegas, superiso, bphysics, lspscat
from ObsCalculator.interfaces import susypope


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
    bpp.pprint(susypope.run(slhafile))
    
