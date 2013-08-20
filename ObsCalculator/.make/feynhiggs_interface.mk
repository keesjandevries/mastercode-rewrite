include $(DEF_DIR)/feynhiggs.mk

.PHONY: clean all

feynhiggs_interface: $(interface_lib) $(interface_src) 

interface_obj=$(interface_src:.cc=.o)

$(interface_lib): $(interface_obj) $(lib)
	$(cc) -g -shared -Wl,-soname,$(interface_lib) -o $(interface_lib) \
		-Wl,-rpath,$(LIB_DIR) \
		$(interface_obj) -L$(lib_dir) -l$(lib_short) -lgfortran -lm

$(interface_obj): $(interface_src)
	$(cc) -g -c -fPIC -o $(interface_obj) $(interface_src) \
		-I$(INCLUDE_DIR)

clean:
	-rm -f $(interface_obj) $(interface_lib)
