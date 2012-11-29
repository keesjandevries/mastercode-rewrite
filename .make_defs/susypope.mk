version=0.1
name=SUSY-POPE-$(version)
src_dir=$(PREDICTOR_DIR)/private/$(name)
lib_dir=$(src_dir)
lib=$(lib_dir)/libAMWObs.a
lib_short=AMWObs
interface_src=$(INTERFACE_DIR)/susypope.cc
interface_lib=$(LIB_DIR)/libmcsusypope.so

cc=g++
