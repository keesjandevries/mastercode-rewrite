#! /usr/bin/env python
from PointAnalyser.Constraints_list import constraints
import argparse, pprint

bpp = pprint.PrettyPrinter(indent=4, depth=3)

def parse_args():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--constraint', '-c', dest='constraint', action='store', type=str,
            default=None, help='give constraint name from PointAnalyser/Constraints_list.py')
    parser.add_argument('--values', '-v', dest='values', nargs='*',action='store', type=float,
            default=None, help='give constraint name from PointAnalyser/Constraints_list.py')
    parser.add_argument('--oid-sigmas',  dest='print_oid_sigmas', action='store_true',
            default=False, help='print dictionary of observable ids and corresponding sigmas')
    return parser.parse_args()


def format_ids_and_values_to_dict(ids,values):
    point={}
    for oid, val in zip(ids,values):
        point[oid]=val
    return point

if __name__=="__main__" :
    args = parse_args()

    if args.print_oid_sigmas:
        d={}
        for name, constr in constraints.items():
            oids=constr.get_oids()
            if len(oids) is 1: #FIXME: no deep thought went into this if statement could well be more general
                oid=oids[0]
                if d.get(oid):
                    print('WARNING: multiple constraints for observable ids: {}'.format(oid))
                d[oid]=constr.get_sigma()
        bpp.pprint(d)


#    data_set=['Al(SLD)', 'sintheta_eff', 'Gamma_Z',  'Rl', 'Afb(b)',  'Afb(c)',    
#                    'sigma_had^0', 'Al(P_tau)', 'Ac', 'Rb', 'Rc', 'Ab',  'Afb_l',  'MW-mc-old', ]
#    d={}
#    for constraint in data_set:
#        d[constraint]=constraints[constraint].get_sigma()
#    print(d)
    #constr=constraints['xenon100']
    #xenon100_cont=constr._data[0]
    #print(xenon100_cont.get_contour_value(423))
    if args.constraint:
        try:
            constraint=constraints[args.constraint]
        except KeyError:
            print("ERROR: {0} is not in PointAnalyser/Constraints_list.py".format(args.constraint))
        else:
            ids=constraint._ids
            if len(args.values) is len(ids):
                point=format_ids_and_values_to_dict(ids,args.values)
                chi2=constraint.get_chi2(point)
                print('Constraint: ',args.constraint, ' for values: ',args.values, ', gives chi2: ', chi2)



