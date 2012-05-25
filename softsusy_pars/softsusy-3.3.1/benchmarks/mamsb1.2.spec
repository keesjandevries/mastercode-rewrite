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
     1    3.75000000e+02   # m0
     2    5.00000000e+04   # m3/2
# Low energy data in SOFTSUSY: MIXING=0 TOLERANCE=1.00000000e-03
# mgut=2.44239940e+16 GeV
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03926084e+01   # MW
        25     1.14136073e+02   # h0
        35     8.96376516e+02   # H0
        36     8.96188892e+02   # A0
        37     9.00013503e+02   # H+
   1000021    -1.08640202e+03   # ~g
   1000022     1.64188757e+02   # ~neutralino(1)
   1000023     4.56136565e+02   # ~neutralino(2)
   1000024     1.64358709e+02   # ~chargino(1)
   1000025    -8.62654016e+02   # ~neutralino(3)
   1000035     8.69327517e+02   # ~neutralino(4)
   1000037     8.68058064e+02   # ~chargino(2)
   1000039     5.00000000e+04   # ~gravitino
   1000001     1.07981184e+03   # ~d_L
   1000002     1.07706830e+03   # ~u_L
   1000003     1.07980534e+03   # ~s_L
   1000004     1.07706178e+03   # ~c_L
   1000005     9.38471412e+02   # ~b_1
   1000006     7.80263903e+02   # ~t_1
   1000011     3.23411650e+02   # ~e_L
   1000012     3.13393737e+02   # ~nue_L
   1000013     3.23401912e+02   # ~mu_L
   1000014     3.13379207e+02   # ~numu_L
   1000015     2.87180340e+02   # ~stau_1
   1000016     3.08925556e+02   # ~nu_tau_L
   2000001     1.09077169e+03   # ~d_R
   2000002     1.08264336e+03   # ~u_R
   2000003     1.09076470e+03   # ~s_R
   2000004     1.08263740e+03   # ~c_R
   2000005     1.07630983e+03   # ~b_2
   2000006     9.78139586e+02   # ~t_2
   2000011     3.13326605e+02   # ~e_R
   2000013     3.13297415e+02   # ~mu_R
   2000015     3.34560933e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -1.06403411e-01       # alpha
Block nmix                  # neutralino mixing matrix
  1  1    -5.33026307e-03   # N_{1,1}
  1  2     9.95025204e-01   # N_{1,2}
  1  3    -9.57766523e-02   # N_{1,3}
  1  4     2.68935858e-02   # N_{1,4}
  2  1     9.96224880e-01   # N_{2,1}
  2  2     1.36028702e-02   # N_{2,2}
  2  3     7.34663267e-02   # N_{2,3}
  2  4    -4.42000988e-02   # N_{2,4}
  3  1    -2.12449528e-02   # N_{3,1}
  3  2     4.85991742e-02   # N_{3,2}
  3  3     7.04737448e-01   # N_{3,3}
  3  4     7.07482792e-01   # N_{3,4}
  4  1    -8.40013586e-02   # N_{4,1}
  4  2     8.58948542e-02   # N_{4,2}
  4  3     6.99124210e-01   # N_{4,3}
  4  4    -7.04834154e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.91200055e-01   # U_{1,1}
  1  2    -1.32372397e-01   # U_{1,2}
  2  1     1.32372397e-01   # U_{2,1}
  2  2     9.91200055e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.99278961e-01   # V_{1,1}
  1  2    -3.79678481e-02   # V_{1,2}
  2  1     3.79678481e-02   # V_{2,1}
  2  2     9.99278961e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1    -4.03366890e-01   # F_{11}
  1  2     9.15038334e-01   # F_{12}
  2  1     9.15038334e-01   # F_{21}
  2  2     4.03366890e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     9.98258027e-01   # F_{11}
  1  2     5.89992510e-02   # F_{12}
  2  1    -5.89992510e-02   # F_{21}
  2  2     9.98258027e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     5.86358085e-01   # F_{11}
  1  2     8.10051972e-01   # F_{12}
  2  1     8.10051972e-01   # F_{21}
  2  2    -5.86358085e-01   # F_{22}
Block gauge Q= 8.41442198e+02  # SM gauge couplings
     1     3.62166289e-01   # g'(Q)MSSM DRbar
     2     6.44972373e-01   # g(Q)MSSM DRbar
     3     1.06272947e+00   # g3(Q)MSSM DRbar
Block yu Q= 8.41442198e+02  
  3  3     8.63512540e-01   # Yt(Q)MSSM DRbar
Block yd Q= 8.41442198e+02  
  3  3     1.48965759e-01   # Yb(Q)MSSM DRbar
Block ye Q= 8.41442198e+02  
  3  3     9.93565883e-02   # Ytau(Q)MSSM DRbar
Block hmix Q= 8.41442198e+02 # Higgs mixing parameters
     1     8.61458975e+02    # mu(Q)MSSM DRbar
     2     9.67925696e+00    # tan beta(Q)MSSM DRbar
     3     2.44429271e+02    # higgs vev(Q)MSSM DRbar
     4     8.03331340e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 8.41442198e+02  # MSSM DRbar SUSY breaking parameters
     1     4.65552301e+02      # M_1(Q)
     2     1.59465729e+02      # M_2(Q)
     3    -1.03437828e+03      # M_3(Q)
    21     4.94119307e+04      # mH1^2(Q)
    22    -7.27123642e+05      # mH2^2(Q)
    31     3.19023339e+02      # meL(Q)
    32     3.19009053e+02      # mmuL(Q)
    33     3.14814379e+02      # mtauL(Q)
    34     3.06001221e+02      # meR(Q)
    35     3.05971419e+02      # mmuR(Q)
    36     2.97151352e+02      # mtauR(Q)
    41     1.04655521e+03      # mqL1(Q)
    42     1.04654850e+03      # mqL2(Q)
    43     9.07858751e+02      # mqL3(Q)
    44     1.05268523e+03      # muR(Q)
    45     1.05267908e+03      # mcR(Q)
    46     7.69261320e+02      # mtR(Q)
    47     1.06023060e+03      # mdR(Q)
    48     1.06022337e+03      # msR(Q)
    49     1.04519946e+03      # mbR(Q)
Block au Q= 8.41442198e+02  
  1  1     1.62902495e+03      # Au(Q)MSSM DRbar
  2  2     1.62901124e+03      # Ac(Q)MSSM DRbar
  3  3     9.24409950e+02      # At(Q)MSSM DRbar
Block ad Q= 8.41442198e+02  
  1  1     2.30319448e+03      # Ad(Q)MSSM DRbar
  2  2     2.30318178e+03      # As(Q)MSSM DRbar
  3  3     2.05129488e+03      # Ab(Q)MSSM DRbar
Block ae Q= 8.41442198e+02  
  1  1     4.90569990e+02      # Ae(Q)MSSM DRbar
  2  2     4.90538245e+02      # Amu(Q)MSSM DRbar
  3  3     4.81175810e+02      # Atau(Q)MSSM DRbar
