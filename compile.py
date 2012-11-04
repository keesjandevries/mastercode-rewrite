#! /usr/bin/env python
import os

from build import predictors, utils, interfaces

OPTIONS = {
        'base_dir': os.getcwd(),
        }

#for mod in [predictors, utils, interfaces]:
for mod in [interfaces]:
    mod.compile(**OPTIONS)
