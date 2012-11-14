include $(DEF_DIR)/bphysics.mk

$(lib):
ifeq ($(wildcard $(src_dir)),)
	git submodule init
	git submodule update
endif
	$(fc) -c -o $(obj) $(fflags) $(src_dir)/bphysics.F

bphysics:  $(obj)

.PHONY: clean all
clean:
	-rm -f $(obj)
