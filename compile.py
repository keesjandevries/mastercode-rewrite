#! /usr/bin/env python
import os
import subprocess
import urllib2

prefix_dir = 'packages'
tar_dir = 'tars'

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

interfaces = {}

OPTIONS = {
        'basedir': os.getcwd(),
        'predictors': [ softsusy, feynhiggs ]
        }


root_flags = subprocess.check_output(['root-config','--cflags','--libs'])

def get_predictor_source(predictor):
    target = predictor['source_url_fmt'].format(predictor['source_filename'])
    try:
        f = urllib2.urlopen(target)
        print("Downloading {0} ...".format(target))
        filename = predictor['source_filename']
        local_path = '{dir}/{file}'.format(dir=tar_dir, file=filename)
        local_file = open(local_path,'wb')
        local_file.write(f.read())
        local_file.close()
        print("  --> Done")
    except urllib2.HTTPError, e:
        print("HTTP Error:", e.code, target)
    except urllib2.URLError, e:
        print("URL Error:", e.reason, target)

def main():
    for predictor in OPTIONS['predictors']:
        get_predictor_source(predictor)

if __name__=='__main__':
    main()
