VERSION=2.9.4
NAME=FeynHiggs-$(VERSION)
DIR=$(NAME)
SRC_TAR=$(NAME).tar.gz
URL=http://wwwth.mpp.mpg.de/members/heinemey/feynhiggs/newversion/
SRC_REMOTE=$(URL)/$(SRC_TAR)
LIBDIR=packages/lib64/
LIB=libFH.a

FEYNHIGGS_SRC_TAR:
	ifeq($(wildcard $(TAR_DIR)/$(FEYNHIGGS_SRC_TAR),)
		wget -N -P $(TAR_DIR) $(FEYNHIGGS_SRC_REMOTE)
	endif

FEYNHIGGS: $(TAR_DIR)/$(FEYNHIGGS_SRC_TAR) 
