#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3 , sys,  argparse
# sql storage modules
import Storage.sqlite_storage as sql
# root storage modules
import Storage.interfaces.ROOT as root
from Storage import old_mc_rootstorage 
#

#X^2 calculation data sets
from User.data_sets import data_sets
from PointAnalyser import Analyse
from PointAnalyser import Constraints_list


def parse_args():
    parser = argparse.ArgumentParser(description='Fill points randomly for the moment')
    parser.add_argument('--input-file','-i', dest='input_file', action='store', 
              help='Name of input date base file')
    parser.add_argument('--n-points','-n',  action='store', type=int, default=10000,
              help='Name of input date base file')
    parser.add_argument('--data-set'  ,  default="mc8", help='data set for X^2 calculation')
    parser.add_argument('--root-save'  , '-r',   help='save to root file')
    return parser.parse_args()

if __name__=="__main__" :
    con = None
    args= parse_args()
    #initialise constraints once
    constraints={name: Constraints_list.constraints[name] for name in data_sets[args.data_set]}
    try:
        #connection 
        con=sqlite3.connect(args.input_file)
        #use row factory (see sqlite3 python documentation sqlite3.Row)
        con.row_factory=sqlite3.Row
        #cursor
        cur=con.cursor()
        #number of points
        n_points=args.n_points
        #open root file
        root.root_open(args.root_save)
        #get observables lookuk
        lookup = sql.get_observable_ids(con,cur)    # lookup={col1: ( .. , .. ) , .... }
        #FIXME: this statement should make a sensible selection, for now just a number of points
        cur.execute('select * from points limit {}'.format(n_points))
        for row in cur:
            point={ oid: row[col]  for col, oid in lookup.items()}
            total, breakdown = Analyse.chi2(point,constraints)
            point[('tot_X2', 'all')]=total
            old_mc_rootstorage.write_point_to_root(point)
        root.root_close()
    
    # Finalise ...
    except sqlite3.Error as e:
        if con:
            con.rollback()
        print('ERROR: {}'.format(e.args[0]))
        sys.exit()
    finally:
        if con:
            con.close()
