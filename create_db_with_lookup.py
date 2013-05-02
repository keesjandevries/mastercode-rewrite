#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3 , sys, random, os, argparse, pickle
import numpy as np

con = None
def parse_args():
    parser = argparse.ArgumentParser(description='Creating an sql data base')
    parser.add_argument('--output-file','-o', dest='output_file', action='store', 
             help='Name of output date base file',required=True)
    parser.add_argument('--pickled-point',help='initiate database with pickled file')
    parser.add_argument('--update', dest='update', action='store_true', 
            default=False,  help='Recreate data base, i.e. delete existing file if exists')
    return parser.parse_args()


def create_lookup(con,cur,obs_ids):
    #create table
    cur.execute('create table if not exists obs_id_lookup(id integer primary key, point_column TEXT, obs_id_field1 TEXT, obs_id_field2 TEXT)')
    #fill 
    for i,obs_id in enumerate(obs_ids):
        cur.execute('insert into obs_id_lookup values(null,?,?,?)',('obs{}'.format(i),obs_id[0],obs_id[1]))
    #commit
    con.commit()
    
def create_points_table(con,cur):
    # get the column names from the lookup table!!!
    cur.execute('select point_column from obs_id_lookup')
    point_column_names=[ name_tuple[0] for name_tuple in cur.fetchall()]
    #create table with (point_id, collection_id, [observables])
    cur.execute('create table if not exists points(point_id integer primary key, collection_id, {})'.format(','.join(point_column_names)))
    #commit
    con.commit()


if __name__=='__main__':
    #get arguments
    args= parse_args()
    #
    if not args.update:
        try:
            os.remove(args.output_file)
        except FileNotFoundError:
            pass
    #data base stuff
    try:
        #connection
        con=sqlite3.connect(args.output_file)
        #cursor
        cur=con.cursor()
        #get all observable ids
        with open(args.pickled_point,'rb') as point_file:
            all_obs_ids=[key for key in pickle.load(point_file).keys()]
        #create lookup 
        create_lookup(con,cur,all_obs_ids)
        create_points_table(con,cur)
        con.commit()
    
    # Finalise ...
    except sqlite3.Error as e:
        if con:
            con.rollback()
        print('ERROR: {}'.format(e.args[0]))
        sys.exit()
    finally:
        if con:
            con.close()
    
