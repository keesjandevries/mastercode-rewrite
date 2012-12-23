import math

from PointAnalyser import Constraints

constraints = Constraints.base_constraints

def set_constraints(d):
    global constraints
    constraints = d.copy()

def chi2(predictions, value):
    chi2 = 0.
    if prediction in constraints:
        constraint = constraints[prediction]
        chi2 = constraint['func'](value, constraint['value'],
                math.sqrt(sum([x**2 for x in constraint['error']])))
    return chi2
