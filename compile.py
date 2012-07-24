#! /usr/bin/env python
import os
import subprocess
from modules.utils import fetch_url, extract_tarfile

prefix_dir = 'packages'
tar_dir = 'tars'
predictor_dir = 'predictors'

softsusy = {
        'name': 'SoftSUSY',
        'version': '3.3.1',
        'source_url_fmt': 'http://www.hepforge.org/archive/softsusy/{0}',
        'source_filename': 'softsusy-3.3.1.tar.gz',
        'library': 'lib/libsoft.so',
        }

feynhiggs = {
        'name': 'FeynHiggs',
        'version': '2.9.1',
        'source_url_fmt': 'http://wwwth.mpp.mpg.de/members/heinemey/feynhiggs/'
                          'newversion/{0}',
        'source_filename': 'FeynHiggs-2.9.1.tar.gz',
        'library': 'lib64/libFH.a',
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

def compile_predictors(predictors, base_dir):
    for predictor in predictors:
        try:
            conf_dir = '{bd}/{pd}/'.format(bd=base_dir,
                pd=predictor['source_dir'])
            conf_file = '{cd}/configure'.format(cd=conf_dir)
            with open(conf_file) as f: pass
            print("Configuring {0} ...".format(predictor['name']))
            prefix_str = '--prefix={bd}/{pd}'.format(bd=base_dir,
                pd=prefix_dir)
            os.chdir(conf_dir)
            subprocess.check_output([conf_file, prefix_str],
                    stderr=subprocess.STDOUT)
            os.chdir(base_dir)
            print("  --> Done")
        except IOError as e:
            print("No config file present for {0}".format(predictor['name']))

def main():
    predictors = OPTIONS['predictors']
    base_dir = OPTIONS['basedir']
    get_predictors(predictors)
    extract_predictors_source(predictors)
    compile_predictors(predictors, base_dir)

if __name__=='__main__':
    main()
