# SOFTSUSY3.3.1 SLHA compliant output
# B.C. Allanach, Comput. Phys. Commun. 143 (2002) 305-331, hep-ph/0104145
Block SPINFO          # Program information
     1    SOFTSUSY    # spectrum calculator
     2    3.3.1       # version number
Block MODSEL  # Select model
     1    0   # nonUniversal
Block SMINPUTS             # Standard Model inputs
     1    1.27934000e+02   # alpha_em^(-1)(MZ) SM MSbar
     2    1.16637000e-05   # G_Fermi
     3    1.17200000e-01   # alpha_s(MZ)MSbar
     4    9.11876000e+01   # MZ(pole)
     5    4.25000000e+00   # mb(mb)
     6    1.73300000e+02   # Mtop(pole)
     7    1.77700000e+00   # Mtau(pole)
Block MINPAR               # SUSY breaking input parameters
     3    1.00000000e+01   # tanb
Block EXTPAR               # non-universal SUSY breaking parameters
     1     8.00000000e+02  # M_1(MX)
     2     2.50000000e+03  # M_2(MX)
     3     9.60000000e+02  # M_3(MX)
     11    0.00000000e+00  # At(MX)
     12    0.00000000e+00  # Ab(MX)
     13    0.00000000e+00  # Atau(MX)
     23    2.50000000e+03  # mu(MX)
     26    2.50000000e+03  # mA(pole)
     31    2.50000000e+03  # meL(MX)
     32    2.50000000e+03  # mmuL(MX)
     33    2.50000000e+03  # mtauL(MX)
     34    2.50000000e+03  # meR(MX)
     35    2.50000000e+03  # mmuR(MX)
     36    2.50000000e+03  # mtauR(MX)
     41    9.60000000e+02  # mqL1(MX)
     42    9.60000000e+02  # mqL2(MX)
     43    2.50000000e+03  # mqL3(MX)
     44    9.60000000e+02  # muR(MX)
     45    9.60000000e+02  # mcR(MX)
     46    2.50000000e+03  # mtR(MX)
     47    9.60000000e+02  # mdR(MX)
     48    9.60000000e+02  # msR(MX)
     49    2.50000000e+03  # mbR(MX)
# Low energy data in SOFTSUSY: MIXING=0 TOLERANCE=1.00000000e-03
# mgut=2.50365416e+03 GeV
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03999751e+01   # MW
        25     1.16911809e+02   # h0
        35     2.50009516e+03   # H0
        36     2.49998804e+03   # A0
        37     2.50164812e+03   # H+
   1000021     1.08705317e+03   # ~g
   1000022     7.89595004e+02   # ~neutralino(1)
   1000023     2.43113562e+03   # ~neutralino(2)
   1000024     2.43144904e+03   # ~chargino(1)
   1000025    -2.50009785e+03   # ~neutralino(3)
   1000035     2.55115318e+03   # ~neutralino(4)
   1000037     2.55064647e+03   # ~chargino(2)
   1000001     1.05759929e+03   # ~d_L
   1000002     1.05490713e+03   # ~u_L
   1000003     1.05759929e+03   # ~s_L
   1000004     1.05490713e+03   # ~c_L
   1000005     2.52499672e+03   # ~b_1
   1000006     2.52776577e+03   # ~t_1
   1000011     2.51894936e+03   # ~e_L
   1000012     2.51742731e+03   # ~nue_L
   1000013     2.51894938e+03   # ~mu_L
   1000014     2.51742731e+03   # ~numu_L
   1000015     2.49953454e+03   # ~stau_1
   1000016     2.51720556e+03   # ~nu_tau_L
   2000001     1.02747147e+03   # ~d_R
   2000002     1.02547020e+03   # ~u_R
   2000003     1.02747147e+03   # ~s_R
   2000004     1.02547020e+03   # ~c_R
   2000005     2.55379562e+03   # ~b_2
   2000006     2.55635224e+03   # ~t_2
   2000011     2.50390659e+03   # ~e_R
   2000013     2.50390659e+03   # ~mu_R
   2000015     2.52269194e+03   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -1.04724929e-01       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.99758562e-01   # N_{1,1}
  1  2    -4.62291903e-04   # N_{1,2}
  1  3     2.03418860e-02   # N_{1,3}
  1  4    -8.29525599e-03   # N_{1,4}
  2  1     1.26184459e-02   # N_{2,1}
  2  2     7.98769812e-01   # N_{2,2}
  2  3    -4.30853359e-01   # N_{2,3}
  2  4     4.19729611e-01   # N_{2,4}
  3  1    -8.51146859e-03   # N_{3,1}
  3  2     9.84827672e-03   # N_{3,2}
  3  3     7.06922353e-01   # N_{3,3}
  3  4     7.07171374e-01   # N_{3,4}
  4  1    -1.58476194e-02   # N_{4,1}
  4  2     6.01555971e-01   # N_{4,2}
  4  3     5.60546499e-01   # N_{4,3}
  4  4    -5.68917296e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     7.56198894e-01   # U_{1,1}
  1  2    -6.54341832e-01   # U_{1,2}
  2  1     6.54341832e-01   # U_{2,1}
  2  2     7.56198894e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     7.68520476e-01   # V_{1,1}
  1  2    -6.39825193e-01   # V_{1,2}
  2  1     6.39825193e-01   # V_{2,1}
  2  2     7.68520476e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     3.75479118e-01   # F_{11}
  1  2     9.26830854e-01   # F_{12}
  2  1     9.26830854e-01   # F_{21}
  2  2    -3.75479118e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     4.03294394e-01   # F_{11}
  1  2     9.15070288e-01   # F_{12}
  2  1     9.15070288e-01   # F_{21}
  2  2    -4.03294394e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     4.08128281e-01   # F_{11}
  1  2     9.12924590e-01   # F_{12}
  2  1     9.12924590e-01   # F_{21}
  2  2    -4.08128281e-01   # F_{22}
Block gauge Q= 2.50365416e+03  # SM gauge couplings
     1     3.64483793e-01   # g'(Q)MSSM DRbar
     2     6.36780035e-01   # g(Q)MSSM DRbar
     3     1.03567243e+00   # g3(Q)MSSM DRbar
Block yu Q= 2.50365416e+03  
  3  3     8.32285308e-01   # Yt(Q)MSSM DRbar
Block yd Q= 2.50365416e+03  
  3  3     1.27818694e-01   # Yb(Q)MSSM DRbar
Block ye Q= 2.50365416e+03  
  3  3     9.96696460e-02   # Ytau(Q)MSSM DRbar
Block hmix Q= 2.50365416e+03 # Higgs mixing parameters
     1     2.50000000e+03    # mu(Q)MSSM DRbar
     2     9.54698601e+00    # tan beta(Q)MSSM DRbar
     3     2.43726562e+02    # higgs vev(Q)MSSM DRbar
     4     6.16289800e+06    # mA^2(Q)MSSM DRbar
Block msoft Q= 2.50365416e+03  # MSSM DRbar SUSY breaking parameters
     1     8.00000000e+02      # M_1(Q)
     2     2.50000000e+03      # M_2(Q)
     3     9.60000000e+02      # M_3(Q)
    21    -1.69437987e+05      # mH1^2(Q)
    22    -6.07084875e+06      # mH2^2(Q)
    31     2.50000000e+03      # meL(Q)
    32     2.50000000e+03      # mmuL(Q)
    33     2.50000000e+03      # mtauL(Q)
    34     2.50000000e+03      # meR(Q)
    35     2.50000000e+03      # mmuR(Q)
    36     2.50000000e+03      # mtauR(Q)
    41     9.59999997e+02      # mqL1(Q)
    42     9.59999997e+02      # mqL2(Q)
    43     2.50000000e+03      # mqL3(Q)
    44     9.59999997e+02      # muR(Q)
    45     9.59999997e+02      # mcR(Q)
    46     2.50000000e+03      # mtR(Q)
    47     9.59999997e+02      # mdR(Q)
    48     9.59999997e+02      # msR(Q)
    49     2.50000000e+03      # mbR(Q)
Block au Q= 2.50365416e+03  
  1  1     3.16525677e-06      # Au(Q)MSSM DRbar
  2  2     3.16528048e-06      # Ac(Q)MSSM DRbar
  3  3     4.85683106e-06      # At(Q)MSSM DRbar
Block ad Q= 2.50365416e+03  
  1  1     1.56828511e-06      # Ad(Q)MSSM DRbar
  2  2     1.56830734e-06      # As(Q)MSSM DRbar
  3  3     2.07751032e-06      # Ab(Q)MSSM DRbar
Block ae Q= 2.50365416e+03  
  1  1     0.00000000e+00      # Ae(Q)MSSM DRbar
  2  2     4.87418503e-08      # Amu(Q)MSSM DRbar
  3  3     4.87089130e-08      # Atau(Q)MSSM DRbar
