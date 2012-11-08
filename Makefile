.PHONY: all clean

INSTALL_DIR=$(PWD)/packages

all:
	$(MAKE) -C utils INSTALL_DIR=$(INSTALL_DIR)

clean:
	$(MAKE) -C utils clean
