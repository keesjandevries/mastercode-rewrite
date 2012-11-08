.PHONY: all clean

INSTALL_DIR=packages

all:
	$(MAKE) -C utils INSTALL_DIR=packages
	#$(MAKE) -C predictors INSTALL_DIR=packages
	#$(MAKE) -C interfaces INSTALL_DIR=packages

clean:
	$(MAKE) -C utils clean
