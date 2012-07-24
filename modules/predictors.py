def get_predictor_module(predictor):
    return __PREDICTORS.get(predictor,
                            'interfaces/{name}'.format(name=predictor))
