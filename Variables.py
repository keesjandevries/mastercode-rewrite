#This file contains a dictionary with all the id's of observables
#used in MC++. Functions should only ever have deal with these id's
#Data from e.g. a point has the structure {id:value, ...}
#examples of id's are
#1) ('slha',('block',(indices),slhalib_nr)))
#2) ('BPhysics','Bsmm')
#
#1) completely defines the slha handles. Note that we have to be
# very careful with the slhalib_nr. We need a script that compares
# the id's. It is important that the slha id can directly be used in
# the slha class, and set
#2) (predictor, specification) is a reasonable way to do this

# in order to get the names of the predictors
from ObsCalculator.interfaces import softsusy
from ObsCalculator.interfaces import feynhiggs, micromegas, superiso, bphysics, lspscat
from ObsCalculator.interfaces import susypope

#for short names corresponding to slha: do use the slha lib comments 
def get_ids():
    ids={
        'Mh0'       :(feynhiggs.name,   'mh'),
        'mstau1'    :('slha',('MASS',   (2000004),  123)),
        'Af(1,1)'   :('slha',('AE',     (1,1),      225)), #FIXME: this number seems wrong
        'mtop'      :('SMINPUTS','Mt'),
        'mh'        :('MASS','Mh0'),
        'm0'        :('MINPAR', 'M0'), 
        'm12'       :('MINPAR', 'M12'),
        'mA'        :('MASS','MA0'),
        'tanb'      :('MINPAR','TB'),
        'mneu1'     :('MASS','MNeu(1)'),
        'ssiKO'     :(lspscat.name,'s3out'),
        'bsmmBP'    :(bphysics.name,'Psll'),
        }
    return ids
