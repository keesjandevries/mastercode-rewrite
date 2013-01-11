import math

from collections import defaultdict

from PointAnalyser import Constraints

_constraints_dict = Constraints.get_constraints_dict()

def chi2(predictions,data_set=None):
    #define here for now:
    if data_set is None:
        data_set=['Higgs125']
    chi2_total = 0.
    chi2_breakdown = defaultdict(dict)
    for name in data_set:
        constraint=_constraints_dict[name]
        chi2=constraint.get_chi2(predictions)
        chi2_total+=chi2
        chi2_breakdown[name] =  chi2
    return chi2_total, chi2_breakdown
