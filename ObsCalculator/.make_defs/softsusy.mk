version=3.3.5
name=softsusy-$(version)
src_dir=$(PREDICTOR_DIR)/$(name)
lib_dir=$(INSTALL_DIR)/lib/
lib=$(lib_dir)/libsoft.so
lib_short=soft
tar_name=$(name).tar.gz
remote_url=http://www.hepforge.org/archive/softsusy/
remote=$(remote_url)/$(tar_name)
tarfile=$(TAR_DIR)/$(tar_name)
interface_src=$(INTERFACE_DIR)/softsusy.cc
interface_lib=$(LIB_DIR)/libmcsoftsusy.so

cc=g++
