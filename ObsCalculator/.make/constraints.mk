include $(DEF_DIR)/constraints.mk

objs=$(subst cc,o,$(srcs))

constraints: $(lib) $(src_dir)/*h
	cp $(src_dir)/*h $(INCLUDE_DIR)

$(lib)	:$(objs)
	$(ld) $(ldflags)  $(lib) $^ 

$(scr_dir)/%.o : $(src_dir)/%.cc $(src_dir)/*h
	$(cc) $(ccflags) -o $@ $< -I$(src_dir)

.PHONY: clean all
clean:
	-rm -f $(objs)
