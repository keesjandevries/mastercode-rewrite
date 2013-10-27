include $(DEF_DIR)/softsusy.mk

$(lib) $(executable):
ifeq ($(wildcard $(tarfile)),)
	wget -N -P $(TAR_DIR) $(remote)
endif
ifeq ($(wildcard $(src_dir)),)
	tar -C $(PREDICTOR_DIR) -xf $(tarfile)
endif
	cd $(src_dir); \
   		patch -N -p1 < $(PATCH_DIR)/$(name).patch; \
		./configure --prefix=$(INSTALL_DIR);
	$(MAKE) -C $(src_dir)
	$(MAKE) -C $(src_dir) install
	mv $(bin_dir)/softpoint.x $(executable)

softsusy: $(lib)

.PHONY: clean all
clean:
	-$(MAKE) -C $(src_dir) clean
	-rm -f $(lib)

tarclean:
	-rm -f $(tarfile)
	-rm -rf $(src_dir)
