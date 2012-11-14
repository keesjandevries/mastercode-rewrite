version=2.4.5
name=micromegas_$(version)
src_dir=$(PREDICTOR_DIR)/$(name)
lib=$(src_dir)/sources/micromegas.a
tar_name=$(name).tgz
remote_url=http://lapth.in2p3.fr/micromegas/downloadarea/code/
remote=$(remote_url)/$(tar_name)
tarfile=$(TAR_DIR)/$(tar_name)
