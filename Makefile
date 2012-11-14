.PHONY: all clean

INSTALL_DIR=$(PWD)/packages
TAR_DIR=$(PWD)/build/tars
PATCH_DIR=$(PWD)/patches
DEF_DIR=$(PWD)/.make_defs
PREDICTOR_DIR=$(PWD)/predictors
UTIL_DIR=$(PWD)/utils
INTERFACE_DIR=$(PWD)/interfaces

MARGS=INSTALL_DIR=$(INSTALL_DIR) TAR_DIR=$(TAR_DIR) PATCH_DIR=$(PATCH_DIR) \
	  INCLUDE_DIR=$(INSTALL_DIR)/include DEF_DIR=$(DEF_DIR) \
	  PREDICTOR_DIR=$(PREDICTOR_DIR) UTIL_DIR=$(UTIL_DIR) \
	  INTERFACE_DIR=$(INTERFACE_DIR)

#utils=slhaclass slhalib
slhalib=utils/slhalib.mk 
slhaclass=utils/slhaclass.mk
feynhiggs=predcitors/feynhiggs.mk

utils=slhalib slhaclass
predictors=feynhiggs micromegas softsusy superiso susypope lspscat bphysics
interfaces=feynhiggs

.PHONY: all clean tarclean

all:
	for u in $(utils); do \
		make -f .make/$$u.mk $(MARGS) ; \
	done
	for p in $(predictors); do \
		make -f .make/$$p.mk $(MARGS) ; \
	done
	for i in $(interfaces); do \
		make -f .make/$$i.mk $(MARGS) ; \
	done

clean:
	for u in $(utils); do \
		make -f .make/$$u.mk clean $(MARGS) ; \
	done
	for p in $(predictors); do \
		make -f .make/$$p.mk clean $(MARGS) ; \
	done

tarclean:
	for u in $(utils); do \
		make -f .make/$$u.mk tarclean $(MARGS) ; \
	done
	for p in $(predictors); do \
		make -f .make/$$p.mk tarclean $(MARGS) ; \
	done
