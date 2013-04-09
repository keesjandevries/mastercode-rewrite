#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3 , sys 




# FIXME: this function is now duplicated from fill_points. Will and up in something lite mc_sql_tools.py
def get_columns_and_observable_ids(con,cur):
    cur.execute('select point_column, obs_id_field1 , obs_id_field2 from obs_id_lookup')
    obs_id_lookup=cur.fetchall()
    columns=[]
    oids={}
    for col, id1, id2 in obs_id_lookup:
        columns.append(col)
        oids[col]=(id1,id2)
    return columns, oids

def retrieve_points_from_rows(con,cur,rows,obs_columns=None,mc_obs_ids=None):
    # get lookup from database if not given
    if not (obs_columns and mc_obs_ids):
        obs_columns, mc_obs_ids = get_columns_and_observable_ids(con,cur)
    # loop over the rows to transform into point dictionaries
    points=[]
    for row in rows:
        point={mc_obs_ids[col]: val for col, val in zip(obs_columns, row[2:]) } #FIXME: we may want to replace this with row_factory
        points.append(point)
    return points

def row_to_point(row,point,oids_lookup):
    point={}
    for col, oid in oids_lookup.items():
        point[oid]=row[col]
    return point
