#! /usr/bin/env python
import os
import subprocess
from modules.utils import fetch_url, extract_tarfile

prefix_dir = 'packages'
tar_dir = 'tars'
predictor_dir = 'predictors'
patch_dir = 'patches'

softsusy = {
        'name': 'SoftSUSY',
        'version': '3.3.4',
        'source_url_fmt': 'http://www.hepforge.org/archive/softsusy/{0}',
        'source_filename': 'softsusy-{v}.tar.gz',
        'library': 'libsoft.so',
        'installed_dir': prefix_dir,
        'lib_dir': 'lib',
        'src_dir': 'include/softsusy'
        }

feynhiggs = {
        'name': 'FeynHiggs',
        'version': '2.9.4',
        'source_url_fmt': 'http://wwwth.mpp.mpg.de/members/heinemey/feynhiggs/'
            'newversion/{0}',
        'source_filename': 'FeynHiggs-{v}.tar.gz',
        'library': 'libFH.a',
        'installed_dir': prefix_dir,
        'lib_dir': 'lib64',
        'src_dir': 'include'
        }

micromegas = {
        'name': 'Micromegas',
        'version': '2.4.5',
        'source_url_fmt': 'http://lapth.in2p3.fr/micromegas/downloadarea/code/'
            '{0}',
        'source_filename': 'micromegas_{v}.tgz',
        'installed_dir': 'predictors/micromegas_{v}',
        'lib_dir': '',
        'src_dir': '',
        'manual_objects': ['sources/micromegas.a', 'MSSM/lib/aLib.a',
            'MSSM/work/work_aux.a', 'CalcHEP_src/lib/dynamic_me.a',
            'CalcHEP_src/lib/libSLHAplus.a', 'CalcHEP_src/lib/num_c.a',
            'CalcHEP_src/lib/serv.a', 'CalcHEP_src/lib/sqme_aux.so'],
        'subdirs': ['MSSM'],
        }

PREDICTORS = [ softsusy, feynhiggs, micromegas ]


def fetch_predictors(predictors):
    for predictor in predictors:
        fn = predictor['source_filename'].format(v=predictor['version'])
        local_path = '{dir}/{file}'.format(dir=tar_dir, file=fn)
        success = True
        try:
            with open(local_path) as f: pass
        except IOError as e:
            # file didn't exist better get it
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
            predictor['source_dir'] = extract_tarfile(predictor['tar'],
                    predictor_dir)

def patch_predictors(predictors):
    for predictor in predictors:
        print "Patching {0} ...".format(predictor['name'])
        try:
            patch_file='{d}/{p}.patch'.format(d=patch_dir,p=predictor['name'])
            with open(patch_file) as f: pass
            subprocess.check_output(['patch','-N','-p','1','-i', patch_file],
                    stderr=subprocess.STDOUT)
            print(" --> Done")
        except IOError:
            print("  --> No patch file present for {0}".format(
                predictor['name']))
        except subprocess.CalledProcessError:
            print("  --> Already patched")


def configure_predictors(predictors, base_dir):
    for predictor in predictors:
        try:
            conf_dir = '{bd}/{pd}/'.format(bd=base_dir,
                pd=predictor['source_dir'])
            conf_file = '{cd}/configure'.format(cd=conf_dir)
            print("Configuring {0} ...".format(predictor['name']))
            with open(conf_file) as f: pass
            prefix_str = '--prefix={bd}/{pd}'.format(bd=base_dir,
                pd=prefix_dir)
            os.chdir(conf_dir)
            subprocess.check_output([conf_file, prefix_str],
                    stderr=subprocess.STDOUT)
            os.chdir(base_dir)
            print("  --> Done")
        except IOError as e:
            print("  --> No config file present for {0}".format(
                predictor['name']))

def compile_predictors(predictors, base_dir):
    for predictor in predictors:
        pred_src_dir = '{bd}/{pd}'.format(bd=base_dir,
                pd=predictor['source_dir'])
        os.chdir(pred_src_dir)
        print("Making {0} ...".format(predictor['name']))
        subprocess.check_output(['make'], stderr=subprocess.STDOUT)
        subprocess.call(['make', 'install'], stderr=subprocess.STDOUT,
                stdout=open(os.devnull,'w'))
        print("  --> Done")
        if 'subdirs' in  predictor:
            for sdir in predictor['subdirs']:
                print("Making {0}:{1} ...".format(predictor['name'], sdir))
                os.chdir(sdir)
                subprocess.check_output(['make'], stderr=subprocess.STDOUT)
                subprocess.call(['make', 'install'], stderr=subprocess.STDOUT,
                        stdout=open(os.devnull,'w'))
                os.chdir(pred_src_dir)
                print("  --> Done")
        os.chdir(base_dir)

def compile(base_dir):
    fetch_predictors(PREDICTORS)
    extract_predictors_source(PREDICTORS)
    patch_predictors(PREDICTORS)
    configure_predictors(PREDICTORS, base_dir)
    compile_predictors(PREDICTORS, base_dir)

if __name__=='__main__':
    compile(os.getcwd())
