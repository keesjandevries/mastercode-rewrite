include $(DEF_DIR)/superiso.mk
$(lib):
ifeq ($(wildcard $(tarfile)),)
	wget -N -P $(TAR_DIR) $(remote)
endif
ifeq ($(wildcard $(src_dir)),)
	tar -xf $(tarfile)
endif
	-patch -N -p2 -i $(PATCH_DIR)/SuperISO.patch
	$(MAKE) -C $(src_dir)

superiso: $(lib)

.PHONY: clean all
clean:
	-$(MAKE) -C $(src_dir) clean

tarclean:
	-rm -f $(tarfile)
	-rm -rf $(src_dir)
