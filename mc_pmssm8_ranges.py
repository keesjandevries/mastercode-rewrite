#! /usr/bin/env python

#very simply dumps pmssm8 ranges into a json file
import json
#For the degenerate masses want to scan Highest and lowers from CMSSM bf
ranges={
        'msq12':   [0.      ,5000. ],
        'msq3':    [0.      ,5000. ],
        'msl':     [0.      ,5000. ],
        'M1':      [0.      ,5000. ],
        'A':       [-5000.  ,5000. ],
        'MA':      [0.      ,5000. ],
        'tanb':    [1.      ,60.   ],
        'mu':      [-5000.  ,5000. ],
        }

with open('User/pmssm8_ranges.json','w') as f:
    json.dump(ranges, f)

#These were the parameters used for an initial scan.
#        'msq12':   [1725. ,1810. ],
#        'msq3':    [1300. , 1600. ],
#        'msl':     [390. ,660. ],
#        'M1':      [330. ,400. ],
#        'A':       [-3300.,-1600  ],
