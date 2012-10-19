import os
import subprocess

slha_class = {
    'source_dir': 'SLHA',
    'name': 'SLHA',
    'installable': False,
    'library': 'SLHA/libs/libSLHAfile.so',
    }

UTILS = [ slha_class ]


def compile(base_dir):
    for util in UTILS:
        os.chdir('{bd}/{ud}'.format(bd=base_dir, ud=util['source_dir']))
        print("Making {0} ...".format(util['name']))
        subprocess.check_output(['make'], stderr=subprocess.STDOUT)
        if util.get('installable', False):
            subprocess.check_output(['make', 'install'],
                    stderr=subprocess.STDOUT)
        os.chdir(base_dir)
        print("  --> Done")


if __name__=='__main__':
    compile(os.getcwd())
