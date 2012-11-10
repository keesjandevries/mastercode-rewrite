version=2.9.4
name=FeynHiggs-$(version)
src_dir=$(name)
machine=$(shell uname -m)
ifeq ($(machine), x86_64)
	lib_dir=lib64
else
	lib_dir=lib
endif
lib=$(INSTALL_DIR)/$(lib_dir)/libFH.a
tar_name=$(name).tar.gz
remote_url=http://wwwth.mpp.mpg.de/members/heinemey/feynhiggs/newversion/
remote=$(remote_url)/$(tar_name)
tarfile=$(TAR_DIR)/$(tar_name)

$(lib):
	echo $(machine)
	echo $(lib_dir)
ifeq ($(wildcard $(tarfile)),)
	wget -N -P $(TAR_DIR) $(remote)
endif
ifeq ($(wildcard $(src_dir)),)
	tar -xf $(tarfile)
endif
	patch -N -p2 -i $(PATCH_DIR)/FeynHiggs.patch
	cd $(src_dir); \
		./configure --prefix=$(INSTALL_DIR);
	$(MAKE) -C $(src_dir)
	$(MAKE) -C $(src_dir) install

fennhiggs: $(lib)

.PHONY: clean all
clean:
	-$(MAKE) -C $(src_dir) clean
	-rm -f $(tarfile)
	-rm -rf $(src_dir)
	-rm -f $(lib)
