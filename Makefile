.PHONY: all clean

CALC_DIR=$(PWD)/ObsCalculator
SAMPLE_DIR=$(PWD)/Samplers
POINTAN_DIR=$(PWD)/PointAnalyser
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
USER_DIR=$(PWD)/User
MAKE_DIR=$(PWD)/ObsCalculator

MARGS=INSTALL_DIR=$(INSTALL_DIR) 	TAR_DIR=$(TAR_DIR) PATCH_DIR=$(PATCH_DIR) \
	  INCLUDE_DIR=$(INCLUDE_DIR) 	DEF_DIR=$(DEF_DIR) \
	  PREDICTOR_DIR=$(PREDICTOR_DIR) UTIL_DIR=$(UTIL_DIR) \
	  INTERFACE_DIR=$(INTERFACE_DIR) LIB_DIR=$(LIB_DIR) \
	  SAMPLE_DIR=$(SAMPLE_DIR) STORAGE_DIR=$(STORAGE_DIR) \
	  POINTAN_DIR=$(POINTAN_DIR)	USER_DIR=$(USER_DIR) \
	  MAKE_DIR=$(MAKE_DIR)

utils=slhalib multinest ROOT
predictors=feynhiggs micromegas softsusy superiso susypope lspscat bphysics
interfaces=feynhiggs_interface softsusy_interface micromegas_interface \
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
		yes | make -f $(MAKE_DIR)/.make/$$t.mk $@ $(MARGS) ; \
	done

tarclean:
	for t in $(targets); do \
		make -f $(MAKE_DIR)/.make/$$t.mk $@ $(MARGS) ; \
	done

%:
	make -f $(MAKE_DIR)/.make/$@.mk $(MARGS) ; \
