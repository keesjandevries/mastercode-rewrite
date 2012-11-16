include $(DEF_DIR)/slhalib.mk

$(lib):
ifeq ($(wildcard $(tarfile)),)
	wget -N -P $(TAR_DIR) $(remote)
endif
ifeq ($(wildcard $(src_dir)),)
	tar -C $(UTIL_DIR) -xf $(tarfile)
endif
	-patch -N -p1 -i $(PATCH_DIR)/SLHALib.patch
	cd $(src_dir); \
		./configure --prefix=$(INSTALL_DIR) FC=gfortran;
	$(MAKE) -C $(src_dir)
	$(MAKE) -C $(src_dir) install

slhalib: $(lib)

.PHONY: clean all
clean:
	$(MAKE) -C $(src_dir) clean

tarclean:
	-rm -f $(tarfile)
	-rm -rf $(src_dir)
