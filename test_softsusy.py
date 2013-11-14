#! /usr/bin/env python

from  ObsCalculator.interfaces import softsusy

slha, error =softsusy.run( {
    ('MINPAR', 'A'): -4894.478766311405, 
    ('SMINPUTS', 'Mt'): 173.030717, 
    ('MINPAR', 'M0'): 474.31438371553725, 
    'model': 'NUHM1', 
    ('EXTPAR', 'MH2'): -16596203.991179556, 
    ('MINPAR', 'TB'): 13.13837036242273, 
    ('MINPAR', 'M12'): 1103.8747750307139, 
    ('MINPAR', 'signMUE'): 1})

print(slha)
