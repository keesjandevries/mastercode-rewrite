include $(DEF_DIR)/slhalib.mk

.PHONY: clean all

slhalib_interface: $(interface_lib) $(interface_src)

interface_obj=$(interface_src:.cc=.o)

$(interface_lib): $(interface_obj)
	$(cc) -shared -Wl,-soname,libmcslhalib.so -o $(interface_lib) \
		-Wl,-rpath,$(LIB_DIR) \
		$(interface_obj) -L$(lib_dir) -l$(lib_short) -lgfortran

$(interface_obj): $(interface_src)
	$(cc) -c -fPIC -o $(interface_obj) $(interface_src) \
		-I$(INCLUDE_DIR)/SLHALib

clean:
	-rm -f $(interface_obj) $(interface_lib)
