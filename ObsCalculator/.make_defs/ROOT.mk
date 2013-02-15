version=5.34.04
name=root_v$(version)
src_dir=$(UTIL_DIR)/root
lib_dir=$(LIB_DIR)
lib=$(INSTALL_DIR)/lib/libPyROOT.so
lib_short=SLHA
tar_name=$(name).source.tar.gz
remote=ftp://root.cern.ch/root/$(tar_name)
tarfile=$(TAR_DIR)/$(tar_name)
#interface_src=$(INTERFACE_DIR)/slhalib.cc
#interface_lib=$(LIB_DIR)/libmcslhalib.so

#cc=g++
#fc=gfortran
