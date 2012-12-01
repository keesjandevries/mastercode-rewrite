version=1.0
name=lspscat
src_dir=$(PREDICTOR_DIR)/private/$(name)
obj=$(src_dir)/lspscat8o.o
interface_src=$(INTERFACE_DIR)/lspscat.cc
interface_lib=$(LIB_DIR)/libmclspscat.so

cc=g++
FC=gfortran
FFLAGS=-fPIC -ffixed-line-length-none -m32
