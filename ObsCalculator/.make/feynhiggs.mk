include $(DEF_DIR)/feynhiggs.mk

$(lib):
ifeq ($(wildcard $(tarfile)),)
	wget -N -P $(TAR_DIR) $(remote)
endif
ifeq ($(wildcard $(src_dir)),)
	tar -C $(PREDICTOR_DIR) -xf $(tarfile)
endif
	cd $(PREDICTOR_DIR);\
   		patch -N -p1 < $(PATCH_DIR)/$(name).patch
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
