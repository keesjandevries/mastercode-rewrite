#ifndef LIKELIHOODFUNCTIONS_H
#define LIKELIHOODFUNCTIONS_H
#include <iostream>
#include <map>
#include <string>
#include <vector>
#include "Constraints.h"


// this function returns the full map
std::map< std::string, GaussFunc>  get_GaussFunc_map();
std::map< std::string, ContourFunc>  get_ContourFunc_map();

// FIXME: maybe should not keep the functions here, since they are more or less
// global variables

/*************************
 * gaussian chi2 functions
 *************************/
double gaussian(std::vector<double> obs,GaussData);
double lowerlimit(std::vector<double> obs,GaussData);
double upperlimit(std::vector<double> obs,GaussData);
/*************************
 * contour  chi2 functions
 *************************/
double ma_tanb_mc8(std::vector<double> obs, Contour *);
#endif
