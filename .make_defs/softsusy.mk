version=3.3.4
name=softsusy-$(version)
src_dir=$(PREDICTOR_DIR)/$(name)
lib=$(INSTALL_DIR)/lib/libsoft.so
tar_name=$(name).tar.gz
remote_url=http://www.hepforge.org/archive/softsusy/
remote=$(remote_url)/$(tar_name)
tarfile=$(TAR_DIR)/$(tar_name)
interface_src=$(INTERFACE_DIR)/softsusy.cc
interface_lib=$(LIB_DIR)/libmcsoftsusy.so

cc=g++
