version=1.0
name=lspscat
src_dir=private/$(name)
obj=$(src_dir)/lspscat8o.o

FC=gfortran
FFLAGS=-ffixed-line-length-none

$(lib):
ifeq ($(wildcard $(src_dir)),)
	git submodule init
	git submodule update
endif
	$(FC) -c -o $(obj) $(FFLAGS) $(src_dir)/lspscat8o.f

lspscat8o:  $(obj)

.PHONY: clean all
clean:
	-rm -f $(obj)
