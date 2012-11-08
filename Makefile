.PHONY: all clean

all:
	$(MAKE) -C predictors
	$(MAKE) -C utils
	$(MAKE) -C interfaces
