#include "Chi2Functions.h"

// use typedef only in this file for convenience
typedef std::map<std::string,GaussFunc> GaussFunc_map;

extern "C"{
     GaussFunc_map* get_new_GaussFunc_map(){
        GaussFunc_map * GaussFuncMap= new GaussFunc_map;
        *GaussFuncMap=get_GaussFunc_map();
        return GaussFuncMap;
    }

    GaussFunc get_GaussFunc(GaussFunc_map * GaussFuncMap, char* func_name){
        std::string str_func_name(func_name);
        // here follows an elaborate way of checking whether the func_name is
        // actually in the map. If so, return it's value
        GaussFunc_map::iterator it= GaussFuncMap->find(str_func_name);
        if (it!=GaussFuncMap->end()){
            return it->second;
        }
        else{
            std::cout << "ERROR: could not find " << str_func_name << " in functions map" << std::endl;
            return NULL;
        }
    }
}
