VERSION=2.4.5
SRC_TAR=micromegas_$(VERSION).tgz
URL=http://lapth.in2p3.fr/micromegas/downloadarea/code/
SRC_REMOTE=$(URL)/$(SRC_TAR)
SRC_DIR=$(SRCDIR)/micromegas_$(VERSION)/
LIBDIR=$(MICORMEGAS_SRC_DIR)/sources/
LIB=micromegas.a

SRC_TAR:
	if [ ! -e $$(TAR_DIR) ]; then \
		wget $$(SRC_REMOTE)
	#wget -N -P $(TAR_DIR) $(SRC_REMOTE)

MICROMEGAS: $(TAR_DIR)/$(SRC_TAR) 
