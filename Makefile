.PHONY: all clean

CALC_DIR=$(PWD)/ObsCalculator
SAMPLE_DIR=$(PWD)/Samplers
STORAGE_DIR=$(PWD)/Storage
PATCH_DIR=$(CALC_DIR)/.patches
DEF_DIR=$(CALC_DIR)/.make_defs
INTERFACE_DIR=$(CALC_DIR)/interfaces
INSTALL_DIR=$(PWD)/packages
UTIL_DIR=$(PWD)/tools
PREDICTOR_DIR=$(PWD)/predictors
TAR_DIR=$(PREDICTOR_DIR)/.tars
LIB_DIR=$(INSTALL_DIR)/lib
INCLUDE_DIR=$(INSTALL_DIR)/include

MARGS=INSTALL_DIR=$(INSTALL_DIR) TAR_DIR=$(TAR_DIR) PATCH_DIR=$(PATCH_DIR) \
	  INCLUDE_DIR=$(INCLUDE_DIR) DEF_DIR=$(DEF_DIR) \
	  PREDICTOR_DIR=$(PREDICTOR_DIR) UTIL_DIR=$(UTIL_DIR) \
	  INTERFACE_DIR=$(INTERFACE_DIR) LIB_DIR=$(LIB_DIR) \
	  SAMPLE_DIR=$(SAMPLE_DIR) STORAGE_DIR=$(STORAGE_DIR)

utils=slhalib multinest ROOT
predictors=feynhiggs micromegas softsusy superiso susypope lspscat bphysics
interfaces=feynhiggs_interface  micromegas_interface \
		   superiso_interface bphysics_interface lspscat_interface \
		   slhalib_interface susypope_interface multinest_interface \
		   ROOT_interface

targets=$(predictors) $(utils) $(interfaces)

.PHONY: all clean tarclean

all:
	for t in $(targets); do \
		make $$t ; \
	done

clean:
	for t in $(targets); do \
		yes | make -f $(CALC_DIR)/.make/$$t.mk $@ $(MARGS) ; \
	done

tarclean:
	for t in $(targets); do \
		make -f $(CALC_DIR)/.make/$$t.mk $@ $(MARGS) ; \
	done

%:
	make -f $(CALC_DIR)/.make/$@.mk $(MARGS) ; \
