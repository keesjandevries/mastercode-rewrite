//FIXME: may want to make "Constraints.h/.cc" a sub module with configure, make and make install
//so that it is usable from other codes as well. For now keep part of the interface
#include "Constraints.h"
//NOTE: members of classes are indicated with "_" in front of the variable

/***************************
* Gaussian Constraint Class  
****************************/
GaussConstraint::GaussConstraint(std::vector<int> int_obs_ids, std::vector<double> gauss_in_data , GaussFunc chi2function){
    _internal_oids      = int_obs_ids;
    _data.mu            = gauss_in_data[0];
    _data.sigma_square  = get_sigma_square(gauss_in_data);
    _gauss_chi2_function=chi2function;
}

double GaussConstraint::GetChi2(double* obs){
    std::vector<double> constraint_obs;
    for (std::vector<int>::iterator it = _internal_oids.begin(); it!=_internal_oids.end(); it++){
        constraint_obs.push_back(obs[*it]);
    }
    return _gauss_chi2_function(constraint_obs, _data);
}

double GaussConstraint::get_sigma_square(std::vector<double> gauss_in_data){
    double sigma_square=0.;
    for(unsigned int i=1;i<gauss_in_data.size();i++){
        sigma_square+= gauss_in_data[i]*gauss_in_data[i] ;
    }
    return sigma_square;
}

/***************************
* Contour  Constraint Class  
****************************/
ContourConstraint::ContourConstraint(std::vector<int> int_obs_ids, Contour * contour_in_data, ContourFunc chi2function){
    _internal_oids          = int_obs_ids;
    _data                   = contour_in_data;
    _contour_chi2_function  = chi2function;
}

double ContourConstraint::GetChi2(double* obs){
    std::vector<double> constraint_obs;
    for (std::vector<int>::iterator it = _internal_oids.begin(); it!=_internal_oids.end(); it++){
        constraint_obs.push_back(obs[*it]);
    }
    return _contour_chi2_function(constraint_obs, _data);
}

//FIXME: may want to make "Constraints.h/.cc" a sub module with configure, make and make install
//so that it is usable from other codes as well. For now keep part of the interface
extern "C"{
    GaussConstraint * new_GaussConstraint(int *int_obs_ids, int len_int_obs_ids, 
            double * gauss_data, int len_gauss_data, GaussFunc chi2function ){
        std::vector<int> int_obs_ids_vec(int_obs_ids,int_obs_ids + len_int_obs_ids);
        std::vector<double> gauss_data_vec(gauss_data,gauss_data + len_gauss_data);
        return new GaussConstraint(int_obs_ids_vec,gauss_data_vec,chi2function);
    }

}
