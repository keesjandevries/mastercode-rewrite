include $(DEF_DIR)/micromegas.mk

$(lib):
ifeq ($(wildcard $(tarfile)),)
	wget -N -P $(TAR_DIR) $(remote)
endif
ifeq ($(wildcard $(src_dir)),)
	tar -xf $(tarfile)
endif
	$(MAKE) -C $(src_dir)
	$(MAKE) -C $(src_dir)/MSSM

micromegas: $(lib)

.PHONY: clean all

clean:
	$(MAKE) -C $(src_dir)/MSSM clean
	$(MAKE) -C $(src_dir) clean
	-rm -f $(lib)

tarclean:
	-rm -f $(tarfile)
	-rm -rf $(src_dir)
