#include "Constraints.h"
#include "Chi2Functions.h"

extern "C"{
    GaussConstraint * new_GaussConstraint(int *int_obs_ids, int len_int_obs_ids, 
            double * gauss_data, int len_gauss_data, char * chi2function_name ){
        // initialise int observalbe ids 
        std::vector<int> int_obs_ids_vec(int_obs_ids,int_obs_ids + len_int_obs_ids);
        // inisialise data vector
        std::vector<double> gauss_data_vec(gauss_data,gauss_data + len_gauss_data);
        // get chi2 function
        std::string str_chi2function_name(chi2function_name);
        std::map<std::string,GaussFunc> GaussFunc_map = get_GaussFunc_map();
        // check if str_chi2function_name is in GaussFunc_map
        if (GaussFunc_map.find(str_chi2function_name)!=GaussFunc_map.end()){
            GaussFunc chi2function=GaussFunc_map[str_chi2function_name];
            return new GaussConstraint(int_obs_ids_vec,gauss_data_vec,chi2function);
        }
        else{
            return NULL;
        }
    }

    double get_GaussChi2(GaussConstraint* gauss_constraint, double* obs ){
        gauss_constraint->ShowInternalOids();
        return gauss_constraint->GetChi2(obs);
    }
}
