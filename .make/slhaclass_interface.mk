include $(DEF_DIR)/slhaclass.mk

.PHONY: clean all

slhaclass_interface: $(interface_lib)

interface_obj=$(interface_src:.cc=.o)

$(interface_lib): $(interface_obj)
	$(cc) -shared -Wl,-soname,libmcslhaclass.so \
		-Wl,-rpath,$(src_dir)/libs \
		-o $(interface_lib) \
		$(interface_obj) -L$(lib)

$(interface_obj):
	$(cc) -c -fPIC -o $(interface_obj) $(interface_src) \
		-I$(src_dir)/inc

clean:
	-rm -f $(interface_obj) $(interface_lib)
