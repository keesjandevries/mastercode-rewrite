def get(name=None):
    if name is None:
        return predictors['default']
    else:
        return predictors[name]

#module names
softsusy='ObsCalculator.interfaces.softsusy'
feynhiggs='ObsCalculator.interfaces.feynhiggs'
micromegas='ObsCalculator.interfaces.micromegas'
bphysics='ObsCalculator.interfaces.bphysics'
susypope='ObsCalculator.interfaces.susypope'
lspscat='ObsCalculator.interfaces.lspscat'
superiso='ObsCalculator.interfaces.superiso'

#collectoins of predictors
predictors={
        'default':{
            'spectrum_generator':softsusy,
            'spectrum_modifiers':[feynhiggs],
            'predictors':[feynhiggs,micromegas,bphysics,susypope,lspscat],
            },
        'public':{
            'spectrum_generator':softsusy,
            'spectrum_modifiers':[feynhiggs],
            'predictors':[feynhiggs,micromegas,superiso],
            },
        }
