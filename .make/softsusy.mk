version=3.3.4
name=softsusy-$(version)
src_dir=$(name)
lib=$(INSTALL_DIR)/lib/libsoft.so
tar_name=$(name).tar.gz
remote_url=http://www.hepforge.org/archive/softsusy/
remote=$(remote_url)/$(tar_name)
tarfile=$(TAR_DIR)/$(tar_name)

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

softsusy: $(lib)

.PHONY: clean all
clean:
	-$(MAKE) -C $(src_dir) clean
	-rm -f $(lib)

tarclean:
	-rm -f $(tarfile)
	-rm -rf $(src_dir)
