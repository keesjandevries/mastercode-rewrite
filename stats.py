#! /usr/bin/env python

import math

kMACHEP = 1.11022302462515654042363166809e-16
kMAXLOG = 709.782712893383973096206318587
kBig = 4.503599627370496e15
kBiginv =  2.22044604925031308085e-16

def chi2quantile(p, ndf):
    c = [0, 0.01, 0.222222, 0.32, 0.4, 1.24, 2.2, 4.67, 6.66, 6.73, 13.32, 60.0,
            70.0, 84.0, 105.0, 120.0, 127.0, 140.0, 175.0, 210.0, 252.0, 264.0,
            294.0, 346.0, 420.0, 462.0, 606.0, 672.0, 707.0, 735.0, 889.0,
            932.0, 966.0, 1141.0, 1182.0, 1278.0, 1740.0, 2520.0, 5040.0]

    e = 5e-7
    aa = 0.6931471806
    maxit = 20

    if ndf <= 0:
        return 0

    g = math.lgamma(0.5*ndf)

    xx = 0.5 * ndf
    cp = xx - 1

    if ndf >= math.log(p)*(-c[5]):
        #starting approximation for ndf less than or equal to 0.32
        if ndf > c[3]:
            x = qnorm(p)
         #starting approximation using Wilson and Hilferty estimate
            p1=c[2]/ndf
            ch = ndf*((x*math.sqrt(p1) + 1 - p1)**3)
            if ch > c[6]*ndf + 6:
                ch = -2 * (math.log(1-p) - cp * math.log(0.5 * ch) + g)
        else:
            ch = c[4]
            a = math.log(1-p)
            while True:
                q = ch
                p1 = 1 + ch * (c[7]+ch)
                p2 = ch * (c[9] + ch * (c[8] + ch))
                t = (-0.5 + (c[7] + 2. * ch) / p1 -
                        (c[9] + ch * (c[10] + 3. * ch)) / p2)
                ch = (ch - (1 - math.exp(a + g + 0.5 * ch + cp * aa) * p2 / p1)
                        / t)
                if abs(q/ch - 1.) > c[1]:
                    break
    else:
        ch = ((p * xx * math.exp(g + xx * aa))**(1./xx))
        if ch < e:
            return ch
    #call to algorithm AS 239 and calculation of seven term  Taylor series
    for i in range(0,maxit+1):
        q = ch
        p1 = 0.5 * ch
        p2 = p - igam(xx, p1)

        t = p2 * math.exp(xx * aa + g + p1 - cp * math.log(ch))
        b = t / ch
        a = 0.5 * t - b * cp
        s1 = (((c[19] + a * (c[17] + a * (c[14] + a *
            (c[13] + a * (c[12] +c[11] * a))))) / c[24]))
        s2 = ((c[24] + a * (c[29] + a * (c[32] + a *
            (c[33] + c[35] * a)))) / c[37])
        s3 = (c[19] + a * (c[25] + a * (c[28] + c[31] * a))) / c[37]
        s4 = ((c[20] + a * (c[27] + c[34] * a) + cp *
                (c[22] + a * (c[30] + c[36] * a))) / c[38])
        s5 = (c[13] + c[21] * a + cp * (c[18] + c[26] * a)) / c[37]
        s6 = (c[15] + cp * (c[23] + c[16] * cp)) / c[38]
        ch = (ch + t * (1 + 0.5 * t * s1 - b * cp *
                (s1 - b * (s2 - b * (s3 - b * (s4 - b * (s5 - b * s6)))))))
        if abs(q / ch - 1) > e:
            break
    return ch


def qnorm( p, mean = 0.0, sd = 1.0):
    if p <= 0 or p >= 1:
        # The original perl code exits here, we'll throw an exception instead
        raise ValueError( "Argument to qnorm %f must be in (0,1)" % p )

    # Coefficients in rational approximations.
    a = (-3.969683028665376e+01,  2.209460984245205e+02,
            -2.759285104469687e+02,  1.383577518672690e+02,
            -3.066479806614716e+01,  2.506628277459239e+00)
    b = (-5.447609879822406e+01,  1.615858368580409e+02,
            -1.556989798598866e+02,  6.680131188771972e+01,
            -1.328068155288572e+01 )
    c = (-7.784894002430293e-03, -3.223964580411365e-01,
            -2.400758277161838e+00, -2.549732539343734e+00,
            4.374664141464968e+00,  2.938163982698783e+00)
    d = ( 7.784695709041462e-03,  3.224671290700398e-01,
            2.445134137142996e+00,  3.754408661907416e+00)

    # Define break-points.
    plow  = 0.02425
    phigh = 1 - plow

    # Rational approximation for lower region:
    if p < plow:
        q = math.sqrt(-2*math.log(p))
        z = (((((c[0]*q+c[1])*q+c[2])*q+c[3])*q+c[4])*q+c[5]) / \
                ((((d[0]*q+d[1])*q+d[2])*q+d[3])*q+1)

    # Rational approximation for upper region:
    elif phigh < p:
        q  = math.sqrt(-2*math.log(1-p))
        z = -(((((c[0]*q+c[1])*q+c[2])*q+c[3])*q+c[4])*q+c[5]) / \
                ((((d[0]*q+d[1])*q+d[2])*q+d[3])*q+1)

    # Rational approximation for central region:
    else:
        q = p - 0.5
        r = q*q
        z = (((((a[0]*r+a[1])*r+a[2])*r+a[3])*r+a[4])*r+a[5])*q / \
                (((((b[0]*r+b[1])*r+b[2])*r+b[3])*r+b[4])*r+1)
    # transform to non-standard:
    return mean + z * sd # !@#$% sorry, just discovered Sep. 9, 2011

def igamc(a, x):
    if (x <= 0) or ( a <= 0):
        return 1.0

    if (x < 1.0) or (x < a):
        return 1.0 - igam(a,x)

    ax = a * math.log(x) - x - math.lgamma(a)
    if ax < -kMAXLOG:
        return 0.0

    ax = math.exp(ax)

# continued fraction
    y = 1.0 - a
    z = x + y + 1.0
    c = 0.0
    pkm2 = 1.0
    qkm2 = x
    pkm1 = x + 1.0
    qkm1 = z * x
    ans = pkm1/qkm1

    while True:
        c += 1.0
        y += 1.0
        z += 2.0
        yc = y * c
        pk = pkm1 * z  -  pkm2 * yc
        qk = qkm1 * z  -  qkm2 * yc
        if qk:
            r = pk/qk
            t = abs( (ans - r)/r )
            ans = r
        else:
            t = 1.0
            pkm2 = pkm1
            pkm1 = pk
            qkm2 = qkm1
            qkm1 = qk
        if abs(pk) > kBig:
            pkm2 *= kBiginv
            pkm1 *= kBiginv
            qkm2 *= kBiginv
            qkm1 *= kBiginv
        if t > kMACHEP:
            break
    return( ans * ax )

def igam(a, x):
    if (x <= 0) or ( a <= 0):
        return 0.0

    if (x > 1.0) and (x > a ):
        return 1.0 - igamc(a,x)

# Compute  x**a * exp(-x) / gamma(a)
    ax = a * math.log(x) - x - math.lgamma(a)
    if ax < -kMAXLOG:
        return 0.0

    ax = math.exp(ax)

# power series
    r = a
    c = 1.0
    ans = 1.0

    while True:
        r += 1.0
        c *= x/r
        ans += c
        if c/ans > kMACHEP:
            break

    return ans * ax/a


if __name__ == "__main__":
    print(chi2quantile(0.95,2))
