include $(DEF_DIR)/slhaclass.mk

$(lib):
	$(MAKE) -C $(src_dir)

slhaclass: $(lib)

.PHONY: clean all
clean:
	$(MAKE) -C $(src_dir) clean
