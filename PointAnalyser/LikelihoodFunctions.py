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
def power_n_inv_scaling(bc, r,n):
    return bc*((1./r)**n)

def power_n_scaling(bc, r,n):
    return bc*(r**n)

def power_4_inv_single_contour(point, contour):
    chi2=0.
    r = contour.point_ratio(point)
    if r is not None:
        chi2=power_n_inv_scaling(contour.chi2, r,4)
    return chi2

def power_2_single_contour(point,contour):
    r = contour.point_ratio(point)
    return power_n_scaling(contour.chi2,r,2)

def power_2_single_ma_tanb(point,contour):
    chi2=0.
    r = contour.point_ratio(point)
    if r:
        chi2=power_n_scaling(contour.chi2,r,2)
    return chi2

def xenon100_jul_2012(point,contour):
    chi2=0.
    r = contour.point_ratio(point)
    if r is not None:
        N = r*5.1   # the number of events on the line times the x-section ratio
        mu = 1.     # these numbers were calculated by Jad
        sigma = 2.7 #
        chi2=gauss([N],mu,sigma)
    else:
        print("WARNING: no valid point ratio. Chi2 is set to 0.")
    return chi2 

def one_dim_chi2_lookup(point,contour):
    chi2=0.
    par=point[0]
    x2=contour.get_contour_value(par)
    if x2 is not None:
        chi2=x2
    else:
        print("WARNING: problem with parameter lookup. Chi2 is set to 0.")
    return chi2

