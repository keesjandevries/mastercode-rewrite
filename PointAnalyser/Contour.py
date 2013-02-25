import math

import stats

def load_contour(filename, mode='radial'):
    f = open(filename,'r')
    s_contour = [tuple(x.split()) for x in f.readlines()]
    f_contour = [(float(x), float(y)) for (x,y) in s_contour]
    f_contour.sort(key=mode_lookup[mode]['parameter'])
    f.close()
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


def interpolate_radial(point_par, segment,interp='linear'):
    intercept_r=None
    if interp == 'linear':
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
    if interp == 'linear':
        segment_gradient = ((segment[1][Y] - segment[0][Y]) /
                (segment[1][X] - segment[0][X]))
        intercept_x = (point_par-segment[0][Y])*(1./segment_gradient) + segment[0][X]
    return intercept_x

def interpolate_y(point_par, segment,interp='linear'):
    #FIXME: log scale interpolation is implemented only here
    #could be made prittier, but at least it works!
    intercept_y=None
    if 'log' in interp:
        if 'x' in interp: point_par, segment=math.log(point_par), [(math.log(point[0]),point[1]) for point in segment  ]
        if 'y' in interp: segment= [( point[0],math.log(point[1]) ) for point in segment]
    segment_gradient = ((segment[1][Y] - segment[0][Y]) /
            (segment[1][X] - segment[0][X]))
    intercept_y = (point_par-segment[0][X])*segment_gradient + segment[0][Y]
    if 'log' in interp and 'y' in interp: intercept_y=math.exp(intercept_y)
    return  intercept_y


mode_lookup = {
        'radial': {
            'parameter': theta,
            'value': radius,
            'interpolate': interpolate_radial,
            },
        'x': {
            'parameter': x_coord,
            'value': y_coord,
            'interpolate': interpolate_y,
            },
        'y': {
            'parameter': y_coord,
            'value': x_coord,
            'interpolate': interpolate_x,
            },
        }


def find_segment_indices(mode,point_par,coords):
    try:
        second_point= next(c_point for c_point in coords if not
                 mode_lookup[mode]['parameter'](c_point) < point_par )
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
        value = mode_lookup[mode]['interpolate'](point_par, segment,interp)
    return value

def get_contour_value(point_par, mode, coords, interp, extrap):
    value=None
    min_par=mode_lookup[mode]['parameter'](coords[0])
    max_par=mode_lookup[mode]['parameter'](coords[-1])
    if point_par < min_par and extrap.get('min'):
        value=extrap_lookup['min'][extrap['min']](mode,coords)
    elif min_par <= point_par and point_par <= max_par:
        value=interpolate(mode, point_par, coords,interp)
    elif point_par > max_par and extrap.get('max'):
        value=extrap_lookup['max'][extrap['max']](mode,coords)
    return value


class Contour(object):
    #FIXME: This class does the job now, but may need some work
    #  It is looking a bit messy now, but for the moment it is sufficient.
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
        point_par   = mode_lookup[self.mode]['parameter'](point)
        point_value = mode_lookup[self.mode]['value'](point)
        cont_value  = get_contour_value(point_par, self.mode, self.coords, self.interp, self.extrap)
        if cont_value:
            point_ratio=point_value/cont_value
        return point_ratio

    def get_contour_value(self,par):
        return get_contour_value(par, self.mode, self.coords, self.interp, self.extrap)
