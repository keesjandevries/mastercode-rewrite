include $(DEF_DIR)/feynhiggs.mk

fennhiggs_interface: $(interface_lib)

interface_obj=$(interface_file:.cc=.o)
interface_obj:
	$(cc) -c -fPIC -o $(interface_obj) $(interface_file) \
		-I$(INCLUDE_DIR)
	
$(interface_lib): $(interface_obj)
	$(cc) -shared -Wl,-soname,libmcfeynhiggs.so -o $(interface_lib) \
		$(interface_obj) -L$(lib) -lgfortran

.PHONY: clean all
clean:
	-rm -f $(interface_obj) $(interface_lib)
