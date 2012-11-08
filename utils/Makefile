.PHONY: all clean

SLHALib_version=2.2
SLHALib_dir=SLHALib-$(SLHALib_version)
SLHAlib:
	echo $(INSTALL_DIR)
	$(SLHALib_dir)/configure --prefix=$(INSTALL_DIR)
	$(MAKE) -C $(SLHALib_dir)
	$(MAKE) -C $(SLHALib_dir) install

SLHA_dir=SLHA
SLHA:
	$(MAKE) -C $(SLHA_dir)

all: SLHA SLHAlib

clea:
	make -C $(SLHALib_dir) clean
	make -C $(SLHA_version) clean
