.PHONY: all clean

MCRW_DIR=$(PWD)/mcrw
PATCH_DIR=$(MCRW_DIR)/.patches
DEF_DIR=$(MCRW_DIR)/.make_defs
INTERFACE_DIR=$(MCRW_DIR)/interfaces
INSTALL_DIR=$(PWD)/packages
UTIL_DIR=$(PWD)/utils
PREDICTOR_DIR=$(PWD)/predictors
TAR_DIR=$(PREDICTOR_DIR)/.tars
LIB_DIR=$(INSTALL_DIR)/lib
INCLUDE_DIR=$(INSTALL_DIR)/include

MARGS=INSTALL_DIR=$(INSTALL_DIR) TAR_DIR=$(TAR_DIR) PATCH_DIR=$(PATCH_DIR) \
	  INCLUDE_DIR=$(INCLUDE_DIR) DEF_DIR=$(DEF_DIR) \
	  PREDICTOR_DIR=$(PREDICTOR_DIR) UTIL_DIR=$(UTIL_DIR) \
	  INTERFACE_DIR=$(INTERFACE_DIR) LIB_DIR=$(LIB_DIR)

utils=slhalib
predictors=feynhiggs micromegas softsusy superiso susypope lspscat bphysics
interfaces=feynhiggs_interface softsusy_interface micromegas_interface \
		   superiso_interface bphysics_interface lspscat_interface \
		   slhalib_interface susypope_interface

targets=$(predictors) $(utils) $(interfaces)

.PHONY: all clean tarclean

all:
	for t in $(targets); do \
		make $$t ; \
	done

clean:
	for t in $(targets); do \
		yes | make -f mcrw/.make/$$t.mk $@ $(MARGS) ; \
	done

tarclean:
	for t in $(targets); do \
		make -f mcrw/.make/$$t.mk $@ $(MARGS) ; \
	done

%:
	make -f mcrw/.make/$@.mk $(MARGS) ; \
