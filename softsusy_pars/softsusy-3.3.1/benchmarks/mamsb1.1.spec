# SOFTSUSY3.3.1 SLHA compliant output
# B.C. Allanach, Comput. Phys. Commun. 143 (2002) 305-331, hep-ph/0104145
Block SPINFO          # Program information
     1    SOFTSUSY    # spectrum calculator
     2    3.3.1       # version number
Block MODSEL  # Select model
     1    3   # amsb
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
     4    1.00000000e+00   # sign(mu)
     1    3.00000000e+02   # m0
     2    4.00000000e+04   # m3/2
# Low energy data in SOFTSUSY: MIXING=0 TOLERANCE=1.00000000e-03
# mgut=2.65794179e+16 GeV
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.04040920e+01   # MW
        25     1.12475088e+02   # h0
        35     7.25708437e+02   # H0
        36     7.25440395e+02   # A0
        37     7.30093459e+02   # H+
   1000021    -8.87573409e+02   # ~g
   1000022     1.30628664e+02   # ~neutralino(1)
   1000023     3.63252049e+02   # ~neutralino(2)
   1000024     1.30805918e+02   # ~chargino(1)
   1000025    -7.02208860e+02   # ~neutralino(3)
   1000035     7.10022128e+02   # ~neutralino(4)
   1000037     7.08618773e+02   # ~chargino(2)
   1000039     4.00000000e+04   # ~gravitino
   1000001     8.80770103e+02   # ~d_L
   1000002     8.77358882e+02   # ~u_L
   1000003     8.80764846e+02   # ~s_L
   1000004     8.77353599e+02   # ~c_L
   1000005     7.66252922e+02   # ~b_1
   1000006     6.31817130e+02   # ~t_1
   1000011     2.59769228e+02   # ~e_L
   1000012     2.47229108e+02   # ~nue_L
   1000013     2.59759987e+02   # ~mu_L
   1000014     2.47217235e+02   # ~numu_L
   1000015     2.25934675e+02   # ~stau_1
   1000016     2.43592783e+02   # ~nu_tau_L
   2000001     8.89127852e+02   # ~d_R
   2000002     8.82345713e+02   # ~u_R
   2000003     8.89122182e+02   # ~s_R
   2000004     8.82340907e+02   # ~c_R
   2000005     8.77496501e+02   # ~b_2
   2000006     8.12727170e+02   # ~t_2
   2000011     2.52017716e+02   # ~e_R
   2000013     2.51994306e+02   # ~mu_R
   2000015     2.73079983e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -1.07944969e-01       # alpha
Block nmix                  # neutralino mixing matrix
  1  1    -8.12365694e-03   # N_{1,1}
  1  2     9.92466105e-01   # N_{1,2}
  1  3    -1.17814122e-01   # N_{1,3}
  1  4     3.26323331e-02   # N_{1,4}
  2  1     9.94607679e-01   # N_{2,1}
  2  2     2.02357688e-02   # N_{2,2}
  2  3     8.75366477e-02   # N_{2,3}
  2  4    -5.18016814e-02   # N_{2,4}
  3  1    -2.62787260e-02   # N_{3,1}
  3  2     6.00267236e-02   # N_{3,2}
  3  3     7.03490617e-01   # N_{3,3}
  3  4     7.07677308e-01   # N_{3,4}
  4  1    -9.99949998e-02   # N_{4,1}
  4  2     1.04872954e-01   # N_{4,2}
  4  3     6.95383433e-01   # N_{4,3}
  4  4    -7.03878217e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.86735879e-01   # U_{1,1}
  1  2    -1.62333932e-01   # U_{1,2}
  2  1     1.62333932e-01   # U_{2,1}
  2  2     9.86735879e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.98942017e-01   # V_{1,1}
  1  2    -4.59874546e-02   # V_{1,2}
  2  1     4.59874546e-02   # V_{2,1}
  2  2     9.98942017e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1    -4.53180415e-01   # F_{11}
  1  2     8.91418820e-01   # F_{12}
  2  1     8.91418820e-01   # F_{21}
  2  2     4.53180415e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     9.97265215e-01   # F_{11}
  1  2     7.39059573e-02   # F_{12}
  2  1    -7.39059573e-02   # F_{21}
  2  2     9.97265215e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     6.14373394e-01   # F_{11}
  1  2     7.89015420e-01   # F_{12}
  2  1     7.89015420e-01   # F_{21}
  2  2    -6.14373394e-01   # F_{22}
Block gauge Q= 6.89366822e+02  # SM gauge couplings
     1     3.61737260e-01   # g'(Q)MSSM DRbar
     2     6.46154216e-01   # g(Q)MSSM DRbar
     3     1.07367374e+00   # g3(Q)MSSM DRbar
Block yu Q= 6.89366822e+02  
  3  3     8.70659320e-01   # Yt(Q)MSSM DRbar
Block yd Q= 6.89366822e+02  
  3  3     1.50840870e-01   # Yb(Q)MSSM DRbar
Block ye Q= 6.89366822e+02  
  3  3     9.94851012e-02   # Ytau(Q)MSSM DRbar
Block hmix Q= 6.89366822e+02 # Higgs mixing parameters
     1     7.00144241e+02    # mu(Q)MSSM DRbar
     2     9.70362220e+00    # tan beta(Q)MSSM DRbar
     3     2.44682825e+02    # higgs vev(Q)MSSM DRbar
     4     5.26245183e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 6.89366822e+02  # MSSM DRbar SUSY breaking parameters
     1     3.71682249e+02      # M_1(Q)
     2     1.28389155e+02      # M_2(Q)
     3    -8.44101264e+02      # M_3(Q)
    21     3.01226632e+04      # mH1^2(Q)
    22    -4.82328944e+05      # mH2^2(Q)
    31     2.54921418e+02      # meL(Q)
    32     2.54909884e+02      # mmuL(Q)
    33     2.51532007e+02      # mtauL(Q)
    34     2.44783134e+02      # meR(Q)
    35     2.44759100e+02      # mmuR(Q)
    36     2.37663995e+02      # mtauR(Q)
    41     8.52463223e+02      # mqL1(Q)
    42     8.52457787e+02      # mqL2(Q)
    43     7.40260622e+02      # mqL3(Q)
    44     8.57467479e+02      # muR(Q)
    45     8.57462516e+02      # mcR(Q)
    46     6.28450609e+02      # mtR(Q)
    47     8.63408642e+02      # mdR(Q)
    48     8.63402772e+02      # msR(Q)
    49     8.51112309e+02      # mbR(Q)
Block au Q= 6.89366822e+02  
  1  1     1.32585506e+03      # Au(Q)MSSM DRbar
  2  2     1.32584394e+03      # Ac(Q)MSSM DRbar
  3  3     7.52928489e+02      # At(Q)MSSM DRbar
Block ad Q= 6.89366822e+02  
  1  1     1.87475917e+03      # Ad(Q)MSSM DRbar
  2  2     1.87474884e+03      # As(Q)MSSM DRbar
  3  3     1.66982073e+03      # Ab(Q)MSSM DRbar
Block ae Q= 6.89366822e+02  
  1  1     3.92909556e+02      # Ae(Q)MSSM DRbar
  2  2     3.92884028e+02      # Amu(Q)MSSM DRbar
  3  3     3.85374980e+02      # Atau(Q)MSSM DRbar
