#! /usr/bin/env python

from ctypes import cdll,  c_char_p, create_string_buffer


name = "SoftSUSY"
SPlib = cdll.LoadLibrary('packages/lib/libmcsoftsusy.so')


#FIXME: should the softsusy parameters be part of this?
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

# instructions: to make add a model function like this
# 1. look in softsusy-<version>/benchmarks/<your_model><example_id>.in, where <version is>
#       the softsusy version, <your_model> is e.g. cmssm, <example_id> is e.g. 1.1
# 2. define slha="""<this slha>""".format(<your_identifier>=slha_params[<observable ids>], ...) 
#       with <this slha> the slha from softsusy-<version>/benchmarks/
#       <your_identifier> is a shortname that you invent yourselve on the spot
#       <observable ids> are obtained as follows
# 3. initialise and slha object <your_object> with <this slha> file and do print( <your_object> ).
#       this gives you the right keys that you should use. This is not strickly nessicary, but it provides
#       consistancy
def get_cmssm_input_slha(slha_params,verbose=None):
    slha="""Block MODSEL		     # Select model
    1    1		     # sugra
Block SMINPUTS		     # Standard Model inputs
    1	{alpha_inv}	     # alpha^(-1) SM MSbar(MZ)
    2   {g_fermi}	     # G_Fermi
    3   {alpha_s}	     # alpha_s(MZ) SM MSbar
    4   {mz}	     # MZ(pole)
    5	{mb}	     # mb(mb) SM MSbar
    6   {mtop}	     # mtop(pole)
    7	{mtau}	     # mtau(pole)
Block MINPAR		     # Input parameters
    1   {m0} 	     # m0
    2   {m12} 	     # m12
    3   {tanb} 	     # tanb
    4   {sign_mu} 	     # sign(mu)
    5   {A0} 	     # A0
Block SOFTSUSY               # Optional SOFTSUSY-specific parameters
    1   1.000000000e-03      # Numerical precision: suggested range 10^(-3...-6)
    2   0.000000000e+00	     # Quark mixing parameter: see manual
    5   1.000000000e+00      # Include 2-loop scalar mass squared/trilinear RGEs""".format(
    alpha_inv   =slha_params[('SMINPUTS', 'invAlfaMZ')] ,
    g_fermi     =slha_params[('SMINPUTS', 'GF')       ] ,
    alpha_s     =slha_params[('SMINPUTS', 'AlfasMZ')  ] ,
    mz          =slha_params[('SMINPUTS', 'MZ')       ] ,
    mb          =slha_params[('SMINPUTS', 'Mb')       ] ,
    mtop        =slha_params[('SMINPUTS', 'Mt')       ] ,
    mtau        =slha_params[('SMINPUTS', 'Mtau')     ] ,
    m0 	        =slha_params[('MINPAR', 'M0')         ]  ,
    m12 	    =slha_params[('MINPAR', 'M12')        ]  ,
    tanb 	    =slha_params[('MINPAR', 'TB')         ]  ,
    sign_mu     =slha_params[('MINPAR', 'signMUE')    ]  ,
    A0 	        =slha_params[('MINPAR', 'A')          ]  
                )
    if verbose:
        print(slha)
    return slha

def get_pmssm_input_slha(slha_params,verbose=None):
    slha="""# BASED ON: Example input in SLHA format, and suitable for input to
# SOFTSUSY (v1.8 or higher): benchmark point - see arXiv:1109.3859
Block MODSEL		     # Select model
    1    0		     # non universal
Block SMINPUTS		     # Standard Model inputs
    1	{alpha_inv}	     # alpha^(-1) SM MSbar(MZ)
    2   {g_fermi}  	     # G_Fermi
    3   {alpha_s}  	     # alpha_s(MZ) SM MSbar
    4   {mz}	   	     # MZ(pole)
    5	{mb}	   	     # mb(mb) SM MSbar
    6   {mtop}	   	     # mtop(pole)
    7	{mtau}	   	     # mtau(pole)
Block MINPAR		     # Input parameters
    3   {tanb}	     # tanb
Block SOFTSUSY               # Optional SOFTSUSY-specific parameters
    1   1.000000000e-03      # Numerical precision: suggested range 10^(-3...-6)
    2   0.000000000e+00	     # Quark mixing parameter: see manual
    5   1.000000000e+00      # Include 2-loop scalar mass squared/trilinear RGEs
Block EXTPAR          # non-universal SUSY breaking parameters
      0   -1.000000000000000e+00	 # Set MX=MSUSY 
      1  { M_1   }         # M_1(MX)
      2  { M_2   }         # M_2(MX)
      3  { M_3   }         # M_3(MX)
     11  { At    }         # At(MX)
     12  { Ab    }         # Ab(MX)
     13  { Atau  }         # Atau(MX)
     23  { mu    }         # mu(MX)
     26  { mA    }         # mA(pole)
     31  { meL   }         # meL(MX)
     32  { mmuL  }         # mmuL(MX)
     33  { mtauL }         # mtauL(MX)
     34  { meR   }         # meR(MX)
     35  { mmuR  }         # mmuR(MX)
     36  { mtauR }         # mtauR(MX)
     41  { mqL1  }         # mqL1(MX)
     42  { mqL2  }         # mqL2(MX)
     43  { mqL3  }         # mqL3(MX)
     44  { muR   }         # muR(MX)
     45  { mcR   }         # mcR(MX)
     46  { mtR   }         # mtR(MX)
     47  { mdR   }         # mdR(MX)
     48  { msR   }         # msR(MX)
     49  { mbR   }         # mbR(MX)""".format(
    alpha_inv   =slha_params[('SMINPUTS', 'invAlfaMZ')] ,
    g_fermi     =slha_params[('SMINPUTS', 'GF')       ] ,
    alpha_s     =slha_params[('SMINPUTS', 'AlfasMZ')  ] ,
    mz          =slha_params[('SMINPUTS', 'MZ')       ] ,
    mb          =slha_params[('SMINPUTS', 'Mb')       ] ,
    mtop        =slha_params[('SMINPUTS', 'Mt')       ] ,
    mtau        =slha_params[('SMINPUTS', 'Mtau')     ] ,
    tanb 	    =slha_params[('MINPAR', 'TB')         ]  ,
    M_1         =slha_params[ 
    M_2         =slha_params[ 
    M_3         =slha_params[ 
    At          =slha_params[ 
    Ab          =slha_params[ 
    Atau        =slha_params[ 
    mu          =slha_params[ 
    mA          =slha_params[ 
    meL         =slha_params[ 
    mmuL        =slha_params[ 
    mtauL       =slha_params[ 
    meR         =slha_params[ 
    mmuR        =slha_params[ 
    mtauR       =slha_params[ 
    mqL1        =slha_params[ 
    mqL2        =slha_params[ 
    mqL3        =slha_params[ 
    muR         =slha_params[ 
    mcR         =slha_params[ 
    mtR         =slha_params[ 
    mdR         =slha_params[ 
    msR         =slha_params[          
    mbR         =slha_params[ 
    )
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
