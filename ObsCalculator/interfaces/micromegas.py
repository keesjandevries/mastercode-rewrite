#! /usr/bin/env python
import subprocess, json
from tools import  ctypes_field_values, rm, unique_filename

name = "Micromegas"
#executable = 'packages/bin/micromegas.x'
default_version='3.2'

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
    try:
        versions=inputs['versions']
    except KeyError:
        versions=[default_version]
    #write out slha file
    fname=unique_filename(inputs.get('tmp_dir'))
    slhadata.write(fname)
    #define default outputs
    return_output={}
    for version in versions:
        executable='packages/bin/micromegas-{}.x'.format(version)
        try:
            std_out=(subprocess.check_output([executable,fname])).decode('utf-8') 
            #define empty and then fill
            output={}
            #get Omega and sigma_p_si and possibly other variables from standard out
            lines=std_out.split('\n')
            nanflag=False
            for line in lines:
                if ('MastercodeTag' in line) :
                    if not ('nan' in line):
                        tag, obs, val = json.loads(line)
                        output[obs]=val
                    else :
                        nanflag=True
            output['error']=int(nanflag)
        except subprocess.CalledProcessError as e:
            #if micromegas fails, it exits with non zero code. This is cought by subprocess.CalledProcessError
            std_out=e.output.decode('utf-8')
            #only output error, since no calculation has been made
            output={'error':1}
        if len(versions)==1:
            return_output={(name,key): val for key, val in output.items() }
        else:
            return_output.update({(name+version,key): val for key, val in output.items() })
    #rm slha file
    rm(fname)
    #handle verbosity
    if 'verbose' in inputs:
        print(std_out)
    return return_output 
