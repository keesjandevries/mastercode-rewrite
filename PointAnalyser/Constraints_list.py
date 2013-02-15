from PointAnalyser import LikelihoodFunctions as LF
from PointAnalyser.Constraints import Constraint

constraints_dict = {
############################# NUISANCE #######################
        'Mt': {
            'oids' : [('SMINPUTS', 'Mt')],
            'data' : [173.2,0.9], 
            'func' : LF.gauss },
        'MZ' :{ 
            'oids' : [('SMINPUTS','MZ')],
            'data' : [91.1875  ,0.0021],  
            'func' : LF.gauss      ,},
        'GZ_in': {   
            'oids': [('SUSY-POPE','GZ_in')],
            'data': [2.4952, 0.0023],
            'func': LF.gauss},
        'DAlpha_had': {   
            'oids': [('SUSY-POPE', 'DAlpha_had_in')],
            'data': [0.02749, 0.0001],
            'func': LF.gauss},
############################# SUSY-POPE ######################
        'Ab': {   
            'oids': [('SUSY-POPE', 'Ab')],
            'data': [0.923, 0.02],
            'func': LF.gauss},
        'Ac': {  
            'oids': [('SUSY-POPE', 'Ac')],
            'data': [0.67, 0.027],
            'func': LF.gauss},
        'Afb(b)': {   
            'oids': [('SUSY-POPE', 'Afb_b')],
            'data': [0.0992, 0.0016],
            'func': LF.gauss},
        'Afb(c)': {   
            'oids': [('SUSY-POPE', 'Afb_c')],
            'data': [0.0707, 0.0035],
            'func': LF.gauss},
        'Al(P_tau)': {   
            'oids': [('SUSY-POPE', 'Al')],
            'data': [0.1465, 0.0032],
            'func': LF.gauss},
        'Al(SLD)': {   
            'oids': [('SUSY-POPE', 'Al')],
            'data': [0.1513, 0.0021],
            'func': LF.gauss},
        'Afb_l': {   
            'oids': [('SUSY-POPE', 'Afb_l')],
            'data': [0.01714, 0.00095],
            'func': LF.gauss},
        'D_0(K*g)': {   
            'oids': [('SuperISO', 'SId0')],
            'data': [0.028, 0.023, 0.024],
            'func': LF.gauss},
        'Gamma_Z': {   
            'oids': [('SUSY-POPE', 'Gamma_z')],
            'data': [2495.2, 2.3, 1.0],
            'func': LF.gauss},
        'MW': {   
            'oids': [('SUSY-POPE', 'MW')],
            'data': [80.385, 0.015, 0.01],
            'func': LF.gauss},
        'MW-mc-old': {   
            'oids': [('SUSY-POPE', 'MW')],
            'data': [80.399, 0.023, 0.01],
            'func': LF.gauss},
        'sintheta_eff': {   
            'oids': [('SUSY-POPE', 'sin_theta_eff')],
            'data': [0.2324, 0.0012],
            'func': LF.gauss},
        'Rb': {   
            'oids': [('SUSY-POPE', 'Rb')],
            'data': [0.21629, 0.00066],
            'func': LF.gauss},
        'Rc': {   
            'oids': [('SUSY-POPE', 'Rc')],
            'data': [0.1721, 0.003],
            'func': LF.gauss},
        'Rl': {   
            'oids': [('SUSY-POPE', 'Rl')],
            'data': [20.767, 0.025],
            'func': LF.gauss},
        'sigma_had^0': {   
            'oids': [('SUSY-POPE', 'sigma_had')],
            'data': [41.54, 0.037],
            'func': LF.gauss},
############################################# FH #######################################
        'Higgs125': {
            'oids' :[('FeynHiggs', 'mh')], 
            'data' : [125.,1.0,1.5], 
            'func' : LF.gauss},
        'HiggsLEP': {   
            'oids': [('FeynHiggs', 'mh')],
            'data': [115.0, 1.0, 1.5],
            'func': LF.lowerlimit},
        'gminus2mu': {   
            'oids': [('FeynHiggs','gm2')],
            'data': [3.02e-09, 8.8e-10, 2e-10],
            'func': LF.gauss},
########################################### MICROMEGAS #################################
        'Oh^2': {   
            'oids': [('Micromegas', 'Omega')],
            'data': [0.1120, 0.0056, 0.012],
            'func': LF.gauss},
        'Oh^2-9-years': {   
            'oids': [('Micromegas', 'Omega')],
            'data': [0.1138, 0.0056, 0.012],
            'func': LF.gauss,
            'info': '1212.5226 table2 9-years'},
########################################### BPHYSICS ###################################        
        'BR(Bd->ll)': {   
            'oids': [('BPhysics', 'Pdll')],
            'data': [2.3e-08, 0.0, 2e-10],
            'func': LF.upperlimit},
        'Bsmumu': {   
            'oids': [('BPhysics', 'Psll')],
            'data': [4.6e-08, 1e-10, 2e-10],
            'func': LF.upperlimit},
        'Bsmumu_test': {   
            'oids': [('BPhysics', 'Psll')],
            'data': [2.3e-09, 1.73e-09],
            'func': LF.upperlimit},
        'R(B->Xsll)': {   
            'oids': [('BPhysics', 'BRXsll')],
            'data': [0.99, 0.32, 0.0],
            'func': LF.gauss},
        'R(B->taunu)': {   
            'oids': [('BPhysics', 'BRbtn')],
            'data': [1.43, 0.43],
            'func': LF.gauss},
        'R(D_ms)': {   
            'oids': [('BPhysics', 'RDMs')],
            'data': [0.97, 0.01, 0.27],
            'func': LF.gauss},
        'R(Delta_md)': {   
            'oids': [('BPhysics', 'RDMb')],
            'data': [1.05, 0.01, 0.34],
            'func': LF.gauss},
        'R(Delta_mk)': {   
            'oids': [('BPhysics', 'RDMK')],
            'data': [1.08, 0.0, 0.14],
            'func': LF.gauss},
        'R(Dms)/R(Dmd)': {   
            'oids': [('BPhysics', 'RDMs'),('BPhysics', 'RDMb')],
            'data': [1.0, 0.01, 0.13],
            'func': LF.ratio_gauss}, #FIXME: here's a function is needed that takes the ratio of these two :)
        'R(K->lnu)': {   
            'oids': [('BPhysics', 'BRKl2')],
            'data': [1.008, 0.014],
            'func': LF.gauss},
        'R(Kp->pinn)': {   
            'oids': [('BPhysics', 'BRKpnn')],
            'data': [4.5, 0.01],
            'func': LF.upperlimit},
        'R(b->sg)': {   
            'oids': [('BPhysics', 'BRbsg')],
            'data': [1.117, 0.12],
            'func': LF.gauss},
########################################### CONSTRAINTS FROM LIKELIHOODS ###############        
        'M0M12': {
            'oids': [('MINPAR', 'M0'),('MINPAR', 'M12')],
            'data': [('PointAnalyser/m0m12.txt', 'radial', 0.95, 2,'linear')],
            'func': LF.power_4_inv_single_contour, 
            'mode': 'contour'},
        'MATANB' : {
            'oids': [('FeynHiggs', 'mA'),('MINPAR', 'TB')],
            'data': [('PointAnalyser/matanb.txt','x',0.95,2,'linear',{'min':'flat'})],
            'func': LF.power_2_single_ma_tanb, 
            'mode': 'contour' },
        'xenon100':{
            'oids': [('MASS', 'MNeu(1)'),('LSP scattering','s3out')],
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
