#! /usr/bin/env python
import argparse

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
    slhafile.data[7]=1000.
    print(slhafile)


