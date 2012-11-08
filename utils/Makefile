.PHONY: all clean SLHA SLHALib

SLHALib_version=2.2
SLHALib_dir=SLHALib-$(SLHALib_version)
SLHALib:
	cd $(SLHALib_dir); \
		./configure --prefix=$(INSTALL_DIR)
	$(MAKE) -C $(SLHALib_dir)
	$(MAKE) -C $(SLHALib_dir) install

SLHA_dir=SLHA
SLHA:
	$(MAKE) -C $(SLHA_dir)

all: $(SLHA) $(SLHALib)

clean:
	make -C $(SLHALib_dir) clean
	make -C $(SLHA_version) clean
