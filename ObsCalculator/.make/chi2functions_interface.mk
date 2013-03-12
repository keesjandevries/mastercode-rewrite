include $(DEF_DIR)/chi2functions.mk

.PHONY: clean all

chi2functions_interface: $(interface_lib) $(interface_src)

interface_obj=$(interface_src:.cc=.o)

$(interface_lib): $(interface_obj) $(lib) $(constraints_lib)
	$(cc) -shared -Wl,-soname,libmcchi2functions.so -o $(interface_lib) \
		-Wl,-rpath,$(LIB_DIR) \
		$(interface_obj) -L$(LIB_DIR) -lchi2functions -lconstraints

$(interface_obj): $(interface_src)
	$(cc) -c -fPIC -o $(interface_obj) $(interface_src) \
		-I$(INCLUDE_DIR)

$(lib) : $(srcs) $(src_dir)/*h 
	$(MAKE) -f $(MAKE_DIR)/.make/$(name).mk

clean:
	-rm -f $(interface_obj) $(interface_lib)
