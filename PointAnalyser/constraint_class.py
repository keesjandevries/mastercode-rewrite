class constraint(object):
    # example constraint([('MASS','Mh0')],[125.0, 1.0, 1.5], GAUSS )
    def __init__(self,pred_id,meas,func):
        self.pred_id    =   pred_id
        self.meas       =   self.init_meas(meas) # could involve reading in a file
        self.func       =   func
    def get_chi2(self,pred_dict):
        preds=[pred_dict[id1][id2] for id1, id2 in self.pred_id ]
        return self.func(self.meas, preds )
    def init_meas(self,meas):
        #for gaussian, it's simple:
        return meas


