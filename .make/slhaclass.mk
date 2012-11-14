src_dir=SLHA
lib=$(src_dir)/libs/libSLHAfile.so

$(lib):
	$(MAKE) -C $(src_dir)

slhaclass: $(lib)

.PHONY: clean all
clean:
	$(MAKE) -C $(src_dir) clean
