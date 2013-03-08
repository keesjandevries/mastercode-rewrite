#! /usr/bin/env python
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
        ('MINPAR','M0')         :1,
        ('MINPAR','M12')        :2,
        ('MINPAR','A')          :3,
        ('MINPAR','TB')         :4,
        ('MINPAR','signMUE')    :5,
        ('SMINPUTS','Mt')       :6,
        ('SMINPUTS','MZ')       :7,
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
        ('MASS', 'MA0')    : 98, # yep that's right, feynhiggs does not change MA0
        ('MASS', 'mod_MHp'): 99,
        ('MASS', 'Mh0'): 104,
        ('MASS', 'MHH'): 105,
        ('MASS', 'MA0'): 106,
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
def fill_VARS_2(point,VARS,model='cMSSM'):
    for mcpp_oid, old_oid in VARS_dict.items():
        try:
            VARS[old_oid]=point[mcpp_oid]
        except TypeError:
            for oldoid in old_oid:
                VARS[oldoid]=point[mcpp_oid]

    if model=='cMSSM':
        VARS[37]=point[('BPhysics', 'RDMs')]/point[('BPhysics', 'RDMb')]
        VARS[89]=sum([point[('MASS',squark)] for squark in ['MSf(2,3,1)','MSf(2,3,2)','MSf(2,4,1)','MSf(2,4,2)'] ] )/4. # ave over R: u,c,d,s squarks
        VARS[90]=sum([point[('MASS',squark)] for squark in ['MSf(1,3,1)','MSf(1,3,2)','MSf(1,4,1)','MSf(1,4,2)'] ] )/4. # ave over L: u,c,d,s squarks
    return VARS


#WARNING: RESULT ORIENTED
def write_point_to_root(point,model='cMSSM'):
    VARS=max_rows*[0.]
#    VARS=fill_VARS(point,VARS,model)
    VARS=fill_VARS_2(point,VARS,model)
    root.root_write(VARS)


#WARNING: VERY RESULT ORIENTED
def write_in_out_to_ab_root(in_vars,out_point,model='cMSSM'):
    VARS=max_rows*[0.]
    out_vars=fill_VARS_2(out_point,VARS,model)
    ab_root.root_write(in_vars, out_vars)



