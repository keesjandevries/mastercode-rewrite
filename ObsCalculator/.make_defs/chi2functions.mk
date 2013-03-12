name=chi2functions
src_dir=$(USER_DIR)/chi2_functions
srcs=$(wildcard $(src_dir)/*cc)
lib=$(LIB_DIR)/lib$(name).a

interface_src=$(POINTAN_DIR)/interfaces/$(name).cc
interface_lib=$(LIB_DIR)/libmc$(name).so

constraints_dir=$(POINTAN_DIR)/cpp-constraints-classes

cc=g++
ld=ar
ldflags=rvs 
