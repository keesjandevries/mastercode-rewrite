#! /usr/bin/env python
import argparse, minuit2


#point calculator
from ObsCalculator import point, inputs
#chi2 calculation
from PointAnalyser import Analyse, Constraints_list
from User.data_sets import data_sets

#FIXME: turn this into a real tool

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data-set' , default="pmssm_with_Oh2", help='data set for X^2 calculation')
    return parser.parse_args()

def f(xx,y):
    return ((xx-2)/3)**2+y**2+y**4


def cmssm_chi2(m0,m12,c,d,e,f,g):
    input_pars=inputs.get_mc_cmssm_inputs(m0,m12,c,d,e,f,g)
    slha_obj, observables ,stdouts= point.run_point(**input_pars)
    #pass this constraints list to the chi2 function
    total, breakdown = Analyse.chi2(observables,constraints)
    return total

def pmssm8_chi2(msq12,msq3,msl, M1, A, MA,tanb,mu,mt,mz,Delta_alpha_had):
    input_pars=inputs.get_mc_pmssm8_inputs(msq12,msq3,msl, M1, A, MA,tanb,mu,mt,mz,Delta_alpha_had)
    slha_obj, observables ,stdouts= point.run_point(**input_pars)
    #pass this constraints list to the chi2 function
    total, breakdown = Analyse.chi2(observables,constraints)
    return total

def pmssm10_chi2(msq12,msq3,msl, M1,M2,M3, A, MA,tanb,mu,mt,mz,Delta_alpha_had):
    input_pars=inputs.get_mc_pmssm10_inputs(msq12,msq3,msl, M1,M2,M3, A, MA,tanb,mu,mt,mz,Delta_alpha_had)
    slha_obj, observables ,stdouts= point.run_point(**input_pars)
    #pass this constraints list to the chi2 function
    total, breakdown = Analyse.chi2(observables,constraints)
    return total
   
if __name__ == '__main__':
    args=parse_args()
    all_constraints=Constraints_list.constraints
    #mc8 data set
    try:
        data_set=data_sets[args.data_set]
    except KeyError:
        print("WARNING: \"{}\" invalid data set. No X^2 is calculated".format(args.data_set))
        data_set=[]
    constraints={name: all_constraints[name] for name in data_set}

    parameters=[271.378279475, 920.368119935, 14.4499538001, -1193.57068242, 173.474173, 91.1877452551, 0.0274821578423]
#    m = minuit2.Minuit2(cmssm_chi2,m0=271.378279475,m12=920.368119935,c=14.4499538001,d=-1193.57068242,e=173.474173,
#            f=91.1877452551,g=0.0274821578423)
    m = minuit2.Minuit2(pmssm10_chi2)
    #1777.45       1693.2      417.803      295.476         1910      711.455      44.2787      747.502      173.227      91.1874    0.0274981
    m.values['msq12']=1777.45
    m.values['msq3']=1693.2
    m.values['msl']=417.803
    m.values['M1']=295.476
    m.values['M2']=2*295.476
    m.values['M3']=6*295.476
    m.values['A']=1910.
    m.values['MA']=711.455
    m.values['tanb']=44.2787
    m.values['mu']=747.502
    m.values['mt']=173.227
    m.values['mz']=91.1874
    m.values['Delta_alpha_had']=0.0274981
    #
    m.errors['msq12']=1.
    m.errors['msq3']=1.
    m.errors['msl']=1.
    m.errors['M1']=1.
    m.errors['M2']=100.
    m.errors['M3']=100.
    m.errors['A']=1.
    m.errors['MA']=1.
    m.errors['tanb']=0.1
    m.errors['mu']=1.
    m.errors['mt']=0.9
    m.errors['mz']=0.0021
    m.errors['Delta_alpha_had']=0.0001
#    m = minuit2.Minuit2(f, xx=1,y=1)
#    m.errors['m0']=500.
    m.fixed['msq12']=True
    m.fixed['msq3']=True
    m.fixed['msl']=True
    m.fixed['M1']=True
    m.fixed['A']=True
    m.fixed['MA']=True
    m.fixed['tanb']=True
    m.fixed['mu']=True
    m.fixed['mt']=True
    m.fixed['mz']=True
    m.fixed['Delta_alpha_had']=True
    m.printMode=1
    m.migrad()
    m.fixed['msq12']=False
    m.fixed['msq3']=False
    m.fixed['msl']=False
    m.fixed['M1']=False
    m.fixed['A']=False
    m.fixed['MA']=False
    m.fixed['tanb']=False
    m.fixed['mu']=False
    m.fixed['mt']=False
    m.fixed['mz']=False
    m.fixed['Delta_alpha_had']=False
    m.migrad()
#20130604 KJ: result from pmssm10 startint from pmssm8 bestfit    
#         19.9565 |      1663.99      1671.75      414.131      294.935      311.199      1712.73      1841.21      718.489      43.4923       775.09      173.233      91.1874    0.0275018




#20130604 KJ: these were from pmssm8 bestfit point outcome was
#1777.45       1693.2      417.803      295.476         1910      711.455      44.2787      747.502      173.227      91.1874    0.0274981
# X^2=22.54 -> 21.17 :D
#    m.values['msq12']=3147.75241565
#    m.values['msq3']=2006.4966607
#    m.values['msl']=418.449318804
#    m.values['M1']=295.558738658
#    m.values['A']=1850.24470262
#    m.values['MA']=711.423108612
#    m.values['tanb']=43.8530565062
#    m.values['mu']=749.184806808
#    m.values['mt']=174.024881
#    m.values['mz']=91.1873524598
#    m.values['Delta_alpha_had']=0.0275569129
#    #
#    m.errors['msq12']=10.
#    m.errors['msq3']=10.
#    m.errors['msl']=10.
#    m.errors['M1']=10.
#    m.errors['A']=10.
#    m.errors['MA']=10.
#    m.errors['tanb']=0.1
#    m.errors['mu']=10.
#    m.errors['mt']=0.9
#    m.errors['mz']=0.0021
#    m.errors['Delta_alpha_had']=0.0001
