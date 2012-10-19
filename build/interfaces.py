import os
import subprocess
from build import predictors
from build import utils

root_cflags = subprocess.check_output(['root-config', '--cflags',
    '--libs']).split()

softsusy_slha = {
    'name': 'softsusy_slha',
    'requires': [predictors.softsusy, utils.slha_class],
    'ROOT': True,
    }

#INTERFACES = [ softsusy, slha, softsusy_slha, feynhiggs ]
INTERFACES = [ softsusy_slha ]

src_dir = 'interfaces'
object_dir = 'obj'
output_lib_dir = 'libs'
rpath = 'packages/lib'

compiler='g++'
compile_opts = ['-c', '-fPIC']
lib_build_opts = ['-shared']


def construct_object_compile_commands(interfaces):
    commands = []
    for interface in interfaces:
        name = interface['name'].lower()
        base_command = [compiler] + compile_opts + ['-o',
                '{0}/{1}.o'.format(object_dir, name)]
        src_files = [ '{0}/{1}.cc'.format(src_dir,name)]
        includes = [ '-I{0}/{1}'.format(r['installed_dir'], r['src_dir'])
            for r in interface['requires'] ]
        # this crazyness below:
        # have have 'some/dir/structure/libSOMETHING.so' and we want SOMETHING
        #            ^                 ^   ^       ^
        #            |_________________|   |_______|
        #                          {1}_|           |
        #                                      {2}_|
        links = ['-L{0}/{1} -l{2}'.format(r['installed_dir'], r['lib_dir'],
            r['library'].rpartition('.')[0][3:]) for r in interface['requires']]
        command = base_command+src_files+includes+links
        if interface.get('ROOT',False):
            command += root_cflags
        subprocess.check_output(command,
                stderr=subprocess.STDOUT)

def compile(base_dir):
    construct_object_compile_commands(INTERFACES)




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
