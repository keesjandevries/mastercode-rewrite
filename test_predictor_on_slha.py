#! /usr/bin/env python
import os, sys, select, argparse, pprint, json, math
from collections import OrderedDict

#from ObsCalculator import point
from ObsCalculator import point
from tools import  pickle_object

from PointAnalyser import Analyse
from PointAnalyser import Constraints_list

#storage
import Storage.interfaces.ROOT as root
from Storage import old_mc_rootstorage 

def parse_args():
    #WARNING: this option list is rather ad hoc
    # feel free to ammend it!
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--observables', '-o', dest='obs'      , action='store_true', 
            help='print observables')
    parser.add_argument('--max_number' , '-N', dest='nmax'     , action='store' ,type=int , 
            help='maximum number of files to process')
    parser.add_argument('--breakdown'  , '-b', dest='breakdown', action='store_true', 
            help='print X^2 breakdonw')
    parser.add_argument('--root_save'  , '-r', dest='root_save', action='store_true', 
            help='save to root file')
    parser.add_argument('--compare'    , '-c', dest='compare'  , action='store_true', 
            help='compare mcpp ouput to block predict in mc-old slha')
    parser.add_argument('--key_has'    , '-k', dest='key_has'  , action='store', default=None, 
            help='look for ')
    parser.add_argument('--verbose'    , '-v', dest='verbose'  , action='store', 
            nargs="+", help='verbosity', default=[])
    parser.add_argument('--input_spectrum' , '-i', dest='input_spectrum', action='store', nargs="+",
            default=[], help='')
    return parser.parse_args()



#WARNING: mc-old specific
index_dict={
        '1' :{'oid':('BPhysics','BRbsg'),   'constraint':'R(b->sg)'},# R(B->s gamma) 
        '2' :{'oid':('BPhysics','RDMs'),    'constraint':'R(D_ms)'},# R(Delta m_s)  
        '3' :{'oid':('BPhysics','Psll'),    'constraint':'mc-old-bsmm'},# BR(Bs->mumu)  
        '4' :{'oid':('BPhysics','BRbtn'),   'constraint':'R(B->taunu)'},# R(B->tau nu)  
        '5' :{'oid':('BPhysics','BRXsll'),  'constraint':'R(B->Xsll)'},# R(Bs->Xsll)   
        '6' :{'oid':('BPhysics','BRKl2'),   'constraint':'R(K->lnu)'},# R(K->tau nu)  
        '24':{'oid':('BPhysics','RDMb'),    'constraint':'R(Delta_md)'}, # R(Delta m_d) 
        '25':{'oid':('BPhysics','RDMK'),    'constraint':'R(Delta_mk)'}, # R(Delta m_k) 
        '26':{'oid':('BPhysics','BRKpnn'),  'constraint':'R(Kp->pinn)'}, # R(Kp->pinn)  
        '27':{'oid':('BPhysics','Pdll'),    'constraint':'BR(Bd->ll)'}, # BR(Bd->ll)   
        '29':{'oid':('SuperISO', 'SId0'),    'constraint':'D_0(K*g)'},
#        '28':{'oid':('BPhysics',''),'constraint':}, # R(Dms)/R(Dmd)
        '20':{'oid':('Micromegas', 'Omega'),'constraint':'Oh^2_mc8'},

        '16':{'oid':('SUSY-POPE','Ab'),'constraint':'Ab'},
        '17':{'oid':('SUSY-POPE','Ac'),'constraint':'Ac'},
        '14':{'oid':('SUSY-POPE','Afb_b'),'constraint':'Afb(b)'},
        '15':{'oid':('SUSY-POPE','Afb_c'),'constraint':'Afb(c)'},
        '18':{'oid':('SUSY-POPE','Al'),'constraint':'Al(SLD)'},
        '21':{'oid':('SUSY-POPE','Al'),'constraint':'Al(P_tau)'},
        '10':{'oid':('SUSY-POPE','Gamma_z'),'constraint':'Gamma_Z'},
        '8' :{'oid':('SUSY-POPE','MW'),'constraint':'MW-mc-old'},
        '12':{'oid':('SUSY-POPE','Rb'),'constraint':'Rb'},
        '13':{'oid':('SUSY-POPE','Rc'),'constraint':'Rc'},
        '11':{'oid':('SUSY-POPE','Rl'),'constraint':'Rl'},
        '22':{'oid':('SUSY-POPE','Afb_l'),'constraint':'Afb_l'},
        '23':{'oid':('SUSY-POPE','sigma_had'),'constraint':'sigma_had^0'},
        '9' :{'oid':('SUSY-POPE','sin_theta_eff'),'constraint':'sintheta_eff'},
        }

#WARNING: mc-old specific
def read_predict_block_mc_old(filename):
    in_pred=False
    count=0
    d=OrderedDict()
    tot_chi2=0
    with open(filename) as f:
        for line in f:
            if 'PREDICT' in line and count ==0:
                in_pred=True
            elif 'PREDICT' in line:
                in_pred=False
            elif in_pred:
                segs=line.split()
                index, value, chi2 = segs[0], segs[1], segs[-1]
                if index in index_dict.keys():
                    try:
                        d[index_dict[index]['oid']]=float(value)
                        d[index_dict[index]['constraint']]=float(chi2)
                    except ValueError:
                        continue
    return d


if __name__=="__main__" :
    args = parse_args()
    all_params={}

    old_new_dict=OrderedDict()
    #loop over command line input slha file 

    #some things need to be defined outside the loop
    all_constraints=Constraints_list.constraints
    data_set= [ 'Al(SLD)', 'Ab', 'Ac', 'Oh^2_mc8', 'Higgs125', 'BR(Bd->ll)',  
            'Gamma_Z', 'GZ_in', 'R(B->Xsll)', 'Al(P_tau)', 'MZ', 'R(D_ms)', 'MW', 'Afb_l', 
            'xenon100', 'DAlpha_had', 'R(Delta_mk)',  'sigma_had^0', 'Afb(c)', 
             'Afb(b)',  'R(b->sg)', 'R(Dms)/R(Dmd)', 'R(B->taunu)', 
            'Rc', 'Rb',  'Rl', 'mc8_bsmm', 'sintheta_eff', 'Mt', 'R(K->lnu)', 'R(Kp->pinn)', 'gminus2mu', 'MATANB',
            'MW-mc-old','Bsmumu','R(Delta_md)','D_0(K*g)','mc-old-bsmm']
    constraints={name: all_constraints[name] for name in data_set}
    bpp = pprint.PrettyPrinter(indent=4, depth=3)
    for count, spec in  enumerate(args.input_spectrum):
        if args.nmax and count>=args.nmax: break
        all_params['spectrumfile']=spec

        #the input for DeltaAlfa5had has to be hard-coded like in SUSY-POPE
        all_params['SUSY-POPE']={'non_slha_inputs':{'DeltaAlfa5had': 0.02758}}
        
        #check verbosity
        if args.verbose:
            all_params['verbose']=args.verbose

        try:
            slha_obj, combined_obs, stdouts = point.run_point(model='dummy', **all_params)
        except TypeError:
            print("ERROR: Point failed to run")
            continue

        #pass this constraints list to the chi2 function
        total, breakdown = Analyse.chi2(combined_obs,constraints)


        # optional printing
        if args.obs:
            bpp.pprint(combined_obs)
        if args.breakdown:
            bpp.pprint(breakdown)
            print('Total chi2:',total)

        # get values from predict block
        mc_old_obs=read_predict_block_mc_old(spec)

        if args.compare:
            combined_obs.update(breakdown)
            for key, old_val in mc_old_obs.items():
                if (not args.key_has) or (args.key_has in key):
                    new_val=combined_obs[key]
                    if 'compare' in args.verbose:
                        print("{:<30}: MC++: {:<25} , mc-old: {:<20}, difference {}".format(key,new_val,old_val,new_val-old_val ))
                    if not old_new_dict.get(key):
                        old_new_dict[key]=[(new_val,old_val)]
                    else:
                        old_new_dict[key].append((new_val,old_val))

    if args.compare and 'stats' in args.verbose:
        ave_d=OrderedDict()
        std_d=OrderedDict()
        max_d=OrderedDict()
        for name, l in old_new_dict.items():
            ave_d[name]=sum([v[1]-v[0] for v in l ])/len(l)
            std_d[name]=math.sqrt( sum([(v[1]-v[0]-ave_d[name])**2 for v in l ])/len(l)  )
            max_d[name]=max([abs(v[1]-v[0]) for v in l])

        print("{:<30}: {:<25} {:<25} {:<25} ".format('observable','average diff','standard dev','maximum outlier'))
        for name, chi2diff in ave_d.items():
            print("{:<30}: {:<25} {:<25} {:<25} ".format(name,chi2diff,std_d[name],max_d[name]))

