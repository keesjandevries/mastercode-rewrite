version=1.0
name=lspscat
src_dir=$(PREDICTOR_DIR)/private/$(name)
obj=$(src_dir)/lspscat8o.o

FC=gfortran
FFLAGS=-ffixed-line-length-none
