.PHONY: all clean
RM=rm

SLHALib_version=2.2
SLHALib_name=SLHALib-$(SLHALib_version)
SLHALib_dir=$(SLHALib_name)
SLHALib_tar_name=$(SLHALib_name).tar.gz
SLHALib_remote=http://www.feynarts.de/slha/$(SLHALib_tar_name)
SLHALib_tarfile=$(TAR_DIR)/$(SLHALib_tar_name)

$(SLHALib_tarfile):
ifeq ($(wildcard $(SLHALib_tarfile)),)
	wget -N -P $(TAR_DIR) $(SLHALib_remote)
endif

$(SLHALib_dir): $(SLHALib_tarfile)
ifeq ($(wildcard $(SLHALib_dir)),)
	tar -xf $(SLHALib_tarfile)
endif

SLHALib: $(SLHALib_dir)
	cd $(SLHALib_dir); \
		./configure --prefix=$(INSTALL_DIR)
	$(MAKE) -C $(SLHALib_dir)
	$(MAKE) -C $(SLHALib_dir) install


SLHAClass_dir=SLHA

SLHAClass:
	$(MAKE) -C $(SLHAClass_dir)

#all: SLHALib SLHAClass

clean:
	$(MAKE) -C $(SLHAClass_dir) clean
	$(MAKE) -C $(SLHALib_dir) clean
	-$(RM) -f $(SLHALib_tarfile)
	-$(RM) -rf $(SLHALib_dir)
