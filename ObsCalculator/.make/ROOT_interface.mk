include $(DEF_DIR)/ROOT.mk

.PHONY: clean all

ROOT_interface: $(interface_lib) $(interface_src)

interface_obj=$(interface_src:.cc=.o)

$(interface_lib): $(interface_obj)
	$(cc) -shared -Wl,-soname,$(interface_lib) -o $(interface_lib) \
		-Wl,-rpath,$(LIB_DIR) \
		$(interface_obj) $(root_flags)

$(interface_obj): $(interface_src)
	$(cc) -c -fPIC -o $(interface_obj) $(interface_src) \
		$(root_flags)


clean:
	-rm -f $(interface_obj) $(interface_lib)
