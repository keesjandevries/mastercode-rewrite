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
     1     5.00000000e+02  # M_1(MX)
     2     2.50000000e+03  # M_2(MX)
     3     6.00000000e+02  # M_3(MX)
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
     41    6.00000000e+02  # mqL1(MX)
     42    6.00000000e+02  # mqL2(MX)
     43    2.50000000e+03  # mqL3(MX)
     44    6.00000000e+02  # muR(MX)
     45    6.00000000e+02  # mcR(MX)
     46    2.50000000e+03  # mtR(MX)
     47    6.00000000e+02  # mdR(MX)
     48    6.00000000e+02  # msR(MX)
     49    2.50000000e+03  # mbR(MX)
# Low energy data in SOFTSUSY: MIXING=0 TOLERANCE=1.00000000e-03
# mgut=2.50362398e+03 GeV
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03981014e+01   # MW
        25     1.16452850e+02   # h0
        35     2.50009551e+03   # H0
        36     2.49998821e+03   # A0
        37     2.50164173e+03   # H+
   1000021     7.00882831e+02   # ~g
   1000022     4.91904242e+02   # ~neutralino(1)
   1000023     2.43297965e+03   # ~neutralino(2)
   1000024     2.43333359e+03   # ~chargino(1)
   1000025    -2.50029992e+03   # ~neutralino(3)
   1000035     2.55282541e+03   # ~neutralino(4)
   1000037     2.55239344e+03   # ~chargino(2)
   1000001     6.95223472e+02   # ~d_L
   1000002     6.91074650e+02   # ~u_L
   1000003     6.95223472e+02   # ~s_L
   1000004     6.91074650e+02   # ~c_L
   1000005     2.51998801e+03   # ~b_1
   1000006     2.52347443e+03   # ~t_1
   1000011     2.51889801e+03   # ~e_L
   1000012     2.51738076e+03   # ~nue_L
   1000013     2.51889803e+03   # ~mu_L
   1000014     2.51738076e+03   # ~numu_L
   1000015     2.49924698e+03   # ~stau_1
   1000016     2.51715886e+03   # ~nu_tau_L
   2000001     6.53816745e+02   # ~d_R
   2000002     6.49481849e+02   # ~u_R
   2000003     6.53816745e+02   # ~s_R
   2000004     6.49481849e+02   # ~c_R
   2000005     2.54916891e+03   # ~b_2
   2000006     2.55091301e+03   # ~t_2
   2000011     2.50357986e+03   # ~e_R
   2000013     2.50357986e+03   # ~mu_R
   2000015     2.52260062e+03   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -1.04704048e-01       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.99807964e-01   # N_{1,1}
  1  2    -2.75376241e-04   # N_{1,2}
  1  3     1.87890722e-02   # N_{1,3}
  1  4    -5.56145169e-03   # N_{1,4}
  2  1     9.68810739e-03   # N_{2,1}
  2  2     8.38569629e-01   # N_{2,2}
  2  3    -3.90973159e-01   # N_{2,3}
  2  4     3.79271811e-01   # N_{2,4}
  3  1    -9.34843113e-03   # N_{3,1}
  3  2     9.85606614e-03   # N_{3,2}
  3  3     7.06913109e-01   # N_{3,3}
  3  4     7.07169938e-01   # N_{3,4}
  4  1    -1.42401623e-02   # N_{4,1}
  4  2     5.44705204e-01   # N_{4,2}
  4  3     5.89118677e-01   # N_{4,3}
  4  4    -5.96684710e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     7.47351266e-01   # U_{1,1}
  1  2    -6.64429142e-01   # U_{1,2}
  2  1     6.64429142e-01   # U_{2,1}
  2  2     7.47351266e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     7.59880790e-01   # V_{1,1}
  1  2    -6.50062447e-01   # V_{1,2}
  2  1     6.50062447e-01   # V_{2,1}
  2  2     7.59880790e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     3.44445290e-01   # F_{11}
  1  2     9.38806392e-01   # F_{12}
  2  1     9.38806392e-01   # F_{21}
  2  2    -3.44445290e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     4.03682639e-01   # F_{11}
  1  2     9.14899080e-01   # F_{12}
  2  1     9.14899080e-01   # F_{21}
  2  2    -4.03682639e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     4.04155593e-01   # F_{11}
  1  2     9.14690252e-01   # F_{12}
  2  1     9.14690252e-01   # F_{21}
  2  2    -4.04155593e-01   # F_{22}
Block gauge Q= 2.50362398e+03  # SM gauge couplings
     1     3.64674481e-01   # g'(Q)MSSM DRbar
     2     6.37368433e-01   # g(Q)MSSM DRbar
     3     1.04644717e+00   # g3(Q)MSSM DRbar
Block yu Q= 2.50362398e+03  
  3  3     8.29086059e-01   # Yt(Q)MSSM DRbar
Block yd Q= 2.50362398e+03  
  3  3     1.29248767e-01   # Yb(Q)MSSM DRbar
Block ye Q= 2.50362398e+03  
  3  3     9.97051907e-02   # Ytau(Q)MSSM DRbar
Block hmix Q= 2.50362398e+03 # Higgs mixing parameters
     1     2.50000000e+03    # mu(Q)MSSM DRbar
     2     9.54888138e+00    # tan beta(Q)MSSM DRbar
     3     2.43775744e+02    # higgs vev(Q)MSSM DRbar
     4     6.16510047e+06    # mA^2(Q)MSSM DRbar
Block msoft Q= 2.50362398e+03  # MSSM DRbar SUSY breaking parameters
     1     5.00000000e+02      # M_1(Q)
     2     2.50000000e+03      # M_2(Q)
     3     6.00000000e+02      # M_3(Q)
    21    -1.69080616e+05      # mH1^2(Q)
    22    -6.07251240e+06      # mH2^2(Q)
    31     2.50000000e+03      # meL(Q)
    32     2.50000000e+03      # mmuL(Q)
    33     2.50000000e+03      # mtauL(Q)
    34     2.50000000e+03      # meR(Q)
    35     2.50000000e+03      # mmuR(Q)
    36     2.50000000e+03      # mtauR(Q)
    41     5.99999998e+02      # mqL1(Q)
    42     5.99999998e+02      # mqL2(Q)
    43     2.50000000e+03      # mqL3(Q)
    44     5.99999998e+02      # muR(Q)
    45     5.99999998e+02      # mcR(Q)
    46     2.50000000e+03      # mtR(Q)
    47     5.99999998e+02      # mdR(Q)
    48     5.99999998e+02      # msR(Q)
    49     2.50000000e+03      # mbR(Q)
Block au Q= 2.50362398e+03  
  1  1     2.33913189e-06      # Au(Q)MSSM DRbar
  2  2     2.33914179e-06      # Ac(Q)MSSM DRbar
  3  3     3.33727866e-06      # At(Q)MSSM DRbar
Block ad Q= 2.50362398e+03  
  1  1     1.45030546e-06      # Ad(Q)MSSM DRbar
  2  2     1.45031236e-06      # As(Q)MSSM DRbar
  3  3     1.71463389e-06      # Ab(Q)MSSM DRbar
Block ae Q= 2.50362398e+03  
  1  1     0.00000000e+00      # Ae(Q)MSSM DRbar
  2  2     2.68559383e-08      # Amu(Q)MSSM DRbar
  3  3     2.67552358e-08      # Atau(Q)MSSM DRbar
