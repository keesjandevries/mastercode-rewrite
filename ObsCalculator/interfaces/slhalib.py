#! /usr/bin/env python
import pprint, math
from collections import OrderedDict, Counter
from ctypes import cdll, c_int, c_double, c_char_p, byref, Structure

from tools import c_complex, pipe_object_to_function, unique_str, is_int, rm, get_slha_ids
from tools import get_slhalibnr_from_oid, get_slha_nr_ids_dict
#import Variables

name = "SLHALib"
SLlib = cdll.LoadLibrary('packages/lib/libmcslhalib.so')
nslhadata = SLlib.get_nslhadata()
ofsetspinfo=SLlib.get_ofsetspinfo()
invalid = -999.0

# this idea *requires* that the memory allocation of a complex type (C99, c++0x)
# is the same as an array of 2 doubles.  This is in the standard, but mileage
# with different compilers may vary
class SLHAData(Structure):
    _fields_ = [('carray', c_complex * nslhadata)]

    def __len__(self):
        return len(self.carray)

    def __setitem__(self,key,value):
        #in fortran, the first array index is 1, so need to shift one back
        self.carray[key-1]=c_complex(value)

    def __getitem__(self,key):
        #FIXME: this is good for now since we don't use complex numbers ever
        #in fortran, the first array index is 1, so need to shift one back
        return self.carray[key-1].re

class SLHA(object):
    def __init__(self, data="",lookup=None):
        self.lookup=lookup
        if data:
            pipe_object_to_function(data, self.read)
            #Can only create a lookup based on an input slha file
            if not self.lookup:
                self.lookup=self.create_lookup()
            else:
                self.lookup=lookup

    def __str__(self):
        tmp_name = "/tmp/mc-{u}".format(u=unique_str())
        self.write(tmp_name)
        txt=open(tmp_name).read()
        rm(tmp_name)
        return txt

    def __len__(self):
        return len(self.data)
# FIXME: this needs to use pipe to function but at the moment fortran doesnt
# work with writing to pipes
    def __setitem__(self,key,value):
        try:
            self.data[self.lookup[key]]=value
        except KeyError:
            print("WARNING: {} is not a valid key".format(key))

    def __getitem__(self,key):
        try:
            return self.data[self.lookup[key]]
        except KeyError:
            print("WARNING: {} is not a valid key".format(key))

    def write(self, filename):
        SLlib.write_slha(filename.encode('ascii'), byref(self.data))

    def read(self, filename):
        self.data = SLHAData()
        SLlib.read_slha(filename.encode('ascii'), byref(self.data))
        if not self.lookup:
            self.lookup=self.create_lookup()

    def get_lookup(self):
        return self.lookup
#    def data_to_dict_using_variables(self):
#        """
#        looks for ids from Variables.py that look like 
#        ('slha',('block',(indicies),slhalib_nr))
#        Then tries to extract these values, if present
#        """
#        ids=Variables.get_ids()
#        slha_dict={}
#        #FIXME: not sure if this should be a function in tools.py
#        slha_ids=get_slha_ids(ids)
#        for oid in slha_ids:
#            slhalib_nr=get_slhalibnr_from_oid(oid)
#            value=self.data[slhalib_nr]
#            #slhalib has -999.0 as the default value
#            if value is not invalid: slha_dict[oid]=value
#        return slha_dict

#    def get_dict(self):
#        d={}
#        for i in range(1,nslhadata+1):
#            val=self.data[i]
#            if (val != invalid):
#                d[i]=val
#        return d


#    def get_oid_val_dict(self,oid_dict,make_suggestions=False):
#        nr_id_d     =get_slha_nr_ids_dict(oid_dict)
##        print(nr_id_d)
#        nr_val_d    =self.get_dict()
#        id_val_d    ={}
#        for nr, val in nr_val_d.items():
#            try:
#                id_val_d[nr_id_d[nr]]=val
#            except KeyError:
#                print("WARNING: no id in Variables.py corresponding to slhalib number {0}".format(nr))
#                id_val_d[('slha',(nr))]=val
#                if make_suggestions:
#                    suggested_ids=self.suggest_variables_index(val,nr)
#                    print("suggested indices for nr {0} and value {1}".format(nr,val))
#                    if len(suggested_ids) > 0: pprint.PrettyPrinter().pprint(suggested_ids)
#        return id_val_d

    def fill_slhadata_with_slhalib_nrs(self):
        #FIXME: this is a hack. If you look in SLHADefs.h, the SPinfo follows the numerical values
        for i in range(1,ofsetspinfo+1):
            if not self.data[i]==invalid :
                self.data[i]=float(i)


    def create_lookup(self):
        """
        This function returns a dictionary
        { slhalib_nr: ('block','comment'), ... , ('block','comment'): nr, ... }
        """
        #first backup the data
        backup_data={nr:self.data[nr] for nr in range(1,ofsetspinfo+1) if not nr == invalid }
        #backup_data=self.data.copy()
        #fill slhafile with slhalib numbers
        self.fill_slhadata_with_slhalib_nrs()
        #retrieve block- and observables- names and make dict
        block_indices_comment_nr_dict=self.process_all()
        lookup=OrderedDict()
        for key, val in block_indices_comment_nr_dict.items():
            # for the moment only need block and comment
            block, indices, comment=key
            try:
                nr=int(val)
            except TypeError:
                print("WARNING: the value for block {0}, indices {1}, comment {2}".format(block,str(indices),comment))
                print("has a non-integer value {0}".format(str(val)))
            else:
                oid=(block,comment)
                lookup[nr]=oid
        # now also save reverse
        for nr, oid in lookup.items():
            lookup[oid]=nr
        # restore data
        for nr, val in backup_data.items():
            self.data[nr]=val
        return lookup
                
            

#    def suggest_variables_index(self,value,slhalib_nr):
#        block_ind_comment_value_d=self.process_all()
#        suggestion_d={}
#        for key, val in block_ind_comment_value_d.items():
#            block,indices,comment=key
#            if val == value:
#                suggestion_d[comment]=('slha',(block,indices,slhalib_nr))
#        return suggestion_d

#    def all_unambiguous_suggestions(self):
#        nr_val_d    =self.get_dict()
#        block_ind_comment_value_d=self.process_all()
#        final_suggestion={}
#        for slhalib_nr,value in nr_val_d.items():
#            suggestion_d={}
#            for key, val in block_ind_comment_value_d.items():
#                block,indices,comment=key
#                if val == value:
#                    suggestion_d[comment]=('slha',(block,indices,slhalib_nr))
#            if len(suggestion_d) == 1:
#                final_suggestion.update(suggestion_d)
#        return final_suggestion


    def process_all(self):
        s = str(self)
        data = OrderedDict()
        block_name = None
        for line in s.split('\n'):
            if line.startswith('B'):
                # is a block
                block_name = line.split()[1]
                #pass
            elif not block_name == 'SPINFO':
                items = line.split()
                if len(items):
                    first_non_index = next(x for x in items if not is_int(x))
#                    hash_index = next(x for x in items if not x=='#')
                    indices_end = items.index(first_non_index)
#                    indices_end = items.index(hash_index) - 1
                    comment_pos = items.index('#') if '#' in items else 0
#                    if comment_pos: indices_end= comment_pos - 2
                    indices = tuple([int(x) for x in items[:indices_end]])
                    values = tuple([float(x) for x in
                            items[indices_end:comment_pos]])
                    if len(values) == 1:
                        values = values[0]
                    comment = ' '.join(items[comment_pos:]).lstrip('#').lstrip()
                    data[(block_name,indices,comment)] = values
        return data

    def process(self):
        data={}
        for i in range(1,nslhadata+1):
            val=self.data[i]
            if not val == invalid:
                try:
                    oid=('slha',self.lookup[i])
                except KeyError:
                    oid=('slha',i)
                data[oid]=val
        return data

def send_to_predictor(slhadata, inputs ,predictor, update=False):
    return predictor.run(slhadata, inputs , update)

def run(*args, **kwargs):
    assert "filename" in kwargs
    slha = SLHA()
    slha.read(kwargs['filename'])
    return slha
