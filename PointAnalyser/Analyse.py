import math

from collections import defaultdict

from PointAnalyser import Constraints

_constraints = Constraints.constraints

#def set_constraints(d):
    #global _constraints
    #_constraints = d.copy()

def chi2(observations):
    chi2_total = 0.
    chi2_breakdown = defaultdict(dict)
    for name, constraint in _constraints.items():
        print(constraint.get_chi2(observations))
    #for predictor, predictions in observations.items():
        #for name, value in predictions.items():
            #if name in _constraints:
                #constraint = _constraints[name]
                #chi2 = constraint['func'](value, constraint['value'],
                        #math.sqrt(sum([x**2 for x in constraint['error']])))
                #chi2_breakdown[predictor][name] = (value, chi2)
                #chi2_total += chi2
    return chi2_total, chi2_breakdown
