#ifndef CONTOUR_H
#define CONTOUR_H
#include <iostream>
#include <map>
#include <utility>  //std::pair
#include <vector>
#include <string>
#include <cmath>    //atan2()

// define double_pair to reduce syntacs
typedef std::pair<double,double> double_pair;

class Contour{
    public:
        // Directly accesible
        Contour(std::vector<double_pair>/*coords*/);   //FIXME: only coordinates for now
//        Contour(std::vector<double_pair>/*coords*/, std::string /*par_mode*/);    //interpolate mode is linear
//        Contour(std::vector<double_pair>/*coords*/, std::string /*par_mode*/,std::string /*interp_mode*/);
        double GetContourValue(double /*parameter*/);
        double GetPointParameter(double_pair /*point_coordinates*/);
        double GetPointParameter(std::vector<double> /*point_coordinates*/);
        double GetPointValue(double_pair /*point_coordinates*/);
        double GetPointValue(std::vector<double> /*point_coordinates*/);

        // FIXME: these should maybe be private memberfunctions
        std::pair<double_pair,double_pair> GetSegment(double /*parameter*/);
        std::vector<double> GetCoordinatesParameters();
    private:
        std::vector<double_pair>    _coordinates;
        std::vector<double>         _coordinates_parameters;     // e.g. 'x' or 'theta'
        double (*_get_point_parameter)(double_pair);    //e.g. get_theta(...), get_x(...)
        double (*_get_point_value)(double_pair);        //e.g. get_radius(...), get_y(...)
        // functions used by GetContourValue(...)
        double (*_interpolate)     (double /*parameter*/,std::pair<double_pair,double_pair> /*segment*/);
        double (*_low_extrapolate) (double /*parameter*/,std::vector<double_pair> * /*coordinates pointer*/);
        double (*_high_extrapolate)(double /*parameter*/,std::vector<double_pair> * /*coordinates pointer*/);
};

// functions that do not belong to the class but may be pointed to

/*************************
 * interpolation functions
 ************************/
double interpolate_x(double parameter, std::pair<double_pair,double_pair> segment);

/*************************
 * extrapolation functions
 ************************/
double extrapolate_low_x_flat(double parameter,std::vector<double_pair> *);
double extrapolate_high_x_flat(double parameter,std::vector<double_pair> *);

/*************************
 * get parameter functions
 ************************/
double get_x(double_pair point_coordinates);
double get_y(double_pair point_coordinates);
double get_theta(double_pair point_coordinates);
#endif
