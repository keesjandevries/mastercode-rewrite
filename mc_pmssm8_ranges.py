#! /usr/bin/env python

#very simply dumps pmssm8 ranges into a json file
import json
#For the degenerate masses want to scan Highest and lowers from CMSSM bf
ranges={
        'msq12':   [1725. ,1810. ],
        'msq3':    [1300. , 1600. ],
        'msl':     [390. ,660. ],
        'M1':      [330. ,400. ],
        'A':       [-3300.,-1600  ],
        }

with open('User/pmssm_ranges.json','w') as f:
    json.dump(ranges, f)
