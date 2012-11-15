include $(DEF_DIR)/softsusy.mk

.PHONY: clean all

fennhiggs_interface: $(interface_lib)

interface_obj=$(interface_src:.cc=.o)

$(interface_lib): $(interface_obj)
	$(cc) -shared -Wl,-soname,libmcsoftsusy.so -o $(interface_lib) \
		-Wl,-rpath,$(LIB_DIR) \
		$(interface_obj) -L$(lib)

$(interface_obj):
	$(cc) -c -fPIC -o $(interface_obj) $(interface_src) \
		-I$(INCLUDE_DIR)/softsusy

clean:
	-rm -f $(interface_obj) $(interface_lib)
