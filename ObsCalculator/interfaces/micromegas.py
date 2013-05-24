#! /usr/bin/env python
import subprocess, json
from tools import  ctypes_field_values, rm, unique_filename

name = "Micromegas"
executable = 'packages/bin/micromegas.x'

#NOTE: KJ 2013/05/23 
#This module does not use a shared library object for an interface to Micromegas.
#It turned out that Micromegas (version 2.4.5, but this is not likely to change) accumulates open shared objects.
#This was verified as follows:
# * cd <MICROMEGAS_DIR>/MSSM
# * comment out "#define SUGRA"
# * make main=main.c
# * valgrind --leak-check=full --track-origins=yes --log-file=log.out --show-reachable=yes ./main slha-file.txt
# In log.out you'll see that a lot of memory is still reachable. 
# This is not a leak, because this memory doen't go out of scope, but in the context mastercode this was found to accumulate

#Instead, subprocess call an executable that generates output like: 
# ... std_out ....
#["MastercodeTag", "Omega", 1.465819  ]
# ... std_out ....
#["MastercodeTag", "sigma_p_si", 1.307291e-09 ]
# ... std_out ....
#The tag is used to identify observables and distiguish it from other standard out

def run(slhadata, inputs=None, update=False) :
    if inputs is None: inputs={}
    #write out slha file
    fname=unique_filename(inputs.get('tmp_dir'))
    slhadata.write(fname)
    #define default outputs
    try:
        std_out=(subprocess.check_output([executable,fname])).decode('utf-8') 
        #define empty and then fill
        output={}
        #get Omega and sigma_p_si and possibly other variables from standard out
        lines=std_out.split('\n')
        for line in lines:
            if 'MastercodeTag' in line:
                tag, obs, val = json.loads(line)
                output[obs]=val
        output['error']=0
    except subprocess.CalledProcessError as e:
        #if micromegas fail, it exits with non zero code. This is cought by subprocess.CalledProcessError
        std_out=e.output.decode('utf-8')
        #FIXME: maybe there is a better way of handling default error output 
        #FIXME: for CMSSM sampling in boxes don't use infinite X^2 for non-neutralino lsp
        output={'Omega':0., 'sigma_p_si':0.,'error':0}
    #rm slha file
    rm(fname)
    #handle verbosity
    if 'verbose' in inputs:
        print(std_out)
    output={(name,key): val for key, val in output.items() }
    return output 
