#! /usr/bin/env python

from ctypes import cdll,  c_char_p, create_string_buffer


name = "SoftSUSY"
SPlib = cdll.LoadLibrary('packages/lib/libmcsoftsusy.so')


default_inputs={
    ('SMINPUTS', 'invAlfaMZ')   : 127.908953,
    ('SMINPUTS', 'GF')          : 1.16639e-05,
    ('SMINPUTS', 'AlfasMZ')     : 0.1187,
    ('SMINPUTS', 'MZ')          : 91.1876,
    ('SMINPUTS', 'Mt')          : 173.2,
    ('SMINPUTS', 'Mb')          : 4.2,
    ('SMINPUTS', 'Mtau')        : 1.77703,
        }


SLHA_MAX_SIZE = 10000

#functions like this need to be defined separately for nuhm models and pmssm
def get_cmssm_input_slha(slha_params,verbose=None):
    slha="""Block MODSEL		     # Select model
    1    1		     # sugra
Block SMINPUTS		     # Standard Model inputs
    1	{0}	     # alpha^(-1) SM MSbar(MZ)
    2   {1}	     # G_Fermi
    3   {2}	     # alpha_s(MZ) SM MSbar
    4   {3}	     # MZ(pole)
    5	{4}	     # mb(mb) SM MSbar
    6   {5}	     # mtop(pole)
    7	{6}	     # mtau(pole)
Block MINPAR		     # Input parameters
    1   {7} 	     # m0
    2   {8} 	     # m12
    3   {9} 	     # tanb
    4   {10} 	     # sign(mu)
    5   {11} 	     # A0
Block SOFTSUSY               # Optional SOFTSUSY-specific parameters
    1   1.000000000e-03      # Numerical precision: suggested range 10^(-3...-6)
    2   0.000000000e+00	     # Quark mixing parameter: see manual
    5   1.000000000e+00      # Include 2-loop scalar mass squared/trilinear RGEs""".format(
    slha_params[('SMINPUTS', 'invAlfaMZ')] ,
    slha_params[('SMINPUTS', 'GF')       ] ,
    slha_params[('SMINPUTS', 'AlfasMZ')  ] ,
    slha_params[('SMINPUTS', 'MZ')       ] ,
    slha_params[('SMINPUTS', 'Mb')       ] ,
    slha_params[('SMINPUTS', 'Mt')       ] ,
    slha_params[('SMINPUTS', 'Mtau')     ] ,
    slha_params[('MINPAR', 'M0')         ]  ,
    slha_params[('MINPAR', 'M12')        ]  ,
    slha_params[('MINPAR', 'TB')         ]  ,
    slha_params[('MINPAR', 'signMUE')    ]  ,
    slha_params[('MINPAR', 'A')          ]  
                )
    if verbose:
        print(slha)
    return slha


def run(model, inputs,verbose=None):
    # set inputs to default
    slha_params=default_inputs.copy()
    # update to get the parsed inputs
    slha_params.update(inputs)

    if model=='cMSSM':
        inputslha=get_cmssm_input_slha(slha_params,verbose)
    # this list ought to be extended for new models
    else:
        return "", 1

    # then run on the inputslha file
    c_str_buf = create_string_buffer(SLHA_MAX_SIZE)
    error = SPlib.run(c_char_p(inputslha.encode('ascii')),c_str_buf,10000)
    return c_str_buf.value.decode('utf-8'), error
