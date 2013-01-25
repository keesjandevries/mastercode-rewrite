from PointAnalyser import LikelihoodFunctions as LF
from PointAnalyser.Constraints import Constraint

constraints_dict = {
        'Mt': {
            'oids' : [('slha', ('SMINPUTS', 'Mt'))],
            'data' : [173.2,0.9], 
            'func' : LF.gauss },
        'Higgs125': {
            'oids' :[('FeynHiggs', 'mh')], 
            'data' : [125.,1.0,1.5], 
            'func' : LF.gauss},
        'MZ' : 
            'oids' : [('slha',('SMINPUTS','MZ'))],
            'data' : [91.1875,  ,0.0021],  
            'func' : LF.gauss      ),
        'Ab16': {   
            'oids': [],
            'data': [0.923, 0.02],
            'func': LF.gauss},
        'Ac17': {  
            'oids': [],
            'data': [0.67, 0.027],
            'func': LF.gauss},
        'Afb(b)': {   
            'oids': [],
            'data': [0.0992, 0.0016],
            'func': LF.gauss},
        'Afb(c)': {   
            'oids': [],
            'data': [0.0707, 0.0035],
            'func': LF.gauss},
        'Al(P_tau)': {   
            'oids': [],
            'data': [0.1465, 0.0032],
            'func': LF.gauss},
        'Al(SLD)': {   
            'oids': [],
            'data': [0.1513, 0.0021],
            'func': LF.gauss},
        'Al_fb': {   
            'oids': [],
            'data': [0.01714, 0.00095],
            'func': LF.gauss},
        'BR(Bd->ll)': {   
            'oids': [],
            'data': [2.3e-08, 0.0, 2e-10],
            'func': 'LF.upperlimit'},
        'BR(b->sg)': {   
            'oids': [],
            'data': [1.117, 0.12],
            'func': LF.gauss},
        'Bsmumu': {   
            'oids': [],
            'data': [4.6e-08, 1e-10, 2e-10],
            'func': 'LF.upperlimit'},
        'Bsmumu_test': {   
            'oids': [],
            'data': [2.3e-09, 1.73e-09],
            'func': 'LF.upperlimit'},
        'DAlpha_had': {   
            'oids': [],
            'data': [0.02749, 0.0001],
            'func': LF.gauss},
        'D_0(K*g)': {   
            'oids': [],
            'data': [0.028, 0.023, 0.024],
            'func': LF.gauss},
        'GZ_in': {   
            'oids': [],
            'data': [2.4952, 0.0023],
            'func': LF.gauss},
        'Gamma_Z': {   
            'oids': [],
            'data': [2495.2, 2.3, 1.0],
            'func': LF.gauss},
        'MW': {   
            'oids': [],
            'data': [80.385, 0.015, 0.01],
            'func': LF.gauss},
        'Mh0': {   
            'oids': [],
            'data': [125.0, 1.0, 1.5],
            'func': LF.gauss},
        'Oh^2': {   
            'oids': [],
            'data': [0.1109, 0.0056, 0.012],
            'func': LF.gauss},
        'R(B->Xsll)': {   
            'oids': [],
            'data': [0.99, 0.32, 0.0],
            'func': LF.gauss},
        'R(B->taunu)': {   
            'oids': [],
            'data': [1.43, 0.43],
            'func': LF.gauss},
        'R(D_ms)': {   
            'oids': [],
            'data': [0.97, 0.01, 0.27],
            'func': LF.gauss},
        'R(Delta_md)': {   
            'oids': [],
            'data': [1.05, 0.01, 0.34],
            'func': LF.gauss},
        'R(Delta_mk)': {   
            'oids': [],
            'data': [1.08, 0.0, 0.14],
            'func': LF.gauss},
        'R(Dms)/R(Dmd)': {   
            'oids': [],
            'data': [1.0, 0.01, 0.13],
            'func': LF.gauss},
        'R(K->lnu)': {   
            'oids': [],
            'data': [1.008, 0.014],
            'func': LF.gauss},
        'R(Kp->pinn)': {   
            'oids': [],
            'data': [4.5, 0.01],
            'func': 'LF.upperlimit'},
        'R(b->sg)': {   
            'oids': [],
            'data': [1.117, 0.12],
            'func': LF.gauss},
        'Rb': {   
            'oids': [],
            'data': [0.21629, 0.00066],
            'func': LF.gauss},
        'Rc': {   
            'oids': [],
            'data': [0.1721, 0.003],
            'func': LF.gauss},
        'Rl': {   
            'oids': [],
            'data': [20.767, 0.025],
            'func': LF.gauss},
        'gminus2mu': {   
            'oids': [],
            'data': [3.02e-09, 8.8e-10, 2e-10],
            'func': LF.gauss},
        'sigma_had^0': {   
            'oids': [],
            'data': [41.54, 0.037],
            'func': LF.gauss},
        'sintheta_eff': {   
            'oids': [],
            'data': [0.2324, 0.0012],
            'func': LF.gauss}}
        ###################################################################
        'M0M12': {
            'oids': [('slha', ('MINPAR', 'M0')),('slha', ('MINPAR', 'M12'))],
            'data': [('PointAnalyser/m0m12.txt', 'radial', 0.95, 2,'linear')],
            'func': LF.power_4_inv_single_contour, 
            'mode': 'contour'},
        'MATANB' : {
            'oids': [('FeynHiggs', 'mA'),('slha', ('MINPAR', 'TB'))],
            'data': [('PointAnalyser/matanb.txt','x',0.95,2,'linear',{'min':'flat'})],
            'func': LF.power_2_single_ma_tanb, 
            'mode': 'contour' },
        'xenon100':{
            'oids': [('slha', ('MASS', 'MNeu(1)')),('LSP scattering','s3out')],
            'data': [('PointAnalyser/xenon100.txt','x',0.9,2,'logxy',{'min':'flat','max':'flat'})],
            'func': LF.xenon100_jul_2012, 
            'mode': 'contour' },
        'bsmm':{
            'oids': [('BPhysics','Psll')],
            'data': [('PointAnalyser/bsmm.txt','x',0.9,1,'linear',{'max':'flat'})],
            'func': LF.one_dim_chi2_lookup, 
            'mode': 'contour' },
       }

constraints={ name: Constraint(kwargs['oids'], kwargs['data'], kwargs['func'], kwargs.get('mode','simple')) 
        for name, kwargs in constraints_dict.items()  }
        #'Mt':           : [173.2,    ,0.9],             LF.gauss      ),
        #"MZ"            : [91.1875,  ,0.0021],          LF.gauss      ),
        #"GZ_in"         : [2.4952,   ,0.0023],          LF.gauss      ),
        #"DAlpha_had"    : [0.027490, ,0.0001],          LF.gauss      ),
        #"R(b->sg)"      : [1.117,    ,0.12],            LF.gauss      ),
        #"R(D_ms)"       : [0.97,     ,0.01, 0.27],      LF.gauss      ),
        #"Bsmumu"        : [4.6E-8,   ,0.1E-9, 0.2E-9],  LF.upperlimit ),
        #"Bsmumu_test"   : [2.3E-9,   ,1.73E-9],         LF.upperlimit ),
        #"R(B->taunu)"   : [1.43,     ,0.43],            LF.gauss      ),
        #"R(B->Xsll)"    : [0.99,     ,0.32, 0.00],      LF.gauss      ),
        #"R(K->lnu)"     : [1.008,    ,0.014 ],          LF.gauss      ),
        #"gminus2mu"     : [30.2E-10, ,8.8E-10, 2.0E-10],LF.gauss      ),
        #"MW"            : [80.385,   ,0.015, 0.01],     LF.gauss      ),
        #"sintheta_eff"  : [0.2324,   ,0.0012],          LF.gauss      ),
        #"Gamma_Z"       : [2495.2,   ,2.3, 1.0],        LF.gauss      ),
        #"Rl"            : [20.767,   ,0.025],           LF.gauss      ),
        #"Rb"            : [0.21629,  ,0.00066],         LF.gauss      ),
        #"Rc"            : [0.1721,   ,0.00300],         LF.gauss      ),
        #"Afb(b)"        : [0.0992,   ,0.0016],          LF.gauss      ),
        #"Afb(c)"        : [0.0707,   ,0.0035],          LF.gauss      ),
        #"Ab16"          : [0.923,    ,0.020],           LF.gauss      ),
        #"Ac17"          : [0.670,    ,0.027],           LF.gauss      ),
        #"Al(SLD)"       : [0.1513,   ,0.0021],          LF.gauss      ),
        #"Mh0"           : [125.0,    ,1.0, 1.5],        LF.gauss      ),
        #"Oh^2"          : [0.1109,   ,0.0056, 0.012],   LF.gauss      ),
        #"Al(P_tau)"     : [0.1465,   ,0.0032],          LF.gauss      ),
        #"Al_fb"         : [0.01714,  ,0.00095],         LF.gauss      ),
        #"sigma_had^0"   : [41.540,   ,0.037],           LF.gauss      ),
        #"R(Delta_md)"   : [1.05,     ,0.01, 0.34],      LF.gauss      ),
        #"R(Delta_mk)"   : [1.08,     ,0.00, 0.14],      LF.gauss      ),
        #"R(Kp->pinn)"   : [4.5,      ,0.01],            LF.upperlimit ),
        #"BR(Bd->ll)"    : [2.3E-8,   ,0.0, 0.2E-9],     LF.upperlimit ),
        #"R(Dms)/R(Dmd)" : [1.00,     ,0.01, 0.13],      LF.gauss      ),
        #"D_0(K*g)"      : [0.028,    ,0.023, 0.024],    LF.gauss      ),
        #"BR(b->sg)"     : [1.117,    ,0.12],            LF.gauss      ),
#        'Mt': Constraint([('slha', ('SMINPUTS', 'Mt'))], [173.2,0.9], LF.gauss),
#        'Higgs125': Constraint([('FeynHiggs', 'mh')], [125.,1.0,1.5], LF.gauss),
#        'M0M12': Constraint([('slha', ('MINPAR', 'M0')),('slha', ('MINPAR', 'M12'))],
#            [('PointAnalyser/m0m12.txt', 'radial', 0.95, 2,'linear')],
#            LF.power_4_inv_single_contour, mode='contour'),
#        'MATANB' : Constraint([('FeynHiggs', 'mA'),('slha', ('MINPAR', 'TB'))],
#            [('PointAnalyser/matanb.txt','x',0.95,2,'linear',{'min':'flat'})],
#            LF.power_2_single_ma_tanb, mode='contour' ),
#        'xenon100':Constraint([('slha', ('MASS', 'MNeu(1)')),('LSP scattering','s3out')],
#            [('PointAnalyser/xenon100.txt','x',0.9,2,'logxy',{'min':'flat','max':'flat'})],
#            LF.xenon100_jul_2012, mode='contour' ),
#        'bsmm':Constraint([('BPhysics','Psll')],
#            [('PointAnalyser/bsmm.txt','x',0.9,1,'linear',{'max':'flat'})],
#            LF.one_dim_chi2_lookup, mode='contour' ),
