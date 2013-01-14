import math

import stats

def load_contour(filename, mode='radial'):
    f = open(filename,'r')
    s_contour = [tuple(x.split()) for x in f.readlines()]
    f_contour = [(float(x), float(y)) for (x,y) in s_contour]
    f_contour.sort(key=mode_lookup[mode]['par'])
    return f_contour

# this might actually be a good use for a class from now on... we'll see

# not convinced this is a good idea yet
X,Y = range(2)

# sort_modes for contours
def theta(point):
    return math.atan2(point[Y],point[X])

def radius(point):
    return math.sqrt(point[X]**2 + point[Y]**2) 

def x_coord(point):
    return point[X]

def y_coord(point):
    return point[Y]

#def past_segment_theta(point, c_point):
#    c_theta = math.atan2(c_point[Y], c_point[X])
#    p_theta = math.atan2(point[Y], c_point[X])
#    return p_theta > c_theta
#
#def past_segment_x(point, c_point):
#    return point[X]>c_point[X]
#
#def past_segment_y(point, c_point):
#    return point[Y]>c_point[Y]

#def distance_ratio_radial(point, segment):
#    point_gradient = point[Y]/point[X]
#    segment_gradient = ((segment[1][Y] - segment[0][Y]) /
#            (segment[1][X] - segment[0][X]))
#    intercept_x = ((segment_gradient*segment[0][X] - segment[0][Y]) /
#            (segment_gradient - point_gradient))
#    intercept_y = point_gradient*intercept_x
#    intercept_r = math.sqrt(intercept_x**2 + intercept_y**2)
#    point_r = math.sqrt(point[X]**2 + point[Y]**2)
#    return point_r/intercept_r
#
#def distance_ratio_x(point, segment):
#    segment_gradient = ((segment[1][Y] - segment[0][Y]) /
#            (segment[1][X] - segment[0][X]))
#    intercept_x = (point[Y]-segment[0][Y])*(1./segment_gradient) + segment[0][X]
#    return point[X] / intercept_x
#
#def distance_ratio_y(point, segment):
#    segment_gradient = ((segment[1][Y] - segment[0][Y]) /
#            (segment[1][X] - segment[0][X]))
#    intercept_y = (point[X]-segment[0][X])*segment_gradient + segment[0][Y]
#    return point[Y] / intercept_y

def interpolate_radial(point_par, segment,interp='linear'):
    intercept_r=None
    if interp is 'linear':
        point_gradient = math.tan(point_par)
        segment_gradient = ((segment[1][Y] - segment[0][Y]) /
                (segment[1][X] - segment[0][X]))
        intercept_x = ((segment_gradient*segment[0][X] - segment[0][Y]) /
                (segment_gradient - point_gradient))
        intercept_y = point_gradient*intercept_x
        intercept_r = math.sqrt(intercept_x**2 + intercept_y**2)
    return  intercept_r

def interpolate_x(point_par, segment,interp='linear'):
    intercept_x=None
    if interp is 'linear':
        segment_gradient = ((segment[1][Y] - segment[0][Y]) /
                (segment[1][X] - segment[0][X]))
        intercept_x = (point_par-segment[0][Y])*(1./segment_gradient) + segment[0][X]
    return intercept_x

def interpolate_y(point_par, segment,interp='linear'):
    intercept_y=None
    if interp is 'linear':

        segment_gradient = ((segment[1][Y] - segment[0][Y]) /
                (segment[1][X] - segment[0][X]))
        intercept_y = (point_par-segment[0][X])*segment_gradient + segment[0][Y]
    return  intercept_y


mode_lookup = {
        'radial': {
            'par': theta,
            'value': radius,
#            'range_test': past_segment_theta,
#            'ratio': distance_ratio_radial,
            'interpolate': interpolate_radial,
            },
        'x': {
            'par': x_coord,
            'value': y_coord,
#            'range_test': past_segment_x,
#            'ratio': distance_ratio_y,
            'interpolate': interpolate_y,
            },
        'y': {
            'par': y_coord,
            'value': x_coord,
#            'range_test': past_segment_y,
#            'ratio': distance_ratio_x,
            'interpolate': interpolate_x,
            },
        }

#def segment_range(point, contour, mode):
#    try:
#        range_end = next(c_point for c_point in contour if not
#                mode_lookup[mode]['range_test'](point,c_point))
#    except StopIteration:
#        print("ERROR: Unable to find intercept for point {p}".format(p=point))
#        segment_positions = None
#    else:
#        range_end_pos = contour.index(range_end)
#        segment_positions = (range_end_pos-1, range_end_pos)
#    return segment_positions

def find_segment_indices(mode,point_par,coords):
    try:
        second_point= next(c_point for c_point in coords if not
                 mode_lookup[mode]['par'](c_point) < point_par )
    except StopIteration:
        print("ERROR: Unable to find intercept for point {p}".format(p=point))
        segment_positions = None
    else:
        second_point_pos = coords.index(second_point)
        segment_positions = (second_point_pos-1, second_point_pos)
    return segment_positions


def extrap_min_flat(mode,coords):
    return mode_lookup[mode]['value'](coords[0])

def extrap_max_flat(mode,coords):
    return mode_lookup[mode]['value'](coords[-1])

extrap_lookup={
        'min':{
            'flat' : extrap_min_flat,
            },
        'max':{
            'flat' : extrap_max_flat,
            },
        }

def interpolate( mode, point_par, coords, interp):
    value= None
    segment_indices = find_segment_indices(mode, point_par, coords )
    if segment_indices:
        segment = (coords[segment_indices[0]], coords[segment_indices[1]])
        print('segment',segment)
        value = mode_lookup[mode]['interpolate'](point_par, segment,interp)
    return value

def get_contour_value(point_par, mode, coords, interp, extrap):
    value=None
    min_par=mode_lookup[mode]['par'](coords[0])
    max_par=mode_lookup[mode]['par'](coords[-1])
    if point_par < min_par and extrap.get('min'):
        value=extrap_lookup['min'][extrap['min']](mode,coords)
        print("below min_par")
    elif min_par <= point_par and point_par <= max_par:
#        value=mode_lookup[mode]['interpolate'](point_par, coords,interp)
        value=interpolate(mode, point_par, coords,interp)
        print("in parameter range")
        print(value)
    elif point_par > max_par and extrap.get('max'):
        value=extrap_lookup['max'][extrap['max']](mode,coords)
        print("above parameter range")
    return value

#def point_ratio(self, point, mode):
#    segment = segment_range(point, self.contour, self.mode)
#    return mode_lookup[mode]['ratio'](point, segment)

class Contour(object):
    # A contour is assumed to be parametrised by par (defined by mode)
    # the value of the contour for that par is given by con_val(par, cont)
    def __init__(self,filename, mode, pval=None , dim=2 , interp='linear', extrap={} ):
        self.coords = load_contour(filename,mode)
        self.interp = interp
        self.extrap = extrap
        self.mode = mode
        self.pval = pval
        self.dim = dim
        if pval:
            self.chi2 = stats.chi2quantile(self.pval, self.dim)
        else:
            self.chi2=None

    def point_ratio(self,point):
        point_ratio=None
        point_par   = mode_lookup[self.mode]['par'](point)
        point_value = mode_lookup[self.mode]['value'](point)
        cont_value  = get_contour_value(point_par, self.mode, self.coords, self.interp, self.extrap)
        if cont_value:
            point_ratio=point_value/cont_value
        return point_ratio
#        segment_indices = segment_range(point, self.contour, self.mode)
#        if segment_indices:
#            segment = (self.contour[segment_indices[0]],
#                self.contour[segment_indices[1]])
#            return mode_lookup[self.mode]['ratio'](point, segment)
#        else:
#            return None
#
#    def bring_in_range(self,point)
#        if 'min' in self.extrapolate: point=mode_lookup[self.mode]['extr_min'](point)
#        return point
#
#
#    def min_x(self):
#        return self.contour[0][0]
#    def max_x(self):
#        return self.contour[-1][0]
#    def min_y(self):
#        return self.contour[0][1]
#    def max_y(self):
#        return self.contour[-1][1]
