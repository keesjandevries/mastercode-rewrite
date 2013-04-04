#! /usr/bin/env python
import pprint, math
from collections import OrderedDict, Counter
from ctypes import cdll, c_int, c_double, c_char_p, byref, Structure

from tools import c_complex, pipe_object_to_function,  is_int, rm, unique_filename

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
    def __init__(self, data="",lookup=None,tmp_dir=None):
        self._tmp_dir=tmp_dir
        if lookup:
            self.lookup=lookup
        else:
            self.lookup=self.create_lookup()
        if data:
#            #cannot do produce lookup on the fly with the pipe_object_to_function
#            #therefore, do it separate
            fname=unique_filename(self._tmp_dir)
            with open(fname,'w') as softpoint_input_file:
                softpoint_input_file.write(data)
            self.read(fname)
            rm(fname)
#            error=pipe_object_to_function(pipe_file_name, data, self.read,args=[],kwargs={})
#            if error: print("HERE SLHA LIB GIVES AN ERROR")

    def __str__(self):
        tmp_name=unique_filename(self._tmp_dir)
        self.write(tmp_name)
        f=open(tmp_name)
        txt=f.read()
        f.close()
        rm(tmp_name)
        return txt

    def __len__(self):
        return len(self.data)
# FIXME: this needs to use pipe to function but at the moment fortran doesnt
# work with writing to pipes

    def __setitem__(self,key,value):
        if self.lookup:
            try:
                self.data[self.lookup[key]]=value
            except KeyError:
                print("WARNING: {0} is not a valid key".format(key))
        else:
            print("WARNING: lookup is not initialised for slha object")


    def __getitem__(self,key):
        if self.lookup:
            try:
                return self.data[self.lookup[key]]
            except KeyError:
                print("WARNING: {0} is not a valid key".format(key))
        else:
            print("WARNING: lookup is not initialised for slha object")

    def write(self, filename):
        SLlib.write_slha(filename.encode('ascii'), byref(self.data))

    def read(self, filename):
        self.data = SLHAData()
        SLlib.read_slha(filename.encode('ascii'), byref(self.data))

    def get_lookup(self):
        if self.lookup:
            return self.lookup.copy()
        else:
            print("WARNING: cannot return lookup, because lookup is not initiated")


    def create_lookup(self):
        """
 This function returns a dictionary
 { slhalib_nr: ('block','comment'), ... , ('block','comment'): slhalib_nr, ... }
        """
        self.data=SLHAData()
        #fill complex array with "invalid", which is equivalent to empty slha file 
        for i in range(1,nslhadata+1):
            self.data[i]=invalid
        #fill every array element that could containt a number with its array index 
        for i in range(1,ofsetspinfo+1):
            self.data[i]=i
        #retrieve block- and observables- names and make dict
        block_indices_comment_nr_dict=self.get_blocks_indices_comments_values()
        #fill lookup
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
        # also save reverse
        for nr, oid in lookup.items():
            lookup[oid]=nr
        return lookup

                
            
    def get_blocks_indices_comments_values(self):
        """
        This function contains knowledge about what an slhafile from slhalib looks like
        It returns a dictionary: {(block_name,indices,comment):  value, ...}
        NB: atm ignoring BLOCK SPINFO  and  DECAY's
        """
        s = str(self)
        data = OrderedDict()
        block_name = None
        for line in s.split('\n'):
            if line.startswith('B'):
                # is a block
                block_name = line.split()[1]
                if 'Q=' in line:
                    data[(block_name,tuple([]),'Qscale')]= float(line.split('=')[1].split()[0])
            elif line.startswith('D'):
                #FIXME: we may want to change this
                print("WARNING: DECAY's are ignored in SLHA.get_blocks_indices_comments_values() ")
                block_name=None
            elif block_name and (not block_name == 'SPINFO') :
                #FIXME: possibly want to have the SPINFO as well at some point
                items = line.split()
                if len(items):
                    first_non_index = next(x for x in items if not is_int(x))
                    indices_end = items.index(first_non_index)
                    comment_pos = items.index('#') if '#' in items else 0
                    if comment_pos >0: indices_end=comment_pos-1
                    indices = tuple([int(x) for x in items[:indices_end]])
                    values = tuple([float(x) for x in
                            items[indices_end:comment_pos]])
                    if len(values) == 1:
                        values = values[0]
                    comment = ' '.join(items[comment_pos:]).lstrip('#').lstrip()
                    data[(block_name,indices,comment)] = values
        return data

    def process(self):
        data=OrderedDict()
        for i in range(1,ofsetspinfo+1):
            val=self.data[i]
            if not val == invalid:
                try:
                    oid=self.lookup[i]
                    data[oid]=val
                except KeyError:
                    print("ERROR: {} not found in lookup".format(i)) 
        return data

def send_to_predictor(slhadata, inputs ,predictor, update=False):
    return predictor.run(slhadata, inputs , update)

def run(*args, **kwargs):
    assert "filename" in kwargs
    slha = SLHA()
    slha.read(kwargs['filename'])
    return slha
