include $(DEF_DIR)/multinest.mk

.PHONY: clean all

multinest_interface: $(interface_lib) $(interface_src)

interface_obj=$(interface_src:.c=.o)

# This used to be g++ maybe it will give errors
$(interface_lib): $(interface_obj)
	$(xx) -shared -Wl,-soname,libmcmultinest.so -o $(interface_lib) \
		-Wl,-rpath,$(lib_dir) \
		$(interface_obj) -L$(src_dir) -l$(lib_short) -lgfortran -llapack -lpthread

$(interface_obj): $(interface_src) $(lib)
	$(cc) -c -I. -DMULTINEST_CALL=__nested_MOD_nestrun \
		-O3 -std=c99 -Wall -Wextra -fPIC  -o $(interface_obj) $(interface_src) \
		-lgfortran 

clean:
	-rm -f $(interface_obj) $(interface_lib)
