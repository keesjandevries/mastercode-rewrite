version=3.3
name=superiso_v$(version)
src_dir=$(PREDICTOR_DIR)/$(name)
machine=$(shell uname -m)
lib=$(src_dir)/src/libisospin.a
tar_name=$(name).tgz
remote_url=http://superiso.in2p3.fr/download/
remote=$(remote_url)/$(tar_name)
tarfile=$(TAR_DIR)/$(tar_name)
