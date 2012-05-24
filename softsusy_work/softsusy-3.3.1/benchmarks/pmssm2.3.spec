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
     1     1.05000000e+02  # M_1(MX)
     2     2.50000000e+03  # M_2(MX)
     3     2.50000000e+03  # M_3(MX)
     11    0.00000000e+00  # At(MX)
     12    0.00000000e+00  # Ab(MX)
     13    0.00000000e+00  # Atau(MX)
     23    2.50000000e+03  # mu(MX)
     26    2.50000000e+03  # mA(pole)
     31    1.40000000e+02  # meL(MX)
     32    1.40000000e+02  # mmuL(MX)
     33    2.50000000e+03  # mtauL(MX)
     34    1.40000000e+02  # meR(MX)
     35    1.40000000e+02  # mmuR(MX)
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
# mgut=2.50366849e+03 GeV
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.04026374e+01   # MW
        25     1.17087967e+02   # h0
        35     2.50009293e+03   # H0
        36     2.49998807e+03   # A0
        37     2.50164198e+03   # H+
   1000021     2.64694938e+03   # ~g
   1000022     1.02290585e+02   # ~neutralino(1)
   1000023     2.44322440e+03   # ~neutralino(2)
   1000024     2.44364875e+03   # ~chargino(1)
   1000025    -2.50013307e+03   # ~neutralino(3)
   1000035     2.56128583e+03   # ~neutralino(4)
   1000037     2.56088700e+03   # ~chargino(2)
   1000001     2.60387059e+03   # ~d_L
   1000002     2.60285521e+03   # ~u_L
   1000003     2.60387059e+03   # ~s_L
   1000004     2.60285521e+03   # ~c_L
   1000005     2.57996809e+03   # ~b_1
   1000006     2.58128999e+03   # ~t_1
   1000011     2.59690603e+02   # ~e_L
   1000012     2.47609233e+02   # ~nue_L
   1000013     2.59690538e+02   # ~mu_L
   1000014     2.47609233e+02   # ~numu_L
   1000015     2.49907557e+03   # ~stau_1
   1000016     2.51704505e+03   # ~nu_tau_L
   2000001     2.58612236e+03   # ~d_R
   2000002     2.58540757e+03   # ~u_R
   2000003     2.58612236e+03   # ~s_R
   2000004     2.58540757e+03   # ~c_R
   2000005     2.60766852e+03   # ~b_2
   2000006     2.61220984e+03   # ~t_2
   2000011     1.63903272e+02   # ~e_R
   2000013     1.63903272e+02   # ~mu_R
   2000015     2.52247811e+03   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -1.04708504e-01       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.99839200e-01   # N_{1,1}
  1  2    -3.05312942e-04   # N_{1,2}
  1  3     1.77431229e-02   # N_{1,3}
  1  4    -2.58106086e-03   # N_{1,4}
  2  1     9.12088930e-03   # N_{2,1}
  2  2     7.90813742e-01   # N_{2,2}
  2  3    -4.38218351e-01   # N_{2,3}
  2  4     4.27194466e-01   # N_{2,4}
  3  1    -1.07160399e-02   # N_{3,1}
  3  2     9.83180270e-03   # N_{3,2}
  3  3     7.06896960e-01   # N_{3,3}
  3  4     7.07167017e-01   # N_{3,4}
  4  1    -1.11152764e-02   # N_{4,1}
  4  2     6.11977833e-01   # N_{4,2}
  4  3     5.54929316e-01   # N_{4,3}
  4  4    -5.63394211e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1    -6.86987486e-01   # U_{1,1}
  1  2     7.26669246e-01   # U_{1,2}
  2  1    -7.26669246e-01   # U_{2,1}
  2  2    -6.86987486e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1    -7.00685251e-01   # V_{1,1}
  1  2     7.13470518e-01   # V_{1,2}
  2  1    -7.13470518e-01   # V_{2,1}
  2  2    -7.00685251e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     4.20741629e-01   # F_{11}
  1  2     9.07180512e-01   # F_{12}
  2  1     9.07180512e-01   # F_{21}
  2  2    -4.20741629e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     4.02296377e-01   # F_{11}
  1  2     9.15509489e-01   # F_{12}
  2  1     9.15509489e-01   # F_{21}
  2  2    -4.02296377e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     4.03241922e-01   # F_{11}
  1  2     9.15093412e-01   # F_{12}
  2  1     9.15093412e-01   # F_{21}
  2  2    -4.03241922e-01   # F_{22}
Block gauge Q= 2.50366849e+03  # SM gauge couplings
     1     3.64738667e-01   # g'(Q)MSSM DRbar
     2     6.36097949e-01   # g(Q)MSSM DRbar
     3     1.01384445e+00   # g3(Q)MSSM DRbar
Block yu Q= 2.50366849e+03  
  3  3     8.33800852e-01   # Yt(Q)MSSM DRbar
Block yd Q= 2.50366849e+03  
  3  3     1.25693913e-01   # Yb(Q)MSSM DRbar
Block ye Q= 2.50366849e+03  
  3  3     9.97671863e-02   # Ytau(Q)MSSM DRbar
Block hmix Q= 2.50366849e+03 # Higgs mixing parameters
     1     2.50000000e+03    # mu(Q)MSSM DRbar
     2     9.54814140e+00    # tan beta(Q)MSSM DRbar
     3     2.43696154e+02    # higgs vev(Q)MSSM DRbar
     4     6.15864340e+06    # mA^2(Q)MSSM DRbar
Block msoft Q= 2.50366849e+03  # MSSM DRbar SUSY breaking parameters
     1     1.05000000e+02      # M_1(Q)
     2     2.50000000e+03      # M_2(Q)
     3     2.50000000e+03      # M_3(Q)
    21    -1.66568368e+05      # mH1^2(Q)
    22    -6.06895358e+06      # mH2^2(Q)
    31     1.39999999e+02      # meL(Q)
    32     1.39999999e+02      # mmuL(Q)
    33     2.50000000e+03      # mtauL(Q)
    34     1.40000001e+02      # meR(Q)
    35     1.40000001e+02      # mmuR(Q)
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
Block au Q= 2.50366849e+03  
  1  1     6.11021255e-06      # Au(Q)MSSM DRbar
  2  2     6.11028505e-06      # Ac(Q)MSSM DRbar
  3  3     1.02311168e-05      # At(Q)MSSM DRbar
Block ad Q= 2.50366849e+03  
  1  1     2.09577213e-06      # Ad(Q)MSSM DRbar
  2  2     2.09584681e-06      # As(Q)MSSM DRbar
  3  3     3.43638754e-06      # Ab(Q)MSSM DRbar
Block ae Q= 2.50366849e+03  
  1  1     0.00000000e+00      # Ae(Q)MSSM DRbar
  2  2     1.21789496e-07      # Amu(Q)MSSM DRbar
  3  3     1.22095305e-07      # Atau(Q)MSSM DRbar
