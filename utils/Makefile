targets = SLHAClass SLHALib 
all: $(targets)

SLHALib_version=2.2
SLHALib_name=SLHALib-$(SLHALib_version)
SLHALib_dir=$(SLHALib_name)
SLHALib_lib=$(SLHALib_dir)/build/libSLHA.a
SLHALib_tar_name=$(SLHALib_name).tar.gz
SLHALib_remote=http://www.feynarts.de/slha/$(SLHALib_tar_name)
SLHALib_tarfile=$(TAR_DIR)/$(SLHALib_tar_name)

$(SLHALib_lib):
ifeq ($(wildcard $(SLHALib_tarfile)),)
	wget -N -P $(TAR_DIR) $(SLHALib_remote)
endif
ifeq ($(wildcard $(SLHALib_dir)),)
	tar -xf $(SLHALib_tarfile)
endif
	cd $(SLHALib_dir); \
		./configure --prefix=$(INSTALL_DIR)
	$(MAKE) -C $(SLHALib_dir)
	$(MAKE) -C $(SLHALib_dir) install

SLHALib: $(SLHALib_lib)


SLHAClass_dir=SLHA
SLHAClass_lib=$(SLHAClass_dir)/libs/libSLHAfile.so
$(SLHAClass_lib):
	$(MAKE) -C $(SLHAClass_dir)

SLHAClass: $(SLHAClass_lib)

.PHONY: clean all
clean:
	$(MAKE) -C $(SLHAClass_dir) clean
	$(MAKE) -C $(SLHALib_dir) clean
	-rm -f $(SLHALib_tarfile)
	-rm -rf $(SLHALib_dir)
