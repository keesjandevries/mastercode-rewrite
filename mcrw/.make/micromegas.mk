include $(DEF_DIR)/micromegas.mk

micromegas: $(mssm_lib)

$(lib):
ifeq ($(wildcard $(tarfile)),)
	wget -N -P $(TAR_DIR) $(remote)
endif
ifeq ($(wildcard $(src_dir)),)
	tar -C $(PREDICTOR_DIR) -xf $(tarfile)
endif
	$(MAKE) -C $(src_dir)

$(mssm_lib): $(lib)
	$(MAKE) -C $(src_dir)/MSSM


.PHONY: clean all

clean:
	$(MAKE) -C $(src_dir)/MSSM clean
	$(MAKE) -C $(src_dir) clean
	-rm -f $(lib)

tarclean:
	-rm -f $(tarfile)
	-rm -rf $(src_dir)
