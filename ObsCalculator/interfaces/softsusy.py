#! /usr/bin/env python

from ctypes import cdll,  c_char_p, create_string_buffer


name = "SoftSUSY"
SPlib = cdll.LoadLibrary('packages/lib/libmcsoftsusy.so')

#NOTE: the input slha observable ids (oids) follow the output of slhalib.py:
#BLOCK MASS
#        25     1.24444583E+02   # Mh0   
# would result in ('MASS','Mh0')
# slhalib.py is based on slhalib (hep-ph/0605049) 
# this code does not recognise all block, so we have to introduce our own definitions
# below I indicate where this is not the case

#NOTE: these defaults come from softsusy-<version>/defs.cpp
default_inputs={
    ('SMINPUTS', 'invAlfaMZ')   : 127.908953,
    ('SMINPUTS', 'GF')          : 1.16639e-05,
    ('SMINPUTS', 'AlfasMZ')     : 0.1187,
    ('SMINPUTS', 'MZ')          : 91.1876,
    ('SMINPUTS', 'Mt')          : 173.2,
    ('SMINPUTS', 'Mb')          : 4.2,
    ('SMINPUTS', 'Mtau')        : 1.77703,
    #NOTE: BLOCK SOFTSUSY is not recognised by slhalib, so have our own definitions
    ('SOFTSUSY','TOLERANCE')    : 1.0e-3,
    ('SOFTSUSY','MIXING')       : 1.0 ,
    ('SOFTSUSY','PRINTOUT')     : 0.0 ,
    ('SOFTSUSY','QEWSB')        : 1.0 ,
    ('SOFTSUSY','2_LOOP')       : 1.0 ,
    ('SOFTSUSY','numHiggsLoops'): 2.0 ,
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
def get_cmssm_input_slha(slha_params):
    slha="""# BASED ON: Example input in SLHA format, and suitable for input to
# SOFTSUSY (v1.8 or higher): benchmark point - see arXiv:1109.3859
Block MODSEL		     # Select model
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
    1   {prec}      # Numerical precision: suggested range 10^(-3...-6)
    2   {mix}      # Quark mixing parameter: see manual
    3   {verb}          # verbose options
    4   {qewsb}         # electro weak symmetry breaking scale x*sqrt(m_stop1,m_stop2)
    5   {two_loop}      # Include 2-loop scalar mass squared/trilinear RGEs
    7   {n_higgs_loops}     # number of loops in REWSB/mh calculation""".format(
    alpha_inv   =slha_params[('SMINPUTS', 'invAlfaMZ')],
    g_fermi     =slha_params[('SMINPUTS', 'GF')       ],
    alpha_s     =slha_params[('SMINPUTS', 'AlfasMZ')  ],
    mz          =slha_params[('SMINPUTS', 'MZ')       ],
    mb          =slha_params[('SMINPUTS', 'Mb')       ],
    mtop        =slha_params[('SMINPUTS', 'Mt')       ],
    mtau        =slha_params[('SMINPUTS', 'Mtau')     ],
    m0 	        =slha_params[('MINPAR', 'M0')         ],
    m12 	    =slha_params[('MINPAR', 'M12')        ],
    tanb 	    =slha_params[('MINPAR', 'TB')         ],
    sign_mu     =slha_params[('MINPAR', 'signMUE')    ],
    A0 	        =slha_params[('MINPAR', 'A')          ], 
    prec        =slha_params[('SOFTSUSY','TOLERANCE') ],
    mix         =slha_params[('SOFTSUSY','MIXING')    ],
    verb        =slha_params[('SOFTSUSY','PRINTOUT')  ], 
    qewsb       =slha_params[('SOFTSUSY','QEWSB')     ],
    two_loop    =slha_params[('SOFTSUSY','2_LOOP')    ], 
    n_higgs_loops=slha_params[('SOFTSUSY','numHiggsLoops')]      
    )
    return slha



def get_pmssm_input_slha(slha_params):
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
    1   {prec}      # Numerical precision: suggested range 10^(-3...-6)
    2   {mix}      # Quark mixing parameter: see manual
    3   {verb}          # verbose options
    4   {qewsb}         # electro weak symmetry breaking scale x*sqrt(m_stop1,m_stop2)
    5   {two_loop}      # Include 2-loop scalar mass squared/trilinear RGEs
    7   {n_higgs_loops}     # number of loops in REWSB/mh calculation
Block EXTPAR          # non-universal SUSY breaking parameters
      0   -1.000000000000000e+00	 # Set MX=MSUSY 
      1  {M_1}         # M_1(MX)
      2  {M_2}         # M_2(MX)
      3  {M_3}         # M_3(MX)
     11  {At}         # At(MX)
     12  {Ab}         # Ab(MX)
     13  {Atau}         # Atau(MX)
     23  {mu}         # mu(MX)
     26  {mA}         # mA(pole)
     31  {meL}         # meL(MX)
     32  {mmuL}         # mmuL(MX)
     33  {mtauL}         # mtauL(MX)
     34  {meR}         # meR(MX)
     35  {mmuR}         # mmuR(MX)
     36  {mtauR}         # mtauR(MX)
     41  {mqL1}         # mqL1(MX)
     42  {mqL2}         # mqL2(MX)
     43  {mqL3}         # mqL3(MX)
     44  {muR}         # muR(MX)
     45  {mcR}         # mcR(MX)
     46  {mtR}         # mtR(MX)
     47  {mdR}         # mdR(MX)
     48  {msR}         # msR(MX)
     49  {mbR}         # mbR(MX)""".format(
    alpha_inv   =slha_params[('SMINPUTS', 'invAlfaMZ')],
    g_fermi     =slha_params[('SMINPUTS', 'GF')       ],
    alpha_s     =slha_params[('SMINPUTS', 'AlfasMZ')  ],
    mz          =slha_params[('SMINPUTS', 'MZ')       ],
    mb          =slha_params[('SMINPUTS', 'Mb')       ],
    mtop        =slha_params[('SMINPUTS', 'Mt')       ],
    mtau        =slha_params[('SMINPUTS', 'Mtau')     ],
    tanb 	    =slha_params[('MINPAR', 'TB')         ],
    prec        =slha_params[('SOFTSUSY','TOLERANCE') ],
    mix         =slha_params[('SOFTSUSY','MIXING')    ],
    verb        =slha_params[('SOFTSUSY','PRINTOUT')  ], 
    qewsb       =slha_params[('SOFTSUSY','QEWSB')     ],
    two_loop    =slha_params[('SOFTSUSY','2_LOOP')    ], 
    n_higgs_loops=slha_params[('SOFTSUSY','numHiggsLoops')],      
    M_1         =slha_params[('EXTPAR', 'M1')         ],  
    M_2         =slha_params[('EXTPAR', 'M2')         ],   
    M_3         =slha_params[('EXTPAR', 'M3')         ],  
    At          =slha_params[('EXTPAR', 'Atau')       ],  
    Ab          =slha_params[('EXTPAR', 'At')         ],  
    Atau        =slha_params[('EXTPAR', 'Ab')         ],  
    mu          =slha_params[('EXTPAR', 'MUE')        ],  
    mA          =slha_params[('EXTPAR', 'MA0')        ],  
    meL         =slha_params[('EXTPAR', 'MSL(1)')     ],        
    mmuL        =slha_params[('EXTPAR', 'MSL(2)')     ],        
    mtauL       =slha_params[('EXTPAR', 'MSL(3)')     ],        
    meR         =slha_params[('EXTPAR', 'MSE(1)')     ],        
    mmuR        =slha_params[('EXTPAR', 'MSE(2)')     ],        
    mtauR       =slha_params[('EXTPAR', 'MSE(3)')     ],        
    mqL1        =slha_params[('EXTPAR', 'MSQ(1)')     ],        
    mqL2        =slha_params[('EXTPAR', 'MSQ(2)')     ],        
    mqL3        =slha_params[('EXTPAR', 'MSQ(3)')     ],        
    muR         =slha_params[('EXTPAR', 'MSU(1)')     ],        
    mcR         =slha_params[('EXTPAR', 'MSU(2)')     ],        
    mtR         =slha_params[('EXTPAR', 'MSU(3)')     ],        
    mdR         =slha_params[('EXTPAR', 'MSD(1)')     ],        
    msR         =slha_params[('EXTPAR', 'MSD(2)')     ],                 
    mbR         =slha_params[('EXTPAR', 'MSD(3)')     ]        
    )
    return slha

def get_nuhm2_input_slha(slha_params):
    return """# INSPIRED BY: Example input in SLHA format, and suitable for input to
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
    1   {m0} 	     # m0
    2   {m12} 	     # m12
    3   {tanb} 	     # tanb
    4   {sign_mu} 	     # sign(mu)
    5   {A0} 	     # A0
Block SOFTSUSY               # Optional SOFTSUSY-specific parameters
    1   {prec}      # Numerical precision: suggested range 10^(-3...-6)
    2   {mix}      # Quark mixing parameter: see manual
    3   {verb}          # verbose options
    4   {qewsb}         # electro weak symmetry breaking scale x*sqrt(m_stop1,m_stop2)
    5   {two_loop}      # Include 2-loop scalar mass squared/trilinear RGEs
    7   {n_higgs_loops}     # number of loops in REWSB/mh calculation
Block EXTPAR          # non-universal SUSY breaking parameters
    21  {mhd2}         # m^2_H_d
    22  {mhu2}         # m^2_H_u""".format(
    alpha_inv   =slha_params[('SMINPUTS', 'invAlfaMZ')],
    g_fermi     =slha_params[('SMINPUTS', 'GF')       ],
    alpha_s     =slha_params[('SMINPUTS', 'AlfasMZ')  ],
    mz          =slha_params[('SMINPUTS', 'MZ')       ],
    mb          =slha_params[('SMINPUTS', 'Mb')       ],
    mtop        =slha_params[('SMINPUTS', 'Mt')       ],
    mtau        =slha_params[('SMINPUTS', 'Mtau')     ],
    m0 	        =slha_params[('MINPAR', 'M0')         ],
    m12 	    =slha_params[('MINPAR', 'M12')        ],
    tanb 	    =slha_params[('MINPAR', 'TB')         ],
    sign_mu     =slha_params[('MINPAR', 'signMUE')    ],
    A0 	        =slha_params[('MINPAR', 'A')          ], 
    prec        =slha_params[('SOFTSUSY','TOLERANCE') ],
    mix         =slha_params[('SOFTSUSY','MIXING')    ],
    verb        =slha_params[('SOFTSUSY','PRINTOUT')  ], 
    qewsb       =slha_params[('SOFTSUSY','QEWSB')     ],
    two_loop    =slha_params[('SOFTSUSY','2_LOOP')    ], 
    n_higgs_loops=slha_params[('SOFTSUSY','numHiggsLoops')],      
    mhd2        =slha_params[('EXTPAR', 'MHd2')       ], 
    mhu2        =slha_params[('EXTPAR', 'MHu2')       ] 
              )
    
def get_nuhm1_input_slha(slha_params):
    #NOTE: MH2 is not defined in slhalib
    slha_params[('EXTPAR', 'MHd2')]=slha_params[('EXTPAR', 'MH2')]  
    slha_params[('EXTPAR', 'MHu2')]=slha_params[('EXTPAR', 'MH2')]
    return get_nuhm2_input_slha(slha_params)
 
def run(model, inputs,verbose=None):
    # set inputs to default
    slha_params=default_inputs.copy()
    # update to get the parsed inputs
    slha_params.update(inputs)

    if model=='cMSSM':
        inputslha=get_cmssm_input_slha(slha_params)
    elif model=='pMSSM':
        inputslha=get_pmssm_input_slha(slha_params)
    elif model=='NUHM2':
        inputslha=get_nuhm2_input_slha(slha_params)

    else:
        print("ERROR: No valid model provided")
        return "", 1
    if verbose: print(inputslha)

    # then run on the inputslha file
    c_str_buf = create_string_buffer(SLHA_MAX_SIZE)
    error = SPlib.run(c_char_p(inputslha.encode('ascii')),c_str_buf,10000)
    return c_str_buf.value.decode('utf-8'), error
