#include "Constraints.h"


extern "C"{
    GaussConstraint * new_GaussConstraint(int *int_obs_ids, int len_int_obs_ids, 
            double * gauss_data, int len_gauss_data, GaussFunc chi2function ){
        std::vector<int> int_obs_ids_vec(int_obs_ids,int_obs_ids + len_int_obs_ids);
        std::vector<double> gauss_data_vec(gauss_data,gauss_data + len_gauss_data);
        return new GaussConstraint(int_obs_ids_vec,gauss_data_vec,chi2function);
    }

}
