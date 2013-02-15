include $(DEF_DIR)/ROOT.mk

python_incdir=$(shell python -c  "import distutils.sysconfig as du; print(du.get_python_inc())" )
python_libdir=$(shell python -c "import sys; print( sys.prefix )")/lib

#$(lib):
ROOT :
ifeq ($(wildcard $(tarfile)),)
	wget -N -P $(TAR_DIR) $(remote)
endif
ifeq ($(wildcard $(src_dir)),)
	tar -C $(UTIL_DIR) -xf $(tarfile)
endif
	cd $(src_dir); \
		./configure --prefix=$(INSTALL_DIR)   \
		--etcdir=$(INSTALL_DIR) 
	$(MAKE) -C $(src_dir)
	$(MAKE) -C $(src_dir) install

#ROOT: $(lib)

.PHONY: clean all
clean:
	$(MAKE) -C $(src_dir) clean

tarclean:
	-rm -f $(tarfile)
	-rm -rf $(src_dir)
