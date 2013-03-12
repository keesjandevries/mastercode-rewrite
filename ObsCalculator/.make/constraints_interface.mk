include $(DEF_DIR)/constraints.mk


objs=$(srcs:%.cc=%.o)
interface_obj=$(interface_src:.cc=.o)

constraints_interface: $(interface_lib)  
#FIXME: want to make sure that dependencies ensure that the interface lib is recompiled 
# if the lib was recompiled. Not sure if this is completely functional, though it seems to be
$(interface_lib): $(interface_obj)  $(lib) $(chi2functions_lib)
	$(cc) -shared -Wall -Wl,-soname,libmcconstraints.so -o $(interface_lib) \
		-Wl,-rpath,$(LIB_DIR) \
		$(interface_obj) -L$(LIB_DIR)  -lchi2functions -lconstraints

$(interface_obj): $(interface_src)
	$(cc) -c -fPIC -o $(interface_obj) $(interface_src) \
		-I$(INCLUDE_DIR)

#FIXME: want to make sure that dependencies ensure that the interface lib is recompiled 
# if any changes are made in the source files.
# Not entirely sure if this is completely functional, though it seems to be
$(chi2functions_lib) : $(chi2functions_srcs) $(chi2functions_incs) $(lib)
	$(MAKE) -f $(MAKE_DIR)/.make/chi2functions.mk

$(lib) : $(srcs)  $(src_dir)/*h
	$(MAKE) -f $(MAKE_DIR)/.make/constraints.mk   



#FIXME: not sure if PHONY is needed here
.PHONY: clean all
clean:
	-rm -f $(interface_obj) $(interface_lib)
