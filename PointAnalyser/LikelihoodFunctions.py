import math
def load_contour(filename):
    f = open(filename,'r')
    s_contour = [tuple(x.split()) for x in f.readlines()]
    f_contour = [(float(x), float(y)) for (x,y) in s_contour]
    f_contour.sort()
    return f_contour

def passed_segment(x,y,cx,cy):
    c_theta = math.atan2(cy,cx)
    p_theta = math.atan2(y,x)
    return p_theta > c_theta

#           |
#           | <-
#           |   |
#   pi ----------- 0

def radial_segment_range(x,y,contour):
    range_end = next((cx,cy) for (cx,cy) in contour if not
            passed_segment(x,y,cx,cy))
    print(range_end)
    range_end_pos = contour.index(range_end)
    return (range_end_pos-1, range_end_pos+1)

def gauss(x, mu, sigma):
    return ((x-mu)/sigma)**2

def upperlimit(x, mu, sigma):
    chi2 = 0
    if x > mu:
        chi2 = gauss(x,mu,sigma)
    else:
        chi2 = 0
    return chi2

def lowerlimit(x, mu, sigma):
    chi2 = 0
    if x < mu:
        chi2 = gauss(x,mu,sigma)
    else:
        chi2 = 0
    return chi2
