#! /usr/bin/env python
from ctypes import cdll, create_string_buffer, c_double, c_int, c_void_p
from collections import defaultdict
from modules import utils

_SLHAfile__MAX_SLHA_SIZE = 10000
_SLHAblock__MAX_SLHA_SIZE = 10000
_SLHAline__MAX_SLHA_SIZE = 10000

SLHAlib = cdll.LoadLibrary('packages/lib/libmcslhaclass.so')

# specify pointer return types
SLHAlib.SLHAline_new.restype = c_void_p
SLHAlib.SLHAblock_new.restype = c_void_p
SLHAlib.SLHAfile_new.restype = c_void_p
SLHAlib.SLHAfile_getblock.restype = c_void_p
SLHAlib.SLHAblock_getline.restype = c_void_p

def send_to_predictor(slhafile, predictor, update=False):
    pipe_name = "/tmp/mc-{u}".format(u=utils.unique_str())
    p_out = utils.pipe_object_to_function(pipe_name, slhafile,
            lambda: predictor.run([pipe_name, "slha/test.slha"][0]))
    if update:
        print """
    * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
    * =============================================================== *
    * WARNING, http://gcc.gnu.org/bugzilla/show_bug.cgi?id=30162a     *
    * gfortran currently doesn't write formatted data to named pipes  *
    * =============================================================== *
    * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
    """
        ## FIXME: currently http://gcc.gnu.org/bugzilla/show_bug.cgi?id=30162
        # this bug prevents gfortran correctly treating pipes.  It is aimed to
        # be fixed by gcc4.7.3 so we have to wait for that update
        #utils.setup_pipe(pipe_name, lambda: slhafile.read_file(pipe_name),
                #lambda: predictor.write_slha(pipe_name))
        pipe_name = "/tmp/mc-{u}_2".format(u=utils.unique_str())
        predictor.write_slha(pipe_name)
        slhafile.read_file(pipe_name)
    return p_out

def c_str_access(obj, func, max_size):
    c_str_buf = create_string_buffer(max_size)
    sz = func(obj, c_str_buf, max_size)
    if sz >= max_size:
        print "*** WARNING: string access has been truncated"
    return c_str_buf.value

def process_slhafile(slhafile):
    slha_info = defaultdict(list)
    current_block = ''
    lines = str(slhafile).replace('\t',' ').split('\n')
    for line in lines:
        clean = line.lstrip()
        fields = clean.split()
        if line:
            if clean[0] == 'B':
                # is block
                current_block = ' '.join(fields[1:])
            else:
                # is info line
                slha_info[current_block].append(tuple(fields))

    return slha_info

class SLHAline(object):
    def __init__(self,value=0, comment=''):
        self._obj = SLHAlib.SLHAline_new(c_double(value), comment)
        self._value = SLHAlib.SLHAline_getvalue(c_void_p(self._obj))
        self._comment = c_str_access(c_void_p(self._obj),
                SLHAlib.SLHAline_getcomment, __MAX_SLHA_SIZE)
        self._index = 0

    def __str__(self):
        return c_str_access(c_void_p(self._obj), SLHAlib.SLHAline_getstr,
                __MAX_SLHA_SIZE)

    def set_value(self, val):
        #try:
        SLHAlib.SLHAline_setvalue(c_void_p(self._obj), c_double(val))
        #except:
            #print "*** ERROR: failed to set value for SLHAline obj", e
        #else:
        self._value = val

    def get_value(self):
        return self._value

    def set_comment(self, comment):
        #try:
        SLHAlib.SLHAline_setcomment(c_void_p(self._obj),comment)
        #except:
            #print "*** ERROR: failed to set comment for SLHAline obj"
        #else:
        self._comment = comment

    def get_comment(self):
        c_str_access(c_void_p(self._obj), SLHAlib.SLHAline_getcomment,
                __MAX_SLHA_SIZE)

    def set_index1(self, index):
        #try:
        SLHAlib.SLHAline_setindex1(c_void_p(self._obj), c_int(index))
        #except:
            #print "*** ERROR: failed to set index for SLHAline obj"
        #else:
        self._index1 = index

    def get_index1(self):
        return SLHAlib.SLHAline_getindex1(c_void_p(self._obj))

    def set_index2(self, index):
        #try:
        SLHAlib.SLHAline_setindex2(c_void_p(self._obj), c_int(index))
        #except:
            #print "*** ERROR: failed to set index for SLHAline obj"
        #else:
        self._index2 = index

    def get_index2(self):
        return SLHAlib.SLHAline_getindex2(c_void_p(self._obj))

    def get_num_indices(self):
        return SLHAlib.SLHAline_getnumindices(c_void_p(self._obj))

    def get_full_index(self):
        return SLHAlib.SLHAline_getfullindex(c_void_p(self._obj))


class SLHAblock(object):
    def __init__(self, name='', lines=[]):
        self._obj = SLHAlib.SLHAblock_new(str(name))
        for line in lines:
            add_line(line)

    def __str__(self):
        return c_str_access(c_void_p(self._obj),
                SLHAlib.SLHAblock_getstr, __MAX_SLHA_SIZE)

    #def __getitem__(self, key):
        #line_obj = SLHAlib.SLHAblock_getline(c_void_p(self._obj), key)

    def add_line(self, line):
        SLHAlib.SLHAblock_addline(c_void_p(self._obj), line._obj)


class SLHAfile(object):
    def __init__(self, file_str=""):
        self._obj = SLHAlib.SLHAfile_new()
        if file_str:
            SLHAlib.SLHAfile_readstr(c_void_p(self._obj), file_str)

    def __str__(self):
        return c_str_access(c_void_p(self._obj), SLHAlib.SLHAfile_getstr,
                __MAX_SLHA_SIZE)

    #def __getitem__(self, key):
        #block_obj = SLHAlib.SLHAfile_getblock(c_void_p(self._obj), key)

    def read_file(self, filename):
        SLHAlib.SLHAfile_readfile(c_void_p(self._obj), str(filename))

    def add_block(self, block):
        SLHAlib.SLHAfile_addblock(c_void_p(self._obj), block._obj)

    def add_values(self, block_name, value_dict):
        lines_to_add = []
        block = SLHAblock(block_name)
        for comment, value in value_dict.iteritems():
            block.add_line( SLHAline(value,str(comment)) )
        self.add_block(block)
