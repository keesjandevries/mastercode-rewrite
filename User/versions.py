def get(name=None):
    if name is None:
        return {}
    else:
        return versions[name]

versions={
        'FH-beta-testing':{
            'FeynHiggs':['2.8.6','2.8.7','2.9.5','2.9.5.r3456v3'],
            }
        }
