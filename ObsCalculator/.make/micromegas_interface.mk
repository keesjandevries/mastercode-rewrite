include $(DEF_DIR)/micromegas.mk

.PHONY: clean all

micromegas_interface: $(interface_bin) $(interface_src)

interface_obj=$(interface_src:.cc=.o)

$(interface_bin): $(interface_src)
	$(cc) -fsigned-char -Wall -fPIC  -o $(interface_bin) \
		-I$(inc)\
		$(interface_src) \
		$(lib) \
		$(src_dir)/MSSM/lib/aLib.a \
		$(src_dir)/MSSM/work/work_aux.a \
		$(src_dir)/CalcHEP_src/lib/dynamic_me.a \
		$(src_dir)/CalcHEP_src/lib/libSLHAplus.a \
		$(src_dir)/CalcHEP_src/lib/num_c.a \
		$(src_dir)/CalcHEP_src/lib/serv.a \
		$(src_dir)/CalcHEP_src/lib/sqme_aux.so \
		-lX11  -rdynamic -ldl -lm

clean:
	-rm -f $(interface_obj) $(interface_bin)
