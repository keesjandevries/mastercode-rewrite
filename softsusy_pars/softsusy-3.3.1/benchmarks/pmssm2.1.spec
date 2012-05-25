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
     1     7.50000000e+01  # M_1(MX)
     2     2.50000000e+03  # M_2(MX)
     3     2.50000000e+03  # M_3(MX)
     11    0.00000000e+00  # At(MX)
     12    0.00000000e+00  # Ab(MX)
     13    0.00000000e+00  # Atau(MX)
     23    2.50000000e+03  # mu(MX)
     26    2.50000000e+03  # mA(pole)
     31    1.00000000e+02  # meL(MX)
     32    1.00000000e+02  # mmuL(MX)
     33    2.50000000e+03  # mtauL(MX)
     34    1.00000000e+02  # meR(MX)
     35    1.00000000e+02  # mmuR(MX)
     36    2.50000000e+03  # mtauR(MX)
     41    2.50000000e+03  # mqL1(MX)
     42    2.50000000e+03  # mqL2(MX)
     43    2.50000000e+03  # mqL3(MX)
     44    2.50000000e+03  # muR(MX)
     45    2.50000000e+03  # mcR(MX)
     46    2.50000000e+03  # mtR(MX)
     47    2.50000000e+03  # mdR(MX)
     48    2.50000000e+03  # msR(MX)
     49    2.50000000e+03  # mbR(MX)
# Low energy data in SOFTSUSY: MIXING=0 TOLERANCE=1.00000000e-03
# mgut=2.50366847e+03 GeV
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.04028204e+01   # MW
        25     1.17002738e+02   # h0
        35     2.50009306e+03   # H0
        36     2.49998807e+03   # A0
        37     2.50163962e+03   # H+
   1000021     2.64694938e+03   # ~g
   1000022     7.27717015e+01   # ~neutralino(1)
   1000023     2.44326953e+03   # ~neutralino(2)
   1000024     2.44369740e+03   # ~chargino(1)
   1000025    -2.50013663e+03   # ~neutralino(3)
   1000035     2.56133632e+03   # ~neutralino(4)
   1000037     2.56094050e+03   # ~chargino(2)
   1000001     2.60386990e+03   # ~d_L
   1000002     2.60285662e+03   # ~u_L
   1000003     2.60386990e+03   # ~s_L
   1000004     2.60285662e+03   # ~c_L
   1000005     2.57996788e+03   # ~b_1
   1000006     2.58129002e+03   # ~t_1
   1000011     2.39932971e+02   # ~e_L
   1000012     2.26869548e+02   # ~nue_L
   1000013     2.39932886e+02   # ~mu_L
   1000014     2.26869548e+02   # ~numu_L
   1000015     2.49907173e+03   # ~stau_1
   1000016     2.51704608e+03   # ~nu_tau_L
   2000001     2.58612181e+03   # ~d_R
   2000002     2.58540649e+03   # ~u_R
   2000003     2.58612181e+03   # ~s_R
   2000004     2.58540649e+03   # ~c_R
   2000005     2.60766728e+03   # ~b_2
   2000006     2.61220923e+03   # ~t_2
   2000011     1.30889898e+02   # ~e_R
   2000013     1.30889898e+02   # ~mu_R
   2000015     2.52247680e+03   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -1.04707819e-01       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.99840548e-01   # N_{1,1}
  1  2    -4.96721185e-04   # N_{1,2}
  1  3     1.76924595e-02   # N_{1,3}
  1  4    -2.36829346e-03   # N_{1,4}
  2  1     8.93178983e-03   # N_{2,1}
  2  2     8.03354673e-01   # N_{2,2}
  2  3    -4.26596018e-01   # N_{2,3}
  2  4     4.15400205e-01   # N_{2,4}
  3  1    -1.08287886e-02   # N_{3,1}
  3  2     9.83187101e-03   # N_{3,2}
  3  3     7.06895701e-01   # N_{3,3}
  3  4     7.07166557e-01   # N_{3,4}
  4  1    -1.10380767e-02   # N_{4,1}
  4  2     5.95419480e-01   # N_{4,2}
  4  3     5.63916023e-01   # N_{4,3}
  4  4    -5.72147290e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1    -6.86661322e-01   # U_{1,1}
  1  2     7.26977461e-01   # U_{1,2}
  2  1    -7.26977461e-01   # U_{2,1}
  2  2    -6.86661322e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1    -7.00365216e-01   # V_{1,1}
  1  2     7.13784676e-01   # V_{1,2}
  2  1    -7.13784676e-01   # V_{2,1}
  2  2    -7.00365216e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     4.20672084e-01   # F_{11}
  1  2     9.07212763e-01   # F_{12}
  2  1     9.07212763e-01   # F_{21}
  2  2    -4.20672084e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     4.02292511e-01   # F_{11}
  1  2     9.15511188e-01   # F_{12}
  2  1     9.15511188e-01   # F_{21}
  2  2    -4.02292511e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     4.03208111e-01   # F_{11}
  1  2     9.15108310e-01   # F_{12}
  2  1     9.15108310e-01   # F_{21}
  2  2    -4.03208111e-01   # F_{22}
Block gauge Q= 2.50366847e+03  # SM gauge couplings
     1     3.64762036e-01   # g'(Q)MSSM DRbar
     2     6.36107860e-01   # g(Q)MSSM DRbar
     3     1.01384444e+00   # g3(Q)MSSM DRbar
Block yu Q= 2.50366847e+03  
  3  3     8.33800947e-01   # Yt(Q)MSSM DRbar
Block yd Q= 2.50366847e+03  
  3  3     1.25688280e-01   # Yb(Q)MSSM DRbar
Block ye Q= 2.50366847e+03  
  3  3     9.97712745e-02   # Ytau(Q)MSSM DRbar
Block hmix Q= 2.50366847e+03 # Higgs mixing parameters
     1     2.50000000e+03    # mu(Q)MSSM DRbar
     2     9.54813986e+00    # tan beta(Q)MSSM DRbar
     3     2.43696315e+02    # higgs vev(Q)MSSM DRbar
     4     6.15803459e+06    # mA^2(Q)MSSM DRbar
Block msoft Q= 2.50366847e+03  # MSSM DRbar SUSY breaking parameters
     1     7.50000000e+01      # M_1(Q)
     2     2.50000000e+03      # M_2(Q)
     3     2.50000000e+03      # M_3(Q)
    21    -1.66584401e+05      # mH1^2(Q)
    22    -6.06894464e+06      # mH2^2(Q)
    31     9.99999988e+01      # meL(Q)
    32     9.99999988e+01      # mmuL(Q)
    33     2.50000000e+03      # mtauL(Q)
    34     1.00000001e+02      # meR(Q)
    35     1.00000001e+02      # mmuR(Q)
    36     2.50000000e+03      # mtauR(Q)
    41     2.49999999e+03      # mqL1(Q)
    42     2.49999999e+03      # mqL2(Q)
    43     2.49999999e+03      # mqL3(Q)
    44     2.49999999e+03      # muR(Q)
    45     2.49999999e+03      # mcR(Q)
    46     2.49999999e+03      # mtR(Q)
    47     2.49999999e+03      # mdR(Q)
    48     2.49999999e+03      # msR(Q)
    49     2.49999999e+03      # mbR(Q)
Block au Q= 2.50366847e+03  
  1  1     6.10956080e-06      # Au(Q)MSSM DRbar
  2  2     6.10963328e-06      # Ac(Q)MSSM DRbar
  3  3     1.02313033e-05      # At(Q)MSSM DRbar
Block ad Q= 2.50366847e+03  
  1  1     2.09467156e-06      # Ad(Q)MSSM DRbar
  2  2     2.09474624e-06      # As(Q)MSSM DRbar
  3  3     3.43560520e-06      # Ab(Q)MSSM DRbar
Block ae Q= 2.50366847e+03  
  1  1     0.00000000e+00      # Ae(Q)MSSM DRbar
  2  2     1.21787895e-07      # Amu(Q)MSSM DRbar
  3  3     1.22095634e-07      # Atau(Q)MSSM DRbar
