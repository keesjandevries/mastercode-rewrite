#! /usr/bin/env python
import argparse

from ObsCalculator.interfaces.slhalib import SLHA, SLHAData, nslhadata, invalid, ofsetspinfo

def parse_args():
    parser = argparse.ArgumentParser(description='Pmssm 8d model from cmssm slha-file')
    parser.add_argument('filename'  ,   help='input cmssm slha file')
    return parser.parse_args()

if __name__=="__main__" :
    args=parse_args()
    filename=args.filename
    slhafile=SLHA()
    slhafile.read(filename)
    
    #M1
    M1=slhafile[('MSOFT', 'M1')]
    #sleptons
    sleptons=[
    slhafile[('MSOFT', 'MSL(1)')],
    slhafile[('MSOFT', 'MSL(2)')],
    slhafile[('MSOFT', 'MSL(3)')],
    slhafile[('MSOFT', 'MSE(1)')],
    slhafile[('MSOFT', 'MSE(2)')],
    slhafile[('MSOFT', 'MSE(3)')],]
    msl=sum(sleptons)/len(sleptons)
    #squarks first generations
    squarks_12=[
    slhafile[('MSOFT', 'MSQ(1)')],
    slhafile[('MSOFT', 'MSQ(2)')],
    slhafile[('MSOFT', 'MSU(1)')],
    slhafile[('MSOFT', 'MSU(2)')],
    slhafile[('MSOFT', 'MSD(1)')],
    slhafile[('MSOFT', 'MSD(2)')],]
    msq12=sum(squarks_12)/len(squarks_12)
    #squarks third generation
    squarks_3=[
    slhafile[('MSOFT', 'MSQ(3)')],
    slhafile[('MSOFT', 'MSU(3)')],
    slhafile[('MSOFT', 'MSD(3)')],]
    msq3=sum(squarks_3)/len(squarks_3)
    #trilinear couplings
    As=[
    slhafile[('AE', 'Af(3,3)')],
    slhafile[('AU', 'Af(3,3)')],
    slhafile[('AD', 'Af(3,3)')],]
    A=sum(As)/len(As)
    #tanb
    tanb=slhafile[('MINPAR','TB')]
    #mu
    mu=slhafile[('HMIX', 'MUE')]
    #MA
    MA=slhafile[('MASS', 'MA0')]

    print('./mc_point.py --mc-8d-pmssm {} {} {} {} {} {} {} {}'.format(msq12,msq3,msl, M1, A, MA,tanb,mu))
