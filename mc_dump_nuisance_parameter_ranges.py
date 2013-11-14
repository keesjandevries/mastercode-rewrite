#! /usr/bin/env python
import json

ranges={
        'mt' :     [171.4,175],
        'mz':      [91.1833,91.1917],
        'delta_alpha_had':[0.02729,0.02769],}

with open('User/nuisance_parameter_ranges.json','w') as f:
    json.dump(ranges, f)
