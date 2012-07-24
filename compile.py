#! /usr/bin/env python
import os
import subprocess
from modules.utils import fetch_url, extract_tarfile

prefix_dir = 'packages'
tar_dir = 'tars'
predictor_dir = 'predictors'

softsusy = {
        'version': '3.3.1',
        'source_url_fmt': 'http://www.hepforge.org/archive/softsusy/{0}',
        'source_filename': 'softsusy-3.3.1.tar.gz',
        'library': 'lib/libsoft.so',
        }

feynhiggs = {
        'version': '2.9.1',
        'source_url_fmt': 'http://wwwth.mpp.mpg.de/members/heinemey/feynhiggs/'
                          'newversion/{0}',
        'source_filename': 'FeynHiggs-2.9.1.tar.gz',
        'library': 'lib64/libFH.a'
        }

OPTIONS = {
        'basedir': os.getcwd(),
        'predictors': [ softsusy, feynhiggs ]
        }


root_flags = subprocess.check_output(['root-config','--cflags','--libs'])


def get_predictors(predictors):
    for predictor in predictors:
        filename = predictor['source_filename']
        local_path = '{dir}/{file}'.format(dir=tar_dir, file=filename)
        success = True
        try:
            with open(local_path) as f: pass
        except IOError as e:
            # file didn't exist better get it
            fn = predictor['source_filename']
            target = predictor['source_url_fmt'].format(fn)
            success = fetch_url(target, local_path)
        finally:
            if success:
                predictor['tar'] = local_path
            else:
                predictor['tar'] = None


def extract_predictors_source(predictors):
    for predictor in predictors:
        if predictor['tar'] is not None:
            predictor['source_dir'] = extract_tarfile(predictor['tar'], predictor_dir)

def compile_predictors(predictors):
    for predictor in predictors:

def main():
    predictors = OPTIONS['predictors']
    get_predictors(predictors)
    extract_predictors_source(predictors)
    compile_predictors(predictors)

if __name__=='__main__':
    main()
