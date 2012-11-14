version=1.0
name=bphysics
src_dir=private/$(name)
obj=$(src_dir)/bphysics.o

fc=gfortran
fflags=-ffixed-line-length-none -I$(INCLUDE_DIR)
