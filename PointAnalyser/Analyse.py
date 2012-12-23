import math

from PointAnalyser import Constraints

_constraints = Constraints.base_constraints

def set_constraints(d):
    global _constraints
    _constraints = d.copy()

def chi2(predictions, value):
    chi2_total = 0.
    chi2_breakdown = {}
    for prediction in predictions:
        if prediction in _constraints:
            constraint = _constraints[prediction]
            chi2 = constraint['func'](value, constraint['value'],
                    math.sqrt(sum([x**2 for x in constraint['error']])))
            chi2_breakdown[prediction] = chi2
            chi2_total += chi2
    return chi2_total, chi2_breakdown
