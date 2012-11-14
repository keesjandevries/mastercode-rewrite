include $(DEF_DIR)/slhalib.mk

$(lib):
ifeq ($(wildcard $(tarfile)),)
	wget -N -P $(TAR_DIR) $(remote)
endif
ifeq ($(wildcard $(src_dir)),)
	tar -xf $(tarfile)
endif
	cd $(src_dir); \
		./configure --prefix=$(INSTALL_DIR);
	$(MAKE) -C $(src_dir)
	$(MAKE) -C $(src_dir) install

slhalib: $(lib)

.PHONY: clean all
clean:
	$(MAKE) -C $(src_dir) clean

tarclean:
	-rm -f $(tarfile)
	-rm -rf $(src_dir)
