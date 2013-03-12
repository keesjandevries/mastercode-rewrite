name=constraints
src_dir=$(POINTAN_DIR)/cpp-constraints-classes
srcs=$(wildcard $(src_dir)/*cc)
lib=$(LIB_DIR)/lib$(name).a

interface_src=$(POINTAN_DIR)/interfaces/$(name).cc
interface_lib=$(LIB_DIR)/libmc$(name).so

chi2functions_lib=$(LIB_DIR)/libchi2functions.a
chi2functions_scr_dif=$(USER_DIR)/chi2_functions
chi2functions_srcs=$(wildcard $(chi2functions_scr_dif)/*c)
chi2functions_incs=$(wildcard $(chi2functions_scr_dif)/*h)

cc=g++
ld=ar
ldflags=rvs 
