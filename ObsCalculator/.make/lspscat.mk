include $(DEF_DIR)/lspscat.mk

$(lib):
ifeq ($(wildcard $(src_dir)),)
	git submodule init
	git submodule update
endif
	$(FC) -fPIC -c -o $(obj) $(FFLAGS) $(src_dir)/lspscat8o.f

lspscat8o:  $(obj)

.PHONY: clean all
clean:
	-rm -f $(obj)
