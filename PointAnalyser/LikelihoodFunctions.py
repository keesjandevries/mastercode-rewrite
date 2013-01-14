def gauss(point, mu, sigma):
    x = point[0]
    return ((x-mu)/sigma)**2

def upperlimit(point, mu, sigma):
    chi2 = 0
    if x > mu:
        chi2 = gauss(point,mu,sigma)
    else:
        chi2 = 0
    return chi2

def lowerlimit(point, mu, sigma):
    chi2 = 0
    if x < mu:
        chi2 = gauss(point,mu,sigma)
    else:
        chi2 = 0
    return chi2

# contour likelihood functions
def power_4_scaling(bc, r):
    return bc*((1./r)**4)

def power_4_single_contour(point, contour):
    r = contour.point_ratio(point)
    return power_4_scaling(contour.chi2, r)
