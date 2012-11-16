version=2.2
name=SLHALib-$(version)
src_dir=$(UTIL_DIR)/$(name)
lib_dir=$(src_dir)/build
lib=$(src_dir)/build/libSLHA.a
lib_short=SLHA
tar_name=$(name).tar.gz
remote=http://www.feynarts.de/slha/$(tar_name)
tarfile=$(TAR_DIR)/$(tar_name)
interface_src=$(INTERFACE_DIR)/slhalib.cc
interface_lib=$(LIB_DIR)/libmcslhalib.so

cc=g++
