#ifndef  INC_CONSTRAINT_H
#define INC_CONSTRAINT_H
#include <iostream>
#include <vector>
#include <map>
#include "Contour.h" 
//FIXME: maybe want separate file for ContourConstraint
//Pro: This would remove dependency on Contour
//Con: keeping the constraints together may be good, you can just comment out "#include "Contour.h"" if you want


// data structure is always central value mu, st
struct GaussData{
    double mu, sigma_square;
}; 
// typedef for member gaussian X^2 function
typedef double(*GaussFunc)(std::vector<double>, GaussData); 
typedef double(*ContourFunc)(std::vector<double>, Contour*); 

/***************************
* Gaussian Constraint Class  
****************************/
class GaussConstraint{
    public:
        GaussConstraint(std::vector<int> /*oids*/ ,std::vector<double>  /*data*/,GaussFunc);
        double GetChi2(double *);
        //Note: no copy or assignment operators are defined
        //following the google c++ style guide, this can be 
        //simply handled by using pointers in the STL containers.
    private:
        // observable ids (Oid) for acces to argument of GetChi2(), in this case double *
        std::vector<int> _internal_oids;
        GaussData        _data; 
        GaussFunc        _gauss_chi2_function;
        // FIXME: not sure if this function should be private, in is not used anywhere else
        double get_sigma_square(std::vector<double>);
};

/***************************
* Contour  Constraint Class  
****************************/
class ContourConstraint{
    public:
        ContourConstraint(std::vector<int> /*internal oids*/, Contour * /*data contour*/,ContourFunc);
        double GetChi2(double *);
    private:
        std::vector<int> _internal_oids;
        Contour *        _data;
        ContourFunc      _contour_chi2_function;
};
#endif
