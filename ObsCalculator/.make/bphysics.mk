include $(DEF_DIR)/bphysics.mk

$(obj):
ifeq ($(wildcard $(src_dir)),)
	git submodule init
	git submodule update
endif
	$(fc) -fPIC -c -o $(obj) $(fflags) $(src_dir)/bphysics.F

bphysics:  $(obj)

.PHONY: clean all
clean:
	-rm -f $(obj)
