#include "Chi2Functions.h"

/************************
 * gaussian functions map
 ************************/
std::map< std::string, GaussFunc>  get_GaussFunc_map(){
    std::map< std::string, GaussFunc> GaussFunc_map;
    GaussFunc_map["gaussian"]=&gaussian;
    GaussFunc_map["lowerlimit"]=&lowerlimit;
    GaussFunc_map["upperlimit"]=&upperlimit;
    return GaussFunc_map;
}
/************************
 * contour  functions map
 ************************/
std::map< std::string, ContourFunc>  get_ContourFunc_map(){
    std::map< std::string, ContourFunc> ContourFunc_map;
    ContourFunc_map["ma_tanb_mc8"]=&ma_tanb_mc8;
    return ContourFunc_map;
}

/********************
 * gaussian functions
 ********************/
double gaussian(std::vector<double> obs,GaussData data){
    return (obs[0]-data.mu)*(obs[0]-data.mu)/data.sigma_square;
}
double lowerlimit(std::vector<double> obs,GaussData data){
    double chi2=0;
    if (obs[0] < data.mu ) chi2=gaussian(obs,data);
    return chi2;
}
double upperlimit(std::vector<double> obs,GaussData data){
    double chi2=0;
    if (obs[0] > data.mu ) chi2=gaussian(obs,data);
    return chi2;
}

/********************
 * contour  functions
 ********************/
double ma_tanb_mc8(std::vector<double> obs, Contour * ma_tanb_95){
    double ma_point     =ma_tanb_95->GetPointParameter(obs);
    double tanb_point   =ma_tanb_95->GetPointValue(obs);
    double tanb_contour =ma_tanb_95->GetContourValue(ma_point);
    return 4*(tanb_point/tanb_contour)*(tanb_point/tanb_contour);
}
