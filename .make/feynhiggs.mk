include $(DEF_DIR)/feynhiggs.mk

$(lib):
ifeq ($(wildcard $(tarfile)),)
	wget -N -P $(TAR_DIR) $(remote)
endif
ifeq ($(wildcard $(src_dir)),)
	tar -xf $(tarfile)
endif
	-patch -N -p2 -i $(PATCH_DIR)/FeynHiggs.patch
	cd $(src_dir); \
		./configure --prefix=$(INSTALL_DIR);
	$(MAKE) -C $(src_dir)
	$(MAKE) -C $(src_dir) install

fennhiggs: $(lib)

.PHONY: clean all
clean:
	-$(MAKE) -C $(src_dir) clean
	-rm -f $(lib)

tarclean:
	-rm -f $(tarfile)
	-rm -rf $(src_dir)
