from math import sqrt

from PointAnalyser.Contours import Contour

class Constraint(object):
    def __init__(self, ids, data, func, mode='simple'):
        """ 
In the case of from_files = True:
    args = [ ('filename', pval), ... ]
Otherwise,
    args = [ fixed inputs for func ]
        """ 
        self._ids = ids
        self._func = func
        if mode is 'simple':
            self._data = [data[0],sqrt(sum([d**2 for d in data[1:]]))]
        else:
            self._data = [ Contour(*arg) for arg in data ]
            for contour in self._data:
                assert contour.dim == len(ids)

    def get_chi2(self, point):
        #  collect necessary ids
        chi2 = 0
        try:
            for (block, name) in self._ids:
                f_inputs = tuple([point[block][name]
                    for (block,name) in self._ids])
        except KeyError:
            print('ERROR: Provided invalid input set {0}'.format(self._ids))
            print('\tSetting chi2 to 0 for this constraint')
        except TypeError:
            print('ERROR: Please provide dictionary that can be accessed using point[id1][id2]')
            print('\tSetting chi2 to 0 for this constraint')
        else:
            args = [f_inputs] + self._data
            chi2 = self._func(*args)
        return chi2

