version=2.2
name=SLHALib-$(version)
src_dir=$(name)
lib=$(src_dir)/build/libSLHA.a
tar_name=$(name).tar.gz
remote=http://www.feynarts.de/slha/$(tar_name)
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

slhalib: $(lib)

.PHONY: clean all
clean:
	$(MAKE) -C $(src_dir) clean

tarclean:
	-rm -f $(tarfile)
	-rm -rf $(src_dir)
