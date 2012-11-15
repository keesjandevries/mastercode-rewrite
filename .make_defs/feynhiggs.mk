version=2.9.4
name=FeynHiggs-$(version)
src_dir=$(PREDICTOR_DIR)/$(name)
machine=$(shell uname -m)
ifeq ($(machine), x86_64)
	lib_dir=lib64
else
	lib_dir=lib
endif
lib=$(INSTALL_DIR)/$(lib_dir)/libFH.a
interface_lib=$(INSTALL_DIR)/lib/libmcfeynhiggs.a
tar_name=$(name).tar.gz
remote_url=http://wwwth.mpp.mpg.de/members/heinemey/feynhiggs/newversion/
remote=$(remote_url)/$(tar_name)
tarfile=$(TAR_DIR)/$(tar_name)
interface_src=$(INTERFACE_DIR)/feynhiggs.cc
interface_lib=$(LIB_DIR)/libmcfeynhiggs.so

cc=g++
