def load_contour(filename):
    f = open(filename,'r')
    s_contour = [tuple(x.split()) for x in f.readlines()]
    f_contour = [(float(x), float(y)) for (x,y) in s_contour]
    f_contour.sort()
    return f_contour

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
