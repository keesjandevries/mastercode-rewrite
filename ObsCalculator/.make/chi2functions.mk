include $(DEF_DIR)/chi2functions.mk

objs=$(srcs:%.cc=%.o)

chi2functions: $(lib)  
	cp $(src_dir)/*h $(INCLUDE_DIR)

#FIXME: should this library be linked against the constraints library..
$(lib)	: $(objs)
	$(ld) $(ldflags)  $(lib) $^ 

#FIXME: I don't understand why %.o makes sure the right directories are checked
# This does seem to work though..
#FIXME: really need to think whether this is the proper way of handling the dependencies
%.o : %.cc %.h  $(constraints_dir)/*.h
	$(cc) -c -fPIC -Wall  -o $@ $< -I$(src_dir) -I$(constraints_dir)

.PHONY: clean all
clean:
	-rm -f $(objs)
