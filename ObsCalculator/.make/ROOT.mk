include $(DEF_DIR)/ROOT.mk


ROOT :
ifeq ($(wildcard $(tarfile)),)
	wget -N -P $(TAR_DIR) $(remote)
endif
ifeq ($(wildcard $(src_dir)),)
	tar -C $(UTIL_DIR) -xf $(tarfile)
endif
	cd $(src_dir); \
		./configure --prefix=$(INSTALL_DIR)   \
		--etcdir=$(INSTALL_DIR) 
	$(MAKE) -C $(src_dir)
	$(MAKE) -C $(src_dir) install

.PHONY: clean all
clean:
	$(MAKE) -C $(src_dir) clean

tarclean:
	-rm -f $(tarfile)
	-rm -rf $(src_dir)
