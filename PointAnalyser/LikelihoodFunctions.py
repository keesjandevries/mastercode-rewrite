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

# contour likelihood functions
def power_4_scaling(bc, r):
    return bc*((1./r)**4)
