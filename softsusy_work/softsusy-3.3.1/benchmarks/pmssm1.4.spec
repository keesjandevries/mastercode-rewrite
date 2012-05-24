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
     1     6.00000000e+02  # M_1(MX)
     2     2.50000000e+03  # M_2(MX)
     3     7.20000000e+02  # M_3(MX)
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
     41    7.20000000e+02  # mqL1(MX)
     42    7.20000000e+02  # mqL2(MX)
     43    2.50000000e+03  # mqL3(MX)
     44    7.20000000e+02  # muR(MX)
     45    7.20000000e+02  # mcR(MX)
     46    2.50000000e+03  # mtR(MX)
     47    7.20000000e+02  # mdR(MX)
     48    7.20000000e+02  # msR(MX)
     49    2.50000000e+03  # mbR(MX)
# Low energy data in SOFTSUSY: MIXING=0 TOLERANCE=1.00000000e-03
# mgut=2.50363692e+03 GeV
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03988519e+01   # MW
        25     1.16641822e+02   # h0
        35     2.50009539e+03   # H0
        36     2.49998816e+03   # A0
        37     2.50164418e+03   # H+
   1000021     8.30979729e+02   # ~g
   1000022     5.91053668e+02   # ~neutralino(1)
   1000023     2.43221887e+03   # ~neutralino(2)
   1000024     2.43256157e+03   # ~chargino(1)
   1000025    -2.50022301e+03   # ~neutralino(3)
   1000035     2.55215383e+03   # ~neutralino(4)
   1000037     2.55169799e+03   # ~chargino(2)
   1000001     8.15362174e+02   # ~d_L
   1000002     8.11839376e+02   # ~u_L
   1000003     8.15362174e+02   # ~s_L
   1000004     8.11839376e+02   # ~c_L
   1000005     2.52129044e+03   # ~b_1
   1000006     2.52454219e+03   # ~t_1
   1000011     2.51890918e+03   # ~e_L
   1000012     2.51739005e+03   # ~nue_L
   1000013     2.51890920e+03   # ~mu_L
   1000014     2.51739005e+03   # ~numu_L
   1000015     2.49932415e+03   # ~stau_1
   1000016     2.51716820e+03   # ~nu_tau_L
   2000001     7.78980958e+02   # ~d_R
   2000002     7.75653700e+02   # ~u_R
   2000003     7.78980958e+02   # ~s_R
   2000004     7.75653700e+02   # ~c_R
   2000005     2.55034218e+03   # ~b_2
   2000006     2.55234932e+03   # ~t_2
   2000011     2.50366738e+03   # ~e_R
   2000013     2.50366738e+03   # ~mu_R
   2000015     2.52262239e+03   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -1.04713655e-01       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.99794680e-01   # N_{1,1}
  1  2    -3.29613741e-04   # N_{1,2}
  1  3     1.92196467e-02   # N_{1,3}
  1  4    -6.41043388e-03   # N_{1,4}
  2  1     1.06094110e-02   # N_{2,1}
  2  2     8.24135993e-01   # N_{2,2}
  2  3    -4.06134496e-01   # N_{2,3}
  2  4     3.94641706e-01   # N_{2,4}
  3  1    -9.05202511e-03   # N_{3,1}
  3  2     9.85299363e-03   # N_{3,2}
  3  3     7.06916432e-01   # N_{3,3}
  3  4     7.07170516e-01   # N_{3,4}
  4  1    -1.47002846e-02   # N_{4,1}
  4  2     5.66306167e-01   # N_{4,2}
  4  3     5.78752568e-01   # N_{4,3}
  4  4    -5.86623126e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     7.51033157e-01   # U_{1,1}
  1  2    -6.60264490e-01   # U_{1,2}
  2  1     6.60264490e-01   # U_{2,1}
  2  2     7.51033157e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     7.63477300e-01   # V_{1,1}
  1  2    -6.45834664e-01   # V_{1,2}
  2  1     6.45834664e-01   # V_{2,1}
  2  2     7.63477300e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     3.54782996e-01   # F_{11}
  1  2     9.34948676e-01   # F_{12}
  2  1     9.34948676e-01   # F_{21}
  2  2    -3.54782996e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     4.03476762e-01   # F_{11}
  1  2     9.14989892e-01   # F_{12}
  2  1     9.14989892e-01   # F_{21}
  2  2    -4.03476762e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     4.05237092e-01   # F_{11}
  1  2     9.14211627e-01   # F_{12}
  2  1     9.14211627e-01   # F_{21}
  2  2    -4.05237092e-01   # F_{22}
Block gauge Q= 2.50363692e+03  # SM gauge couplings
     1     3.64599870e-01   # g'(Q)MSSM DRbar
     2     6.37157577e-01   # g(Q)MSSM DRbar
     3     1.04226762e+00   # g3(Q)MSSM DRbar
Block yu Q= 2.50363692e+03  
  3  3     8.30462865e-01   # Yt(Q)MSSM DRbar
Block yd Q= 2.50363692e+03  
  3  3     1.28710928e-01   # Yb(Q)MSSM DRbar
Block ye Q= 2.50363692e+03  
  3  3     9.96921261e-02   # Ytau(Q)MSSM DRbar
Block hmix Q= 2.50363692e+03 # Higgs mixing parameters
     1     2.50000000e+03    # mu(Q)MSSM DRbar
     2     9.54801512e+00    # tan beta(Q)MSSM DRbar
     3     2.43754580e+02    # higgs vev(Q)MSSM DRbar
     4     6.16431302e+06    # mA^2(Q)MSSM DRbar
Block msoft Q= 2.50363692e+03  # MSSM DRbar SUSY breaking parameters
     1     6.00000000e+02      # M_1(Q)
     2     2.50000000e+03      # M_2(Q)
     3     7.20000000e+02      # M_3(Q)
    21    -1.69190357e+05      # mH1^2(Q)
    22    -6.07186188e+06      # mH2^2(Q)
    31     2.50000000e+03      # meL(Q)
    32     2.50000000e+03      # mmuL(Q)
    33     2.50000000e+03      # mtauL(Q)
    34     2.50000000e+03      # meR(Q)
    35     2.50000000e+03      # mmuR(Q)
    36     2.50000000e+03      # mtauR(Q)
    41     7.19999998e+02      # mqL1(Q)
    42     7.19999998e+02      # mqL2(Q)
    43     2.50000000e+03      # mqL3(Q)
    44     7.19999998e+02      # muR(Q)
    45     7.19999998e+02      # mcR(Q)
    46     2.50000000e+03      # mtR(Q)
    47     7.19999998e+02      # mdR(Q)
    48     7.19999998e+02      # msR(Q)
    49     2.50000000e+03      # mbR(Q)
Block au Q= 2.50363692e+03  
  1  1     2.62294046e-06      # Au(Q)MSSM DRbar
  2  2     2.62295525e-06      # Ac(Q)MSSM DRbar
  3  3     3.86295333e-06      # At(Q)MSSM DRbar
Block ad Q= 2.50363692e+03  
  1  1     1.48628297e-06      # Ad(Q)MSSM DRbar
  2  2     1.48629524e-06      # As(Q)MSSM DRbar
  3  3     1.83679706e-06      # Ab(Q)MSSM DRbar
Block ae Q= 2.50363692e+03  
  1  1     0.00000000e+00      # Ae(Q)MSSM DRbar
  2  2     3.46237940e-08      # Amu(Q)MSSM DRbar
  3  3     3.45474169e-08      # Atau(Q)MSSM DRbar
