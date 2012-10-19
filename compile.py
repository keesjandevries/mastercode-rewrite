#! /usr/bin/env python
import os

from build import predictors, utils, interfaces

OPTIONS = {
        'base_dir': os.getcwd(),
        }

#root_flags = subprocess.check_output(['root-config','--cflags','--libs'])
if not os.environ.get('ROOTSYS',None):
    raise OSError("ROOTSYS not defined: please source ROOT before building")

#for mod in [ predictors, utils, interfaces ]:
for mod in [ interfaces ]:
    mod.compile(**OPTIONS)
