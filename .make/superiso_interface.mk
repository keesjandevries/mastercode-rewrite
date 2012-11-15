include $(DEF_DIR)/superiso.mk

.PHONY: clean all

superiso_interface: $(interface_lib)

interface_obj=$(interface_src:.cc=.o)

$(interface_lib): $(interface_obj)
	$(cc) -shared -Wl,-soname,libmcsuperiso.so -o $(interface_lib) \
		-Wl,-rpath,$(src_dir) \
		$(interface_obj) -L$(lib)

$(interface_obj):
	$(cc) -c -fPIC -o $(interface_obj) $(interface_src) \
		-I$(src_dir)/src

clean:
	-rm -f $(interface_obj) $(interface_lib)
