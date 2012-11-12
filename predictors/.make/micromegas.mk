version=2.4.5
name=micromegas_$(version)
src_dir=$(name)
lib=$(src_dir)/sources/micromegas.a
tar_name=$(name).tgz
remote_url=http://lapth.in2p3.fr/micromegas/downloadarea/code/
remote=$(remote_url)/$(tar_name)
tarfile=$(TAR_DIR)/$(tar_name)

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
