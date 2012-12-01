include $(DEF_DIR)/bphysics.mk

.PHONY: clean all

bphysics_interface: $(interface_lib)

interface_obj=$(interface_src:.cc=.o)

$(interface_lib): $(interface_obj)
	$(cc) -m32 -shared -Wl,-soname,libmcbphysics.so -o $(interface_lib) \
		-Wl,-rpath,$(LIB_DIR) \
		$(interface_obj) $(obj) -L$(LIB_DIR) -lSLHA \
		-lgfortran

$(interface_obj):
	$(cc) -m32 -c -fPIC -o $(interface_obj) $(interface_src) \
		-I$(INCLUDE_DIR)/SLHALib

clean:
	-rm -f $(interface_obj) $(interface_lib)
