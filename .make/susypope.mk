include $(DEF_DIR)/susypope.mk

$(lib):
ifeq ($(wildcard $(src_dir)),)
	git submodule init
	git submodule update
endif
	-patch -N -p2 -i $(PATCH_DIR)/SUSY-POPE.patch
	$(MAKE) -C $(src_dir)

susypope: $(lib)

.PHONY: clean all
clean:
	-$(MAKE) -C $(src_dir) clean
	-rm -f $(lib)
