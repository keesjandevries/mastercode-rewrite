version=2.2
name=SLHALib-$(version)
src_dir=$(name)
lib=$(src_dir)/build/libSLHA.a
tar_name=$(name).tar.gz
remote=http://www.feynarts.de/slha/$(tar_name)
tarfile=$(TAR_src_dir)/$(tar_name)

$(lib):
ifeq ($(wildcard $(tarfile)),)
	wget -N -P $(TAR_src_dir) $(remote)
endif
ifeq ($(wildcard $(src_dir)),)
	tar -xf $(tarfile)
endif
	cd $(src_dir); \
		./configure --prefix=$(INSTALL_src_dir);
		#sed -i 's:ln -s:\\\n\t\t-&:' makefile
	$(MAKE) -C $(src_dir)
	$(MAKE) -C $(src_dir) install

target: $(lib)

.PHONY: clean all
clean:
	$(MAKE) -C $(src_dir) clean
	-rm -f $(tarfile)
	-rm -rf $(src_dir)
