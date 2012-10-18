#! /usr/bin/env python

_SLHAfile__MAX_SLHA_SIZE = 10000
_SLHAblock__MAX_SLHA_SIZE = 10000
_SLHAline__MAX_SLHA_SIZE = 10000

from ctypes import cdll, create_string_buffer, c_double, c_int
SLHAlib = cdll.LoadLibrary('./libs/libmcslha.so')

def c_str_access(obj, func, max_size):
    c_str_buf = create_string_buffer(max_size)
    sz = func(obj, c_str_buf, max_size)
    if sz >= max_size:
        print "*** WARNING: string access has been truncated"
    return c_str_buf.value


class SLHAline(object):
    def __init__(self,value=0, comment=''):
        self._obj = SLHAlib.SLHAline_new(c_double(value), comment)
        self._value = SLHAlib.SLHAline_getvalue(self._obj)
        self._comment = c_str_access(self._obj, SLHAlib.SLHAline_getcomment,
                __MAX_SLHA_SIZE)
        self._index = 0

    def __str__(self):
        return c_str_access(self._obj, SLHAlib.SLHAline_getstr, __MAX_SLHA_SIZE)

    def set_value(self, val):
        #try:
        SLHAlib.SLHAline_setvalue(self._obj, c_double(val))
        #except:
            #print "*** ERROR: failed to set value for SLHAline obj", e
        #else:
        self._value = val

    def get_value(self):
        return self._value

    def set_comment(self, comment):
        #try:
        SLHAlib.SLHAline_setcomment(self._obj,comment)
        #except:
            #print "*** ERROR: failed to set comment for SLHAline obj"
        #else:
        self._comment = comment

    def get_comment(self):
        c_str_access(self._obj, SLHAlib.SLHAline_getcomment, __MAX_SLHA_SIZE)

    def set_index1(self, index):
        #try:
        SLHAlib.SLHAline_setindex1(self._obj, c_int(index))
        #except:
            #print "*** ERROR: failed to set index for SLHAline obj"
        #else:
        self._index1 = index

    def get_index1(self):
        return SLHAlib.SLHAline_getindex1(self._obj)

    def set_index2(self, index):
        #try:
        SLHAlib.SLHAline_setindex2(self._obj, c_int(index))
        #except:
            #print "*** ERROR: failed to set index for SLHAline obj"
        #else:
        self._index2 = index

    def get_index2(self):
        return SLHAlib.SLHAline_getindex2(self._obj)

    def get_num_indices(self):
        return SLHAlib.SLHAline_getnumindices(self._obj)

    def get_full_index(self):
        return SLHAlib.SLHAline_getfullindex(self._obj)


class SLHAblock(object):
    def __init__(self, name='', lines=[]):
        self._obj = SLHAlib.SLHAblock_new(str(name))
        for line in lines:
            add_line(line)

    def __str__(self):
        return c_str_access(self._obj, SLHAlib.SLHAblock_getstr,
                __MAX_SLHA_SIZE)

    def add_line(self, line):
        SLHAlib.SLHAblock_addline(self._obj, line._obj)


class SLHAfile(object):
    def __init__(self):
        self._obj = SLHAlib.SLHAfile_new()

    def __str__(self):
        return c_str_access(self._obj, SLHAlib.SLHAfile_getstr,
                __MAX_SLHA_SIZE)

    def read_file(self, filename):
        SLHAlib.SLHAfile_readfile(self._obj, str(filename))

    def add_block(self, block):
        SLHAlib.SLHAfile_addblock(self._obj, block._obj)

    def add_values(self, block_name, value_dict):
        lines_to_add = []
        block = SLHAblock(block_name)
        for comment, value in value_dict.iteritems():
            block.add_line( SLHAline(value,str(comment)) )
        self.add_block(block)
