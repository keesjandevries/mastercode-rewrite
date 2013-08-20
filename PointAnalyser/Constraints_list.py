from PointAnalyser import LikelihoodFunctions as LF
from PointAnalyser.Constraints import Constraint

constraints_dict = {
############################# MC-OLD-ONCE HARD-CODED #########
        'LEP-chargino':{
            'oids': [ ('MASS', 'MCha(1)'), ('MASS', 'MCha(2)')],
            'data': [103., 1.],
            'func': LF.multi_lowerlimit},
        'LEP-neutralino':{
            'oids': [ ('MASS', 'MNeu(1)')],
            'data': [50., 1.],
            'func': LF.lowerlimit},
        'LEP-neutralino-abs':{
            'oids': [ ('MASS', 'MNeu(1)')],
            'data': [50., 1.],
            'func': LF.abs_lowerlimit},
        'LEP-slepton':{
            'oids': [
                ('MASS', 'MSf(1,2,1)'),#se_L
                ('MASS', 'MSf(2,2,1)'),#se_R
                ('MASS', 'MSf(1,2,2)'),#smu_L
                ('MASS', 'MSf(2,2,2)'),#smu_R
                ('MASS', 'MSf(1,2,3)'),#stau_1
                ('MASS', 'MSf(2,2,3)'),#stau_2
                ],
            'data': [90., 1.],
            'func': LF.multi_lowerlimit},
        'LEP-sneutrino':{
            'oids': [
                ('MASS', 'MSf(1,2,1)'),#sneutrino_e
                ('MASS', 'MSf(1,2,2)'),#sneutrino_mu
                ('MASS', 'MSf(1,2,3)'),#sneutrino_tau
                ],
            'data': [90., 1.],
            'func': LF.multi_lowerlimit},
        'LEP-squark':{
            'oids': [
                ('MASS', 'MSf(1,3,1)'),#su_L
                ('MASS', 'MSf(2,3,1)'),#su_R
                ('MASS', 'MSf(1,3,2)'),#sc_L
                ('MASS', 'MSf(2,3,2)'),#sc_R
                ('MASS', 'MSf(1,3,3)'),#st_1
                ('MASS', 'MSf(2,3,3)'),#st_2
                ('MASS', 'MSf(1,4,1)'),#sd_L
                ('MASS', 'MSf(2,4,1)'),#sd_R
                ('MASS', 'MSf(1,4,2)'),#ss_L
                ('MASS', 'MSf(2,4,2)'),#ss_R
                ('MASS', 'MSf(1,4,3)'),#sb_1
                ('MASS', 'MSf(2,4,3)'),#sb_2
                ],
            'data': [90., 1.],
            'func': LF.multi_lowerlimit},
        'neutralino-lsp':{
            'oids': [
                #firt index should have the neutralino
                ('MASS', 'MNeu(1)'),   
                #charginos
                ('MASS', 'MCha(1)'),
                ('MASS', 'MCha(2)'),
                #sleptons
                ('MASS', 'MSf(1,2,1)'),#se_L
                ('MASS', 'MSf(2,2,1)'),#se_R
                ('MASS', 'MSf(1,2,2)'),#smu_L
                ('MASS', 'MSf(2,2,2)'),#smu_R
                ('MASS', 'MSf(1,2,3)'),#stau_1
                ('MASS', 'MSf(2,2,3)'),#stau_2
                #sneutrinos
                ('MASS', 'MSf(1,2,1)'),#sneutrino_e
                ('MASS', 'MSf(1,2,2)'),#sneutrino_mu
                ('MASS', 'MSf(1,2,3)'),#sneutrino_tau
                #squarks
                ('MASS', 'MSf(1,3,1)'),#su_L
                ('MASS', 'MSf(2,3,1)'),#su_R
                ('MASS', 'MSf(1,3,2)'),#sc_L
                ('MASS', 'MSf(2,3,2)'),#sc_R
                ('MASS', 'MSf(1,3,3)'),#st_1
                ('MASS', 'MSf(2,3,3)'),#st_2
                ('MASS', 'MSf(1,4,1)'),#sd_L
                ('MASS', 'MSf(2,4,1)'),#sd_R
                ('MASS', 'MSf(1,4,2)'),#ss_L
                ('MASS', 'MSf(2,4,2)'),#ss_R
                ('MASS', 'MSf(1,4,3)'),#sb_1
                ('MASS', 'MSf(2,4,3)'),#sb_2
                #gluino
                ('MASS','MGl'),
                ],
            'data' : [],
            'func' : LF.neutralino_lsp, 
            'mode' : 'neutralino-lsp' },
############################# NUISANCE #######################
        'Mt': {
            'oids' : [('SMINPUTS', 'Mt')],
            'data' : [173.2,0.9], 
            'func' : LF.gauss },
        'mc9_Mt': {
            'oids' : [('SMINPUTS', 'Mt')],
            'data' : [173.2,0.87], 
            'func' : LF.gauss,
            'info' : 'http://gfitter.desy.de/Figures/Standard_Model/2013_05_29_ShowFullFitTable_large.gif',
            'texname':r'$m_t$',
            'texvalue':r'$173.20\pm0.87$',
            },
        'MZ' :{ 
            'oids' : [('SMINPUTS','mod_MZ')],
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
        'mc9_DAlpha_had': {   
            'oids': [('SUSY-POPE', 'DAlpha_had_in')],
            'data': [0.02756, 0.0001],
            'func': LF.gauss,
            'info' : 'http://gfitter.desy.de/Figures/Standard_Model/2013_05_29_ShowFullFitTable_large.gif; \"rescaled due to alpha_s dependence\"',
            'texname':r'$\Delta\alpha_{had}^{(5)(M_{Z})}$',
            'texvalue':r'$0.02756\pm0.0001',
            },
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
        'mc9_Mh': {
            'oids' :[('FeynHiggs', 'mh'),('FeynHiggs','Dmh')], 
            'data' : [125.7,0.4], 
            'func' : LF.higgs_gauss,
            'info' : 'http://gfitter.desy.de/Figures/Standard_Model/2013_05_29_ShowFullFitTable_large.gif',
            'texname': r'$M_h$',
            'texvalue': r'$125.7\pm0.4\pm\Delta(M_h)_{FH}$',
            },
        'HiggsLEP': {   
            'oids': [('FeynHiggs', 'mh')],
            'data': [115.0, 1.1, 1.5],
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
        'Oh^2_mc8': {   
            'oids': [('Micromegas', 'Omega')],
            'data': [0.1109, 0.0056, 0.012],
            'func': LF.gauss},
        'mc9_Oh2': {   
            'oids': [('Micromegas', 'Omega')],
            'data': [0.1186, 0.0022, 0.012],
            'func': LF.gauss,
            'info': 'arXiv:1303.5076v1; table 5; Plank+lensing+WP+highL',
            'texname': r'$\Omega_{CDM}h^2$',
            },
        'Oh2_upper_limit': {   
            'oids': [('Micromegas', 'Omega')],
            'data': [0.1109, 0.0056, 0.012],
            'func': LF.upperlimit},
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
        'Bsmumu_July2013': {   
            'oids': [('BPhysics', 'Psll')],
            'data': [3.4946e-09, 1.0726e-09, 8.996e-10],
            'func': LF.asymmetric_gauss,
            'mode': 'default',},
        'R_Bsmm_mc9': {   
            'oids': [('BPhysics', 'Psll')],
            'data': [0.94, 0.22, -0.20],
            'func': LF.R_bsmm_chi2,
            'mode': 'default',
            'info': 'formula from Diego\'s slides, on 2013/08/13 first page, number from last slide'
            },
        'mc-old-bsmm': {   
            'oids': [('BPhysics', 'Psll')],
            'data': [1.08E-8 , 0.1E-9 ,    0.2E-9],
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
        #from Gino's e-mail notes2.pdf
        'mc9_R_B->Xsg': {   
            'oids': [('BPhysics', 'BRbsg')],
            'data': [1.089, 0.070,0.080,0.050],
            'func': LF.gauss,
            'info': 'notes2.pdf from Gino 2013/08/09: arXiv:1207.1158 & hep-ph/0609323',
            'texname': r'$R_{B\toX_s\gamma}$',
            'texvalue': r'$1.089\pm0.070_{exp}\pm0.080_{th-SM}\pm0.050_{th-SUSY}$'
            },
        'mc9_R_Bs->mumu': {   
            'oids': [('BPhysics', 'Psll')],
            'data': [0.81,0.2,0.07,0.05],
            'func': LF.bsmm_ratio_gauss,
            'info': 'notes2.pdf from Gino 2013/08/09: LHCb and CMS, EPs-2013 & arXiv:1208.0934',
            'texname' : r'$R_{B_s\to\mu^{+}mu^{-}}',
            'texvalue': r'0.81\pm0.20_{exp}\pm0.07_{th-SM}\pm0.05_{th-SUSY}$',
            },
        'mc9_R_B->taunu': {   
            'oids': [('BPhysics', 'BRbtn')],
            'data': [1.39,0.28,0.13],
            'func': LF.gauss,
            'info': 'notes2.pdf from Gino 2013/08/09: arXiv:1207.1158 & http://utfit.org/UTfit/',
            'texname' : r'$R_{B\to\tau\nu}$',
            'texvalue': r'$1.39\pm0.28_{exp}\pm0.13_{th-SM}$'
            },
        'mc9_Bd->mumu': {   
            'oids': [('BPhysics', 'Pdll')],
            'data': [3.6e-10,1.6e-10,1.4e-10],
            'func': LF.asymmetric_gauss,
            'mode': 'default',
            'info': 'notes2.pdf from Gino 2013/08/09: LHCb and CMS, EPS-2013',
            'texname' : r'$BR(B_d\to\mu^{+}\mu^{-}})$',
            'texvalue'  : r'$(3.6^{+1.6}_{-1.4})\times10^{-10}$',
            },
        'mc9_R_DMBs': {   
            'oids': [('BPhysics', 'RDMs')],
            'data': [0.97,0.20],
            'func': LF.gauss,
            'info': 'notes2.pdf from Gino 2013/08/09: arXiv:1203.0238',
            'texname' : r'$R_{\DeltaM_{B_s}}$',
            'texvalue'  : r'$0.97\pm0.20_{th-SM}$',
            },
        'mc9_R_DMBs/DMBd': {   
            'oids': [('BPhysics', 'RDMs'),('BPhysics', 'RDMb')],
            'data': [0.86,0.14],
            'func': LF.ratio_gauss, 
            'info': 'notes2.pdf from Gino 2013/08/09: arXiv:1203.0238',
            'texname' : r'$R_{\DeltaM_{B_s}/\Delta{B_d}}$',
            'texvalue'  : r'$0.86\pm0.14_{th-SM}$',
            },
        'mc9_epsilon_K': {   
            'oids': [('BPhysics', 'RDMK')],
            'data': [1.14,0.10],
            'func': LF.gauss,
            'info': 'notes2.pdf from Gino 2013/08/09: arXiv:1212.6847',
            'texname' : r'$\epsilon_K$',
            'texvalue'  : r'$1.14\pm0.10_{th-SM}$',
            },
########################################### CONSTRAINTS FROM LIKELIHOODS ###############        
        'M0M12': {
            'oids': [('MINPAR', 'M0_in'),('MINPAR', 'M12_in')],
            'data': [('PointAnalyser/m0m12.txt', 'radial', 0.95, 2,'linear')],
            'func': LF.power_4_inv_single_contour, 
            'mode': 'contour'},
        'atlas20_m0_m12': {
            'oids': [('MINPAR', 'in_M0'),('MINPAR', 'in_M12')],
            'data': [('PointAnalyser/atlas_20_m0m12.txt', 'radial', 0.95, 2,'linear')],
            'func': LF.power_4_inv_single_contour, 
            'mode': 'contour',
            'info': 'https://twiki.cern.ch/twiki/pub/AtlasPublic/CombinedSummaryPlots/ATLAS_SUSY_MSUGRA_CMSSM_lp13.pdf',
            'texname': r'$jets+\notE_T$',
            'texvalue': r'$(m_0,m_{1/2})$ plane',
            },
        'atlas5_m0_m12': {
            'oids': [('MINPAR', 'in_M0'),('MINPAR', 'in_M12')],
            'data': [('PointAnalyser/atlas_5fb_m0_m12.txt', 'radial', 0.95, 2,'linear')],
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
        'xenon100_SpiN_unc':{
            'oids': [('MASS', 'MNeu(1)'),('LSP scattering','s3out'),('LSP scattering','ss3out')],
            'data': [('PointAnalyser/xenon100.txt','x',0.9,2,'logxy',{'min':'flat','max':'flat'})],
            'func': LF.xenon100_jul_2012_Sigma_pi_N_unc, 
            'mode': 'contour' },
        'mc8_bsmm':{
            'oids': [('BPhysics','Psll')],
            'data': [('PointAnalyser/mc8_bsmm.txt','x',0.9,1,'linear',{'max':'flat'})],
            'func': LF.one_dim_chi2_lookup, 
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
