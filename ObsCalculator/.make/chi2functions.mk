include $(DEF_DIR)/chi2functions.mk

objs=$(srcs:%.cc=%.o)

chi2functions: $(lib)  $(src_dir)/*h
	cp $(src_dir)/*h $(INCLUDE_DIR)

$(lib)	: $(objs)
	$(ld) $(ldflags)  $(lib) $^ 

#FIXME: I don't understand why %.o makes sure the right directories are checked
# This does seem to work though..
%.o : %.cc 
	$(cc) -c -fPIC  -o $@ $< -I$(src_dir) -I$(INCLUDE_DIR)

.PHONY: clean all
clean:
	-rm -f $(objs)
