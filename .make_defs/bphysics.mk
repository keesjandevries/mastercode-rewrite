version=1.0
name=bphysics
src_dir=$(PREDICTOR_DIR)/private/$(name)
obj=$(src_dir)/bphysics.o
interface_src=$(INTERFACE_DIR)/bphysics.cc
interface_lib=$(LIB_DIR)/libmcbphysics.so

cc=g++
fc=gfortran
fflags=-ffixed-line-length-none -I$(INCLUDE_DIR) -m32
