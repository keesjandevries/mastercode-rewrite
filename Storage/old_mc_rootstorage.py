#! /usr/bin/env python
import Storage.interfaces.ROOT as root
from example_point import point 
from mc_new_old_oids_dict import get_mc_old_oid

#WARNING: This module will be changed.
def fill_vars(d,vars):
    for oid, val in point.items():
        old_oid=get_mc_old_oid(oid)
        if old_oid: 
            # To deal with stupid dubble assignment of Al
            try:
                vars[old_oid]=val
            except TypeError: 
                for o_oid in old_oid:
                    vars[o_oid]=val
    return vars

if __name__=="__main__" :
    vars=100*[0.]
    vars=fill_vars(point,vars)
    root.root_open('test.root')
    root.root_write(vars)
    root.root_close()
