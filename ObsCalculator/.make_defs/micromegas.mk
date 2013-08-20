#version=2.4.5
version=3.2
name=micromegas_$(version)
src_dir=$(PREDICTOR_DIR)/$(name)
inc=$(src_dir)/MSSM
lib=$(src_dir)/sources/micromegas.a
mssm_lib=$(src_dir)/MSSM/aLib.a
tar_name=$(name).tgz
remote_url=http://lapth.in2p3.fr/micromegas/downloadarea/code/
remote=$(remote_url)/$(tar_name)
tarfile=$(TAR_DIR)/$(tar_name)
interface_src=$(INTERFACE_DIR)/micromegas-$(version).c
interface_bin=$(BIN_DIR)/micromegas-$(version).x
ifeq ($(version),3.2)
libs=   $(src_dir)/MSSM/lib/aLib.a \
		$(src_dir)/sources/micromegas.a  \
		$(src_dir)/CalcHEP_src/lib/dynamic_me.a \
		$(src_dir)/sources/micromegas.a \
		$(src_dir)/MSSM/work/work_aux.a  \
		$(src_dir)/MSSM/lib/aLib.a   \
		$(src_dir)/CalcHEP_src/lib/sqme_aux.so \
		$(src_dir)/CalcHEP_src/lib/libSLHAplus.a \
		$(src_dir)/CalcHEP_src/lib/num_c.a \
		$(src_dir)/CalcHEP_src/lib/ntools.a   \
		$(src_dir)/CalcHEP_src/lib/serv.a \
		-lX11  -rdynamic -ldl   -lm
endif
ifeq ($(version),2.4.5) 
libs =	$(lib) \
        $(src_dir)/MSSM/lib/aLib.a \
        $(src_dir)/MSSM/work/work_aux.a \
        $(src_dir)/CalcHEP_src/lib/dynamic_me.a \
        $(src_dir)/CalcHEP_src/lib/libSLHAplus.a \
        $(src_dir)/CalcHEP_src/lib/num_c.a \
        $(src_dir)/CalcHEP_src/lib/serv.a \
        $(src_dir)/CalcHEP_src/lib/sqme_aux.so \
        -lX11  -rdynamic -ldl -lm
endif

cc=gcc
