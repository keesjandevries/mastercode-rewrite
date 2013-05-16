#NOTE: This is a convenience wrapper to parse the right parameters to 
# ObsCalculator/point.py
#This module contains knowledge about which parameters are parsed to which predictors

def get_mc_cmssm_inputs(m0,m12,tanb,A0,mt,mz,Delta_alpha_had ):
    return {
            'SoftSUSY':{
                'model'         :     'cMSSM'  ,
                ('MINPAR', 'M0'):       m0,
                ('MINPAR', 'M12'):      m12,
                ('MINPAR', 'TB'):       tanb,
                ('MINPAR', 'A'):        A0,
                ('SMINPUTS', 'Mt') :    mt,
                },
            'mc_slha_update':{
                ('SMINPUTS','MZ')   : mz, 
                },
            'SUSY-POPE':{
                'non_slha_inputs':{
                    'DeltaAlfa5had' : Delta_alpha_had,
                    }
                },
            }

def get_mc_nuhm1_inputs(m0,m12,tanb,A0,mh2,mt,mz,Delta_alpha_had):
    return {
            'SoftSUSY':{
                'model'         :       'NUHM1',
                ('MINPAR', 'M0'):       m0,
                ('MINPAR', 'M12'):      m12,
                ('MINPAR', 'TB'):       tanb,
                ('MINPAR', 'A'):        A0,
                ('SMINPUTS', 'Mt') :    mt,
                ('EXTPAR','MH2') :       mh2,
                },
            'mc_slha_update':{
                ('SMINPUTS','MZ')   : mz, 
                },
            'SUSY-POPE':{
                'non_slha_inputs':{
                    'DeltaAlfa5had' : Delta_alpha_had,
                    }
                },
            'FeynHiggs':{
                'drop_extpar' : True,
                }
            }
#NOTE: this is a first order function, only setting SoftSUSY slha input
def get_mc_8d_pmssm_inputs(msq12,msq3,msl, M1, A, MA,tanb,mu):
    return {
            'SoftSUSY':{
                'model'     :   '8d_pMSSM',   
                #values that we set equal
                ('MC_EXTPAR','MC_Msq12') :msq12, 
                ('MC_EXTPAR','MC_Msq3')  :msq3, 
                ('MC_EXTPAR','MC_Msl')   :msl,       
                ('MC_EXTPAR','MC_A')     :A,
                #M2=2*M1, M3=6*M1
                ('EXTPAR','M1')          :M1,
                #Directly set
                ('MINPAR','TB')          :tanb,
                ('EXTPAR', 'MUE')        :mu,
                ('EXTPAR', 'MA0')        :MA,
                },
            }
