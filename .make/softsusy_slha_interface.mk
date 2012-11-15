include $(DEF_DIR)/slhaclass.mk
slhaclass_src_dir:=$(src_dir)
slhaclass_lib:=$(lib)
include $(DEF_DIR)/softsusy.mk
softsusy_src_dir:=$(src_dir)
softsusy_lib:=$(lib)

.PHONY: clean all

interface_src=$(INTERFACE_DIR)/softsusy_slha.cc
interface_lib=$(LIB_DIR)/libmcsoftsusy_slha.so

softsusy_slha_interface: $(interface_lib)

interface_obj=$(interface_src:.cc=.o)

$(interface_lib): $(interface_obj)
	$(cc) -shared -Wl,-soname,libmcsoftsusy_slha.so \
		-o $(interface_lib)
		-Wl,-rpath,$(slhaclass_src_dir)/libs:$(LIB_DIR) \
		obj/softsusy_slha.o \
		-L$(slhaclass_lib) \
		-L$(softsusy_lib)

$(interface_obj):
	$(cc) -c -fPIC -o $(INTERFACE_DIR)/softsusy_slha.o \
		$(INTERFACE_DIR)/softsusy_slha.cc \
		-I$(slhaclass_src_dir)/inc \
		-I$(INCLUDE_DIR)/softsusy

clean:
	-rm -f $(interface_obj) $(interface_lib)


