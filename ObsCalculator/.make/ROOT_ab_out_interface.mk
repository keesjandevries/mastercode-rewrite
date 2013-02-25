include $(DEF_DIR)/ROOT.mk

.PHONY: clean all

ROOT_ab_out_interface: $(interface_ab_out_lib) $(interface_ab_out_src)

interface_ab_out_obj=$(interface_ab_out_src:.cc=.o)

$(interface_ab_out_lib): $(interface_ab_out_obj)
	$(cc) -shared -Wl,-soname,$(interface_ab_out_lib) -o $(interface_ab_out_lib) \
		-Wl,-rpath,$(LIB_DIR) \
		$(interface_ab_out_obj) $(root_flags)

$(interface_ab_out_obj): $(interface_ab_out_src)
	$(cc) -c -fPIC -o $(interface_ab_out_obj) $(interface_ab_out_src) \
		$(root_flags)


clean:
	-rm -f $(interface_ab_out_obj) $(interface_ab_out_lib)
