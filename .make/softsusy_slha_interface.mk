include $(DEF_DIR)/slhaclass.mk
slhaclass_src_dir:=$(src_dir)
slhaclass_lib_dir:=$(lib_dir)
slhaclass_lib_short:=$(lib_short)
include $(DEF_DIR)/softsusy.mk
softsusy_src_dir:=$(src_dir)
softsusy_lib_dir:=$(lib_dir)
softsusy_lib_short:=$(lib_short)

.PHONY: clean all

interface_src=$(INTERFACE_DIR)/softsusy_slha.cc
interface_lib=$(LIB_DIR)/libmcsoftsusy_slha.so

softsusy_slha_interface: $(interface_lib)

interface_obj=$(interface_src:.cc=.o)

$(interface_lib): $(interface_obj)
	$(cc) -shared -Wl,-soname,libmcsoftsusy_slha.so \
		-o $(interface_lib) \
		-Wl,-rpath,$(slhaclass_src_dir)/libs:$(LIB_DIR) \
		$(INTERFACE_DIR)/softsusy_slha.o \
		-L$(slhaclass_lib_dir) -l$(slhaclass_lib_short) \
		-L$(softsusy_lib_dir) -l$(slhaclass_lib_short)

$(interface_obj):
	$(cc) -c -fPIC -o $(INTERFACE_DIR)/softsusy_slha.o \
		$(INTERFACE_DIR)/softsusy_slha.cc \
		-I$(slhaclass_src_dir)/inc \
		-I$(INCLUDE_DIR)/softsusy

clean:
	-rm -f $(interface_obj) $(interface_lib)


