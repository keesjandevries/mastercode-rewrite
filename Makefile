.PHONY: all clean

INSTALL_DIR=$(PWD)/packages
TAR_DIR=$(PWD)/build/tars
PATCH_DIR=$(PWD)/patches
MARGS=INSTALL_DIR=$(INSTALL_DIR) TAR_DIR=$(TAR_DIR) PATCH_DIR=$(PATCH_DIR)

#utils=slhaclass slhalib
utils=
predictors=feynhiggs

all:
	cd utils ; \
		for u in $(utils); do \
			make -f $$u.mk $(MARGS) ; \
		done
	cd predictors ; \
		for p in $(predictors); do \
			make -f $$p.mk $(MARGS) ; \
		done

clean:
	cd utils ; \
		for uin $(utils); do \
			make -f $$u.mk clean $(MARGS) ; \
		done
	cd predictors ; \
		for p in $(predictors); do \
			make -f $$p.mk clean $(MARGS) ; \
		done
