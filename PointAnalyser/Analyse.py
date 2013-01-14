import math

from collections import defaultdict

def chi2(point,constraints):
    """
chi2 takes 'point', which is a dictionary of dictionaries point['id1']['id2']
and constraints, which are literaly the classes.
    """
    chi2_total = 0.
    chi2_breakdown = defaultdict(dict)
    for name , constraint in constraints.items():
        chi2=constraint.get_chi2(point)
        chi2_breakdown[name]=chi2
        chi2_total+=chi2
    return chi2_total, chi2_breakdown
