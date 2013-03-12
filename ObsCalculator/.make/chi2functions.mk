include $(DEF_DIR)/constraints.mk

objs=$(srcs:%.cc=%.o)

constraints: $(lib)  $(src_dir)/*h

$(lib)	: $(objs)
	$(ld) $(ldflags)  $(lib) $^ 

#FIXME: I don't understand why %.o makes sure the right directories are checked
# This does seem to work though..
%.o : %.cc 
	$(cc) -c -fPIC  -o $@ $< -I$(src_dir)

.PHONY: clean all
clean:
	-rm -f $(objs)
