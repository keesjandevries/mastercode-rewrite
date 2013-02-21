version=5.34.04
name=root_v$(version)
src_dir=$(UTIL_DIR)/root
lib_dir=$(LIB_DIR)
lib=$(INSTALL_DIR)/lib/libPyROOT.so
tar_name=$(name).source.tar.gz
remote=ftp://root.cern.ch/root/$(tar_name)
tarfile=$(TAR_DIR)/$(tar_name)
interface_src=$(STORAGE_DIR)/interfaces/ROOT.cc
interface_lib=$(LIB_DIR)/libmcROOT.so
interface_read_src=$(STORAGE_DIR)/interfaces/ROOT_read.cc
interface_read_lib=$(LIB_DIR)/libmcROOT_read.so
root_flags=$(shell $(INSTALL_DIR)/bin/root-config --cflags --libs )

cc=g++
#fc=gfortran
