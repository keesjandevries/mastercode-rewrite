import os
import subprocess

slha_class = {
    'source_dir': 'utils/{n}',
    'name': 'SLHA',
    'installable': False,
    'library': 'libSLHAfile.so',
    'installed_dir': 'utils/SLHA',
    'src_dir': 'inc',
    'lib_dir': 'libs',
    'version': '0.1',
    }

slhalib = {
    'source_dir': 'utils/{n}-{v}',
    'name': 'SLHALib',
    'library': 'libSLHA.a',
    'installed_dir': 'packages',
    'src_dir': 'include',
    'lib_dir': 'lib',
    'version': '2.2',
    }

UTILS = [slha_class, slhalib]


def compile(base_dir):
    for util in UTILS:
        udir = util['source_dir'].format(n=util['name'], v=util['version'])
        os.chdir('{bd}/{ud}'.format(bd=base_dir, ud=udir))
        try:
            conf_file = 'configure'
            print("Configuring {0} ...".format(util['name']))
            with open('configure') as f: pass
            prefix_str = '--prefix={bd}/{pd}'.format(bd=base_dir,
                pd=util['installed_dir'])
            subprocess.check_output([conf_file, prefix_str],
                    stderr=subprocess.STDOUT)
            print("  --> Done")
        except IOError as e:
            print("  --> No config file present for {0}".format(
                util['name']))
        print("Making {0} ...".format(util['name']))
        subprocess.check_output(['make'], stderr=subprocess.STDOUT)
        print("  --> Done")
        if util.get('installable', False):
            print("Installing {0} ...".format(util['name']))
            subprocess.check_output(['make', 'install'],
                    stderr=subprocess.STDOUT)
            print("  --> Done")
        os.chdir(base_dir)


if __name__=='__main__':
    compile(os.getcwd())
