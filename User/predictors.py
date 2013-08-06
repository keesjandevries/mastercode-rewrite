def get(name=None):
    if name is None:
        return predictors['default']
    else:
        return predictors[name]

#module names
softsusy='ObsCalculator.interfaces.softsusy'
feynhiggs='ObsCalculator.interfaces.feynhiggs'
micromegas='ObsCalculator.interfaces.micromegas'

#collectoins of predictors
predictors={
        'default':{
            'spectrum_generator':softsusy,
            'spectrum_modifiers':[feynhiggs],
            'predictors':[feynhiggs,micromegas],
            }
        }
