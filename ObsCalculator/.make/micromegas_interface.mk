include $(DEF_DIR)/micromegas.mk

.PHONY: clean all

micromegas_interface: $(interface_bin) $(interface_src)

interface_obj=$(interface_src:.cc=.o)

$(interface_bin): $(interface_src)
	$(cc) -fsigned-char -Wall -fPIC  -o $(interface_bin) \
		$(interface_src) \
		-I$(inc)\
		$(libs)	

clean:
	-rm -f $(interface_obj) $(interface_bin)
