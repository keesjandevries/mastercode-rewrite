include $(DEF_DIR)/softsusy.mk

.PHONY: clean all

softsusy2_interface: $(interface_lib) $(interface_src)

interface_obj=$(interface_src:.cc=.o)

$(interface_lib): $(interface_obj) $(lib)
	$(cc) -shared -Wl,-soname,libmcsoftsusy.so -o $(interface_lib) \
		-Wl,-rpath,$(LIB_DIR) \
		$(interface_obj) -L$(lib_dir) -l$(lib_short)

$(interface_obj): $(interface_src)
	$(cc) -c -fPIC -o $(interface_obj) $(interface_src) \
		-I$(INCLUDE_DIR)/softsusy

clean:
	-rm -f $(interface_obj) $(interface_lib)
