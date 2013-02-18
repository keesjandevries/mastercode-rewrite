#! /usr/bin/env python
from ObsCalculator.interfaces import softsusy2

d={ ('MINPAR', 'M0'): 300.53,
       ('MINPAR', 'M12'): 905.0,
           ('MINPAR', 'TB'): 16.26,
               ('MINPAR', 'signMUE'): 1.0,
                   ('MINPAR', 'A'): -1303.97,
                   'verbose': True
                   }
softsusy2.run('cMSSM',d)
