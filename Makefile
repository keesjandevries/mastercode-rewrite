.PHONY: all clean

INSTALL_DIR=$(PWD)/packages
TAR_DIR=$(PWD)/build/tars
PATCH_DIR=$(PWD)/patches
MARGS=INSTALL_DIR=$(INSTALL_DIR) TAR_DIR=$(TAR_DIR) PATCH_DIR=$(PATCH_DIR) \
	  INCLUDE_DIR=$(INSTALL_DIR)/include

#utils=slhaclass slhalib
slhalib=utils/slhalib.mk
slhaclass=utils/slhaclass.mk
feynhiggs=predcitors/feynhiggs.mk

utils=slhalib slhaclass
predictors=feynhiggs micromegas softsusy superiso susypope lspscat bphysics
interfaces=feynhiggs

.PHONY: all clean tarclean

all:
	cd utils ; \
		for u in $(utils); do \
			make -f .make/$$u.mk $(MARGS) ; \
		done
	cd predictors ; \
		for p in $(predictors); do \
			make -f .make/$$p.mk $(MARGS) ; \
		done
	cd predictors ; \
		for i in $(interfaces); do \
			make -f .make/$$i.mk $(MARGS) ; \
		done

clean:
	cd utils ; \
		for u in $(utils); do \
			make -f .make/$$u.mk clean $(MARGS) ; \
		done
	cd predictors ; \
		for p in $(predictors); do \
			make -f .make/$$p.mk clean $(MARGS) ; \
		done

tarclean:
	cd utils ; \
		for u in $(utils); do \
			make -f .make/$$u.mk tarclean $(MARGS) ; \
		done
	cd predictors ; \
		for p in $(predictors); do \
			make -f .make/$$p.mk tarclean $(MARGS) ; \
		done
