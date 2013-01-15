from PointAnalyser import LikelihoodFunctions as LF
from PointAnalyser.Constraints import Constraint

constraints = {
        'Mt': Constraint([('SMINPUTS','Mt')], [173.2,0.9], LF.gauss),
        'Higgs125': Constraint([('MASS','Mh0')], [125.,1.0,1.5], LF.gauss),
        'M0M12': Constraint([('MINPAR', 'M0'), ('MINPAR', 'M12')],
            [('PointAnalyser/m0m12.txt', 'radial', 0.95, 2,'linear')],
            LF.power_4_inv_single_contour, mode='contour'),
        'MATANB' : Constraint([('MASS','MA0'),('MINPAR','TB')],
            [('PointAnalyser/matanb.txt','x',0.95,2,'linear',{'min':'flat'})],
            LF.power_2_single_ma_tanb, mode='contour' ),
        'xenon100':Constraint([('MASS','MNeu(1)'),('LSP scattering','s3out')],
            [('PointAnalyser/xenon100.txt','x',0.9,2,'logxy',{'min':'flat','max':'flat'})],
            LF.xenon100_jul_2012, mode='contour' ),
        'bsmm':Constraint([('BPhysics','Psll')],
            [('PointAnalyser/bsmm.txt','x',0.9,1,'linear',{'max':'flat'})],
            LF.one_dim_chi2_lookup, mode='contour' ),
       }
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