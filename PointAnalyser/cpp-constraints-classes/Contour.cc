#include "Contour.h"
Contour::Contour(std::vector<double_pair> coords){
    //FIXME: this is only the first iteration contructor, everything is set to default values
    _coordinates=coords ; //FIXME: don't sort for not
    _get_point_parameter=&get_x;
    _get_point_value=&get_y;
    _coordinates_parameters=GetCoordinatesParameters();     // e.g. 'x' or 'theta'
    _low_extrapolate    =&extrapolate_low_x_flat;
    _high_extrapolate   =&extrapolate_high_x_flat;
    _interpolate        =&interpolate_x;

}

double Contour::GetContourValue(double parameter){
    if      (parameter < _coordinates_parameters.front() ){ 
        return _low_extrapolate(parameter,&_coordinates);
    }
    else if (parameter <=_coordinates_parameters.back()){ 
        std::pair< double_pair,double_pair > segment=GetSegment(parameter);
        return _interpolate(parameter,segment);
    }
    else { 
        return _high_extrapolate(parameter,&_coordinates);
    }
}

double Contour::GetPointParameter(double_pair point_coordinates){
    return _get_point_parameter(point_coordinates); 
}
double Contour::GetPointParameter(std::vector<double> point_coordinates_vec){
    // in the likelihood functions, a double vector is given. 
    // this is a convenience function to allow for giving a double vector.
    if (point_coordinates_vec.size() ==2){
        double_pair point_coordinates=std::make_pair(point_coordinates_vec[0],point_coordinates_vec[1]);
        return GetPointParameter(point_coordinates);    
    }
    else{
        //FIXME: maybe have to throw something.. this may be better error handling
        std::cout << "ERROR: GetPointParameter takes two doubles in a vector or pair" << std::endl;
        std::cout << "       " << point_coordinates_vec.size() << " were given" << std::endl;
    }
}
double Contour::GetPointValue(double_pair point_coordinates){
    return _get_point_value(point_coordinates); 
}
double Contour::GetPointValue(std::vector<double> point_coordinates_vec){
    // in the likelihood functions, a double vector is given. 
    // this is a convenience function to allow for giving a double vector.
    if (point_coordinates_vec.size() ==2){
        double_pair point_coordinates=std::make_pair(point_coordinates_vec[0],point_coordinates_vec[1]);
        return GetPointValue(point_coordinates);    
    }
    else{
        //FIXME: maybe have to throw something.. this may be better error handling
        std::cout << "ERROR: GetPointValue takes two doubles in a vector or pair" << std::endl;
        std::cout << "       " << point_coordinates_vec.size() << " were given" << std::endl;
    }
}

std::pair<double_pair,double_pair> Contour::GetSegment(double parameter){
    //loop over coordinates paramters and compare with parameter
    std::pair<double_pair,double_pair> segment;
    for (unsigned int i =0;i<_coordinates_parameters.size();i++){
        //FIXME: this comparison depends on the coordinates being 
        //       sorted according to the magnitude of their parameter
        if (parameter < _coordinates_parameters[i]){
            segment=std::make_pair(_coordinates[i-1],_coordinates[i]);
        }
    }
    return segment;
}

std::vector<double> Contour::GetCoordinatesParameters(){
    std::vector<double> coordinates_parameters;
    for (std::vector<double_pair>::iterator it=_coordinates.begin();it!=_coordinates.end();it++){
        coordinates_parameters.push_back(_get_point_parameter(*it));
    }
    return coordinates_parameters;
}

/*************************
 * interpolation functions
 ************************/
double interpolate_x(double parameter, std::pair<double_pair,double_pair> segment){
    double x1,x2,y1,y2;
    x1=segment.first.first;
    y1=segment.first.second;    
    x2=segment.second.first;
    y2=segment.second.second;
    double gradient=(y2-y1)/(x2-x1);
    return y1+(parameter-x1)*gradient;
}

/*************************
 * extrapolation functions
 ************************/
double extrapolate_low_x_flat(double parameter,std::vector<double_pair> * coordinates){
    return coordinates->front().second; // the y-coordinate of the first element
}
double extrapolate_high_x_flat(double parameter,std::vector<double_pair> * coordinates){
    return coordinates->back().second; // the y-coordinate of the first element
}

/*************************
 * get parameter functions
 ************************/
double get_x(double_pair point_coordinates){
    return point_coordinates.first;
}
double get_y(double_pair point_coordinates){
    return point_coordinates.second;
}

double get_theta(double_pair point_coordinates){
    return atan2(point_coordinates.second,point_coordinates.first);
}
