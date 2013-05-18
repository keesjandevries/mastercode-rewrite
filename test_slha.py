#! /usr/bin/env python
import argparse, pprint
import cProfile
#import Variables

from ObsCalculator.interfaces.slhalib import SLHA, SLHAData, nslhadata, invalid, ofsetspinfo

from tools import c_complex

def parse_args():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--filename', '-f', dest='filename', action='store', type=str,
            default='slhas/test.slha', help='slha file name')

    return parser.parse_args()

if __name__=="__main__" :
    args=parse_args()
    filename=args.filename
    slhafile=SLHA()
    lookup=slhafile.get_lookup()
    slhafile.read(filename)
    oids=[oid for oid in lookup.keys() if isinstance(oid,tuple)]
    extpars=([oid for oid in oids if oid[0]=='EXTPAR'])
#    print(slhafile[('MASS', 'Mh0')])
#    slhafile.read(filename)
#    for v in slhafile.data:
#        print(v)
#    cProfile.run('slhafile=SLHA();slhafile.read(filename)')
#    lookup=slhafile.get_lookup()
    

#    slhafile[('SMINPUTS','Mt')]=1.
#    print(slhafile[('SMINPUTS','Mt')])
#    slhafile2=SLHA(lookup=lookup)
#    slhafile2.read(filename)
#    cProfile.run('slhafile2=SLHA(lookup=lookup);slhafile2.read(filename)')
#    slhafile2[('SMINPUTS','Mt')]=1.
#    print(slhafile2[('SMINPUTS','Mt')])
#    slhafile2.write('temp2.slha')
#       print(slhafile.data_to_dict_using_variables())
    pp = pprint.PrettyPrinter(indent=4, depth=5)
    pp.pprint(extpars)
#    pp.pprint(lookup)
#    pp.pprint(slhafile2.get_lookup())
#    print(slhafile)

#    slhafile[('MSOFT', 'MHu2')]=90.
#    print(slhafile[('MSOFT', 'MHu2')])
#    pp.pprint(slhafile.process())
#    pp.pprint(slhafile.create_lookup())
#    print(slhafile) 
#    pp.pprint(slhafile.get_oid_val_dict(Variables.get_ids(),True))
#    pp.pprint(slhafile.all_unambiguous_suggestions())
    
#    pp.pprint(slhafile.process_all())



