include $(DEF_DIR)/micromegas.mk

.PHONY: clean all

micromegas_interface: $(interface_lib)

interface_obj=$(interface_src:.cc=.o)

$(interface_lib): $(interface_obj)
	$(cc) -shared -Wl,-soname,libmcmicromegas.so -o $(interface_lib) \
		-Wl,-rpath,$(src_dir) \
		$(interface_obj) \
		$(lib) \
		$(src_dir)/MSSM/lib/aLib.a \
		$(src_dir)/MSSM/work/work_aux.a \
		$(src_dir)/CalcHEP_src/lib/dynamic_me.a \
		$(src_dir)/CalcHEP_src/lib/libSLHAplus.a \
		$(src_dir)/CalcHEP_src/lib/num_c.a \
		$(src_dir)/CalcHEP_src/lib/serv.a \
		$(src_dir)/CalcHEP_src/lib/sqme_aux.so \
		-lX11 -ldl 
$(interface_obj): $(interface_src)
	$(cc) -c -fPIC -o $(interface_obj) $(interface_src) \
		-I$(src_dir)

clean:
	-rm -f $(interface_obj) $(interface_lib)
