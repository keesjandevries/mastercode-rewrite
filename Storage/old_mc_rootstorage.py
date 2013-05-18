#! /usr/bin/env python

#WARNING: THIS FUNCTIONALITY IS SOON TO BE REPLACED
#THIS IS THE OLD WAY OF STORING OBSERVALBES TO ROOT FILES
#UNFORTUNATLY NOT ALL THE ANALYSIS TOOLS ARE READY FOR A NEW FORMAT YET
#HENCE THIS STUPID WAY OF DOING IT

parameter_array_ids={
        #parameters
        ('tot_X2', 'all')       :0,
        ('MINPAR','in_M0')      :1,
        ('MINPAR','in_M12')     :2,
        ('MINPAR','in_A')       :3,
        ('MINPAR','in_TB')      :4,
        ('MINPAR','signMUE')    :5,
        ('EXTPAR', 'in_MH2')    :[6,7],}
nuisance_array_ids={
        ('SMINPUTS','Mt')       :0,
        ('SMINPUTS','mod_MZ')   :1,
        ('SUSY-POPE', 'GZ_in')  :2,
        ('SUSY-POPE', 'DAlpha_had_in'):3,}
        #predictions
prediction_array_ids={
        ('BPhysics', 'BRbsg')   : 0,
        ('BPhysics', 'RDMs')    : 1,
        ('BPhysics', 'Psll')    : 2,
        ('BPhysics', 'BRbtn')   : 3,
        ('BPhysics', 'BRXsll')  : 4,
        ('BPhysics', 'BRKl2')   : 5,
        ('FeynHiggs','gm2')     : 6,
        ('SUSY-POPE', 'MW')     : 7, 
        ('SUSY-POPE', 'sin_theta_eff'): 8,
        ('SUSY-POPE', 'Gamma_z'): 9,
        ('SUSY-POPE', 'Rl')     : 10,
        ('SUSY-POPE', 'Rb')     : 11, 
        ('SUSY-POPE', 'Rc')     : 12,
        ('SUSY-POPE', 'Afb_b')  : 13,
        ('SUSY-POPE', 'Afb_c')  : 14,
        ('SUSY-POPE', 'Ab')     : 15,
        ('SUSY-POPE', 'Ac')     : 16,
        ('SUSY-POPE', 'Al')     : [17,20],
        ('FeynHiggs', 'mh')     : 18,
        ('Micromegas', 'Omega') : 19,
        ('SUSY-POPE', 'Afb_l')  : 21,
        ('SUSY-POPE', 'sigma_had'):22,
        ('BPhysics', 'RDMb')    : 23,
        ('BPhysics', 'RDMK')    : 24,
        ('BPhysics', 'BRKpnn')  : 25,
        ('BPhysics', 'Pdll')    : 26,
        # 37 is that bloody ratio
        ('SuperISO', 'SId0')    : 28,
        # 40, 41 is DarkSUSY
        ('SuperISO', 'SIbsg')   : 29,
        ('HMIX', 'MUE')         : 32,
        ('Micromegas', 'sigma_p_si'): 33,
        ('ALPHA', 'Alpha')      : 34, 
        ('HMIX', 'MA02')        : 35,
        ('NMIX','ZNeu(1,1)')    : 36,
        ('NMIX','ZNeu(1,2)')    : 37,
        ('NMIX','ZNeu(1,3)')    : 38,
        ('NMIX','ZNeu(1,4)')    : 39,
        ('NMIX','ZNeu(2,1)')    : 40,
        ('NMIX','ZNeu(2,2)')    : 41,
        ('NMIX','ZNeu(2,3)')    : 42,
        ('NMIX','ZNeu(2,4)')    : 43,
        ('NMIX','ZNeu(3,1)')    : 44,
        ('NMIX','ZNeu(3,2)')    : 45,
        ('NMIX','ZNeu(3,3)')    : 46,
        ('NMIX','ZNeu(3,4)')    : 47,
        ('NMIX','ZNeu(4,1)')    : 48,
        ('NMIX','ZNeu(4,2)')    : 49,
        ('NMIX','ZNeu(4,3)')    : 50,
        ('NMIX','ZNeu(4,4)')    : 51,
        ('MASS', 'MSf(1,3,1)')  : 52, #muL
        ('MASS', 'MSf(2,3,1)')  : 53, #muR
        ('MASS', 'MSf(1,4,1)')  : 54, #mdL
        ('MASS', 'MSf(2,4,1)')  : 55, #mdR
        ('STOPMIX', 'USf(1,1)') : 56,
        ('STOPMIX', 'USf(1,2)') : 57,
        ('STOPMIX', 'USf(2,1)') : 58,
        ('STOPMIX', 'USf(2,2)') : 59,
        ('SBOTMIX', 'USf(1,1)') : 60,
        ('SBOTMIX', 'USf(1,2)') : 61,
        ('SBOTMIX', 'USf(2,1)') : 62,
        ('SBOTMIX', 'USf(2,2)') : 63,}
spectrum_array_ids={
        ('MASS', 'MCha(1)'): 0,
        ('MASS', 'MCha(2)'): 1,
        ('MASS', 'MNeu(1)'): 2,
        ('MASS', 'MNeu(2)'): 3,
        ('MASS', 'MNeu(3)'): 4,
        ('MASS', 'MNeu(4)'): 5,
        ('MASS', 'MSf(2,2,1)'): 6, #er
        ('MASS', 'MSf(1,2,1)'): 7, #el
        ('MASS', 'MSf(1,1,1)'): 8, #nu_e
 #
        ('MASS', 'MSf(2,2,2)'): 9, #mur
        ('MASS', 'MSf(1,2,2)'): 10, #mul
        ('MASS', 'MSf(1,1,2)'): 11, #nu_mu
 #
        ('MASS', 'MSf(1,2,3)'): 12, #tau1
        ('MASS', 'MSf(2,2,3)'): 13, #tau2
        ('MASS', 'MSf(1,1,3)'): 14, #nu_tau
 # 89, 90 are averages
        ('MASS', 'MSf(1,3,3)'): 17, #top1
        ('MASS', 'MSf(2,3,3)'): 18, #top2
        ('MASS', 'MSf(1,4,3)'): 19, #bot1
        ('MASS', 'MSf(2,4,3)'): 20, #bot2
# Gluino mass
        ('MASS', 'MGl'): 21,
# Higgs masses
        ('MASS', 'mod_Mh0'): 22,
        ('MASS', 'mod_MHH'): 23,
#        ('MASS', 'MA0')    : 98, # yep that's right, feynhiggs does not change MA0
        ('MASS', 'mod_MHp'): 25,
        ('MASS', 'Mh0'): 30,
        ('MASS', 'MHH'): 31,
        ('MASS', 'MA0'): [24,32],
        ('MASS', 'MHp'): 33,
        }

# WARING: THIS FUNCTION IS BETTER THAN THOSE ABOVE, BUT SHOULD STILL BE REPLACED ASAP
# THIS IS RESULT ORIENTED
# It reproduces the hardcoded order of observables as it was done in mc-old :(
def get_VARS(point,model):
    # VARS=[X2, parameters, nuisance parameters, predictions, spectrum]
    # following the relative numbering scheme as defined above :(
    n_predictions=64# this is hardcoded and the same for 
    n_spectrum=35   # this is hardcoded and the same for 
    n_nuisance=4    # one of which is latent
    n_dm=0          # for the moment :(
    # Only the number of parameters differs per model
    if model == 'cMSSM':
        n_parameters=5  # including sign mu
    if model == 'NUHM1':
        n_parameters=7  # including sign mu
    elif model  == 'pMSSM8':
        n_parameters=8  
    #Define some fixed indices
    nuisance_index  = 1+n_parameters
    prediction_index= nuisance_index+n_nuisance
    dm_index        = prediction_index+n_predictions
    spectrum_index  = dm_index+n_dm
    #Define VARS
    VARS=(spectrum_index+n_spectrum)*[0.]
    #first fill the non functions
    for oid, value in point.items():
        for id_dict, index in [(parameter_array_ids,0),(nuisance_array_ids,nuisance_index),
                (prediction_array_ids,prediction_index) ,(spectrum_array_ids,spectrum_index) ]:
            array_ids=id_dict.get(oid)
            if not array_ids==None: 
                if not isinstance(array_ids,list):
                    array_ids=[array_ids]
                for array_id in array_ids:
                    VARS[array_id+index]=value
                break
    #then some functions of variables
    try:
        VARS[27+prediction_index]=point[('BPhysics', 'RDMs')]/point[('BPhysics', 'RDMb')]
        VARS[15+spectrum_index]=sum([point[('MASS',squark)] for squark in 
                ['MSf(2,3,1)','MSf(2,3,2)','MSf(2,4,1)','MSf(2,4,2)'] ] )/4. # ave over R: u,c,d,s squarks
        VARS[16+spectrum_index]=sum([point[('MASS',squark)] for squark in 
                ['MSf(1,3,1)','MSf(1,3,2)','MSf(1,4,1)','MSf(1,4,2)'] ] )/4. # ave over L: u,c,d,s squarks
    except KeyError:
        pass
    return VARS
