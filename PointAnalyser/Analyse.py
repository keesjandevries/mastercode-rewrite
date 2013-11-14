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

# Want to print in order of the data set
def print_chi2_breakdown(point,constraints, data_set):
    header='{:<20}: {:>13} | {:<50} '.format('Name constraint','Chi2 penalty','Observables')
    print('='*len(header))
    print(header)
    print('='*len(header))
    total=0.
    for name in data_set: 
        oids= constraints[name].get_oids()
        chi2= constraints[name].get_chi2(point)
        try:
            print('{:<20}: {:>13.3f} | {} '.format(name,chi2, ['{:<30} : {:.6}'.format(str(oid),point[oid]) for oid in oids[:2] ] ))
        except KeyError:
            print('Continue building table...')
            continue
        total+=chi2
    print('='*len(header))
    print('Total Chi2: {}'.format(total))



