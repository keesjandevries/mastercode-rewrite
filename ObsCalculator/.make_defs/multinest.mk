version=2.18
name=MultiNest_v$(version)
src_dir=$(PREDICTOR_DIR)/private/$(name)
lib_dir=$(src_dir)
lib_name=libnest3.a
lib=$(lib_dir)/$(lib_name)
lib_short=nest3
interface_dir=$(SAMPLE_DIR)/interfaces
interface_src=$(interface_dir)/multinest.c
interface_lib=$(LIB_DIR)/libmcmultinest.so

cc=g++
fc=gfortran
