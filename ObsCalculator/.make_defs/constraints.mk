src_dir=$(POINTAN_DIR)/cpp-constraints-classes
srcs=$(wildcard $(src_dir)/*cc)
lib=$(LIB_DIR)/libconstraints.a

interface_src=$(POINTAN_DIR)/interfaces/constraints.cc
interface_lib=$(LIB_DIR)/libmconstraints.so

cc=g++
ld=ar
ccflags= -fPIC -c -Wall
ldflags=rvs 
