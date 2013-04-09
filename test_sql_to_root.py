#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3 , sys,  argparse
# sql storage modules
import Storage.sqlite_storage as sql
# root storage modules
import Storage.interfaces.ROOT as root
from Storage import old_mc_rootstorage 

def parse_args():
    parser = argparse.ArgumentParser(description='Fill points randomly for the moment')
    parser.add_argument('--input-file','-i', dest='input_file', action='store', 
              help='Name of input date base file')
    parser.add_argument('--n-points','-n', dest='n_points', action='store', type=int, default=10000,
              help='Name of input date base file')
    parser.add_argument('--root_save'  , '-r', dest='root_save', action='store_true', help='save to root file')
    return parser.parse_args()


if __name__=="__main__" :
    con = None
    args= parse_args()
    try:
        #connection and cursor
        con=sqlite3.connect(args.input_file)
        cur=con.cursor()
        #retrieve a point
        n_points=args.n_points
        root.root_open('temp/test.root')
        cur.execute('select * from points limit {}'.format(n_points))
        for row in cur:
            root.root_write(row)
        root.root_close()
#        rows=cur.fetchmany(100000)
#        points=sql.retrieve_points_from_rows(con,cur,rows)
    
    # Finalise ...
    except sqlite3.Error as e:
        if con:
            con.rollback()
        print('ERROR: {}'.format(e.args[0]))
        sys.exit()
    finally:
        if con:
            con.close()
#
#    # save to root
#    if args.root_save:
#        # NOTE: for old_mc_rootstorage, need X^2 
#        root.root_open('temp/test.root')
#        total=5.0
#        for combined_obs in points:
#            combined_obs[('tot_X2','all')]=total
#            old_mc_rootstorage.write_point_to_root(combined_obs)
#        root.root_close()
