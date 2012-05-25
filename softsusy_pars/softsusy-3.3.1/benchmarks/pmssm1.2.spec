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
     1     4.00000000e+02  # M_1(MX)
     2     2.50000000e+03  # M_2(MX)
     3     4.80000000e+02  # M_3(MX)
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
     41    4.80000000e+02  # mqL1(MX)
     42    4.80000000e+02  # mqL2(MX)
     43    2.50000000e+03  # mqL3(MX)
     44    4.80000000e+02  # muR(MX)
     45    4.80000000e+02  # mcR(MX)
     46    2.50000000e+03  # mtR(MX)
     47    4.80000000e+02  # mdR(MX)
     48    4.80000000e+02  # msR(MX)
     49    2.50000000e+03  # mbR(MX)
# Low energy data in SOFTSUSY: MIXING=0 TOLERANCE=1.00000000e-03
# mgut=2.50360651e+03 GeV
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03972046e+01   # MW
        25     1.16205712e+02   # h0
        35     2.50009561e+03   # H0
        36     2.49998827e+03   # A0
        37     2.50163872e+03   # H+
   1000021     5.69041808e+02   # ~g
   1000022     3.92865292e+02   # ~neutralino(1)
   1000023     2.43381680e+03   # ~neutralino(2)
   1000024     2.43417959e+03   # ~chargino(1)
   1000025    -2.50039352e+03   # ~neutralino(3)
   1000035     2.55356695e+03   # ~neutralino(4)
   1000037     2.55315876e+03   # ~chargino(2)
   1000001     5.76753564e+02   # ~d_L
   1000002     5.71732207e+02   # ~u_L
   1000003     5.76753564e+02   # ~s_L
   1000004     5.71732207e+02   # ~c_L
   1000005     2.51903471e+03   # ~b_1
   1000006     2.52275077e+03   # ~t_1
   1000011     2.51889201e+03   # ~e_L
   1000012     2.51737718e+03   # ~nue_L
   1000013     2.51889203e+03   # ~mu_L
   1000014     2.51737718e+03   # ~numu_L
   1000015     2.49918666e+03   # ~stau_1
   1000016     2.51715522e+03   # ~nu_tau_L
   2000001     5.27919620e+02   # ~d_R
   2000002     5.22129747e+02   # ~u_R
   2000003     5.27919620e+02   # ~s_R
   2000004     5.22129747e+02   # ~c_R
   2000005     2.54834778e+03   # ~b_2
   2000006     2.54983436e+03   # ~t_2
   2000011     2.50351173e+03   # ~e_R
   2000013     2.50351173e+03   # ~mu_R
   2000015     2.52258659e+03   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -1.04690296e-01       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.99818753e-01   # N_{1,1}
  1  2    -2.25400505e-04   # N_{1,2}
  1  3     1.84326544e-02   # N_{1,3}
  1  4    -4.75899842e-03   # N_{1,4}
  2  1     8.78865391e-03   # N_{2,1}
  2  2     8.54621441e-01   # N_{2,2}
  2  3    -3.73031414e-01   # N_{2,3}
  2  4     3.61099039e-01   # N_{2,4}
  3  1    -9.66433087e-03   # N_{3,1}
  3  2     9.85964549e-03   # N_{3,2}
  3  3     7.06909519e-01   # N_{3,3}
  3  4     7.07169230e-01   # N_{3,4}
  4  1    -1.38499780e-02   # N_{4,1}
  4  2     5.19157904e-01   # N_{4,2}
  4  3     6.00655254e-01   # N_{4,3}
  4  4    -6.07862251e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     7.43282212e-01   # U_{1,1}
  1  2    -6.68977991e-01   # U_{1,2}
  2  1     6.68977991e-01   # U_{2,1}
  2  2     7.43282212e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     7.55905324e-01   # V_{1,1}
  1  2    -6.54680946e-01   # V_{1,2}
  2  1     6.54680946e-01   # V_{2,1}
  2  2     7.55905324e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     3.34104572e-01   # F_{11}
  1  2     9.42536012e-01   # F_{12}
  2  1     9.42536012e-01   # F_{21}
  2  2    -3.34104572e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     4.03926222e-01   # F_{11}
  1  2     9.14791565e-01   # F_{12}
  2  1     9.14791565e-01   # F_{21}
  2  2    -4.03926222e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     4.03297920e-01   # F_{11}
  1  2     9.15068734e-01   # F_{12}
  2  1     9.15068734e-01   # F_{21}
  2  2    -4.03297920e-01   # F_{22}
Block gauge Q= 2.50360651e+03  # SM gauge couplings
     1     3.64768429e-01   # g'(Q)MSSM DRbar
     2     6.37592041e-01   # g(Q)MSSM DRbar
     3     1.05156607e+00   # g3(Q)MSSM DRbar
Block yu Q= 2.50360651e+03  
  3  3     8.27217156e-01   # Yt(Q)MSSM DRbar
Block yd Q= 2.50360651e+03  
  3  3     1.29843469e-01   # Yb(Q)MSSM DRbar
Block ye Q= 2.50360651e+03  
  3  3     9.97197362e-02   # Ytau(Q)MSSM DRbar
Block hmix Q= 2.50360651e+03 # Higgs mixing parameters
     1     2.50000000e+03    # mu(Q)MSSM DRbar
     2     9.55011093e+00    # tan beta(Q)MSSM DRbar
     3     2.43804231e+02    # higgs vev(Q)MSSM DRbar
     4     6.16592278e+06    # mA^2(Q)MSSM DRbar
Block msoft Q= 2.50360651e+03  # MSSM DRbar SUSY breaking parameters
     1     4.00000000e+02      # M_1(Q)
     2     2.50000000e+03      # M_2(Q)
     3     4.80000000e+02      # M_3(Q)
    21    -1.68994929e+05      # mH1^2(Q)
    22    -6.07331391e+06      # mH2^2(Q)
    31     2.50000000e+03      # meL(Q)
    32     2.50000000e+03      # mmuL(Q)
    33     2.50000000e+03      # mtauL(Q)
    34     2.50000000e+03      # meR(Q)
    35     2.50000000e+03      # mmuR(Q)
    36     2.50000000e+03      # mtauR(Q)
    41     4.79999999e+02      # mqL1(Q)
    42     4.79999999e+02      # mqL2(Q)
    43     2.50000000e+03      # mqL3(Q)
    44     4.79999999e+02      # muR(Q)
    45     4.79999999e+02      # mcR(Q)
    46     2.50000000e+03      # mtR(Q)
    47     4.79999999e+02      # mdR(Q)
    48     4.79999999e+02      # msR(Q)
    49     2.50000000e+03      # mbR(Q)
Block au Q= 2.50360651e+03  
  1  1     2.04541236e-06      # Au(Q)MSSM DRbar
  2  2     2.04541710e-06      # Ac(Q)MSSM DRbar
  3  3     2.78701717e-06      # At(Q)MSSM DRbar
Block ad Q= 2.50360651e+03  
  1  1     1.42059117e-06      # Ad(Q)MSSM DRbar
  2  2     1.42059226e-06      # As(Q)MSSM DRbar
  3  3     1.59239866e-06      # Ab(Q)MSSM DRbar
Block ae Q= 2.50360651e+03  
  1  1     0.00000000e+00      # Ae(Q)MSSM DRbar
  2  2     1.83944256e-08      # Amu(Q)MSSM DRbar
  3  3     1.82669178e-08      # Atau(Q)MSSM DRbar
