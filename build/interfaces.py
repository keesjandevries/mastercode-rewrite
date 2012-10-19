import os
import subprocess
from build import predictors
from build import utils

softsusy = {
        'name': 'softsusy',
        'requires': [predictors.softsusy]
        }

softsusy_slha = {
        'name': 'softsusy_slha',
        'requires': [predictors.softsusy, utils.slha_class]
        }

feynhiggs = {
        'name': 'feynhiggs',
        'requires': [predictors.feynhiggs],
        }

slha = {
        'name': 'slha',
        'requires': [utils.slha_class],
        }

INTERFACES = [ softsusy, feynhiggs, slha, softsusy_slha ]

src_dir = 'interfaces'
object_dir = 'obj'
lib_dir = 'libs'
rpath = 'packages/lib'

compiler=['g++']
compile_opts = ['-c', '-fPIC']
lib_build_opts = ['-Wl', '-shared']

def get_include_options(interface):
    includes = [ '-I{0}/{1}'.format(r['installed_dir'], r['src_dir'])
        for r in interface.get('requires',[]) ]
    return includes

def get_library_link_options(interface):
    # this crazyness below:
    # have have 'some/dir/structure/libSOMETHING.so' and we want SOMETHING
    #            ^                 ^   ^       ^
    #            |_________________|   |_______|
    #                          {1}_|           |
    #                                      {2}_|
    links = ['-L{0}/{1} -l{2}'.format(r['installed_dir'], r['lib_dir'],
        r['library'].rpartition('.')[0][3:])
        for r in interface.get('requires',[])]
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
        links = get_library_link_options(interface)
        command = base_command+src_files+includes+links
        subprocess.check_output(command,
                stderr=subprocess.STDOUT)

def compile_libraries(interfaces):
    for interface in interfaces:
        name = interface['name'].lower()
        soname = 'libmc{0}.so'.format(name)
        soname_opt = ['-Wl,-soname,{0}'.format(soname)]
        rpath_opts = get_rpath_options(interface)
        output =  ['-o', '{0}/{1}'.format(lib_dir, soname)]
        obj_input = ['{0}/{1}.o'.format(object_dir, name)]
        links = get_library_link_options(interface)
        command = compiler + lib_build_opts + rpath_opts + output + \
                obj_input + links
        subprocess.check_output(command, stderr=subprocess.STDOUT)

def compile(base_dir):
    compile_objects(INTERFACES)
    compile_libraries(INTERFACES)

#function compile_softsusy_interfaces {
    #g++ -c -fPIC -o obj/softsusy.o interfaces/softsusy.cc \
        #-I${MAINDIR}/packages/include/softsusy/ \
        #-L${MAINDIR}/packages/lib -lsoft
    #g++ -shared -Wl,-soname,libmcsoftsusy.so \
        #-Wl,-rpath,${MAINDIR}/packages/lib -o libs/libmcsoftsusy.so \
       #obj/softsusy.o -L${MAINDIR}/packages/lib -lsoft
#}

#function compile_slha_interfaces {
    #g++ -c -fPIC -o obj/slha.o interfaces/slha.cc \
        #-I${MAINDIR}/SLHA/inc/ -L${MAINDIR}/SLHA/libs -lSLHAfile \
        #${RFLAGS}
    #g++ -shared -Wl,-soname,libmcslha.so \
        #-Wl,-rpath,${MAINDIR}/SLHA/libs -o libs/libmcslha.so \
        #obj/slha.o -L${MAINDIR}/SLHA/libs -lSLHAfile \
        #${RFLAGS}
#}


#function compile_joint_interfaces {
    #g++ -c -fPIC -o obj/softsusy_slha.o interfaces/softsusy_slha.cc \
        #-I${MAINDIR}/SLHA/inc/ -L${MAINDIR}/SLHA/libs -lSLHAfile \
        #-I${MAINDIR}/packages/include/softsusy \
        #-L${MAINDIR}/packages/lib -lsoft \
        #${RFLAGS}

    #g++ -shared -Wl,-soname,libmcsoftsusyslha.so \
        #-Wl,-rpath,${MAINDIR}/SLHA/libs:${MAINDIR}/packages/lib  \
        #-o libs/libmcsoftsusyslha.so obj/softsusy_slha.o \
        #-L${MAINDIR}/SLHA/libs -lSLHAfile -L${MAINDIR}/packages/lib -lsoft \
        #${RFLAGS}
#}


#function compile_feynhiggs_interfaces {
    #g++ -c -fPIC -o obj/feynhiggs.o interfaces/feynhiggs.cc \
        #-I${MAINDIR}/packages/include/ -L${MAINDIR}/packages/lib64 -lFH \
         #-lgfortran
    #g++ -shared -Wl,-soname,libmcfeynhiggs.so -o libs/libmcfeynhiggs.so \
        #obj/feynhiggs.o -L${MAINDIR}/packages/lib64 -lFH \
        #-lgfortran
#}
