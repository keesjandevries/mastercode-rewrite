include $(DEF_DIR)/susypope.mk

$(lib):
ifeq ($(wildcard $(src_dir)),)
	git submodule init
	git submodule update
endif
	$(MAKE) -C $(src_dir)

susypope: $(lib)

.PHONY: clean all
clean:
	-$(MAKE) -C $(src_dir) clean
	-rm -f $(lib)
