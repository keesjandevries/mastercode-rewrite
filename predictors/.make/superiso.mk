version=3.3
name=superiso_v$(version)
src_dir=$(name)
machine=$(shell uname -m)
lib=$(src_dir)/src/libisospin.a
tar_name=$(name).tgz
remote_url=http://superiso.in2p3.fr/download/
remote=$(remote_url)/$(tar_name)
tarfile=$(TAR_DIR)/$(tar_name)

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
