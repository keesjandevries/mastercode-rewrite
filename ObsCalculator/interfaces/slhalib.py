#! /usr/bin/env python

from collections import OrderedDict
from ctypes import cdll, c_int, c_double, c_char_p, byref, Structure

from tools import c_complex, pipe_object_to_function, unique_str, is_int, rm, get_slha_ids
from tools import get_slhalibnr_from_oid
import Variables

name = "SLHALib"
SLlib = cdll.LoadLibrary('packages/lib/libmcslhalib.so')
nslhadata = SLlib.get_nslhadata()

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
    def __init__(self, data=""):
        if data:
            pipe_object_to_function(data, self.read)

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

    def write(self, filename):
        SLlib.write_slha(filename.encode('ascii'), byref(self.data))

    def read(self, filename):
        self.data = SLHAData()
        SLlib.read_slha(filename.encode('ascii'), byref(self.data))

    def data_to_dict_using_variables(self):
        """
        looks for ids from Variables.py that look like 
        ('slha',('block',(indicies),slhalib_nr))
        Then tries to extract these values, if present
        """
        ids=Variables.get_ids()
        slha_dict={}
        #FIXME: not sure if this should be a function in tools.py
        slha_ids=get_slha_ids(ids)
        for oid in slha_ids:
            slhalib_nr=get_slhalibnr_from_oid(oid)
            value=self.data[slhalib_nr]
            #slhalib has -999.0 as the default value
            if value is not -999.0: slha_dict[oid]=value
        return slha_dict

    def process(self):
        s = str(self)
        data = OrderedDict()
        block_name = None
        for line in s.split('\n'):
            if line.startswith('B'):
                # is a block
                block_name = line.split()[1]
                #pass
            else:
                items = line.split()
                if len(items):
                    first_non_index = next(x for x in items if not is_int(x))
                    indices_end = items.index(first_non_index)
                    comment_pos = items.index('#') if '#' in items else 0
                    indices = tuple([int(x) for x in items[:indices_end]])
                    values = tuple([float(x) for x in
                            items[indices_end:comment_pos]])
                    if len(values) == 1:
                        values = values[0]
                    comment = ' '.join(items[comment_pos:]).lstrip('#').lstrip()
                    data[(block_name,comment)] = values
        return data

def send_to_predictor(slhadata, inputs ,predictor, update=False):
    return predictor.run(slhadata, inputs , update)

def run(*args, **kwargs):
    assert "filename" in kwargs
    slha = SLHA()
    slha.read(kwargs['filename'])
    return slha
