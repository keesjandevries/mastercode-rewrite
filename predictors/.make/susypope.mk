version=0.1
name=SUSY-POPE-$(version)
src_dir=private/$(name)
lib=$(src_dir)/libAMWObs.a

$(lib):
ifeq ($(wildcard $(src_dir)),)
	git submodule init
	git submodule update
endif
	-patch -N -p2 -i $(PATCH_DIR)/SUSY-POPE.patch
	$(MAKE) -C $(src_dir)

susypope: $(lib)

.PHONY: clean all
clean:
	-$(MAKE) -C $(src_dir) clean
	-rm -f $(lib)
