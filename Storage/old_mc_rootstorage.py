#! /usr/bin/env python
import sys
import Storage.interfaces.ROOT as root
import Storage.interfaces.ROOT_ab_out as ab_root
#from example_point import point 
#from mc_new_old_oids_dict import get_mc_old_oid

#KJ 2013/02/15 WARNING: This module is horrific and thus temporary
# Key word to keep in mind is "RESULT ORIENTED" :D:D:D:D

# RESULT ORIENTED :D

# This is the index list as it comes from mc-old
# WARNING: RESULT ORIENTED
max_rows = 110 # this number is also valid for nuhm2, 
                                       #and does not include the funny numbers at the end of the tree
# WARNING: RESULT ORIENTED
VARS_dict={
        #parameters
        ('tot_X2', 'all')       :0,
        ('MINPAR','in_M0')      :1,
        ('MINPAR','in_M12')     :2,
        ('MINPAR','in_A')       :3,
        ('MINPAR','in_TB')      :4,
        ('MINPAR','signMUE')    :5,
        ('EXTPAR', 'in_MH2')    :[6,7],
        ('SMINPUTS','Mt')       :6,
        ('SMINPUTS','mod_MZ')   :7,
        ('SUSY-POPE', 'GZ_in')  :8,
        ('SUSY-POPE', 'DAlpha_had_in'):9,
        #predictions
        ('BPhysics', 'BRbsg')   : 10,
        ('BPhysics', 'RDMs')    : 11,
        ('BPhysics', 'Psll')    : 12,
        ('BPhysics', 'BRbtn')   : 13,
        ('BPhysics', 'BRXsll')  : 14,
        ('BPhysics', 'BRKl2')   : 15,
        ('FeynHiggs','gm2')     : 16,
        ('SUSY-POPE', 'MW')     : 17, 
        ('SUSY-POPE', 'sin_theta_eff'): 18,
        ('SUSY-POPE', 'Gamma_z'): 19,
        ('SUSY-POPE', 'Rl')     : 20,
        ('SUSY-POPE', 'Rb')     : 21, 
        ('SUSY-POPE', 'Rc')     : 22,
        ('SUSY-POPE', 'Afb_b')  : 23,
        ('SUSY-POPE', 'Afb_c')  : 24,
        ('SUSY-POPE', 'Ab')     : 25,
        ('SUSY-POPE', 'Ac')     : 26,
        ('SUSY-POPE', 'Al')     : [27,30],
        ('FeynHiggs', 'mh')     : 28,
        ('Micromegas', 'Omega') : 29,
        ('SUSY-POPE', 'Afb_l')  : 31,
        ('SUSY-POPE', 'sigma_had'):32,
        ('BPhysics', 'RDMb')    : 33,
        ('BPhysics', 'RDMK')    : 34,
        ('BPhysics', 'BRKpnn')  : 35,
        ('BPhysics', 'Pdll')    : 36,
        # 37 is that bloody ratio
        ('SuperISO', 'SId0')    : 38,
        # 40, 41 is DarkSUSY
        ('SuperISO', 'SIbsg')   : 39,
        ('HMIX', 'MUE')         : 42,
        ('Micromegas', 'sigma_p_si'): 43,
        ('ALPHA', 'Alpha')      : 44, 
        ('HMIX', 'MA02')        : 45,
        ('NMIX','ZNeu(1,1)')    : 46,
        ('NMIX','ZNeu(1,2)')    : 47,
        ('NMIX','ZNeu(1,3)')    : 48,
        ('NMIX','ZNeu(1,4)')    : 49,
        ('NMIX','ZNeu(2,1)')    : 50,
        ('NMIX','ZNeu(2,2)')    : 51,
        ('NMIX','ZNeu(2,3)')    : 52,
        ('NMIX','ZNeu(2,4)')    : 53,
        ('NMIX','ZNeu(3,1)')    : 54,
        ('NMIX','ZNeu(3,2)')    : 55,
        ('NMIX','ZNeu(3,3)')    : 56,
        ('NMIX','ZNeu(3,4)')    : 57,
        ('NMIX','ZNeu(4,1)')    : 58,
        ('NMIX','ZNeu(4,2)')    : 59,
        ('NMIX','ZNeu(4,3)')    : 60,
        ('NMIX','ZNeu(4,4)')    : 61,
        ('MASS', 'MSf(1,3,1)')  : 62, #muL
        ('MASS', 'MSf(2,3,1)')  : 63, #muR
        ('MASS', 'MSf(1,4,1)')  : 64, #mdL
        ('MASS', 'MSf(2,4,1)')  : 65, #mdR
        ('STOPMIX', 'USf(1,1)') : 66,
        ('STOPMIX', 'USf(1,2)') : 67,
        ('STOPMIX', 'USf(2,1)') : 68,
        ('STOPMIX', 'USf(2,2)') : 69,
        ('SBOTMIX', 'USf(1,1)') : 70,
        ('SBOTMIX', 'USf(1,2)') : 71,
        ('SBOTMIX', 'USf(2,1)') : 72,
        ('SBOTMIX', 'USf(2,2)') : 73,
        ('MASS', 'MCha(1)'): 74,
        ('MASS', 'MCha(2)'): 75,
        ('MASS', 'MNeu(1)'): 76,
        ('MASS', 'MNeu(2)'): 77,
        ('MASS', 'MNeu(3)'): 78,
        ('MASS', 'MNeu(4)'): 79,
        ('MASS', 'MSf(2,2,1)'): 80, #er
        ('MASS', 'MSf(1,2,1)'): 81, #el
        ('MASS', 'MSf(1,1,1)'): 82, #nu_e
 #
        ('MASS', 'MSf(2,2,2)'): 83, #mur
        ('MASS', 'MSf(1,2,2)'): 84, #mul
        ('MASS', 'MSf(1,1,2)'): 85, #nu_mu
 #
        ('MASS', 'MSf(1,2,3)'): 86, #tau1
        ('MASS', 'MSf(2,2,3)'): 87, #tau2
        ('MASS', 'MSf(1,1,3)'): 88, #nu_tau
 # 89, 90 are averages
        ('MASS', 'MSf(1,3,3)'): 91, #top1
        ('MASS', 'MSf(2,3,3)'): 92, #top2
        ('MASS', 'MSf(1,4,3)'): 93, #bot1
        ('MASS', 'MSf(2,4,3)'): 94, #bot2
# Gluino mass
        ('MASS', 'MGl'): 95,
# Higgs masses
        ('MASS', 'mod_Mh0'): 96,
        ('MASS', 'mod_MHH'): 97,
#        ('MASS', 'MA0')    : 98, # yep that's right, feynhiggs does not change MA0
        ('MASS', 'mod_MHp'): 99,
        ('MASS', 'Mh0'): 104,
        ('MASS', 'MHH'): 105,
        ('MASS', 'MA0'): [98,106],
        ('MASS', 'MHp'): 107,
        }

# WARNING: RESULT ORIENTED
def get_mc_old_oid(mcpp_oid,model='cMSSM'):
    if model=='cMSSM':
        return VARS_dict.get(mcpp_oid)

#WARNING: RESULT ORIENTED
def fill_VARS(point,VARS,model='cMSSM'):
    for oid, val in point.items():
        old_oid=get_mc_old_oid(oid,model)
        if old_oid: 
            # To deal with stupid dubble assignment of Al
            try:
                if old_oid==0: print("should be filled", val)
                VARS[old_oid]=val
            except TypeError: 
                for o_oid in old_oid:
                    VARS[o_oid]=val
    return VARS

#WARNING: RESULT ORIENTED
def fill_VARS_2(point,VARS,params=None,model='cMSSM'):
    nuhm1=( ('EXTPAR','in_MH2') in point.keys())
    for mcpp_oid, old_oid in VARS_dict.items():
        try:
            index=old_oid
            if nuhm1 and old_oid>5 and not mcpp_oid== ('EXTPAR','in_MH2'):index+=2
            VARS[index]=point[mcpp_oid]
        except TypeError:
            try:
                for oldoid in old_oid:
                    index=oldoid
                    if nuhm1 and oldoid>5 and not mcpp_oid== ('EXTPAR','in_MH2'):index+=2
                    VARS[index]=point[mcpp_oid]
            except KeyError:
                if params:  print(params,file=sys.stderr)
        except KeyError:
            if params: print(params,file=sys.stderr)
    try:
        VARS[37+2*int(nuhm1)]=point[('BPhysics', 'RDMs')]/point[('BPhysics', 'RDMb')]
        VARS[89+2*int(nuhm1)]=sum([point[('MASS',squark)] for squark in 
            ['MSf(2,3,1)','MSf(2,3,2)','MSf(2,4,1)','MSf(2,4,2)'] ] )/4. # ave over R: u,c,d,s squarks
        VARS[90+2*int(nuhm1)]=sum([point[('MASS',squark)] for squark in 
            ['MSf(1,3,1)','MSf(1,3,2)','MSf(1,4,1)','MSf(1,4,2)'] ] )/4. # ave over L: u,c,d,s squarks
    except KeyError:
        if params: print(params,file=sys.stderr)
    return VARS


#WARNING: RESULT ORIENTED
def write_point_to_root(point,params=None, model='cMSSM'):
    VARS=max_rows*[0.]
#    VARS=fill_VARS(point,VARS,model)
    VARS=fill_VARS_2(point,VARS,params,model)
    root.root_write(VARS)


#WARNING: VERY RESULT ORIENTED
def write_in_out_to_ab_root(in_vars,out_point,params=None,model='cMSSM'):
    VARS=max_rows*[0.]
    out_vars=fill_VARS_2(out_point,VARS,params,model)
    ab_root.root_write(in_vars, out_vars)



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
    n_predictions=64# this is hardcoded and the same for 
    n_spectrum=35   # this is hardcoded and the same for 
    n_nuisance=4    # one of which is latent
    n_dm=0          # for the moment :(
    # Only the number of parameters differs per model
    if model == 'cMSSM':
        n_parameters=5  # including sign mu
    elif model  == 'pMSSM8':
        n_parameters=8  # including sign mu
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


