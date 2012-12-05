.PHONY: all clean

INSTALL_DIR=$(PWD)/packages
LIB_DIR=$(INSTALL_DIR)/lib
PATCH_DIR=$(PWD)/patches
DEF_DIR=$(PWD)/.make_defs
PREDICTOR_DIR=$(PWD)/predictors
TAR_DIR=$(PREDICTOR_DIR)/.tars
UTIL_DIR=$(PWD)/utils
INTERFACE_DIR=$(PWD)/interfaces
INCLUDE_DIR=$(INSTALL_DIR)/include

MARGS=INSTALL_DIR=$(INSTALL_DIR) TAR_DIR=$(TAR_DIR) PATCH_DIR=$(PATCH_DIR) \
	  INCLUDE_DIR=$(INCLUDE_DIR) DEF_DIR=$(DEF_DIR) \
	  PREDICTOR_DIR=$(PREDICTOR_DIR) UTIL_DIR=$(UTIL_DIR) \
	  INTERFACE_DIR=$(INTERFACE_DIR) LIB_DIR=$(LIB_DIR)

utils=slhalib slhaclass
predictors=feynhiggs micromegas softsusy superiso susypope lspscat bphysics
interfaces=feynhiggs_interface softsusy_interface micromegas_interface \
		   slhaclass_interface superiso_interface bphysics_interface \
		   lspscat_interface

targets=$(predictors) $(utils) $(interfaces)

.PHONY: all clean tarclean

all:
	for t in $(targets); do \
		make $$t ; \
	done

clean:
	for t in $(targets); do \
		yes | make -f .make/$$t.mk $@ $(MARGS) ; \
	done

tarclean:
	for t in $(targets); do \
		make -f .make/$$t.mk $@ $(MARGS) ; \
	done

%:
	make -f .make/$@.mk $(MARGS) ; \
