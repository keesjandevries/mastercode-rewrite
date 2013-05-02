#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3 , sys, random, os, argparse
import numpy as np
all_obs_ids= [   ('MINPAR', 'in_M0'),
    ('MINPAR', 'in_M12'),
    ('MINPAR', 'in_TB'),
    ('SMINPUTS', 'in_Mt'),
    ('MINPAR', 'in_A'),
    ('MODSEL', 'Model'),
    ('SMINPUTS', 'invAlfaMZ'),
    ('SMINPUTS', 'GF'),
    ('SMINPUTS', 'AlfasMZ'),
    ('SMINPUTS', 'MZ'),
    ('SMINPUTS', 'Mtau'),
    ('SMINPUTS', 'Mt'),
    ('SMINPUTS', 'Mb'),
    ('MINPAR', 'M0'),
    ('MINPAR', 'M12'),
    ('MINPAR', 'TB'),
    ('MINPAR', 'signMUE'),
    ('MINPAR', 'A'),
    ('MASS', 'MSf(1,1,1)'),
    ('MASS', 'MSf(1,2,1)'),
    ('MASS', 'MSf(2,2,1)'),
    ('MASS', 'MSf(1,3,1)'),
    ('MASS', 'MSf(2,3,1)'),
    ('MASS', 'MSf(1,4,1)'),
    ('MASS', 'MSf(2,4,1)'),
    ('MASS', 'MSf(1,1,2)'),
    ('MASS', 'MSf(1,2,2)'),
    ('MASS', 'MSf(2,2,2)'),
    ('MASS', 'MSf(1,3,2)'),
    ('MASS', 'MSf(2,3,2)'),
    ('MASS', 'MSf(1,4,2)'),
    ('MASS', 'MSf(2,4,2)'),
    ('MASS', 'MSf(1,1,3)'),
    ('MASS', 'MSf(1,2,3)'),
    ('MASS', 'MSf(2,2,3)'),
    ('MASS', 'MSf(1,3,3)'),
    ('MASS', 'MSf(2,3,3)'),
    ('MASS', 'MSf(1,4,3)'),
    ('MASS', 'MSf(2,4,3)'),
    ('MASS', 'MW'),
    ('MASS', 'Mh0'),
    ('MASS', 'MHH'),
    ('MASS', 'MA0'),
    ('MASS', 'MHp'),
    ('MASS', 'MNeu(1)'),
    ('MASS', 'MNeu(2)'),
    ('MASS', 'MNeu(3)'),
    ('MASS', 'MNeu(4)'),
    ('MASS', 'MCha(1)'),
    ('MASS', 'MCha(2)'),
    ('MASS', 'MGl'),
    ('NMIX', 'ZNeu(1,1)'),
    ('NMIX', 'ZNeu(2,1)'),
    ('NMIX', 'ZNeu(3,1)'),
    ('NMIX', 'ZNeu(4,1)'),
    ('NMIX', 'ZNeu(1,2)'),
    ('NMIX', 'ZNeu(2,2)'),
    ('NMIX', 'ZNeu(3,2)'),
    ('NMIX', 'ZNeu(4,2)'),
    ('NMIX', 'ZNeu(1,3)'),
    ('NMIX', 'ZNeu(2,3)'),
    ('NMIX', 'ZNeu(3,3)'),
    ('NMIX', 'ZNeu(4,3)'),
    ('NMIX', 'ZNeu(1,4)'),
    ('NMIX', 'ZNeu(2,4)'),
    ('NMIX', 'ZNeu(3,4)'),
    ('NMIX', 'ZNeu(4,4)'),
    ('UMIX', 'UCha(1,1)'),
    ('UMIX', 'UCha(2,1)'),
    ('UMIX', 'UCha(1,2)'),
    ('UMIX', 'UCha(2,2)'),
    ('VMIX', 'VCha(1,1)'),
    ('VMIX', 'VCha(2,1)'),
    ('VMIX', 'VCha(1,2)'),
    ('VMIX', 'VCha(2,2)'),
    ('STAUMIX', 'USf(1,1)'),
    ('STAUMIX', 'USf(2,1)'),
    ('STAUMIX', 'USf(1,2)'),
    ('STAUMIX', 'USf(2,2)'),
    ('STOPMIX', 'USf(1,1)'),
    ('STOPMIX', 'USf(2,1)'),
    ('STOPMIX', 'USf(1,2)'),
    ('STOPMIX', 'USf(2,2)'),
    ('SBOTMIX', 'USf(1,1)'),
    ('SBOTMIX', 'USf(2,1)'),
    ('SBOTMIX', 'USf(1,2)'),
    ('SBOTMIX', 'USf(2,2)'),
    ('ALPHA', 'Alpha'),
    ('HMIX', 'Qscale'),
    ('HMIX', 'MUE'),
    ('HMIX', 'TB'),
    ('HMIX', 'VEV'),
    ('HMIX', 'MA02'),
    ('GAUGE', 'Qscale'),
    ('GAUGE', 'g1'),
    ('GAUGE', 'g2'),
    ('GAUGE', 'g3'),
    ('MSOFT', 'Qscale'),
    ('MSOFT', 'M1'),
    ('MSOFT', 'M2'),
    ('MSOFT', 'M3'),
    ('MSOFT', 'MHu2'),
    ('MSOFT', 'MHd2'),
    ('MSOFT', 'MSL(1)'),
    ('MSOFT', 'MSL(2)'),
    ('MSOFT', 'MSL(3)'),
    ('MSOFT', 'MSE(1)'),
    ('MSOFT', 'MSE(2)'),
    ('MSOFT', 'MSE(3)'),
    ('MSOFT', 'MSQ(1)'),
    ('MSOFT', 'MSQ(2)'),
    ('MSOFT', 'MSQ(3)'),
    ('MSOFT', 'MSU(1)'),
    ('MSOFT', 'MSU(2)'),
    ('MSOFT', 'MSU(3)'),
    ('MSOFT', 'MSD(1)'),
    ('MSOFT', 'MSD(2)'),
    ('MSOFT', 'MSD(3)'),
    ('AE', 'Qscale'),
    ('AE', 'Af(1,1)'),
    ('AE', 'Af(2,2)'),
    ('AE', 'Af(3,3)'),
    ('AU', 'Qscale'),
    ('AU', 'Af(1,1)'),
    ('AU', 'Af(2,2)'),
    ('AU', 'Af(3,3)'),
    ('AD', 'Qscale'),
    ('AD', 'Af(1,1)'),
    ('AD', 'Af(2,2)'),
    ('AD', 'Af(3,3)'),
    ('YE', 'Qscale'),
    ('YE', 'Yf(3,3)'),
    ('YU', 'Qscale'),
    ('YU', 'Yf(3,3)'),
    ('YD', 'Qscale'),
    ('YD', 'Yf(3,3)'),
    ('SMINPUTS', 'mod_MZ'),
    ('MASS', 'mod_MW'),
    ('FeynHiggs', 'gm2'),
    ('FeynHiggs', 'EDMn'),
    ('FeynHiggs', 'DeltaRho'),
    ('FeynHiggs', 'MWSM'),
    ('FeynHiggs', 'EDMeTh'),
    ('FeynHiggs', 'MWMSSM'),
    ('FeynHiggs', 'mHpm'),
    ('FeynHiggs', 'mH'),
    ('FeynHiggs', 'SW2effMSSM'),
    ('FeynHiggs', 'EDMHg'),
    ('FeynHiggs', 'SW2effSM'),
    ('FeynHiggs', 'mA'),
    ('FeynHiggs', 'mh'),
    ('Micromegas', 'SMbsg'),
    ('Micromegas', 'Bll'),
    ('Micromegas', 'Omega'),
    ('Micromegas', 'Bsg'),
    ('Micromegas', 'sigma_p_si'),
    ('SuperISO', 'SIbsg'),
    ('SuperISO', 'SIgm2'),
    ('SuperISO', 'SId0'),
    ('BPhysics', 'RDMK'),
    ('BPhysics', 'Psll'),
    ('BPhysics', 'BRbtn'),
    ('BPhysics', 'Pllsapx'),
    ('BPhysics', 'BRXsll'),
    ('BPhysics', 'RDMs'),
    ('BPhysics', 'BRbsg'),
    ('BPhysics', 'BRKl2'),
    ('BPhysics', 'RDMb'),
    ('BPhysics', 'Pdll'),
    ('BPhysics', 'BRKpnn'),
    ('LSP scattering', 's2out'),
    ('LSP scattering', 's3out'),
    ('LSP scattering', 'ss2out'),
    ('LSP scattering', 'ss3out'),
    ('SUSY-POPE', 'Ab'),
    ('SUSY-POPE', 'Afb_l'),
    ('SUSY-POPE', 'sigma_had'),
    ('SUSY-POPE', 'Afb_b'),
    ('SUSY-POPE', 'Al'),
    ('SUSY-POPE', 'Afb_c'),
    ('SUSY-POPE', 'MW'),
    ('SUSY-POPE', 'Rc'),
    ('SUSY-POPE', 'Rl'),
    ('SUSY-POPE', 'sin_theta_eff'),
    ('SUSY-POPE', 'GZ_in'),
    ('SUSY-POPE', 'DAlpha_had_in'),
    ('SUSY-POPE', 'Gamma_z'),
    ('SUSY-POPE', 'Ac'),
    ('SUSY-POPE', 'Rb'),
    ('MASS', 'mod_Mh0'),
    ('MASS', 'mod_MHH'),
    ('MASS', 'mod_MHp'),
    ('ALPHA', 'mod_Alpha'),
    ('CVHMIX', 'mod_UH(1,1)'),
    ('CVHMIX', 'mod_UH(2,1)'),
    ('CVHMIX', 'mod_UH(3,1)'),
    ('CVHMIX', 'mod_UH(1,2)'),
    ('CVHMIX', 'mod_UH(2,2)'),
    ('CVHMIX', 'mod_UH(3,2)'),
    ('CVHMIX', 'mod_UH(1,3)'),
    ('CVHMIX', 'mod_UH(2,3)'),
    ('CVHMIX', 'mod_UH(3,3)'),
    ('PRECOBS', 'mod_DeltaRho'),
    ('PRECOBS', 'mod_MWSM'),
    ('PRECOBS', 'mod_SW2effSM'),
    ('PRECOBS', 'mod_gminus2mu'),
    ('PRECOBS', 'mod_EDMeTh'),
    ('PRECOBS', 'mod_EDMn'),
    ('PRECOBS', 'mod_EDMHg')]

con = None
def parse_args():
    parser = argparse.ArgumentParser(description='Creating an sql data base')
    parser.add_argument('--output-file','-o', dest='output_file', action='store', 
            default='test.db',  help='Name of output date base file')
    parser.add_argument('--update', dest='update', action='store_true', 
            default=False,  help='Recreate data base, i.e. delete existing file if exists')
    return parser.parse_args()

args= parse_args()

def create_lookup(con,cur,obs_ids):
    #create table
    cur.execute('create table if not exists obs_id_lookup(id integer primary key, point_column TEXT, obs_id_field1 TEXT, obs_id_field2 TEXT)')
    #fill 
    for i,obs_id in enumerate(obs_ids):
        cur.execute('insert into obs_id_lookup values(null,?,?,?)',('obs{}'.format(i),obs_id[0],obs_id[1]))
    #commit
    con.commit()
    
def create_points_table(con,cur):
    # get the column names from the lookup table!!!
    cur.execute('select point_column from obs_id_lookup')
    point_column_names=[ name_tuple[0] for name_tuple in cur.fetchall()]
    #create table with (point_id, collection_id, [observables])
    cur.execute('create table if not exists points(point_id integer primary key, collection_id, {})'.format(','.join(point_column_names)))
    #commit
    con.commit()

if not args.update:
    try:
        os.remove(args.output_file)
    except FileNotFoundError:
        pass

# the real stuff
try:
    #connection
    con=sqlite3.connect(args.output_file)
    #cursor
    cur=con.cursor()
    #create lookup 
    create_lookup(con,cur,all_obs_ids)
    create_points_table(con,cur)
    con.commit()

# Finalise ...
except sqlite3.Error as e:
    if con:
        con.rollback()
    print('ERROR: {}'.format(e.args[0]))
    sys.exit()
finally:
    if con:
        con.close()

