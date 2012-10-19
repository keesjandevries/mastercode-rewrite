#! /usr/bin/env python
import os

from build import predictors, utils

OPTIONS = {
        'base_dir': os.getcwd(),
        }

for mod in [ predictors, utils ]:
    mod.compile(**OPTIONS)
