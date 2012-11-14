version=1.0
name=bphysics
src_dir=private/$(name)
obj=$(src_dir)/bphysics.o

fc=gfortran
fflags=-ffixed-line-length-none -I$(INCLUDE_DIR)

$(lib):
ifeq ($(wildcard $(src_dir)),)
	git submodule init
	git submodule update
endif
	$(fc) -c -o $(obj) $(fflags) $(src_dir)/bphysics.F

bphysics:  $(obj)

.PHONY: clean all
clean:
	-rm -f $(obj)
