#! /usr/bin/env python

_SLHAfile__MAX_SLHA_SIZE = 10000
_SLHAblock__MAX_SLHA_SIZE = 10000
_SLHAline__MAX_SLHA_SIZE = 10000

from ctypes import cdll, create_string_buffer
SLHAlib = cdll.LoadLibrary('./libs/libmcslha.so')

def c_str_access(obj, func, max_size):
    c_str_buf = create_string_buffer(max_size)
    sz = func(obj, c_str_buf, max_size)
    if sz >= max_size:
        print "*** WARNING: string access has been truncated"
    return c_str_buf.value


class SLHAline(object):
    def __init__(self, name):
        self._obj = SLHAlib.SLHAline_new(str(name))
        self._value = SLHAlib.SLHAline_getvalue(self._obj)
        self._comment = c_str_access(self._obj, SLHAlib.SLHAline_getcomment,
                __MAX_SLHA_SIZE)

    def __str__(self):
        return c_str_access(self._obj, SLHAlib.SLHAline_getstr, __MAX_SLHA_SIZE)

    def set_value(self, val):
        try:
            SLHAlib.SLHAline_setvalue(self._obj, c_double(val))
        except:
            print "*** ERROR: failed to set value for SLHAline obj"
        else:
            self._value = val

    def get_value(self):
        return self._value

    def set_comment(self, comment):
        try:
            SLHAlib.SLHAline_setcomment(self._obj,comment)
        except:
            print "*** ERROR: failed to set comment for SLHAline obj"
        else:
            self._comment = comment

    def get_comment(self):
        c_str_access(self._obj, SLHAlib.SLHAline_getcomment, __MAX_SLHA_SIZE)


class SLHAblock(object):
    def __init__(self, name=''):
        self._obj = SLHAlib.SLHAblock_new(str(name))
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
