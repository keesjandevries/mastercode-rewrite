import os
import subprocess
from build import predictors
from build import utils
#import shlex

softsusy = {
        'name': 'softsusy',
        'requires': [predictors.softsusy]
        }

softsusy_slha = {
        'name': 'softsusy_slha',
        'requires': [utils.slha_class, predictors.softsusy]
        }

feynhiggs = {
        'name': 'feynhiggs',
        'requires': [predictors.feynhiggs],
        'extra_link_opts': ['-lgfortran'],
        }

slha = {
        'name': 'slha',
        'requires': [utils.slha_class],
        }

micromegas = {
        'name': 'micromegas',
        'requires': [predictors.micromegas],
        'extra_link_opts': ['-ldl', '-lX11']
        }

INTERFACES = [ softsusy, slha, softsusy_slha, feynhiggs, micromegas ]

src_dir = 'interfaces'
object_dir = 'obj'
lib_dir = 'libs'
rpath = 'packages/lib'

compiler=['g++']
compile_opts = ['-c', '-fPIC']
lib_build_opts = ['-shared']

def get_include_options(interface):
    includes = []
    if 'requires' in interface:
        includes = ['-I{0}/{1}'.format(r['installed_dir'].format(
            v=r['version']), r['src_dir']) for r in interface['requires']]
    return includes

def get_library_link_options(interface):
    # this crazyness below:
    # have have 'some/dir/structure/libSOMETHING.so' and we want SOMETHING
    #            ^                 ^   ^       ^
    #            |_________________|   |_______|
    #                          {1}_|           |
    #                                      {2}_|
    links = []
    for r in interface.get('requires',[]):
        if 'library' in r:
            links += ['-L{0}/{1}'.format(r['installed_dir'], r['lib_dir']),
                    '-l{0}'.format(r['library'].rpartition('.')[0][3:])]
        links += ['{d}/{l}'.format(d=r['installed_dir'].format(v=r['version']),
                l=linkobj) for linkobj in r.get('manual_objects',[])]
    return links

def get_rpath_options(interface):
        opts = '-Wl,-rpath,'
        paths = []
        for req in interface.get('requires',[]):
            paths.append('{0}/{1}'.format(req['installed_dir'], req['lib_dir']))
        opts += ':'.join(paths)
        return [opts]

def compile_objects(interfaces):
    for interface in interfaces:
        name = interface['name'].lower()
        base_command = compiler + compile_opts + ['-o',
                '{0}/{1}.o'.format(object_dir, name)]
        src_files = [ '{0}/{1}.cc'.format(src_dir,name)]
        includes = get_include_options(interface)
        #links = get_library_link_options(interface)
        command = base_command+src_files+includes
        command += interface.get('extra_compile_opts',[])
        subprocess.check_call(command, stderr=subprocess.STDOUT)

def compile_libraries(interfaces):
    for interface in interfaces:
        name = interface['name'].lower()
        soname = 'libmc{0}.so'.format(name)
        soname_opt = ['-Wl,-soname,{0}'.format(soname)]
        rpath_opts = get_rpath_options(interface)
        output =  ['-o', '{0}/{1}'.format(lib_dir, soname)]
        obj_input = ['{0}/{1}.o'.format(object_dir, name)]
        links = get_library_link_options(interface)
        command = compiler + lib_build_opts + soname_opt + rpath_opts + \
                output + obj_input + links + \
                interface.get('extra_link_opts',[])

        subprocess.check_call(command, stderr=subprocess.STDOUT)

def compile(base_dir):
    print "Building interface objects ..."
    compile_objects(INTERFACES)
    print "  --> Done"
    print "Building interface libraries ..."
    compile_libraries(INTERFACES)
    print "  --> Done"
