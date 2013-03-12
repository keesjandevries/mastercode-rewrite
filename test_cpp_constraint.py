#! /usr/bin/env python
from PointAnalyser.interfaces.constraints import Constraint
import argparse


def parse_args():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--constraint', '-c', dest='constraint', action='store', type=str,
            default=None, help='give constraint name from PointAnalyser/Constraints_list.py')
    parser.add_argument('--values', '-v', dest='values', nargs='*',action='store', type=float,
            default=None, help='give constraint name from PointAnalyser/Constraints_list.py')

    return parser.parse_args()


def format_ids_and_values_to_dict(ids,values):
    point={}
    for oid, val in zip(ids,values):
        point[oid]=val
    return point

if __name__=="__main__" :
    args = parse_args()
    Constraint(1,[2.0,3.0],3)
