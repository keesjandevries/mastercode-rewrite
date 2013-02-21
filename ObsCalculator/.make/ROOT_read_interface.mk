include $(DEF_DIR)/ROOT.mk

.PHONY: clean all

ROOT_read_interface: $(interface_read_lib) $(interface_read_src)

interface_read_obj=$(interface_read_src:.cc=.o)

$(interface_read_lib): $(interface_read_obj)
	$(cc) -shared -Wl,-soname,$(interface_read_lib) -o $(interface_read_lib) \
		-Wl,-rpath,$(LIB_DIR) \
		$(interface_read_obj) $(root_flags)

$(interface_read_obj): $(interface_read_src)
	$(cc) -c -fPIC -o $(interface_read_obj) $(interface_read_src) \
		$(root_flags)


clean:
	-rm -f $(interface_read_obj) $(interface_read_lib)
