version=3.3
name=superiso_v$(version)
src_dir=$(PREDICTOR_DIR)/$(name)
machine=$(shell uname -m)
lib_dir=$(src_dir)/src
lib=$(lib_dir)/libisospin.a
lib_short=isospin
tar_name=$(name).tgz
remote_url=http://superiso.in2p3.fr/download/
remote=$(remote_url)/$(tar_name)
tarfile=$(TAR_DIR)/$(tar_name)
interface_src=$(INTERFACE_DIR)/superiso.cc
interface_lib=$(LIB_DIR)/libmcsuperiso.so

cc=g++
