#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3 , sys, random, os, argparse, pickle
import numpy as np

one_point={   ('MINPAR', 'in_M12'): 905.0,
    ('MINPAR', 'in_A'): -1303.97,
    ('SMINPUTS', 'in_Mt'): 173.2,
    ('MINPAR', 'in_M0'): 300.53,
    ('MINPAR', 'in_TB'): 16.26,
    ('MODSEL', 'Model'): 1.0,
    ('SMINPUTS', 'invAlfaMZ'): 127.908953,
    ('SMINPUTS', 'GF'): 1.16639e-05,
    ('SMINPUTS', 'AlfasMZ'): 0.1187,
    ('SMINPUTS', 'MZ'): 91.1876,
    ('SMINPUTS', 'Mtau'): 1.77703,
    ('SMINPUTS', 'Mt'): 173.2,
    ('SMINPUTS', 'Mb'): 4.2,
    ('MINPAR', 'M0'): 300.53,
    ('MINPAR', 'M12'): 905.0,
    ('MINPAR', 'TB'): 16.26,
    ('MINPAR', 'signMUE'): 1.0,
    ('MINPAR', 'A'): -1303.97,
    ('MASS', 'MSf(1,1,1)'): 669.827102,
    ('MASS', 'MSf(1,2,1)'): 674.681906,
    ('MASS', 'MSf(2,2,1)'): 455.121218,
    ('MASS', 'MSf(1,3,1)'): 1837.53455,
    ('MASS', 'MSf(2,3,1)'): 1765.35475,
    ('MASS', 'MSf(1,4,1)'): 1839.09195,
    ('MASS', 'MSf(2,4,1)'): 1757.81833,
    ('MASS', 'MSf(1,1,2)'): 669.827102,
    ('MASS', 'MSf(1,2,2)'): 674.761458,
    ('MASS', 'MSf(2,2,2)'): 455.121218,
    ('MASS', 'MSf(1,3,2)'): 1837.53455,
    ('MASS', 'MSf(2,3,2)'): 1765.35475,
    ('MASS', 'MSf(1,4,2)'): 1839.09195,
    ('MASS', 'MSf(2,4,2)'): 1757.81833,
    ('MASS', 'MSf(1,1,3)'): 649.62685,
    ('MASS', 'MSf(1,2,3)'): 385.757152,
    ('MASS', 'MSf(2,2,3)'): 659.115303,
    ('MASS', 'MSf(1,3,3)'): 1281.26462,
    ('MASS', 'MSf(2,3,3)'): 1648.72473,
    ('MASS', 'MSf(1,4,3)'): 1611.13112,
    ('MASS', 'MSf(2,4,3)'): 1722.53099,
    ('MASS', 'MW'): 80.3848929,
    ('MASS', 'Mh0'): 121.40748,
    ('MASS', 'MHH'): 1405.79771,
    ('MASS', 'MA0'): 1405.85632,
    ('MASS', 'MHp'): 1408.34071,
    ('MASS', 'MNeu(1)'): 384.070899,
    ('MASS', 'MNeu(2)'): 729.022682,
    ('MASS', 'MNeu(3)'): -1312.3184,
    ('MASS', 'MNeu(4)'): 1316.60155,
    ('MASS', 'MCha(1)'): 729.232278,
    ('MASS', 'MCha(2)'): 1324.2931,
    ('MASS', 'MGl'): 1995.60271,
    ('NMIX', 'ZNeu(1,1)'): 0.999178076,
    ('NMIX', 'ZNeu(2,1)'): 0.00768134628,
    ('NMIX', 'ZNeu(3,1)'): -0.0172428891,
    ('NMIX', 'ZNeu(4,1)'): -0.0358727167,
    ('NMIX', 'ZNeu(1,2)'): -0.00366066548,
    ('NMIX', 'ZNeu(2,2)'): 0.99477054,
    ('NMIX', 'ZNeu(3,2)'): 0.0253038217,
    ('NMIX', 'ZNeu(4,2)'): 0.0988832076,
    ('NMIX', 'ZNeu(1,3)'): 0.0380480344,
    ('NMIX', 'ZNeu(2,3)'): -0.0875627403,
    ('NMIX', 'ZNeu(3,3)'): 0.706153575,
    ('NMIX', 'ZNeu(4,3)'): 0.701592647,
    ('NMIX', 'ZNeu(1,4)'): -0.0134951369,
    ('NMIX', 'ZNeu(2,4)'): 0.052012845,
    ('NMIX', 'ZNeu(3,4)'): 0.707396302,
    ('NMIX', 'ZNeu(4,4)'): -0.704771606,
    ('UMIX', 'UCha(1,1)'): 0.992525071,
    ('UMIX', 'UCha(2,1)'): 0.122040912,
    ('UMIX', 'UCha(1,2)'): -0.122040912,
    ('UMIX', 'UCha(2,2)'): 0.992525071,
    ('VMIX', 'VCha(1,1)'): 0.997317942,
    ('VMIX', 'VCha(2,1)'): 0.0731909971,
    ('VMIX', 'VCha(1,2)'): -0.0731909971,
    ('VMIX', 'VCha(2,2)'): 0.997317942,
    ('STAUMIX', 'USf(1,1)'): 0.143825558,
    ('STAUMIX', 'USf(2,1)'): 0.989603056,
    ('STAUMIX', 'USf(1,2)'): 0.989603056,
    ('STAUMIX', 'USf(2,2)'): -0.143825558,
    ('STOPMIX', 'USf(1,1)'): 0.301917167,
    ('STOPMIX', 'USf(2,1)'): 0.953334162,
    ('STOPMIX', 'USf(1,2)'): 0.953334162,
    ('STOPMIX', 'USf(2,2)'): -0.301917167,
    ('SBOTMIX', 'USf(1,1)'): 0.989716337,
    ('SBOTMIX', 'USf(2,1)'): -0.143043954,
    ('SBOTMIX', 'USf(1,2)'): 0.143043954,
    ('SBOTMIX', 'USf(2,2)'): 0.989716337,
    ('ALPHA', 'Alpha'): -0.0642548553,
    ('HMIX', 'Qscale'): 1414.22899,
    ('HMIX', 'MUE'): 1316.65148,
    ('HMIX', 'TB'): 15.6772724,
    ('HMIX', 'VEV'): 243.591566,
    ('HMIX', 'MA02'): 2067007.82,
    ('GAUGE', 'Qscale'): 1414.22899,
    ('GAUGE', 'g1'): 0.363326287,
    ('GAUGE', 'g2'): 0.639520144,
    ('GAUGE', 'g3'): 1.0390044,
    ('MSOFT', 'Qscale'): 1414.22899,
    ('MSOFT', 'M1'): 389.95347,
    ('MSOFT', 'M2'): 713.638173,
    ('MSOFT', 'M3'): 1951.02828,
    ('MSOFT', 'MHu2'): -1703051.08,
    ('MSOFT', 'MHd2'): 222071.536,
    ('MSOFT', 'MSL(1)'): 664.825866,
    ('MSOFT', 'MSL(2)'): 664.825866,
    ('MSOFT', 'MSL(3)'): 645.816927,
    ('MSOFT', 'MSE(1)'): 447.199023,
    ('MSOFT', 'MSE(2)'): 447.199023,
    ('MSOFT', 'MSE(3)'): 386.803404,
    ('MSOFT', 'MSQ(1)'): 1784.05918,
    ('MSOFT', 'MSQ(2)'): 1784.05918,
    ('MSOFT', 'MSQ(3)'): 1574.25629,
    ('MSOFT', 'MSU(1)'): 1714.13504,
    ('MSOFT', 'MSU(2)'): 1714.13504,
    ('MSOFT', 'MSU(3)'): 1272.71219,
    ('MSOFT', 'MSD(1)'): 1705.53751,
    ('MSOFT', 'MSD(2)'): 1705.53751,
    ('MSOFT', 'MSD(3)'): 1669.01227,
    ('AE', 'Qscale'): 1414.22899,
    ('AE', 'Af(1,1)'): 0.0,
    ('AE', 'Af(2,2)'): 0.0,
    ('AE', 'Af(3,3)'): -1743.17733,
    ('AU', 'Qscale'): 1414.22899,
    ('AU', 'Af(1,1)'): 0.0,
    ('AU', 'Af(2,2)'): 0.0,
    ('AU', 'Af(3,3)'): -2021.63389,
    ('AD', 'Qscale'): 1414.22899,
    ('AD', 'Af(1,1)'): 0.0,
    ('AD', 'Af(2,2)'): 0.0,
    ('AD', 'Af(3,3)'): -3316.0707,
    ('YE', 'Qscale'): 1414.22899,
    ('YE', 'Yf(3,3)'): 0.164296816,
    ('YU', 'Qscale'): 1414.22899,
    ('YU', 'Yf(3,3)'): 0.836246072,
    ('YD', 'Qscale'): 1414.22899,
    ('YD', 'Yf(3,3)'): 0.202972947,
    ('SMINPUTS', 'mod_MZ'): 91.1876,
    ('MASS', 'mod_MW'): 80.4,
    ('FeynHiggs', 'SW2effMSSM'): 0.23148819257948183,
    ('FeynHiggs', 'MWMSSM'): 80.36606352730006,
    ('FeynHiggs', 'SW2effSM'): 0.23151404241792578,
    ('FeynHiggs', 'MWSM'): 80.36140085953079,
    ('FeynHiggs', 'EDMHg'): 0.0,
    ('FeynHiggs', 'EDMeTh'): 0.0,
    ('FeynHiggs', 'gm2'): 3.928595336603956e-10,
    ('FeynHiggs', 'mA'): 1405.85632,
    ('FeynHiggs', 'DeltaRho'): 8.278388844044644e-05,
    ('FeynHiggs', 'mH'): 1405.7800021657267,
    ('FeynHiggs', 'mHpm'): 1408.4436616042146,
    ('FeynHiggs', 'EDMn'): 0.0,
    ('FeynHiggs', 'mh'): 124.39934815798615,
    ('Micromegas', 'SMbsg'): 0.00033064619800191904,
    ('Micromegas', 'sigma_p_si'): 8.442990349421708e-11,
    ('Micromegas', 'Bll'): 3.1370704760727043e-09,
    ('Micromegas', 'Omega'): 0.1371525574443451,
    ('Micromegas', 'Bsg'): 0.00032259637433566037,
    ('SuperISO', 'SIgm2'): 3.6824295477471766e-10,
    ('SuperISO', 'SId0'): 0.07989376094766454,
    ('SuperISO', 'SIbsg'): 0.00030453996849957556,
    ('BPhysics', 'BRKl2'): 0.999946548298358,
    ('BPhysics', 'Psll'): 3.579837335471622e-09,
    ('BPhysics', 'RDMK'): 1.0044216847125753,
    ('BPhysics', 'BRXsll'): 0.9990829464231566,
    ('BPhysics', 'Pllsapx'): 3.3700646786799186e-09,
    ('BPhysics', 'BRbtn'): 0.99397852855041,
    ('BPhysics', 'BRKpnn'): 0.9995842507438331,
    ('BPhysics', 'RDMs'): 1.0042949509238812,
    ('BPhysics', 'BRbsg'): 0.9864044993663432,
    ('BPhysics', 'RDMb'): 1.0044284421622642,
    ('BPhysics', 'Pdll'): 2.0674198578277746e-10,
    ('LSP scattering', 'ss2out'): 2.5058215783445047e-09,
    ('LSP scattering', 'ss3out'): 4.8348205512644426e-11,
    ('LSP scattering', 's2out'): 1.5529473757560673e-08,
    ('LSP scattering', 's3out'): 5.150685311586715e-11,
    ('SUSY-POPE', 'sin_theta_eff'): 0.2315160621913348,
    ('SUSY-POPE', 'DAlpha_had_in'): 0.02759,
    ('SUSY-POPE', 'MW'): 80.36106695648735,
    ('SUSY-POPE', 'Afb_b'): 0.10311113821602272,
    ('SUSY-POPE', 'Afb_c'): 0.07367081028057079,
    ('SUSY-POPE', 'sigma_had'): 41.48155479390193,
    ('SUSY-POPE', 'Rb'): 0.2159547059272715,
    ('SUSY-POPE', 'Ab'): 0.9348187945910564,
    ('SUSY-POPE', 'GZ_in'): 2.4952,
    ('SUSY-POPE', 'Al'): 0.14706755835124813,
    ('SUSY-POPE', 'Ac'): 0.6679090082270848,
    ('SUSY-POPE', 'Gamma_z'): 2494.27319800561,
    ('SUSY-POPE', 'Afb_l'): 0.01622165003954833,
    ('SUSY-POPE', 'Rc'): 0.17223404067393286,
    ('SUSY-POPE', 'Rl'): 20.740302022254717,
    ('MASS', 'mod_Mh0'): 124.39934815798615,
    ('MASS', 'mod_MHH'): 1405.7800021657267,
    ('MASS', 'mod_MHp'): 1408.4436616042146,
    ('ALPHA', 'mod_Alpha'): -0.06409481490527785,
    ('CVHMIX', 'mod_UH(1,1)'): 0.9999976719181932,
    ('CVHMIX', 'mod_UH(2,1)'): 0.0,
    ('CVHMIX', 'mod_UH(3,1)'): -0.004953127459291144,
    ('CVHMIX', 'mod_UH(1,2)'): 0.0,
    ('CVHMIX', 'mod_UH(2,2)'): 1.0,
    ('CVHMIX', 'mod_UH(3,2)'): 0.0,
    ('CVHMIX', 'mod_UH(1,3)'): 0.0,
    ('CVHMIX', 'mod_UH(2,3)'): 1.0128606380053085,
    ('CVHMIX', 'mod_UH(3,3)'): 6.20712136052181e-05,
    ('PRECOBS', 'mod_DeltaRho'): 8.278388844044644e-05,
    ('PRECOBS', 'mod_MWSM'): 80.36140085953079,
    ('PRECOBS', 'mod_SW2effSM'): 0.23151404241792578,
    ('PRECOBS', 'mod_gminus2mu'): 3.928595336603956e-10,
    ('PRECOBS', 'mod_EDMeTh'): 0.0,
    ('PRECOBS', 'mod_EDMn'): 0.0,
    ('PRECOBS', 'mod_EDMHg'): 0.0}

def parse_args():
    parser = argparse.ArgumentParser(description='Fill points randomly for the moment')
    parser.add_argument('--n-points', '-n',dest='n_points', action='store',type=int, 
            default=10000,  help='Number of points')
    parser.add_argument('--input-file','-i', dest='input_file', action='store', 
            default='test.db',  help='Name of input date base file')
    parser.add_argument('--pickle-in',dest='pickle_in', action='store', 
            default=None,  help='Name of pickled file containing (a) points(s)')
    return parser.parse_args()


def dump_rows(con,cur,rows):
    #NOTE: this takes rows without index
    # the index should be generated by sql
    question_marks=','.join(['?']*len(rows[0]))
    cur.executemany('insert into points values(null,{})'.format(question_marks), rows )
    #commit
    con.commit()

def get_columns_and_observable_ids(con,cur):
    cur.execute('select point_column, obs_id_field1 , obs_id_field2 from obs_id_lookup')
    obs_id_lookup=cur.fetchall()
    columns=[]
    oids={}
    for col, id1, id2 in obs_id_lookup:
        columns.append(col)
        oids[col]=(id1,id2)
    return columns, oids

def mc_points_to_rows(con,cur,points,collection_id=1):
    #Here starts the niceness!
    obs_columns, mc_obs_ids = get_columns_and_observable_ids(con,cur)
    rows=[]
    for point in points:
        #The following checks whether
        #   the point contains all the information in the lookup table, 
        #   the lookup table is complete
        try:
            observables=[point[mc_obs_ids[col]] for col in obs_columns]
        except KeyError:
            #This crashes if the KeyError was caused in calling mc_obs_ids[col], which should not happend
            print("WARNING: presumably point does not contain key {}".format(mc_obs_ids[col]))
        if len(point) > len(obs_columns):
            print("WARNING: DATABASE IS MISSING COLUMNS")
            print("         FIXME: A function is needed to take care of this")

        #Et voila: le point :D :D
        rows.append(tuple([collection_id]+observables))
    return rows

#def make_some_random_rows(con,cur):
#    #count number of columns
#    cur.execute("pragma table_info(points)")
#    n_columns=len(cur.fetchall())
#    rows=[]
#    for i in range(args.n_points):
#        rows.append(tuple(np.append([2], np.random.rand(n_columns-2)))) 
#    return rows


if __name__=="__main__" :
    con = None
    args= parse_args()
    # the real stuff
    try:
        #connection and cursor
        con=sqlite3.connect(args.input_file)
        cur=con.cursor()
        #dump one point
#        rows=make_some_random_rows(con,cur)
        if args.pickle_in:
            with open(args.pickle_in,'rb') as pickle_file:
                point=pickle.load(pickle_file)
#        rows=mc_points_to_rows(con,cur,[one_point])
        rows=mc_points_to_rows(con,cur,[point])
        dump_rows(con,cur,rows)
    
    # Finalise ...
    except sqlite3.Error as e:
        if con:
            con.rollback()
        print('ERROR: {}'.format(e.args[0]))
        sys.exit()
    finally:
        if con:
            con.close()

