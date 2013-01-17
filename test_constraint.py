#! /usr/bin/env python
from PointAnalyser.Constraints_list import constraints
import argparse


def parse_args():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--constraint', '-c', dest='constraint', action='store', type=str,
            default=None, help='give constraint name from PointAnalyser/Constraints_list.py')
    parser.add_argument('--values', '-v', dest='values', nargs='*',action='store', type=float,
            default=None, help='give constraint name from PointAnalyser/Constraints_list.py')

    return parser.parse_args()


def format_ids_and_values_to_dict(ids,values):
    point={id1:{} for (id1,id2) in ids}
    for ((id1,id2),val)  in zip(ids,values):
        point[id1].update({id2:val})
    return point

if __name__=="__main__" :
    args = parse_args()

    try:
        constraint=constraints[args.constraint]
    except KeyError:
        print("ERROR: {0} is not in PointAnalyser/Constraints_list.py".format(args.constraint))
    else:
        ids=constraint._ids
        if len(args.values) is len(ids):
            point=format_ids_and_values_to_dict(ids,args.values)
            chi2=constraint.get_chi2(point)
            print('Constraint: ',args.constraint,', for values: ',args.values, ', gives chi2: ', chi2)



