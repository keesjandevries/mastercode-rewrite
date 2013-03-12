include $(DEF_DIR)/constraints.mk

.PHONY: clean all

constraints_interface: $(interface_lib) $(interface_src)

interface_obj=$(interface_src:.cc=.o)

$(interface_lib): $(interface_obj)
	$(cc) -shared -Wl,-soname,libmcconstraints.so -o $(interface_lib) \
		-Wl,-rpath,$(LIB_DIR) \
		$(interface_obj) -L$(LIB_DIR) -lconstraints

$(interface_obj): $(interface_src)
	$(cc) -c -fPIC -o $(interface_obj) $(interface_src) \
		-I$(INCLUDE_DIR)

clean:
	-rm -f $(interface_obj) $(interface_lib)
