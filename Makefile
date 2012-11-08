.PHONY: all clean

INSTALL_DIR=$(PWD)/packages
TAR_DIR=$(PWD)/build/tars

all:
	$(MAKE) -C utils INSTALL_DIR=$(INSTALL_DIR) TAR_DIR=$(TAR_DIR)

clean:
	$(MAKE) clean -C utils
