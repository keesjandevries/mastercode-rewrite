from math import sqrt
def gauss(point, mu, sigma):
    x = point[0]
    return ((x-mu)/sigma)**2

def higgs_gauss(point, mu, sigma):
    mh = point[0]
    dmh = point[1]
    sigma=sqrt(sigma**2 + dmh**2)
    return ((mh-mu)/sigma)**2


def ratio_gauss(point, mu, sigma):
    x1 = point[0]
    x2 = point[1]
    x=x1/x2
    return ((x-mu)/sigma)**2

def bsmm_ratio_gauss(point,mu,sigma):
    x=point[0]/3.46e-9
    return ((x-mu)/sigma)**2

def upperlimit(point, mu, sigma):
    chi2 = 0
    x = point[0]
    if x > mu:
        chi2 = gauss(point,mu,sigma)
    else:
        chi2 = 0
    return chi2

def lowerlimit(point, mu, sigma):
    chi2 = 0
    x = point[0]
    if x < mu:
        chi2 = gauss(point,mu,sigma)
    else:
        chi2 = 0
    return chi2

def asymmetric_gauss(point,mu,sigma_plus,sigma_min):
    chi2=0
    x=point[0]
    if x < mu:
        chi2=gauss(point,mu,sigma_min)
    elif x > mu:
        chi2=gauss(point,mu,sigma_plus)
    return chi2

def abs_lowerlimit(point, mu, sigma):
    chi2 = 0
    x = abs(point[0])
    if x < mu:
        chi2 = gauss(point,mu,sigma)
    else:
        chi2 = 0
    return chi2

def multi_lowerlimit(point, mu, sigma):
    chi2 = 0
    x = min(point)
    if x < mu:
        chi2 = gauss([x],mu,sigma)
    else:
        chi2 = 0
    return chi2

# other function
def neutralino_lsp(point): # FIXME: mu and sigma are not right
    #point[0] is the neutralino
    return sum([ (abs(mass)-abs(point[0]))**2 for mass in point  if (abs(mass) < abs(point[0]))] )


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

