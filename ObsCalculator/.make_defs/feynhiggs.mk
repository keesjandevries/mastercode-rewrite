version=2.8.6
#version=2.8.7
#version=2.9.5
#version=2.9.5.r3456v3
name=FeynHiggs-$(version)
src_dir=$(PREDICTOR_DIR)/$(name)
machine=$(shell uname -m)
ifeq ($(machine), x86_64)
	machine_lib_dir=lib64
else
	machine_lib_dir=lib
endif
lib_dir=$(INSTALL_DIR)/$(machine_lib_dir)
lib_short=FH$(version)
lib=$(lib_dir)/lib$(lib_short).a
#tar_name=$(name).tar
tar_name=$(name).tar.gz
remote_url=http://wwwth.mpp.mpg.de/members/heinemey/feynhiggs/newversion/
remote=$(remote_url)/$(tar_name)
tarfile=$(TAR_DIR)/$(tar_name)
interface_src=$(INTERFACE_DIR)/feynhiggs$(version).cc
interface_lib=$(LIB_DIR)/libmcfeynhiggs$(version).so

cc=g++
