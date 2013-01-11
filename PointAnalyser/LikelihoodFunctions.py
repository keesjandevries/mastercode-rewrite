import math
def gauss(meas,pred):
    x, mu, sigma=intern_get_x_mu_sigma(meas,pred)
    return intern_gauss(x,mu,sigma) 

def upperlimit(meas,pred):
    x, mu, sigma=intern_get_x_mu_sigma(meas,pred)
    chi2 = 0
    if x > mu:
        chi2 = inter_gauss(x,mu,sigma)
    else:
        chi2 = 0
    return chi2

def lowerlimit(meas,pred):
    x, mu, sigma=intern_get_x_mu_sigma(meas,pred)
    chi2 = 0
    if x < mu:
        chi2 = inter_gauss(x,mu,sigma)
    else:
        chi2 = 0
    return chi2

def intern_get_x_mu_sigma(meas,pred):
    assert len(pred) is 1
    assert len(meas) > 1
    x=pred[0]
    mu=meas[0]
    sigma= math.sqrt(sum([x**2 for x in meas[1:] ]))
    assert sigma is not 0.
    return x, mu , sigma 

def intern_gauss(x,mu,sigma):
    return ((x-mu)/sigma)**2
