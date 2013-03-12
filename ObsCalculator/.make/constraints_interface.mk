include $(DEF_DIR)/constraints.mk

.PHONY: clean all

objs=$(srcs:%.cc=%.o)

constraints_interface: $(interface_lib) $(interface_src)

interface_obj=$(interface_src:.cc=.o)

#FIXME: want to make sure that dependencies ensure that the interface lib is recompiled 
# if the lib was recompiled. Not sure if this is completely functional, though it seems to be
$(interface_lib): $(interface_obj)  $(lib)
	$(cc) -shared -Wl,-soname,libmcconstraints.so -o $(interface_lib) \
		-Wl,-rpath,$(LIB_DIR) \
		$(interface_obj) -L$(LIB_DIR) -lconstraints

$(interface_obj): $(interface_src)
	$(cc) -c -fPIC -o $(interface_obj) $(interface_src) \
		-I$(INCLUDE_DIR)

#FIXME: want to make sure that dependencies ensure that the interface lib is recompiled 
# if any changes are made in the source files.
# Not entirely sure if this is completely functional, though it seems to be
$(lib) : $(srcs)  $(src_dir)/*h
	$(MAKE) -f $(MAKE_DIR)/.make/constraints.mk   

clean:
	-rm -f $(interface_obj) $(interface_lib)
