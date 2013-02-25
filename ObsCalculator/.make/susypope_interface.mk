include $(DEF_DIR)/susypope.mk

.PHONY: clean all

susypope_interface: $(interface_lib) $(interface_src)

interface_obj=$(interface_src:.cc=.o)

$(interface_lib):  $(lib) $(interface_obj) $(interface_lib)
	$(cc) -shared -Wl,-soname,libmcsusypope.so -o $(interface_lib) \
		-Wl,-rpath,$(LIB_DIR):$(lib_dir) \
		$(interface_obj) -L$(lib_dir) -l$(lib_short) -L$(LIB_DIR) -lSLHA \
		-lgfortran

$(interface_obj): $(lib) $(interface_src)
	$(cc) -c -fPIC -o $(interface_obj) $(interface_src) \
		-I$(INCLUDE_DIR)/SLHALib

clean:
	-rm -f $(interface_obj) $(interface_lib)
