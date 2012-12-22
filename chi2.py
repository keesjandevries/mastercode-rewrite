import math

def gauss(x, mu, sigma):
    return ((x-mu)/sigma)**2


constraints = {
        'Mt': { 'value': 173.2, 'error': [0.9], 'func': gauss, },
        }

def get_chi2(prediction, value):
    chi2 = 0.
    if prediction in constraints:
        constraint = constraints[prediction]
        chi2 = constraint['func'](value, constraint['value'],
                math.sqrt(sum([x**2 for x in constraint['error']])))
    return chi2
