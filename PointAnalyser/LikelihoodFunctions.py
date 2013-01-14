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
    r = contour.point_ratio(point)
    return power_n_inv_scaling(contour.chi2, r,4)

def power_2_single_contour(point,contour):
    r = contour.point_ratio(point)
    return power_n_scaling(contour.chi2,r,2)

def power_2_single_ma_tanb(point,contour):
    """
Need to catch the scenario where MA is not in the range.
if MA below range: take minimum MA
chi2=0 if MA above range
    """
    chi2=0.
    minma=contour.contour[0][0]
    maxma=contour.contour[-1][0]
    if point[0] < minma:
        point=(minma,point[1])
    if point[0] < maxma:
        r = contour.point_ratio(point)
        chi2=power_n_scaling(contour.chi2,r,2)
    return chi2
