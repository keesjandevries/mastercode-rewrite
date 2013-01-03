import math

def load_contour(filename, mode='radial'):
    f = open(filename,'r')
    s_contour = [tuple(x.split()) for x in f.readlines()]
    f_contour = [(float(x), float(y)) for (x,y) in s_contour]
    f_contour.sort(key=mode_lookup[mode]['sort_key'])
    return f_contour

# this might actually be a good use for a class from now on... we'll see

# not convinced this is a good idea yet
X,Y = range(2)

# sort_modes for contours
def theta(point):
    return math.atan2(point[Y],point[X])

def x_coord(point):
    return point[X]

def y_coord(point):
    return point[Y]

def past_segment_theta(point, c_point):
    c_theta = math.atan2(c_point[Y], c_point[X])
    p_theta = math.atan2(point[Y], c_point[X])
    return p_theta > c_theta

def past_segment_x(point, c_point):
    return point[X]>c_point[X]

def past_segment_y(point, c_point):
    return point[Y]>c_point[Y]

def distance_ratio_radial(point, segment):
    point_gradient = point[Y]/point[X]
    segment_gradient = ((segment[1][Y] - segment[0][Y]) /
            (segment[1][X] - segment[0][X]))
    intercept_x = ((segment_gradient*segment[0][X] - segment[0][Y]) /
            (segment_gradient - point_gradient))
    intercept_y = point_gradient*intercept_x
    intercept_r = math.sqrt(intercept_x**2 + intercept_y**2)
    point_r = math.sqrt(point[X]**2 + point[Y]**2)
    return point_r/intercept_r

def distance_ratio_x(point, segment):
    segment_gradient = ((segment[1][Y] - segment[0][Y]) /
            (segment[1][X] - segment[0][X]))
    intercept_x = (point[Y]-segment[0][Y])*(1./segment_gradient) + segment[0][X]
    return point[X] / intercept_x

def distance_ratio_y(point, segment):
    segment_gradient = ((segment[1][Y] - segment[0][Y]) /
            (segment[1][X] - segment[0][X]))
    intercept_y = (point[X]-segment[0][X])*segment_gradient + segment[0][Y]
    return point[Y] / intercept_y

mode_lookup = {
        'radial': {
            'sort_key': theta,
            'range_test': past_segment_theta,
            'ratio': distance_ratio_radial,
            },
        'x': {
            'sort_key': x_coord,
            'range_test': past_segment_x,
            'ratio': distance_ratio_y,
            },
        'y': {
            'sort_key': y_coord,
            'range_test': past_segment_y,
            'ratio': distance_ratio_x,
            },
        }

def segment_range(point, contour, mode):
    try:
        range_end = next(c_point for c_point in contour if not
                mode_lookup[mode]['range_test'](point,c_point))
    except StopIteration:
        print("ERROR: Unable to find intercept for point {p}".format(p=point))
        segment_positions = None
    else:
        range_end_pos = contour.index(range_end)
        segment_positions = (range_end_pos-1, range_end_pos)
    return segment_positions

def point_ratio(self, point, mode):
    segment = segment_range(point, self.contour, self.mode)
    return mode_lookup[mode]['ratio'](point, segment)

class Contour(object):
    def __init__(self,filename, mode, pval):
        self.contour = load_contour(filename,mode)
        self.mode = mode
        self.pval = pval

    def point_ratio(self,point):
        segment_indices = segment_range(point, self.contour, self.mode)
        segment = (self.contour[segment_indices[0]],
                self.contour[segment_indices[1]])
        return mode_lookup[self.mode]['ratio'](point, segment)
