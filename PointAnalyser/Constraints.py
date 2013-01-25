from math import sqrt

from PointAnalyser.Contour import Contour

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
                point_values = tuple([point[pred_id]
                    for pred_id in self._ids])
        except KeyError:
            print('ERROR: Provided invalid input set {0}'.format(self._ids))
            print('\tSetting chi2 to 0 for this constraint')
        except TypeError:
            print('ERROR: Please provide dictionary that can be accessed using point[id1][id2]')
            print('\tSetting chi2 to 0 for this constraint')
        else:
            try:
                args = [point_values] + self._data
                chi2 = self._func(*args)
            except UnboundLocalError:
                print("ERROR: no ids were specified")
                print('\tSetting chi2 to 0 for this constraint')
        return chi2

