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
     1    4.50000000e+02   # m0
     2    6.00000000e+04   # m3/2
# Low energy data in SOFTSUSY: MIXING=0 TOLERANCE=1.00000000e-03
# mgut=2.29800543e+16 GeV
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03891487e+01   # MW
        25     1.15406364e+02   # h0
        35     1.06455406e+03   # H0
        36     1.06438989e+03   # A0
        37     1.06766010e+03   # H+
   1000021    -1.28186063e+03   # ~g
   1000022     1.97403598e+02   # ~neutralino(1)
   1000023     5.49082499e+02   # ~neutralino(2)
   1000024     1.97570584e+02   # ~chargino(1)
   1000025    -1.02068798e+03   # ~neutralino(3)
   1000035     1.02660754e+03   # ~neutralino(4)
   1000037     1.02542691e+03   # ~chargino(2)
   1000039     6.00000000e+04   # ~gravitino
   1000001     1.27601327e+03   # ~d_L
   1000002     1.27372105e+03   # ~u_L
   1000003     1.27600554e+03   # ~s_L
   1000004     1.27371330e+03   # ~c_L
   1000005     1.10807170e+03   # ~b_1
   1000006     9.26032221e+02   # ~t_1
   1000011     3.87375003e+02   # ~e_L
   1000012     3.79015664e+02   # ~nue_L
   1000013     3.87365416e+02   # ~mu_L
   1000014     3.78998466e+02   # ~numu_L
   1000015     3.48474967e+02   # ~stau_1
   1000016     3.73711575e+02   # ~nu_tau_L
   2000001     1.28948779e+03   # ~d_R
   2000002     1.27992985e+03   # ~u_R
   2000003     1.28947950e+03   # ~s_R
   2000004     1.27992275e+03   # ~c_R
   2000005     1.27227780e+03   # ~b_2
   2000006     1.14254192e+03   # ~t_2
   2000011     3.74874359e+02   # ~e_R
   2000013     3.74839452e+02   # ~mu_R
   2000015     3.96425695e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -1.05614332e-01       # alpha
Block nmix                  # neutralino mixing matrix
  1  1    -3.76957481e-03   # N_{1,1}
  1  2     9.96454576e-01   # N_{1,2}
  1  3    -8.08594484e-02   # N_{1,3}
  1  4     2.29307174e-02   # N_{1,4}
  2  1     9.97184002e-01   # N_{2,1}
  2  2     9.81425055e-03   # N_{2,2}
  2  3     6.34803653e-02   # N_{2,3}
  2  4    -3.87038854e-02   # N_{2,4}
  3  1    -1.78543628e-02   # N_{3,1}
  3  2     4.08976449e-02   # N_{3,2}
  3  3     7.05428530e-01   # N_{3,3}
  3  4     7.07374861e-01   # N_{3,4}
  4  1    -7.27398039e-02   # N_{4,1}
  4  2     7.28652250e-02   # N_{4,2}
  4  3     7.01286376e-01   # N_{4,3}
  4  4    -7.05405556e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.93713721e-01   # U_{1,1}
  1  2    -1.11951064e-01   # U_{1,2}
  2  1     1.11951064e-01   # U_{2,1}
  2  2     9.93713721e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.99474774e-01   # V_{1,1}
  1  2    -3.24064263e-02   # V_{1,2}
  2  1     3.24064263e-02   # V_{2,1}
  2  2     9.99474774e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1    -3.61085041e-01   # F_{11}
  1  2     9.32532891e-01   # F_{12}
  2  1     9.32532891e-01   # F_{21}
  2  2     3.61085041e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     9.98794598e-01   # F_{11}
  1  2     4.90851398e-02   # F_{12}
  2  1    -4.90851398e-02   # F_{21}
  2  2     9.98794598e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     5.57669229e-01   # F_{11}
  1  2     8.30063269e-01   # F_{12}
  2  1     8.30063269e-01   # F_{21}
  2  2    -5.57669229e-01   # F_{22}
Block gauge Q= 9.91555579e+02  # SM gauge couplings
     1     3.62514803e-01   # g'(Q)MSSM DRbar
     2     6.44063827e-01   # g(Q)MSSM DRbar
     3     1.05399641e+00   # g3(Q)MSSM DRbar
Block yu Q= 9.91555579e+02  
  3  3     8.57801961e-01   # Yt(Q)MSSM DRbar
Block yd Q= 9.91555579e+02  
  3  3     1.47512588e-01   # Yb(Q)MSSM DRbar
Block ye Q= 9.91555579e+02  
  3  3     9.92488213e-02   # Ytau(Q)MSSM DRbar
Block hmix Q= 9.91555579e+02 # Higgs mixing parameters
     1     1.02019070e+03    # mu(Q)MSSM DRbar
     2     9.65969749e+00    # tan beta(Q)MSSM DRbar
     3     2.44234163e+02    # higgs vev(Q)MSSM DRbar
     4     1.13335036e+06    # mA^2(Q)MSSM DRbar
Block msoft Q= 9.91555579e+02  # MSSM DRbar SUSY breaking parameters
     1     5.59593076e+02      # M_1(Q)
     2     1.90410355e+02      # M_2(Q)
     3    -1.22154530e+03      # M_3(Q)
    21     7.37286245e+04      # mH1^2(Q)
    22    -1.01737764e+06      # mH2^2(Q)
    31     3.83170251e+02      # meL(Q)
    32     3.83153234e+02      # mmuL(Q)
    33     3.78146395e+02      # mtauL(Q)
    34     3.67223814e+02      # meR(Q)
    35     3.67188286e+02      # mmuR(Q)
    36     3.56652040e+02      # mtauR(Q)
    41     1.23783751e+03      # mqL1(Q)
    42     1.23782953e+03      # mqL2(Q)
    43     1.07286724e+03      # mqL3(Q)
    44     1.24507705e+03      # muR(Q)
    45     1.24506973e+03      # mcR(Q)
    46     9.07652663e+02      # mtR(Q)
    47     1.25424823e+03      # mdR(Q)
    48     1.25423967e+03      # msR(Q)
    49     1.23652233e+03      # mbR(Q)
Block au Q= 9.91555579e+02  
  1  1     1.92805120e+03      # Au(Q)MSSM DRbar
  2  2     1.92803493e+03      # Ac(Q)MSSM DRbar
  3  3     1.09349647e+03      # At(Q)MSSM DRbar
Block ad Q= 9.91555579e+02  
  1  1     2.72566287e+03      # Ad(Q)MSSM DRbar
  2  2     2.72564782e+03      # As(Q)MSSM DRbar
  3  3     2.42743755e+03      # Ab(Q)MSSM DRbar
Block ae Q= 9.91555579e+02  
  1  1     5.88178495e+02      # Ae(Q)MSSM DRbar
  2  2     5.88140562e+02      # Amu(Q)MSSM DRbar
  3  3     5.76929630e+02      # Atau(Q)MSSM DRbar
