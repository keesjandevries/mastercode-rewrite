*------------------------------------------------------------------------
      SUBROUTINE BPHYSICSINTERFACE( ERROR, slhadata, BRbsg,BRKpnn, RDMb,RDMs,RDMK,BRXsll,
     &     BRbtn,BRKl2,Psll,Pdll,Pllsapx )
*------------------------------------------------------------------------
*
*     Interface to B Physics code
*
*     INPUT:
*     - slhadata: SLHALib array of SLHA input
*
*     OUTPUT:
*     - ERROR: error code (non-zero if failure)
*     - ...: see bphysics code below
*
*    $Id: bphysics.F,v 1.2 2008/11/07 14:39:01 fronga Exp $
*
*------------------------------------------------------------------------

      IMPLICIT NONE
      INTEGER ERROR,I,J,K
      DOUBLE COMPLEX slhadata(*)
      DOUBLE PRECISION TANBETA,MH,MUR,A0soft,MSL,MQL,M1TZ,M2TZ,M3TZ
      DOUBLE PRECISION CEG(2),NEG(4),SNEG(3),SLEG(6),SUEG(6),SDEG(6),VCKM(6,6)
      DOUBLE PRECISION USU1(6,6),USU(6,6),USD(6,6),USL(6,6),USN(3,3)
      DOUBLE PRECISION OCL(2,2),OCR(2,2),ON(4,4)
      DOUBLE PRECISION BRBSG,BRKPNN,RDMB,RDMS,RDMK,BRXSLL,
     &     BRBTN,BRKL2,PSLL,PDLL,PLLSAPX

#include "SLHA.h"

      ERROR = 0

***   SUSY breaking parameters
      tanbeta = HMix_TB
      mH      = DSQRT(DBLE(HMix_MA02))
      mur     = HMix_MUE
      MSL     = MSoft_MSL(1)
      MQL     = MSoft_MSQ(1)
      A0soft  = Au_At
      M1tz    = MSoft_M1
      M2tz    = MSoft_M2
      M3tz    = MSoft_M3

*     Set CKM matrix by hand! (b-physics code)
      DO i=1,6
         DO j=1,6
            VCKM(i,j) = 0.0D0
            IF (i.eq.j) VCKM(i,j) = 1.0D0
         ENDDO
      ENDDO
                                ! PDG 2006/7
      VCKM(1,1) =  0.974167d0   ! 0.97383 
      VCKM(1,2) =  0.225798d0   ! 0.2272 
      VCKM(1,3) =  0.00366922d0 ! 0.00396
      VCKM(2,1) = -0.225753d0   ! 0.2271  
      VCKM(2,2) =  0.973296d0   ! 0.97296 
      VCKM(2,3) =  0.0415997d0  ! 0.04221 
      VCKM(3,1) =  0.00582192d0 ! 0.00814 
      VCKM(3,2) = -0.0413534d0  ! 0.04161 
      VCKM(3,3) =  0.999138875d0 ! 0.999100


***   Chargino sector
      DO I=1,2
         Ceg(I) = Mass_MCha(I)
      ENDDO
      
      DO I=1,2
         DO J=1,2
            OCR(I,J) = VMix_VCha(I,J) ! Orig: U
         ENDDO
      ENDDO   
      DO I=1,2
         DO J=1,2
            OCL(I,J) = UMix_UCha(J,I)
         ENDDO
      ENDDO

***   Neutralino sector
      DO I=1,4
         Neg(I) = Mass_MNeu(I)
      ENDDO
      DO I=1,4
         DO J=1,4
            ON(I,J) = NMix_ZNeu(I,J)
         ENDDO
      ENDDO

***   Up squark sector: heaviest first!
      SUeg(1) = Mass_MSf(2,3,1)*Mass_MSf(2,3,1)
      SUeg(2) = Mass_MSf(2,3,2)*Mass_MSf(2,3,2)
      SUeg(3) = Mass_MSf(2,3,3)*Mass_MSf(2,3,3)
      SUeg(4) = Mass_MSf(1,3,1)*Mass_MSf(1,3,1)
      SUeg(5) = Mass_MSf(1,3,2)*Mass_MSf(1,3,2)
      SUeg(6) = Mass_MSf(1,3,3)*Mass_MSf(1,3,3)
*     Mixing matrix (default: no mixing)
*     Nota Bene: this is the conjugate of the StopMix matrix (?)
      DO i=1,6
         DO j=1,6
            USU1(i,j) = 0.0D0
            IF (i.eq.j) USU1(i,j) = 1.0D0
         ENDDO
      ENDDO
      USU1(3,3) =  StopMix_USf(1,1) ! O_{IJ}
      USU1(6,6) =  USU1(3,3)
      USU1(3,6) = -DSIN( DACOS(USU1(3,3)) )
      USU1(6,3) =  DSIN( DACOS(USU1(3,3)) )

*     Now rotate with CKM matrix
      DO I=1,6
         DO J=1,6
            USU(I,J) = 0.0D0
            DO K=1,6
               USU(I,J) = USU(I,J)+USU1(I,K)*VCKM(K,J)
            ENDDO
         ENDDO
      ENDDO
      
      
***   Down squark sector
      SDeg(1) = Mass_MSf(2,4,1)*Mass_MSf(2,4,1)
      SDeg(2) = Mass_MSf(2,4,2)*Mass_MSf(2,4,2)
      SDeg(3) = Mass_MSf(2,4,3)*Mass_MSf(2,4,3)
      SDeg(4) = Mass_MSf(1,4,1)*Mass_MSf(1,4,1)
      SDeg(5) = Mass_MSf(1,4,2)*Mass_MSf(1,4,2)
      SDeg(6) = Mass_MSf(1,4,3)*Mass_MSf(1,4,3)
*     No mixing in 2 first generations
      DO i=1,6
         DO j=1,6
            USD(i,j) = 0.0D0
            IF (i.eq.j) USD(i,j) = 1.0D0
         ENDDO
      ENDDO
      USD(3,3) =  SbotMix_USf(1,1) ! O_{IJ}
      USD(6,6) =  USD(3,3)
      USD(3,6) =  DSIN( DACOS(USD(3,3)) )
      USD(6,3) = -DSIN( DACOS(USD(3,3)) )

***   Slepton sector
      SLeg(1) = Mass_MSf(2,2,1)*Mass_MSf(2,2,1)
      SLeg(2) = Mass_MSf(2,2,2)*Mass_MSf(2,2,2)
      SLeg(3) = Mass_MSf(2,2,3)*Mass_MSf(2,2,3)
      SLeg(4) = Mass_MSf(1,2,1)*Mass_MSf(1,2,1)
      SLeg(5) = Mass_MSf(1,2,2)*Mass_MSf(1,2,2)
      SLeg(6) = Mass_MSf(1,2,3)*Mass_MSf(1,2,3)
*     No mixing in 2 first generations
      DO i=1,6
         DO j=1,6
            USL(i,j) = 0.0D0
            IF (i.eq.j) USL(i,j) = 1.0D0
         ENDDO
      ENDDO
      USL(3,3) =  StauMix_USf(1,1) ! O_{IJ}
      USL(6,6) =  USL(3,3)
      USL(3,6) =  DSIN( DACOS(USL(3,3)) )
      USL(6,3) = -DSIN( DACOS(USL(3,3)) )

***   Sneutrino sector
      SNeg(1) =  Mass_MSf(1,1,1)*Mass_MSf(1,1,1)
      SNeg(2) =  Mass_MSf(1,1,2)*Mass_MSf(1,1,2)
      SNeg(3) =  Mass_MSf(1,1,3)*Mass_MSf(1,1,3)
*     No sneutrino mixing
      DO i=1,3
         DO j=1,3
            USN(i,j) = 0.0D0
            IF (i.eq.j) USN(i,j) = 1.0D0
         ENDDO
      ENDDO



      CALL bphysics( tanbeta,mH,mur,MSL,mQL,A0soft,M2tz,M1tz,M3tz,
     &     Ceg,Neg,SNeg,Sleg,SUeg,SDeg,USU,USD,USL,USN,OCL,
     &     OCR,ON,
     &     BRbsg,BRKpnn,RDMb,RDMs,RDMK,BRXsll,
     &     BRbtn,BRKl2,Psll,Pdll,Pllsapx )

      END

*********************************************************************************
      subroutine bphysics(tanbeta,mH,mur,mL,MQL,A0,M2tz,M1tz,M3tz,
     &      Ceg,Neg,SNeg,Sleg,SUeg,SDeg,USU,USD,USL,USN,OCL,
     &      OCR,ON,
     &      BRbsg,BRKpnn,RDMb,RDMs,RDMK,BRXsll,
     &      BRbtn,BRKl2,Psll,Pdll,Pllsapx )

C     ------------------------------------------------------------------
C     INPUTS  [all inputs are defined at the low (~1 TeV) scale]
C     ------------------------------------------------------------------
C
C     tanbeta = tan(beta)=<H_down>/<H_up>
C     MH  =     Heavy pseuodscalar neutral Higgs mass (MA)
C     mur =     mu-parameter
C     MQL =     Universal Squark mass term at soft scale
C     ML  =     Universal Slepton mass term at soft scale
C     A0  =     Universal effective A term at soft scale
C     M1tz =    gaugino mass term M1
C     M2tz =    gaugino mass term M2
C     M3tz =    gaugino mass term M3
C
C     Ceg = 2 singular values of the Chargino Mass Matrix
C     OCR, OCL = 2x2 orth. matr. such that 
C     MChar = Transp[OCR].Diag[MChar].OCL
C     Neg = 4 singular values (descending order) of the Neutralino mass matrix.
C     ON = (4 X 4) orth. matrix such that ON.MNeut.Transp[ON] = Diag[MNeut] 
C
C     SUeg = 6 eigenvalues (ascending order) of UP-Squark mass matrix.
C     USU = (6 X 6) real orth. matrix such that USU*MSU*Transp[USU] = Diag[MSU].
C     SDeg = 6 eigenvalues (ascending order) of Down-Squark mass matrix.
C     USD = (6 X 6) real orth. matrix such that USD*MSD*Transp[USD] = Diag[MSD].
C
C     Sleg = 6 eigenvalues (ascending order) of slepton mass matrix.
C     USL = (6 X 6) real orth. matrix such that USL*MSL*Transp[USL] = Diag[MSL].
C     SNeg = 3 eigenvalues (ascending order) of sneutrino mass matrix.
C     USN = (3 X 3) real orth. matrix such that USN*mSN*Transp[USN] = Diag[MSN].
C
C
C     ------------------------------------------------------------------
C     OUTPUTS
C     ------------------------------------------------------------------
C
C     BRbsg  = BR(b->Xs gamma) normalised to SM
C     BRXsll = BR(b->Xs ll)    normalised to SM
C     BRKpnn = BR(Kp ->pi nn)  normalised to SM
C     BRbtn  = BR(B+ -> lv)    normalised to SM
C     BRKl2  = BR(K+ -> lv)    normalised to SM
C     Psll   = BR(Bs->ll)      absolute
C     Pdll   = BR(Bd->ll)      absolute 
C     RDMb   = Delta M_Bd      normalised to SM
C     RDMs   = Delta M_Bs      normalised to SM
C     RDMK   = Delta M_K       normalised to SM



      implicit none

      integer x, alp, alp2, i, ip, jp, j, n, m
      integer AOK,gen,Niter,ido,Nmid,l,a,im,jm
      integer dcheck1,dcheck2,dcheck3,dcheck4,COK,BOK1,k
      integer BOK2,BOK3,BOK4,idum15
      integer idum1,idum2,idum3,idum4,idum5,idum6,idum7,idum8
      integer idum9,idum10,idum11,idum12,idum13,idum14

      double precision stw,ctw,beta,sbeta,cbeta,vev,vev1
      double precision mSLRG(3,3),AERG(3,3),mSERG(3,3)
      double precision SLeg(6), USL(6,6)
      double precision USN(3,3),SNeg(3),Neg(4),ON(4,4)
      double precision OCR(2,2),OCL(2,2),Ceg(2)
      double precision Zp(2,2),Zm(2,2),mU(3),mdown(3),ZN(4,4)
      double precision ZU(6,6),ZD(6,6),Zsn(3,3),ZL(6,6)
      double precision mSQRG(3,3),mSURG(3,3),mSDRG(3,3),AURG(3,3)
      double precision ADRG(3,3),SUeg(6),USU(6,6)
      double precision USD(6,6),SDeg(6)

      double precision mL,mR,mRu,mRd,mQL,M1tz,M2tz,M3tz,mur,mh1,mh2
      double precision cos2beta,tanbeta,alpha2,MGUT,epsL,epsR
      double precision delta,mlsq,mesq,musq,mdsq,mqsq,mDsq12
      double precision mhlight,mHheavy,mApsq,d1higgs,mhlightsq
      double precision mHheavysq,delmhlightsq,mhlightsqnew,mhlightnew
      double precision tansqtw,alph3tz,alph2tz,alph1tz,tw,vev2,M12
      double precision mHcharsq, mHchar,Bbsg,CSMFVfsgl
      double precision mhavg,mhmax,mhmin,mhdiff,mHp,mh,dLL23
      double precision A0,A0min,A0max,A0avg,A0diff,AU3,mDsq23

      double precision H17,H18,H27,H28

      double precision xx,dd,deltams,deltamsgiudice,xgq,xmuq
      double precision C7,C8,a0pa1,BrBmm,BrBmmgiudice,BrSUSYonSM,xth
      double precision eps0p,eps0,eps2,eps1p,mbs,rH,rV,xamu,ytop,yb
      double precision f2,f7,f8,f37,f38,f17,f18,c7chone,c8chone,gtop
      double precision c1t,ml2t,mr2t,mt1sq,mt2sq,s1t,sgnt,tantetat,tetat
      double precision y(2),z(2),t(2),c7ch,c8ch,mtsusy
      double precision C7H,C8H,C7chRes,C8chRes,eta,Brtot,BrH,BrDGG 
      double precision Brtotapx,C7apx,C8apx,C7chResapx,C8chResapx
      double precision mtb,msusy,mtlr,mblr,as,F7pr,F8pr
      double precision mzt,mza,mlrs,c,c2,c22,s,s2,s22,aa
      double precision del1,del2,mhalptst,msusy2,msz,mbz,mzb,mlrsy
      double precision nc,ng,Qb,Qt,pb,pf,pg,pg1,p1h,p2h,p2h1,deltarest1
      double precision deltarest2,deltarest3,mhrest,mhalpalps,diffst
      double precision sumst,mst21,tst,tildex,mhalp2,sw,alps
      double precision mh0lightsq,mh0light,mtlrq,mts,mtlrs,f1r,f2r
      double precision c1b,s1b,ft1t2,ft1b,ft2b,mst1sq,mst2sq
      double precision mb1sq,mb2sq,tetab,sgnb,tantetab,lam,rHK,rHD
      double precision ft1b1,ft1b2,ft2b1,ft2b2,fb1b2,deltarho1,deltarho2
      double precision ml2b,mr2b,xhw,xasq,oneloop,twoloop,rho2loop
      double precision edm,cedm,edmgluino,rhglu,rhgam,g,cedmgluino
      double precision F7p,F8p,c7chapprox,gmN2,gmC2,gm2,scgm2,rhooneloop
      double precision C8chratio,C7chratio,C8chapx,C7chapx,dgamma
      double precision F3,F4,C7gl,C7glappr,alph2,j6,c7ch31,dLL32

      double precision scSDeg(6),scM3tz,yy(2,6),AdUC(3,6,2)
      double precision BdUC(3,6,2),gdown(3),ys,yd,mSD(6,6)
      double precision BRbsg,f11,f22,f33,f44,C8gl,c7ch91,c8ch91

      double precision c8chDGG,c7chDGG,c7DGG,c8DGG,c7DGGRES,c8DGGRES
      double precision c7chDGGRES,c8chDGGRES,CSMFVfsold,CSglfsold

      double precision P2LRbar,S0,Echistot,C2LR,DeltaMsapx,alphasmu
      double precision dRR32,alphas_mb,mB_mb,eta1,mS_mb,mT_mu

ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
c     New variables for e.w. penguins 
ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc

      integer          Qin,Qout
      double precision Vin,Vout
      double precision echarge,gscharge,MW2
      double precision V(2,2),Vh(2,2),U(2,2),Uh(2,2)
      double precision H(6,6),Hh(6,6),RR(6,6)
      double precision deltaKronecker(6,6)
      double precision ZperZ,Zpeng,Zpeng12,Zpeng13,Zpeng23
      double precision BoxChll,BoxChnn,Boxll12,Boxnn12
      double precision Boxll23,Boxnn23,Boxll13,Boxnn13
      double precision Abox,Sbox13,Sbox23,SBox12
      double precision kk,jj,kk3,jj3
      double precision X0SM,Y0SM,Z0SM,S0SM,Peff,P0KSM
      double precision P0BSM,DC9,DC10,DC7

      double precision RX13,RX23,RX12
      double precision RY13,RY23,RY12
      double precision RZ13,RZ23,RZ12
      double precision RS13,RS23,RS12
      double precision BRKpnn,RDMb,RDMs,y7V,y7A,C9,C10,BRXsll
      double precision RDMK,BRbsgapx

      double precision ELLEb(2,6),ERREs(2,6)

ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
c     New variables for Higgs penguins 
ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc

      double precision BRbtn,rhb,BRKl2
      double precision DMsH,CSTs,CSTd,CBs
      double precision xlk(6,6),xnk(2,6),scSUeg(6),scCeg(2)
      double precision xdl2g,xdl3g,xdr2g,xdr3g,xur3g,CS1,xur3mu,xul3mu

      double precision Echis, Echid,CSMFV,CSMFVfs,CSMFVfd,I3,H2
      double precision ELLEs(2,6),ELLEd(2,6),ERREb(2,6),G48(2,6,6)
      double precision Echigls,Echigld,H22(2,6,6),CSglfs,CSglapx,CSglfd
      double precision Psll,Pdll,Pllsapx,Plldapx,CSTsapx
      double precision ymu,gb,gs,gd,deltas,PllsapxIP,CSglfspr

      double precision xdmu,xmug,xumu,xqmu,xug,xqg,xdg,xq12gl
      double precision mDsq3,mUsq3,mQsq3,mgluino,mQsq12,mQsq23,dLL13 

cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
c     Standard Model inputs, including CKM (former stinpus.f)
cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc

      double precision MW,MZ,sinsqtw,Gf,alph,pi,alphas,alphas_susy
      double precision alphas_mt,alphas_mw,mt_mw
      double precision mE, mMU, mTAU, mUQ, mC, mT, mD,mS,mB
      double precision VCKM(3,3),Vud,Vus,Vub,Vcd,Vcs,Vcb 
      double precision Vtd,Vts,Vtb,VCKM0(3,3)

      double precision Echigl(3,3),ydown(3)

      double precision eps2EW,xt1mu,xt2mu,xb1mu,xb2mu,xm2mu,xm1mu,
     .                 xb1m1,xb2m1,xb1gl,xb2gl,xt1gl,xt2gl

      double precision delta8h,delta7h,G8H,G7H,C8H1,C7H1
      double precision epsmu,epstau,mR3,mL3,mR2,mL2,ytau


cccccccccccccccccc DUMP INPUT PARAMETERS cccccccccccccccccccccccccccc
c      GOTO 505

      PRINT *, 'tanbeta,mH,mur,mSL,mQL,A0_soft =',tanbeta,mH,mur,mL,mQL,A0
      PRINT *, 'M1tz,M2tz,M3tz =',M1tz,M2tz,M3tz
      PRINT 1002,'Ceg(J)  =',(Ceg(J),J=1,2)
      PRINT 1002,'OCR(1,J)=',(OCR(1,J),J=1,2)
      PRINT 1002,'OCR(2,J)=',(OCR(2,J),J=1,2)
      PRINT *,''
      PRINT 1002,'OCL(1,J)=',(OCL(1,J),J=1,2)
      PRINT 1002,'OCL(2,J)=',(OCL(2,J),J=1,2)
      PRINT *,''
      PRINT 1004,'Neg(J) =',(Neg(J),J=1,4)
      PRINT 1003,'ON(1,J)=',(ON(1,J),J=1,4)
      PRINT 1003,'ON(2,J)=',(ON(2,J),J=1,4)
      PRINT 1003,'ON(3,J)=',(ON(3,J),J=1,4)
      PRINT 1003,'ON(4,J)=',(ON(4,J),J=1,4)
      PRINT *,''
      PRINT 1001,'SUeg(J) =',(SUeg(I),I=1,6)
      PRINT 1000,'USU(1,J)=',(USU(1,J),J=1,6)
      PRINT 1000,'USU(2,J)=',(USU(2,J),J=1,6)
      PRINT 1000,'USU(3,J)=',(USU(3,J),J=1,6)
      PRINT 1000,'USU(4,J)=',(USU(4,J),J=1,6)
      PRINT 1000,'USU(5,J)=',(USU(5,J),J=1,6)
      PRINT 1000,'USU(6,J)=',(USU(6,J),J=1,6)
      PRINT *,''
      PRINT 1001,'SDeg(J) =',(SDeg(I),I=1,6)
      PRINT 1000,'USD(1,J)=',(USD(1,J),J=1,6)
      PRINT 1000,'USD(2,J)=',(USD(2,J),J=1,6)
      PRINT 1000,'USD(3,J)=',(USD(3,J),J=1,6)
      PRINT 1000,'USD(4,J)=',(USD(4,J),J=1,6)
      PRINT 1000,'USD(5,J)=',(USD(5,J),J=1,6)
      PRINT 1000,'USD(6,J)=',(USD(6,J),J=1,6)
      PRINT *,''
      PRINT 1001,'SLeg(J) =',(SLeg(I),I=1,6)
      PRINT 1000,'USL(1,J)=',(USL(1,J),J=1,6)
      PRINT 1000,'USL(2,J)=',(USL(2,J),J=1,6)
      PRINT 1000,'USL(3,J)=',(USL(3,J),J=1,6)
      PRINT 1000,'USL(4,J)=',(USL(4,J),J=1,6)
      PRINT 1000,'USL(5,J)=',(USL(5,J),J=1,6)
      PRINT 1000,'USL(6,J)=',(USL(6,J),J=1,6)

 1000 FORMAT(A,'[',f8.4,f8.4,f8.4,f8.4,f8.4,f8.4,' ]')
 1001 FORMAT(A,'[',f8.0,f8.0,f8.0,f8.0,f8.0,f8.0,' ]')
 1002 FORMAT(A,'[',f8.3,f8.3,' ]')
 1003 FORMAT(A,'[',f8.4,f8.4,f8.4,f8.4,' ]')
 1004 FORMAT(A,'[',f8.0,f8.0,f8.0,f8.0,' ]')


 505  CONTINUE


ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc

      MW = 80.403D0
      MZ = 91.1876D0
      sinsqtw = 0.23105d0
      Gf = 1.16d0*10.d0**(-5.d0)
      pi = DATAN(1.d0)*4.d0
      Mbs = 5.3696d0

      mE = 0.511d0*10.d0**(-3.d0)
      mMU = 105.66d0*10.d0**(-3.d0)
      mTAU = 1.777d0


      alph = 1.d0/128.92d0
      alphas = 0.1176d0

      mUQ = 2.3d0*10.d0**(-3.d0)
      mC = 0.677d0
      mT = 170.5d0

cccccccccccccccccc     mt scale (MSbar masses)   ccccccccccccccccc

      mD = 0.0023d0
      mS = 0.06d0
      mB = 3.d0

ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc

      alphas_mb = 0.d0
      alphas_mb= alphas/(1.d0+alphas*(7.d0/(2.d0*pi))*dlog(mB/mt))*
     .           (
     .            1.d0-(26.d0/7.d0)*alphas/(4.d0*pi)/
     .            (1.d0+alphas*(7.d0/(2.d0*pi))*dlog(mB/mt))*
     .            dlog((1.d0+alphas*(7.d0/(2.d0*pi))*dlog(mB/mt)))
     .           )


      mB_mb = 0.d0
      mB_mb = mB*((alphas_mb/alphas)**(4.d0/7.d0))*
     .           (1.d0 + (54.d0/7.d0-104.d0/49.d0)*
     .           (alphas_mb - alphas)/(4.d0*pi))

      mS_mb = 0.d0
      mS_mb = mS*((alphas_mb/alphas)**(4.d0/7.d0))*
     .           (1.d0 + (54.d0/7.d0-104.d0/49.d0)*
     .           (alphas_mb - alphas)/(4.d0*pi))


      alphas_mb = 0.d0
      alphas_mb= alphas/(1.d0+alphas*(7.d0/(2.d0*pi))*dlog(mB/mz))*
     .           (
     .            1.d0-(26.d0/7.d0)*alphas/(4.d0*pi)/
     .            (1.d0+alphas*(7.d0/(2.d0*pi))*dlog(mB/mz))*
     .            dlog((1.d0+alphas*(7.d0/(2.d0*pi))*dlog(mB/mz)))
     .           )

      alphas_mt = 0.d0
      alphas_mt= alphas/(1.d0+alphas*(7.d0/(2.d0*pi))*dlog(mt/mz))*
     .           (
     .            1.d0-(26.d0/7.d0)*alphas/(4.d0*pi)/
     .            (1.d0+alphas*(7.d0/(2.d0*pi))*dlog(mt/mz))*
     .            dlog((1.d0+alphas*(7.d0/(2.d0*pi))*dlog(mt/mz)))
     .           )

      alphas_mw = 0.d0
      alphas_mw= alphas/(1.d0+alphas*(7.d0/(2.d0*pi))*dlog(mw/mz))*
     .           (
     .            1.d0-(26.d0/7.d0)*alphas/(4.d0*pi)/
     .            (1.d0+alphas*(7.d0/(2.d0*pi))*dlog(mw/mz))*
     .            dlog((1.d0+alphas*(7.d0/(2.d0*pi))*dlog(mw/mz)))
     .           )

      mt_mw = 0.d0
      mt_mw = mt*((alphas_mw/alphas_mt)**(4.d0/7.d0))*
     .           (1.d0 + (54.d0/7.d0-104.d0/49.d0)*
     .           (alphas_mw - alphas_mt)/(4.d0*pi))

cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc

        Vud = 0.974167d0
      VCKM(1,1) = Vud
        Vus= 0.225798d0
      VCKM(1,2) = Vus
c        Vub= 0.00157d0 - i*0.0033d0
        Vub= 0.00366922d0
      VCKM(1,3) = Vub
        Vcd = -0.225753d0
      VCKM(2,1) = Vcd
        Vcs =0.973296d0
      VCKM(2,2) = Vcs
        Vcb=0.0415997d0
      VCKM(2,3) = Vcb
c        Vtd=0.007864d0 +i*0.0032d0
        Vtd=0.00582192d0
      VCKM(3,1) = Vtd
c        Vts=-0.0412370313d0
        Vts=-0.0413534d0
      VCKM(3,2) = Vts
        Vtb= 0.999138875d0
      VCKM(3,3) = Vtb


cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
c      Standard Definitions (former stddef.dat)
cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
 
      stw = dsqrt(sinsqtw)
      ctw = dsqrt(1.d0 - sinsqtw)

      beta = datan(tanbeta)
      sbeta = dsin(beta)
      cbeta = dcos(beta)
      cos2beta = cbeta*cbeta - sbeta*sbeta

      tansqtw = (stw/ctw)**2.d0

      alph3tZ = alphaS/(4.d0*pi)
      alph2tz = alph/(4.d0*pi*sinsqtw)
      alph2 = alph/sinsqtw
      alph1tz = alph2tz*tansqtw

       echarge=dsqrt(4.d0*pi*alph)
       gscharge=dsqrt(4.d0*pi*alphas)

C-------------------------------------------------------------------
C      VACUUM EXPECTATION VALUE (Normalisation vev = 246 GeV)
C-------------------------------------------------------------------

       vev = dsqrt(MW*MW*sinsqtw/(pi*alph))
       vev1= vev*cbeta
       vev2= vev*sbeta

ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
cc   MATCHING HIGH SCALE (SUGRA) AND LOW SCALE MFV SCENARIOS   cc
ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc

       mL3 = 0.d0
       mR3 = 0.d0
       mL2 = 0.d0
       mR2 = 0.d0
       mqsq3 = 0.d0
       mdsq3 = 0.d0
       musq3 = 0.d0
       mQsq12 = 0.d0
       AU3 = 0.d0
       mgluino = 0.d0
       dLL23 = 0.d0
       dLL13 = 0.d0

       mL3 = mL
       mR3 = mL
       mL2 = mL
       mR2 = mL
       mqsq3 = mQL**2.d0
       mdsq3 = mQL**2.d0
       musq3 = mQL**2.d0
       mQsq12 = mQL**2.d0
       AU3 = A0
       mgluino = M3tz
       dLL23 = 0.d0
       dLL13 = 0.d0

ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
c      PART O.     Risommazioni Yukawa & Higgs penguins
ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc


c    sbottom mass eigenstates

      mblr = 0.d0
      mblr = -mur*tanbeta

      ml2b = 0.d0
      ml2b = mqsq3 + mb*mb + MZ*MZ*cos2beta*(-0.5d0 
     .           + (1.d0/3.d0)*sinsqtw)
      mr2b = 0.d0
      mr2b = mdsq3 + mb*mb - (1.d0/3.d0)*MZ*MZ*cos2beta*sinsqtw
 
      sgnb = 0.d0
      sgnb = (ml2b-mr2b)/dabs(ml2b-mr2b) 

      tantetab = 0.d0
      tantetab = ((-sgnb*2.d0*mb*mblr)/(-sgnb*(ml2b-mr2b)-
     .             dsqrt((ml2b-mr2b)**2.d0+4.d0*(mb*mblr)**2.d0)))

      tetab = 0.d0
      tetab = datan(((-sgnb*2.d0*mb*mblr)/(-sgnb*(ml2b-mr2b)-
     .             dsqrt((ml2b-mr2b)**2.d0+4.d0*(mb*mblr)**2.d0))))

      c1b = 0.d0
      s1b = 0.d0
      c1b = dcos(tetab)
      s1b = dsin(tetab)

      mb1sq = 0.d0
      mb1sq = ((ml2b+mr2b)+sgnb*
     .         dsqrt((ml2b-mr2b)**2.d0+4.d0*(mb*mblr)**2.d0))/2.d0

      mb2sq = 0.d0
      mb2sq = ((ml2b+mr2b)-sgnb*
     .         dsqrt((ml2b-mr2b)**2.d0+4.d0*(mb*mblr)**2.d0))/2.d0 


c    stop mass eigenstates

      mtlr = 0.d0
      mtlr = AU3-mur/tanbeta

      ml2t = 0.d0
      ml2t = mQsq3 + mT*mT + MZ*MZ*cos2beta*(0.5d0 
     .           - (2.d0/3.d0)*sinsqtw)
      mr2t = 0.d0
      mr2t = mUsq3 + mT*mT+(2.d0/3.d0)*MZ*MZ*cos2beta*sinsqtw
 
      sgnt = 0.d0
      sgnt = (ml2t-mr2t)/dabs(ml2t-mr2t)

      tantetat = 0.d0
      tantetat = ((-sgnt*2.d0*mt*mtlr)/(-sgnt*(ml2t-mr2t)-
     .             dsqrt((ml2t-mr2t)**2.d0+4.d0*(mt*mtlr)**2.d0)))

      tetat = 0.d0
      tetat = datan(((-sgnt*2.d0*mt*mtlr)/(-sgnt*(ml2t-mr2t)-
     .             dsqrt((ml2t-mr2t)**2.d0+4.d0*(mt*mtlr)**2.d0))))

      c1t = 0.d0
      s1t = 0.d0
      c1t = dcos(tetat)
      s1t = dsin(tetat)

      mt1sq = 0.d0
      mt1sq = ((ml2t+mr2t)+sgnt*
     .         dsqrt((ml2t-mr2t)**2.d0+4.d0*(mt*mtlr)**2.d0))/2.d0

      mt2sq = 0.d0
      mt2sq = ((ml2t+mr2t)-sgnt*
     .         dsqrt((ml2t-mr2t)**2.d0+4.d0*(mt*mtlr)**2.d0))/2.d0

ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc

       mU(1)=mUQ
       mU(2)=mC
       mU(3)=mT
       mDown(1)=md
       mDown(2)=ms
       mDown(3)=mb

       xumu = 0.d0
       xdmu = 0.d0
       xqmu = 0.d0
       xug =  0.d0 
       xqg =  0.d0
       xdg =  0.d0
       xamu = 0.d0
       xmug = 0.d0


       xumu = mUsq3/(mur**2.d0)
       xdmu = mDsq3/(mur**2.d0)
       xqmu = mQsq3/(mur**2.d0)
       xug  =  mUsq3/(mgluino**2.d0)
       xqg  =  mQsq3/(mgluino**2.d0)
       xdg  =  mDsq3/(mgluino**2.d0)
       xmug = mur/mgluino
       xamu = AU3/mur

       ytop = 0.d0
       gtop = 0.d0
       ytop = ((2.d0*dsqrt(2.d0)*Gf)**(1.d0/2.d0))*(mt/dsin(beta))
       gtop = ytop/dsqrt(4.d0*pi*alph2)

      xt1mu = 0.d0
      xt2mu = 0.d0
      xb1mu = 0.d0
      xb2mu = 0.d0
      xm2mu = 0.d0
      xm1mu = 0.d0
      xb1m1 = 0.d0
      xb2m1 = 0.d0
      xb1gl = 0.d0
      xb2gl = 0.d0
      xt1gl = 0.d0
      xt2gl = 0.d0
      xq12gl = 0.d0

      xt1mu = mt1sq/(mur**2.d0)
      xt2mu = mt2sq/(mur**2.d0)
      xb1mu = mb1sq/(mur**2.d0)
      xb2mu = mb2sq/(mur**2.d0)
      xm2mu = (M2tz/mur)**2.d0
      xm1mu = (M1tz/mur)**2.d0
      xb1m1 = mb1sq/(M1tz**2.d0)
      xb2m1 = mb2sq/(M1tz**2.d0)
      xb1gl = mb1sq/(mgluino**2.d0)
      xb2gl = mb2sq/(mgluino**2.d0)
      xt1gl = mt1sq/(mgluino**2.d0)
      xt2gl = mt2sq/(mgluino**2.d0)
      xq12gl = mQsq12/(mgluino**2.d0)

       eps0 = 0.d0
       eps0p= 0.d0
       eps2 = 0.d0



       eps0  = ((2.d0*alphas)/(3.d0*pi))*xmug*H2(xb1gl,xb2gl)

       eps0p = -((2.d0*alphas)/(3.d0*pi))*xmug*
     .                     (
     .          (c1t**2.d0)*H2(xt2gl,xq12gl)
     .                     +
     .          (s1t**2.d0)*H2(xt1gl,xq12gl)
     .                     )

       eps2  = (xamu*(ytop**2.d0)/(16.d0*pi**2.d0))*H2(xt1mu,xt2mu)
       
       eps2EW = 0.d0
       eps2EW = -alph2tz*(M2tz/mur)*
     .                   (
     .                    (c1t**2.d0)*H2(xt1mu,xm2mu)+
     .                    (s1t**2.d0)*H2(xt2mu,xm2mu)+
     .                    (c1b**2.d0)*H2(xb1mu,xm2mu)/2.d0+
     .                    (s1b**2.d0)*H2(xb2mu,xm2mu)/2.d0
     .                   )
     .          -alph1tz*((M1tz/(mur*3.d0))*
     .                   (
     .                    (c1b**2.d0)*H2(xb2mu,xm1mu)+
     .                    (s1b**2.d0)*H2(xb1mu,xm1mu)+
     .                    (c1b**2.d0)*H2(xb1mu,xm1mu)/2.d0+
     .                    (s1b**2.d0)*H2(xb2mu,xm1mu)/2.d0
     .                   )
     .                  )
     .         -(alph1tz/9.d0)*(mur/M1tz)*H2(xb1m1,xb2m1)


       eps0 = eps0 + eps2EW


       do i= 1,3
       mdown(i) = 0.d0
       enddo

       mdown(3) = mb
       mdown(2) = ms
       mdown(1) = md


       yb= 0.d0
       ys= 0.d0
       yd= 0.d0

       yb = ((2.d0*dsqrt(2.d0)*Gf)**(1.d0/2.d0))*(mb/dcos(beta))
     &      /(1.d0+(eps0+eps2)*tanbeta)

       ys = ((2.d0*dsqrt(2.d0)*Gf)**(1.d0/2.d0))*(ms/dcos(beta))
     &      /(1.d0+eps0*tanbeta)
       yd = ((2.d0*dsqrt(2.d0)*Gf)**(1.d0/2.d0))*(md/dcos(beta))
     &      /(1.d0+eps0*tanbeta)

       do i=1,3
           ydown(i)=0.d0
       enddo

       ydown(3) = yb
       ydown(2) = ys
       ydown(1) = yd

       do i=1,3
           gdown(i)=0.d0
       enddo
       gdown(3) = (mb/(dsqrt(2.d0)*mw*dcos(beta)))
     &      /(1.d0+(eps0+eps2)*tanbeta)
       gdown(2) = (ms/(dsqrt(2.d0)*mw*dcos(beta)))/(1.d0+eps0*tanbeta)
       gdown(1) = (md/(dsqrt(2.d0)*mw*dcos(beta)))/(1.d0+eps0*tanbeta)


       eps1p = 0.d0
       eps1p=-(xamu*(yb**2.d0)/(16.d0*pi**2.d0))*H2(xqmu,xdmu)



cccccccccc    Resummation in the leptonic sector     cccccccccc

       epstau = 0.d0
       epstau = -alph2tz*(3.d0/2.d0)*(mur/M2tz)*
     .          H2((mur/M2tz)**2.d0,(mL3/M2tz)**2.d0)
     .                    +
     .          alph1tz*(mur/M1tz)*
     .     (    (1.d0/2.d0)*H2((mur/M1tz)**2.d0,(mL3/M1tz)**2.d0)+
     .           H2((mL3/M1tz)**2.d0,(mR3/M1tz)**2.d0) -
     .           H2((mur/M1tz)**2.d0,(mR3/M1tz)**2.d0)
     .     )


       epsmu = 0.d0
       epsmu = -alph2tz*(3.d0/2.d0)*(mur/M2tz)*
     .          H2((mur/M2tz)**2.d0,(mL2/M2tz)**2.d0)
     .                    +
     .          alph1tz*(mur/M1tz)*
     .     (    (1.d0/2.d0)*H2((mur/M1tz)**2.d0,(mL2/M1tz)**2.d0)+
     .           H2((mL2/M1tz)**2.d0,(mR2/M1tz)**2.d0) -
     .           H2((mur/M1tz)**2.d0,(mR2/M1tz)**2.d0)
     .     )


       ymu= 0.d0
       ymu = ((2.d0*dsqrt(2.d0)*Gf)**(1.d0/2.d0))*(mmu/dcos(beta))
     .       /(1.d0 + epsmu*tanbeta)

       ytau= 0.d0
       ytau = ((2.d0*dsqrt(2.d0)*Gf)**(1.d0/2.d0))*(mtau/dcos(beta))
     .       /(1.d0 + epstau*tanbeta)

ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
ccccccccc                   CKM bare              ccccccccccccccccccc
ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc

      xdl2g = 0.d0
      xdl3g = 0.d0
      xdr3g = 0.d0
      xur3g = 0.d0
      xur3mu= 0.d0
      xul3mu= 0.d0
      xdl2g = mQsq12/(mgluino**2.d0)
      xdl3g = mQsq3/(mgluino**2.d0)
      xdr3g = mDsq3/(mgluino**2.d0)
      xur3g = mUsq3/(mgluino**2.d0)
      xur3mu= mUsq3/(mur**2.d0)
      xul3mu= mQsq3/(mur**2.d0)

      epsL = 0.d0

      if(dabs(xdl2g/xdl3g - 1.d0).ge.0.01d0)then
      epsL= ((2.d0*alphas)/(3.d0*pi))*(mur/mgluino)*
     .       dsqrt(xdl3g*xdl2g)*
     .      ((I3(xdr3g,xdl2g)-I3(xdr3g,xdl3g))/(xdl2g-xdl3g))
      else
      xdl2g = xdl3g*(1.d0 + 0.01d0)
      epsL= ((2.d0*alphas)/(3.d0*pi))*(mur/mgluino)*
     .       dsqrt(xdl3g*xdl2g)*
     .      ((I3(xdr3g,xdl2g)-I3(xdr3g,xdl3g))/(xdl2g-xdl3g))
      endif


      VCKM0(3,2) = 0.d0
      VCKM0(3,1) = 0.d0
      VCKM0(2,3) = 0.d0
      VCKM0(1,3) = 0.d0
      VCKM0(1,1) = 0.d0
      VCKM0(2,2) = 0.d0
      VCKM0(3,3) = 0.d0
      VCKM0(1,2) = 0.d0
      VCKM0(2,1) = 0.d0

      VCKM0(1,1) = VCKM(1,1)
      VCKM0(2,2) = VCKM(2,2)
      VCKM0(3,3) = VCKM(3,3)
      VCKM0(1,2) = VCKM(1,2)
      VCKM0(2,1) = VCKM(2,1)

      VCKM0(3,2) = VCKM(3,2)*(1.d0+(eps0+eps2)*tanbeta)
     .             /(1.d0+eps0*tanbeta)
     .                          +
     .             epsL*tanbeta*dLL23/(1.d0+eps0*tanbeta)

      VCKM0(3,1) = VCKM(3,1)*(1.d0+(eps0+eps2)*tanbeta)
     .             /(1.d0+eps0*tanbeta)
     .                          +
     .             epsL*tanbeta*dLL13/(1.d0+eps0*tanbeta)

      VCKM0(2,3) = VCKM(2,3)*(1.d0+(eps0+eps2)*tanbeta)
     .             /(1.d0+eps0*tanbeta)
     .                          -
     .             epsL*tanbeta*dLL23/(1.d0+eps0*tanbeta)

      VCKM0(1,3) = VCKM(1,3)*(1.d0+(eps0+eps2)*tanbeta)
     .             /(1.d0+eps0*tanbeta)
     .                          -
     .             epsL*tanbeta*dLL13/(1.d0+eps0*tanbeta)

       do im=1,6
         do jm=1,6
      deltaKronecker(im,jm)=0.d0
       enddo
      deltaKronecker(im,im)=1.d0
       enddo

         do im=1,6
         do jm=1,6
       RR(im,jm)=0.d0
 	 enddo
 	 enddo

         do im=1,3
         do jm=1,3
       RR(im,jm)=VCKM(im,jm)
 	 enddo
 	 enddo

         do im=3,6
       RR(im,im)=1.0d0
 	 enddo

ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
c
c     Syllabus for the unitary matrices which diagonalise all
c     relevant sparticle mass matrices (chargino & squarks)
c     Full complex structure ready & commented
c
ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc

       do im=1,2
         do jm=1,2
        Zp(im,jm)=OCR(im,jm)
        Zm(im,jm)=OCL(im,jm)
       enddo
       enddo

       do im=1,2
         do jm=1,2
ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
c
c     Changed by G.I.  June 2012:
c
         Vh(im,jm)=Zp(jm,im)
         Uh(im,jm)=Zm(im,jm)
c 
ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
       enddo
       enddo

       do im=1,2
         do jm=1,2
        V(im,jm)=Vh(jm,im)
        U(im,jm)=Uh(jm,im)
       enddo
       enddo

       do im=1,4
         do jm=1,4
        ZN(im,jm)=ON(jm,im)
       enddo
       enddo

       do im=1,3
         do jm=1,3
        Zsn(im,jm)=USN(jm,im)
       enddo
       enddo

       do im=1,6
         do jm=1,6
        ZU(im,jm)=USU(jm,im)
        ZD(im,jm)=USD(jm,im)
        ZL(im,jm)=USL(jm,im)
       enddo
       enddo

       do im=1,6
         do jm=1,6
       H(im,jm)=0.d0
         do j=1,6
c         H(im,jm)= H(im,jm)+ZU(j,im)*RR(j,jm)
         H(im,jm)= H(im,jm)+ZU(j,im)*RR(jm,j)
         enddo
 	 enddo
       enddo
       
       do im=1,6
         do jm=1,6
       Hh(im,jm)= H(jm,im)
        enddo
       enddo

cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
cccccccccccccccccc          P --> l nu          cccccccccccccccccccc
cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc

       MHp = 0.d0
       MHp = dsqrt(MH**2.d0 + MW**2.d0)

       xth = 0.d0
       xth = (mt/MHp)**2.d0

       rHB = 0.d0
       rHB = (
     &        1.d0-((5.279d0/MHp)**2.d0)*(tanbeta**2.d0)*
     &        (VCKM0(3,1)/VCKM(3,1))/
     &        ((1.d0+(eps0+eps2)*tanbeta)*(1.d0+epstau*tanbeta))
     &       )**2.d0
c       rHB = (1.d0-((5.279d0/MHp)**2.d0)*(tanbeta**2.d0)/
c     &       ((1.d0+eps0*tanbeta)*(1.d0+epstau*tanbeta)
c     &       ))**2.d0
       BRbtn = 0.d0
       BRbtn = rHB

       rHK = 0.d0
       rHK = (1.d0-((0.497d0/MHp)**2.d0)*(tanbeta**2.d0)/
     .       ((1.d0+eps0*tanbeta)*(1.d0+epsmu*tanbeta)))**2.d0
       BRKl2 = 0.d0
       BRKl2 = rHK

cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
cccccccccccc                 P --> ll                       cccccccccc
cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc

        do l=1,6
        do k=1,6

           xlk(l,k)=0.d0
           xlk(l,k)= SUeg(l)/SUeg(k)

        enddo
        enddo


        do n=1,2
        do k=1,6

           xnk(n,k)=0.d0
           xnk(n,k)= (Ceg(n)**2.d0)/SUeg(k)

        enddo
        enddo

c Chargino contribution

        do n=1,2
        do l=1,6
        do k=1,6

         G48(n,l,k) = 0.d0
         G48(n,l,k) = ytop*AU3*H(k,3)*Hh(6,l)*(Ceg(n)/SUeg(k))*
     &                H2(xlk(l,k),xnk(n,k))

        enddo
        enddo
        enddo


        do l=1,6
        do n=1,2

	  ELLEs(n,l) = 0.d0
          ELLEs(n,l) = -dsqrt(4.d0*pi*alph2)*H(l,2)*Vh(1,n)
     &                 +ytop*VCKM0(3,2)*H(l,6)*Vh(2,n)

          ELLEd(n,l) = 0.d0
          ELLEd(n,l) = -dsqrt(4.d0*pi*alph2)*H(l,1)*Vh(1,n)
     &                 +ytop*VCKM0(3,1)*H(l,6)*Vh(2,n)

	  ERREb(n,l) = 0.d0
          ERREb(n,l) = yb*Hh(3,l)*Uh(2,n)

        enddo
        enddo


	Echis=0.d0
	Echid=0.d0

        do n=1,2
        do l=1,6
        do k=1,6

         Echis = Echis+ ELLEs(n,l)*ERREb(n,k)*G48(n,l,k)
         Echid = Echid+ ELLEd(n,l)*ERREb(n,k)*G48(n,l,k)

        enddo
        enddo
        enddo

        Echis = Echis/(16.d0*pi*pi)
        Echid = Echid/(16.d0*pi*pi)


      CSMFVfs = 0.d0
      CSMFVfd = 0.d0

      CSMFVfs = ymu*Echis*tanbeta*
     &          (1.d0/(1.d0+(eps0+eps2)*tanbeta))*
     &          (pi**2.d0/(2.d0*(Gf**2.d0)*(MW**2.d0)*(MH**2.d0)))

      CSMFVfd = ymu*Echid*tanbeta*
     &          (1.d0/(1.d0+(eps0+eps2)*tanbeta))*
     &          (pi**2.d0/(2.d0*(Gf**2.d0)*(MW**2.d0)*(MH**2.d0)))


c Gluino contribution

        do i= 1,3
        do j= 1,3

        Echigl(i,j)=0.d0

        enddo
        enddo

        do i= 1,3
        do j= 1,3
        do m= 1,3
        do l=1,6
        do k=1,6

        Echigl(i,j) = Echigl(i,j) + ((8.d0/3.d0)*alphas*4.d0*pi)*
     .                (mur*mgluino/SDeg(l))*
     .            USD(l,j)*USD(k,i+3)*ydown(m)*USD(k,m+3)*USD(l,m)*
     .            H2((mgluino**2.d0)/SDeg(l),SDeg(k)/SDeg(l))

        enddo
        enddo
        enddo
        enddo
        enddo

        do i= 1,3
        do j= 1,3

        Echigl(i,j) = Echigl(i,j)/(16.d0*pi*pi)

        enddo
        enddo


        CSglfs = 0.d0
        CSglfd = 0.d0

        CSglfs = ymu*Echigl(3,2)*tanbeta*
     .           (1.d0/(1.d0+(eps0+eps2)*tanbeta))*
     .           (pi**2.d0/(2.d0*(Gf**2.d0)*(MW**2.d0)*(MH**2.d0)))

        CSglfd = ymu*Echigl(3,1)*tanbeta*
     .           (1.d0/(1.d0+(eps0+eps2)*tanbeta))*
     .           (pi**2.d0/(2.d0*(Gf**2.d0)*(MW**2.d0)*(MH**2.d0)))

cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
cccc         Total Wilson coeff for P->ll & DMBs            cccccccc
cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc

       CSTs = 0.d0
       CSTd = 0.d0

       CSTs = CSMFVfs+CSglfs
       CSTd = CSMFVfd+CSglfd


cccccccc                    Delta M_s                   ccccccccc

      P2LRbar = 0.9d0
      S0 = 2.33d0

      C2LR = 0.d0
      C2LR = -((Echis+Echigl(3,2))**2.d0)*(mS/mB)*
     .        ((tanbeta**2.d0)/
     .        ((1.d0+(eps0+eps2)*tanbeta)**2.d0))/(MH**2.d0)*
     .        ((4.d0*pi/(Gf*MW*Vts))**2.d0)

      DMsH = 0.d0
      DMsH = (P2LRbar/S0)*C2LR

ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
ccccccccc               MIA APPROXIMATION                cccccccccc
ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc

cccccccc                      Bs->mm                      ccccccccc

c     chargino contribution

      xdl2g = 0.d0
      xdl3g = 0.d0
      xdr3g = 0.d0
      xur3g = 0.d0
      xur3mu= 0.d0
      xul3mu= 0.d0
      xdl2g = mQsq12/(mgluino**2.d0)
      xdl3g = mQsq3/(mgluino**2.d0)
      xdr3g = mDsq3/(mgluino**2.d0)
      xur3g = mUsq3/(mgluino**2.d0)
      xur3mu= mUsq3/(mur**2.d0)
      xul3mu= mQsq3/(mur**2.d0)

      CSMFV = 0.d0

      CSMFV = (((mt**2.d0)*mmu)/(4.d0*MW**2.d0))*
     .        ((tanbeta**3.d0)/(MH**2.d0))*(AU3/mur)*
     .        H2(xur3mu,xul3mu)
     .        /((1.d0+eps0*tanbeta)*(1.d0+(eps0+eps2)*tanbeta)
     .         *(1.d0 + epsmu*tanbeta))

c     gluino contribution in the MIA (Bs)

      CSglapx = 0.d0
 
      if(dabs(xdl2g/xdl3g-1.d0).ge.0.01d0)then
      CSglapx = ((4.d0/3.d0)*alphas/alph2)*mmu*dLL23/Vts*
     .          ((tanbeta**3.d0)/(MH**2.d0))*
     .          (mur/mgluino)*dsqrt(xdl3g*xdl2g)*
     .          ((I3(xdr3g,xdl2g)-I3(xdr3g,xdl3g))/(xdl2g-xdl3g))
     .          /((1.d0+(eps0+eps2)*tanbeta)**2.d0
     .           *(1.d0 + epsmu*tanbeta))
      else
      xdl2g = xdl3g*(1.d0 + 0.01d0)
      CSglapx = ((4.d0/3.d0)*alphas/alph2)*mmu*dLL23/Vts*
     .          ((tanbeta**3.d0)/(MH**2.d0))*
     .          (mur/mgluino)*dsqrt(xdl3g*xdl2g)*
     .          ((I3(xdr3g,xdl2g)-I3(xdr3g,xdl3g))/(xdl2g-xdl3g))
     .          /((1.d0+(eps0+eps2)*tanbeta)**2.d0
     .           *(1.d0 + epsmu*tanbeta))
      endif


       CSTsapx = 0.d0
       CSTsapx = CSMFV+CSglapx

       Pllsapx = 0.d0
       Pllsapx = 2.16d0*(10.d0**(-6.d0))*
     .          ((Mbs*CSTsapx)**2.d0+(Mbs*CSTsapx+0.04d0)**2.d0)


cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
cccccccc     PART I. DIPOLE Operators:  B-->X_s gamma     cccccccc
cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc

c  CHARGED/NEUTRAL HIGGS CONTRIBUTION

       C7H = 0.d0
       C7H= (1.d0/(1.d0+(eps0+eps2)*tanbeta))*
     .      (1.d0+eps0p*tanbeta-
     .      (eps2*eps1p/(1.d0+eps0*tanbeta))*(tanbeta**2.d0))*F7(xth)
     .                  -
     .      (eps2*(tanbeta**3.d0)/
     .      ((1.d0+eps0*tanbeta)*(1.d0+(eps0+eps2)*tanbeta)**2.d0))*
     .      ((3.d0)**2.d0)/(36.d0*MH**2.d0)

       C8H = 0.d0
       C8H= (1.d0/(1.d0+(eps0+eps2)*tanbeta))*
     .      (1.d0+eps0p*tanbeta-
     .      (eps2*eps1p/(1.d0+eps0*tanbeta))*(tanbeta**2.d0))*F8(xth)
     .                  -
     .      (eps2*(tanbeta**3.d0)/
     .      ((1.d0+eps0*tanbeta)*(1.d0+(eps0+eps2)*tanbeta)**2.d0))*
     .      ((3.d0)**2.d0)/(36.d0*MH**2.d0)


       C7H1 = 0.d0
       C7H1 = (1.d0/(1.d0+(eps0+eps2)*tanbeta))*
     .        (1.d0+eps0p*tanbeta-
     .        (eps2*eps1p/(1.d0+eps0*tanbeta))*(tanbeta**2.d0))*
     .        (G7H(xth) + 2.d0*delta7h(xth)*dlog(mw/mHp))

       C8H1 = 0.d0
       C8H1 = (1.d0/(1.d0+(eps0+eps2)*tanbeta))*
     .        (1.d0+eps0p*tanbeta-
     .        (eps2*eps1p/(1.d0+eps0*tanbeta))*(tanbeta**2.d0))*
     .        (G8H(xth) + 2.d0*delta8h(xth)*dlog(mw/mHp))


c  CHARGINO CONTRIBUTION

      alphas_susy = 0.d0
      alphas_susy= alphas/(1.d0+alphas*(7.d0/(2.d0*pi))*
     .             dlog(dsqrt(mt1sq)/mz))*
     .        (
     .   1.d0-(26.d0/7.d0)*alphas/(4.d0*pi)/
     .   (1.d0+alphas*(7.d0/(2.d0*pi))*dlog(dsqrt(mt1sq)/mz))*
     .   dlog((1.d0+alphas*(7.d0/(2.d0*pi))*dlog(dsqrt(mt1sq)/mz)))
     .        )


        eta= 0.d0
        eta= alphas_susy/alphas

        mtsusy= 0.d0
        mtsusy= (mt_mw*((alphas_susy/alphas_mt)**(4.d0/7.d0))*
     .          ((alphas_mt/alphas_mw)**(12.d0/23.d0)))
     .          /(
     .            dsqrt(1.d0+((9.d0*ytop**2.d0)/(8.d0*pi*alphas_mt))*
     .            (((alphas_susy/alphas_mt)**(1.d0/7.d0))-1.d0))
     .           )


        do I=1,3
        do ip=1,6
        do jp=1,2

         AdUC(I,ip,jp)=0.d0
         BdUC(I,ip,jp)=0.d0

              do J=1,3
          AdUC(I,ip,jp) = AdUC(I,ip,jp)+
     .                    (-H(ip,J)*Zp(jp,1)+(mtsusy/mt)*
     .                    (mU(J)/(dsqrt(2.d0)*mw*dsin(beta)))*
     .                    H(ip,J+3)*Zp(jp,2)
     .                    )*VCKM(J,I)

          BdUC(I,ip,jp) = BdUC(I,ip,jp) +
     .                    gdown(I)*H(ip,J)*Zm(2,jp)*VCKM0(J,I)
                enddo
        enddo
        enddo
        enddo
        

      do a = 1, 2
      do x = 1, 6

      yy(a,x) = 0.d0
      yy(a,x) = (Ceg(a)**2.d0)/SUeg(x)

      enddo
      enddo

c      chargino contribution

      c7ch = 0.d0

      do jp = 1, 2
      do ip = 1, 6

      c7ch = c7ch + (1.d0/(VCKM(3,3)*VCKM(3,2)))*
     .            (MW*MW/SUeg(ip))*
     .            (
     .             AdUC(2,ip,jp)*AdUC(3,ip,jp)*
     .            (f11(yy(jp,ip))+(2.d0/3.d0)*f22(yy(jp,ip)))
     .                                +
     .            AdUC(2,ip,jp)*BdUC(3,ip,jp)*(Ceg(jp)/mb)*
     .            (f33(yy(jp,ip))+(2.d0/3.d0)*f44(yy(jp,ip)))
     .            )

      enddo
      enddo


      c8ch = 0.d0

      do jp = 1, 2
      do ip = 1, 6

      c8ch = c8ch + (1.d0/(VCKM(3,3)*VCKM(3,2)))*
     .            (MW*MW/SUeg(ip))*
     .            (
     .             AdUC(2,ip,jp)*AdUC(3,ip,jp)*
     .             f22(yy(jp,ip))+
     .             AdUC(2,ip,jp)*BdUC(3,ip,jp)
     .             *(Ceg(jp)/mb)*f44(yy(jp,ip))
     .            )
      enddo
      enddo


c      gluino contribution

       C7gl= 0.d0

       do im = 1,6
       C7gl = C7gl + ((4.d0/9.d0)*(alphas/alph2)*((mw/mgluino)**2.d0)
     .               /(VCKM(3,3)*VCKM(3,2)))*
     .               (
     .               -USD(im,2)*USD(im,3)*f3(SDeg(im)/mgluino**2.d0)
     .               +2.d0*USD(im,2)*USD(im,6)*
     .               f4(SDeg(im)/mgluino**2.d0)*(mgluino/mb)
     .               )
        enddo



       C8gl= 0.d0

       do im = 1,6
       C8gl = C8gl -
     .          ((1.d0/2.d0)*(alphas/alph2)*((mw**2.d0)/SDeg(im))
     .               /(VCKM(3,3)*VCKM(3,2)))*
     .               (
     .               -USD(im,2)*USD(im,3)*
     .               (-3.d0*f11(mgluino**2.d0/SDeg(im))
     .                -(1.d0/3.d0)*f22(mgluino**2.d0/SDeg(im)))
     .               +2.d0*USD(im,2)*USD(im,6)*
     .               (-3.d0*f33(mgluino**2.d0/SDeg(im))
     .                -(1.d0/3.d0)*f44(mgluino**2.d0/SDeg(im)))
     .               *(mgluino/mb)
     .               )
        enddo

ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
c                        RGE effects
ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc

       C7chRES= 0.d0
       C8chRES= 0.d0

       C7chRES= (eta**(16.d0/21.d0))*(C7ch+C7gl) +
     .          (8.d0/3.d0)*((eta**(14.d0/21.d0))-
     .          (eta**(16.d0/21.d0)))*(C8ch+C8gl)

       C8chRES= (eta**(14.d0/21.d0))*(C8ch+C8gl)


        C7 = 0.d0
        C8 = 0.d0
        C7 = C7chRes+C7H
        C8 = C8chRes+C8H

ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
c      B-Xs gamma   Bracnhing ratio: MISIAK
ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc

c       Brtot = 0.d0
c       Brtot = 3.150055981433902
c     .         - 7.824786698647555*C7
c     .         - 2.0945629943122532*C8
c     .         + 5.133484906701248*C7**2.d0
c     .         + 0.518633676234877*C8**2.d0
c     .         + 2.5928603736700957*C7*C8
c     .         - 0.08142794331649322*C7H1
c     .         - 0.02430412152072149*C8H1
c     .         + 0.09209321186259296*C7*C7H1
c     .         + 0.027487426566116562*C7H1*C8
c     .         + 0.027487426566116562*C7*C8H1
c     .         + 0.008204281335686028*C8*C8H1

c       BRbsg = Brtot/3.150055981433902


       Brtot = 0.d0
       Brtot = 3.15d0 - 8.d0*C7 - 1.9d0*C8

       BRbsg = Brtot/3.15d0

cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
c
c     Part II. Electroweak penguins & boxes 
c     (for B->ll, B->Xsll, K->pll, Delta MB, Delta MK)
c
cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc


C  ***************************************************************
C                      Chargino Z penguin
C  ***************************************************************

	Qin=1
        Qout=2
        Vin=Vtd
        Vout=Vts

       ZPeng=0.d0
	do j=1,2
	   do i=1,2
	    do l=1,6
	     do k=1,6
	     ZperZ=0.d0
	         do N=1,3
	       ZperZ=ZperZ+H(k,N)*Hh(N,l)
	         enddo
	ZPeng=ZPeng + 1.d0/8.d0
     &	 *(H(l,Qin)*Vh(1,j)- gtop*Vin*H(l,6)*Vh(2,j))
     &	 *(Hh(Qout,k)*V(i,1)- gtop*Vout*Hh(6,k)*V(i,2))
     &	 *(V(j,1)*Vh(1,i)*deltaKronecker(l,k)
     &   *KK(Ceg(i)**2.d0/Sueg(k),Ceg(j)**2.d0/Sueg(k))
     &   -2.d0*U(i,1)*Uh(1,j)*deltaKronecker(l,k)
     &   *Ceg(i)*Ceg(j)/Sueg(k)
     &    *JJ(Ceg(i)**2.d0/Sueg(k),Ceg(j)**2.d0/Sueg(k))
     &   - deltaKronecker(i, j)
     &   *ZperZ*KK(Ceg(i)**2.d0/Sueg(k),Sueg(l)/Sueg(k))
     &    )
	     enddo
	    enddo
	   enddo
	 enddo

        Zpeng12=0.d0
        Zpeng12=Zpeng

        Qin=1
        Qout=3
        Vin=Vtd
        Vout=Vtb
 
       ZPeng=0.d0
	do j=1,2
	   do i=1,2
	    do l=1,6
	     do k=1,6
	     ZperZ=0.d0
	         do N=1,3
	       ZperZ=ZperZ+H(k,N)*Hh(N,l)
	         enddo
	ZPeng=ZPeng + 1.d0/8.d0
     &	 *(H(l,Qin)*Vh(1,j)- gtop*Vin*H(l,6)*Vh(2,j))
     &	 *(Hh(Qout,k)*V(i,1)- gtop*Vout*Hh(6,k)*V(i, 2))
     &	 *(V(j,1)*Vh(1,i)*deltaKronecker(l,k)
     &   *KK(Ceg(i)**2.d0/Sueg(k),Ceg(j)**2.d0/Sueg(k)) 
     &   -2.d0*U(i,1)*Uh(1,j)*deltaKronecker(l,k)
     &   *Ceg(i)*Ceg(j)/Sueg(k)
     &    *JJ(Ceg(i)**2.d0/Sueg(k),Ceg(j)**2.d0/Sueg(k))
     &   - deltaKronecker(i, j)
     &   *ZperZ*KK(Ceg(i)**2.d0/Sueg(k),Sueg(l)/Sueg(k))
     &     )
	     enddo
	    enddo
	   enddo
	 enddo

        Zpeng13=0.d0
        Zpeng13=Zpeng

        Qin=2
        Qout=3
        Vin=Vts
        Vout=Vtb

       ZPeng=0.d0
	do j=1,2
	   do i=1,2
	    do l=1,6
	     do k=1,6
	     ZperZ=0.d0
	         do N=1,3
	       ZperZ=ZperZ+H(k,N)*Hh(N,l)
	         enddo
	ZPeng=ZPeng + 1.d0/8.d0
     &	 *(H(l,Qin)*Vh(1,j)- gtop*Vin*H(l,6)*Vh(2,j))
     &	 *(Hh(Qout,k)*V(i,1)- gtop*Vout*Hh(6,k)*V(i, 2))
     &	 *(V(j,1)*Vh(1,i)*deltaKronecker(l,k)
     &   *KK(Ceg(i)**2.d0/Sueg(k),Ceg(j)**2.d0/Sueg(k)) 
     &   -2.d0*U(i,1)*Uh(1,j)*deltaKronecker(l,k)
     &   *Ceg(i)*Ceg(j)/Sueg(k)
     &    *JJ(Ceg(i)**2.d0/Sueg(k),Ceg(j)**2.d0/Sueg(k))
     &   - deltaKronecker(i, j)
     &   *ZperZ*KK(Ceg(i)**2.d0/Sueg(k),Sueg(l)/Sueg(k))
     &     )
	     enddo
	    enddo
	   enddo  
	 enddo  

        Zpeng23=0.d0
        Zpeng23=Zpeng



C  ***************************************************************
C       DF=1 chargino Boxes 
C  ***************************************************************

	Qin=1
        Qout=2
        Vin=Vtd
        Vout=Vts

	BoxChnn=0.d0
	do j=1,2
	   do i=1,2
	     do k=1,6
	      do l=1,6
	  BoxChnn=BoxChnn+MW**2/12.d0
     & *(H(k,Qin)*Vh(1,i)-gtop*Vin*H(k,6)*Vh(2,i)) 		
     & *(Hh(Qout,k)*V(j,1)-gtop*Vout*Hh(6,k)*V(j, 2))
     &   /Sueg(k)*Ceg(i)*Ceg(j)/Sueg(k)*U(i,1)*Uh(1,j)
     & *JJ3(Ceg(i)**2.d0/Sueg(k),Ceg(j)**2.d0/Sueg(k),Sleg(l)/Sueg(k))
	     enddo
	    enddo
	   enddo  
	   enddo  

	BoxChll=0.d0
	do j=1,2
	   do i=1,2
	     do k=1,6
	      do l=1,3
	  BoxChll=BoxChll-MW**2/12.d0
     & *(H(k,Qin)*Vh(1,i)-gtop*Vin*H(k,6)*Vh(2,i)) 		
     & *(Hh(Qout,k)*V(j,1)-gtop*Vout*Hh(6,k)*V(j, 2))
     &   /Sueg(k)*V(i,1)*Vh(1,j)
     & *KK3(Ceg(i)**2.d0/Sueg(k),Ceg(j)**2.d0/Sueg(k),Sneg(l)/Sueg(k))
	     enddo
	    enddo
	   enddo  
	   enddo  

	Boxnn12=0.d0
	Boxll12=0.d0
	Boxnn12=BoxChnn
	Boxll12=BoxChll

	Qin=1
        Qout=3
        Vin=Vtd
        Vout=Vtb

	BoxChnn=0.d0
	do j=1,2
	   do i=1,2
	     do k=1,6
	      do l=1,6
	  BoxChnn=BoxChnn+MW**2/12.d0
     & *(H(k,Qin)*Vh(1,i)-gtop*Vin*H(k,6)*Vh(2,i)) 		
     & *(Hh(Qout,k)*V(j,1)-gtop*Vout*Hh(6,k)*V(j, 2))
     &   /Sueg(k)*Ceg(i)*Ceg(j)/Sueg(k)*U(i,1)*Uh(1,j)
     & *JJ3(Ceg(i)**2.d0/Sueg(k),Ceg(j)**2.d0/Sueg(k),Sleg(l)/Sueg(k))
	     enddo
	    enddo
	   enddo  
	   enddo  

	BoxChll=0.d0
	do j=1,2
	   do i=1,2
	     do k=1,6
	      do l=1,3
	  BoxChll=BoxChll-MW**2/12.d0
     & *(H(k,Qin)*Vh(1,i)-gtop*Vin*H(k,6)*Vh(2,i)) 		
     & *(Hh(Qout,k)*V(j,1)-gtop*Vout*Hh(6,k)*V(j, 2))
     &   /Sueg(k)*V(i,1)*Vh(1,j)
     & *KK3(Ceg(i)**2.d0/Sueg(k),Ceg(j)**2.d0/Sueg(k),Sneg(l)/Sueg(k))
	     enddo
	    enddo
	   enddo  
	   enddo  

	Boxnn13=0.d0
	Boxll13=0.d0
	Boxnn13=BoxChnn
	Boxll13=BoxChll

	Qin=2
        Qout=3
        Vin=Vts
        Vout=Vtb

	BoxChnn=0.d0
	do j=1,2
	   do i=1,2
	     do k=1,6
	      do l=1,6
	  BoxChnn=BoxChnn+MW**2/12.d0
     & *(H(k,Qin)*Vh(1,i)-gtop*Vin*H(k,6)*Vh(2,i)) 		
     & *(Hh(Qout,k)*V(j,1)-gtop*Vout*Hh(6,k)*V(j, 2))
     &   /Sueg(k)*Ceg(i)*Ceg(j)/Sueg(k)*U(i,1)*Uh(1,j)
     & *JJ3(Ceg(i)**2.d0/Sueg(k),Ceg(j)**2.d0/Sueg(k),Sleg(l)/Sueg(k))
	     enddo
	    enddo
	   enddo
	   enddo

	BoxChll=0.d0
	do j=1,2
	   do i=1,2
	     do k=1,6
	      do l=1,3
	  BoxChll=BoxChll-MW**2/12.d0
     & *(H(k,Qin)*Vh(1,i)-gtop*Vin*H(k,6)*Vh(2,i)) 		
     & *(Hh(Qout,k)*V(j,1)-gtop*Vout*Hh(6,k)*V(j, 2))
     &   /Sueg(k)*V(i,1)*Vh(1,j)
     & *KK3(Ceg(i)**2.d0/Sueg(k),Ceg(j)**2.d0/Sueg(k),Sneg(l)/Sueg(k))
	     enddo
	    enddo
	   enddo  
	   enddo  

	Boxnn23=0.d0
	Boxll23=0.d0
	Boxnn23=BoxChnn
	Boxll23=BoxChll


C  ***************************************************************
C       DF=2 chargino Boxes
C  ***************************************************************

	MW2 = MW**2.0d0

	Qin=1
        Qout=3
        Vin=Vtd
        Vout=Vtb

	Abox=0.d0
	do j=1,2
	   do i=1,2
	    do l=1,6
	     do k=1,6
	Abox=Abox+1.d0/4.d0
     &	 *(H(l,Qin)*Vh(1,j)-gtop*Vin*H(l,6)*Vh(2,j))
     &	 *(H(k,Qin)*Vh(1,i)-gtop*Vin*H(k,6)*Vh(2,i))
     &	 *(Hh(Qout,k)*V(j,1)-gtop*Vout*Hh(6,k)*V(j, 2))
     &	 *(Hh(Qout,l)*V(i,1)-gtop*Vout*Hh(6,l)*V(i, 2))
     &   *(MW2/Sueg(k))*KK3( Ceg(i)**2.d0/Sueg(k),
     &      Ceg(j)**2.d0/Sueg(k), Sueg(l)/Sueg(k) )
	     enddo
	    enddo
	   enddo
	 enddo

        Sbox13=0.0d0
        Sbox13=Abox

 	Qin=2
        Qout=3
        Vin=Vts
        Vout=Vtb

	Abox=0.d0
	do j=1,2
	   do i=1,2
	    do l=1,6
	     do k=1,6
	Abox=Abox+1.d0/4.d0
     &	 *(H(l,Qin)*Vh(1,j)-gtop*Vin*H(l,6)*Vh(2,j))
     &	 *(H(k,Qin)*Vh(1,i)-gtop*Vin*H(k,6)*Vh(2,i))
     &	 *(Hh(Qout,k)*V(j,1)-gtop*Vout*Hh(6,k)*V(j, 2))
     &	 *(Hh(Qout,l)*V(i,1)-gtop*Vout*Hh(6,l)*V(i, 2))
     &   *(MW2/Sueg(k))*KK3( Ceg(i)**2.d0/Sueg(k),
     &      Ceg(j)**2.d0/Sueg(k), Sueg(l)/Sueg(k) )
	     enddo
	    enddo
	   enddo
	 enddo

        Sbox23=0.0d0
        Sbox23=Abox

 	Qin=1
        Qout=2
        Vin=Vtd
        Vout=Vts

	Abox=0.d0
	do j=1,2
	   do i=1,2
	    do l=1,6
	     do k=1,6
	Abox=Abox+1.d0/4.d0
     &	 *(H(l,Qin)*Vh(1,j)-gtop*Vin*H(l,6)*Vh(2,j))
     &	 *(H(k,Qin)*Vh(1,i)-gtop*Vin*H(k,6)*Vh(2,i))
     &	 *(Hh(Qout,k)*V(j,1)-gtop*Vout*Hh(6,k)*V(j, 2))
     &	 *(Hh(Qout,l)*V(i,1)-gtop*Vout*Hh(6,l)*V(i, 2))
     &   *(MW2/Sueg(k))*KK3( Ceg(i)**2.d0/Sueg(k),
     &      Ceg(j)**2.d0/Sueg(k), Sueg(l)/Sueg(k) )
	     enddo
	    enddo
	   enddo
	 enddo

        Sbox12=0.0d0
        Sbox12=Abox


C  ***************************************************************
C       Output varaibles
C  ***************************************************************

c  So far we neglect the chargino photon-penguin ==> Z0=C0

       Z0SM=0.7d0
       Y0SM=1.d0
       X0SM=1.53d0
       S0SM=2.33d0/8.d0
       Peff=-0.39d0*(Vus**4.d0)/(Vtd*Vts)
       P0BSM=2.6d0
       P0KSM=3.d0

       RZ12=0.d0
       RZ13=0.d0
       RZ23=0.d0
       RZ12=(1.d0+(Zpeng12)/(Z0SM*Vtd*(Vts)))
       RZ13=(1.d0+(Zpeng13)/(Z0SM*Vtd*(Vtb)))
       RZ23=(1.d0+(Zpeng23)/(Z0SM*Vts*(Vtb)))

       RX12=0.d0
       RX13=0.d0
       RX23=0.d0
       RX12=(1.d0+(Boxnn12 + Zpeng12)/(X0SM*Vtd*(Vts)))
       RX13=(1.d0+(Boxnn13 + Zpeng13)/(X0SM*Vtd*(Vtb)))
       RX23=(1.d0+(Boxnn23 + Zpeng23)/(X0SM*Vts*(Vtb)))

       RY12=0.d0
       RY13=0.d0
       RY23=0.d0
       RY12=(1.d0+(Boxll12 + Zpeng12)/(Y0SM*Vtd*(Vts)))
       RY13=(1.d0+(Boxll13 + Zpeng13)/(Y0SM*Vtd*(Vtb)))
       RY23=(1.d0+(Boxll23 + Zpeng23)/(Y0SM*Vts*(Vtb)))

       RS12=0.d0
       RS13=0.d0 
       RS23=0.d0
       RS12=(1.d0+Sbox12/(S0SM*Vtd*Vtd*(Vts)*(Vts))) 
       RS13=(1.d0+Sbox13/(S0SM*Vtd*Vtd*(Vtb)*(Vtb))) 
       RS23=(1.d0+Sbox23/(S0SM*Vts*Vts*(Vtb)*(Vtb)))

c---------------------------------------------------------------
c  C9,C10 = Wilson coeff. for b->ll at the e.w. scale, with
c  SM contrib. included
c---------------------------------------------------------------

       C9   = 0.d0
       C10  = 0.d0
       C9   = (alph/(2.d0*pi))*( Y0SM*RY23/sinsqtw - 4.d0*Z0SM*RZ23 )
       C10  = -(alph/(2.d0*pi*sinsqtw))*Y0SM*RY23

       DC9 = 0.d0
       DC10= 0.d0
       DC7 = 0.d0
       DC9 = C9 - (alph/(2.d0*pi))*( Y0SM/sinsqtw - 4.d0*Z0SM )
       DC10 = C10 + (alph/(2.d0*pi*sinsqtw))*Y0SM
       DC7 = C7

       BRXsll = 0.d0
       BRXsll = (1.55d0+35100.d0*(DC9**2.d0+DC10**2.d0)
     &  +0.45d0*(DC7**2.d0)+180.d0*DC9-360.d0*DC10
     &  -0.17d0*DC7-200.d0*DC9*DC10)/(1.55d0)

c---------------------------------------------------------------
c  y7v, y7a = Wilson coeff. for K->pi ll at 1 GeV, with
c  SM contrib. included
c---------------------------------------------------------------

       y7V =0.d0
       y7A =0.d0
       y7V =  +(1.d0/(2.d0*pi))*( Y0SM*RY23/sinsqtw - 4.d0*Z0SM*RZ23
     &         +P0KSM )
       y7A =  -(1.d0/(2.d0*pi*sinsqtw))*Y0SM*RY12

       BRKpnn = 0.d0
       BRKpnn = ((X0SM*RX12+Peff)**2.d0)/((X0SM+Peff)**2.d0)

c---------------------------------------------------------------
c     Mass differences:
c---------------------------------------------------------------

       RDMb = 0.d0
       RDMs = 0.d0
       RDMK = 0.d0
       RDMb = dsqrt(RS13**2.d0)
       RDMK = dsqrt(RS12**2.d0)
       RDMs = dsqrt((RS23+DMsH)**2.d0)

c---------------------------------------------------------------
c     BR(B->ll), complete of H & Z penguins:
c---------------------------------------------------------------

       Psll = 0.d0
       Pdll = 0.d0

       Psll = (3.46d0*(10.d0**(-9.d0)))*(
     &     (1.d0-4.d0*((mmu/Mbs)**2.d0))*((Mbs**2.d0)/(2.d0*mb*mmu)*CSTs
     &      )**2.d0 + ((Mbs**2.d0)/(2.d0*mb*mmu)*CSTs
     &     - Y0SM*Vts*Vtb*RY23 )**2.d0)/((Y0SM*Vts*Vtb)**2.d0)

       Pdll = (2.d0*(10.d0**(-10.d0)))*(
     &     (1.d0-4.d0*((mmu/Mbs)**2.d0))*((Mbs**2.d0)/(2.d0*mb*mmu)*CSTd
     &      )**2.d0 + ( (Mbs**2.d0)/(2.d0*mb*mmu)*CSTd
     &     - Y0SM*Vtd*Vtb*RY13 )**2.d0)/((Y0SM*Vtd*Vtb)**2.d0)


       end subroutine bphysics



C====================================================================
C       Loop functions
C====================================================================

      double precision function G7H(x2)

      double precision x2
      complex*16 G7Hc, x, cspenBF

      x = (dsqrt(x2) - (0d0,1d0) * 10d-10)**2d0

      if (cdabs(x-1.d0).ge.0.001d0) then
      G7Hc = -(4.d0/3.d0)*x*
     .        (
     .        (4.d0/3.d0)*(-3.d0+7.d0*x-2.d0*x*x)/
     .        ((x-1.d0)**3.d0)*cspenBF(1.d0-1.d0/x)
     .                              +
     .        (8.d0-14.d0*x-3.d0*x*x)/
     .        (3.d0*(x-1.d0)**4.d0)*(cdlog(x)**2.d0)
     .                              + 
     .        (2.d0/3.d0)*(-3.d0-x+12.d0*x*x-2.d0*x*x*x)/
     .        ((x-1.d0)**4.d0)*cdlog(x)
     .                              +
     .        (7.d0-13.d0*x+2.d0*x*x)/((x-1.d0)**3.d0)
     .        )

      G7H = dreal(G7Hc)
      else
      G7H = 2.2345d0
      endif

      end

ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc

      double precision function G8H(x2)

      double precision x2
      complex*16 G8Hc, x, cspenBF

      x = (dsqrt(x2) - (0d0,1d0) * 10d-10)**2d0

      if (cdabs(x-1.d0).ge.0.001d0) then

      G8Hc = -(x/3.d0)*
     .        (
     .        (-36.d0+25.d0*x-17.d0*x*x)/(2.d0*(x-1.d0)**3.d0)*
     .          cspenBF(1.d0-1.d0/x)
     .                              +
     .        (19.d0+17.d0*x)/((x-1.d0)**4.d0)*(cdlog(x)**2.d0)
     .                              +
     .        (-3.d0-187.d0*x+12.d0*x*x-14.d0*x*x*x)/
     .        (4.d0*(x-1.d0)**4.d0)*cdlog(x)
     .                              + 
     .        (3.d0/8.d0)*(143.d0-44.d0*x+29.d0*x*x)/
     .        ((x-1.d0)**3.d0)
     .        )

      G8H = dreal(G8Hc)
      else
      G8H = 0.8379d0
      endif

      end

ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc

      double precision function delta7h(x)
      implicit none 
      double precision x

       if (dabs(x-1.d0).ge.0.001d0) then
        delta7h= -(2.d0/9.d0)*x*
     .            (
     .            (21.d0 - 47.d0*x + 8.d0*x*x)/((x-1.d0)**3.d0)+
     .            2.d0*(-8.d0 + 14.d0*x + 3.d0*x*x)*dlog(x)/
     .            ((x-1.d0)**4.d0)
     .            )
       else
        delta7h = -1.2963d0
       endif

      end function

ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc

      double precision function delta8h(x)
      implicit none 
      double precision x

       if (dabs(x-1.d0).ge.0.001d0) then
        delta8h= -(1.d0/3.d0)*x*
     .            (
     .            (81.d0 - 16.d0*x + 7.d0*x*x)/(2.d0*(x-1.d0)**3.d0)-
     .            (19.d0 + 17.d0*x)*dlog(x)/((x-1.d0)**4.d0)
     .            )
       else
        delta8h = -1.11d0
       endif

      end function

CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC

        FUNCTION CSPENBF(Z)
        COMPLEX*16 CSPENBF,W,SUM,Z,U
        REAL*8 RZ,AZ,A1
        REAL*8 B(9)/
     1   0.1666666666666666666666666667D0,
     2  -0.0333333333333333333333333333D0,
     3   0.0238095238095238095238095238D0,
     4  -0.0333333333333333333333333333D0,
     5   0.0757575757575757575757575758D0,
     6  -0.2531135531135531135531135531D0,
     7   1.1666666666666666666666666667D0,
     8  -7.09215686274509804D0         ,
     9  54.97117794486215539D0         /
      Z =Z*DCMPLX(1D0)
      RZ=DREAL(Z)
      AZ=CDABS(Z)
      A1=CDABS(1D0-Z)
      IF(AZ .LT. 1D-20) THEN
        CSPENBF=-CDLOG(1D0-Z)
        RETURN
      END IF
      IF((SNGL(RZ) .EQ. 1.0) .AND. (SNGL(DIMAG(Z)) .EQ. 0.0)) THEN
        CSPENBF=1.64493406684822643D0
        RETURN
      END IF
      IF(RZ.GT.5D-1) GOTO 20
      IF(AZ.GT.1D0) GOTO 10
      W=-CDLOG(1D0-Z)
      SUM=W-0.25D0*W*W
      U=W
      IF(CDABS(U).LT.1D-10) GOTO 2
      DO 1 K=1,9
      U=U*W*W/DFLOAT(2*K*(2*K+1))
      IF(CDABS(U*B(K)/SUM).LT.1D-20) GOTO 2
      SUM=SUM+U*B(K)
 1    CONTINUE
 2    CSPENBF=SUM
      RETURN
10    W=-CDLOG(1D0-1D0/Z)
      SUM=W-0.25D0*W*W
      U=W
      IF(CDABS(U).LT.1D-10) GOTO 12

      DO 11 K=1,9
      U=U*W*W/DFLOAT(2*K*(2*K+1))
      IF(CDABS(B(K)*U/SUM).LT.1D-20) GOTO 12
      SUM=SUM+U*B(K)
11    CONTINUE
12    CSPENBF=-SUM-1.64493406684822643D0-.5D0*CDLOG(-Z)**2
      RETURN
20    IF(A1.GT.1D0) GOTO 30
      W=-CDLOG(Z)
      SUM=W-0.25D0*W*W
      U=W
      IF(CDABS(U).LT.1D-10) GOTO 22
      DO 21 K=1,9
      U=U*W*W/DFLOAT(2*K*(2*K+1))
      IF(CDABS(U*B(K)/SUM).LT.1D-20) GOTO 22
      SUM=SUM+U*B(K)
21    CONTINUE
22    CSPENBF=-SUM+1.64493406684822643D0-CDLOG(Z)*CDLOG(1D0-Z)
      RETURN
30    W=CDLOG(1D0-1D0/Z)
      SUM=W-0.25D0*W*W
      U=W
      IF(CDABS(U).LT.1D-10) GOTO 32
      DO 31 K=1,9
      U=U*W*W/DFLOAT(2*K*(2*K+1))
      IF(CDABS(U*B(K)/SUM).LT.1D-20) GOTO 32
      SUM=SUM+U*B(K)
31    CONTINUE
32    CSPENBF=SUM+3.28986813369645287D0
     *               +.5D0*CDLOG(Z-1D0)**2-CDLOG(Z)*CDLOG(1D0-Z)
50    CONTINUE
      END

c=================================================================

ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
ccccccccccccc   	     Masiero '91             cccccccccccccccc
ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc

    	double precision function f11(x)
      implicit none 
      double precision x

       if (dabs(x-1.d0).ge.0.001d0) then
        f11= (2.d0 + 3.d0*x -6.d0*x**2.d0+x**3.d0+6.d0*x*dLog(x))/
     .       (12.d0*(1.d0 - x)**4.d0)
       else
        f11 = 0.0417d0
       endif

      end function


      double precision function f22(x)
      implicit none
      double precision x
       if (dabs(x-1.d0).ge.0.001d0) then
        f22 = (1.d0-6.d0*x +3.d0*x**2.d0+2.d0*x**3.d0-
     .        6.d0*x**2.d0*dLog(x))/(12.d0*(1.d0 - x)**4.d0)
       else
        f22 = 0.0417d0
       endif

      end function


      double precision function f33(x)
      implicit none
      double precision x
       if (dabs(x-1.d0).ge.0.001d0) then
        f33 = (x**2.d0 +3.d0+2.d0*dLog(x)-4.d0*x)/
     .        (2.d0*(x-1.d0)**3.d0)
       else
        f33 = 0.333d0
       endif

      end function


        double precision function f44(x)
      implicit none
      double precision x
       if (dabs(x-1.d0).ge.0.001d0) then
        f44 = (x**2.d0-1.d0-2.d0*x*dLog(x))/(2.d0*(x-1.d0)**3.d0)
       else
        f44 = 0.167d0
       endif

      end function

cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
ccccccccccccccccccc        end Masiero '91         ccccccccccccccccccccc
cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc


        double precision function f1r(x)
      implicit none 
      double precision  x

        if (dabs(x-1.d0).ge.0.001d0) then
        f1r = ((3.d0*x**2.d0-2.d0*x)*dlog(x))/((1.d0-x)**4.d0) +
     .          (8.d0*x**2.d0+5.d0*x-7.d0)/(6.d0*(1.d0 - x)**3.d0)
        else
        f1r = -0.4166d0
        endif

      end function 


        double precision function f2r(x)
      implicit none 
      double precision  x 

        if (dabs(x-1.d0).ge.0.001d0) then
        f2r = ((-3.d0*x**2.d0+2.d0*x)*dlog(x))/((1.d0-x)**3.d0) +
     .          (-5.d0*x**2.d0+3.d0*x)/(2.d0*(1.d0 - x)**2.d0)
        else
        f2r = -1.167d0
        endif

      end function


        double precision function F3(x)
      implicit none
      double precision x

        if (dabs(x-1.d0).ge.0.001d0) then
        F3 =((2.d0+5.d0*x-x*x)/(6.d0*(1.d0-x)**3.d0))+
     .      (x/((x-1.d0)**4.d0))*dLog(x)
       else
        F3 = 0.0625d0
       endif
      end function

        double precision function F4(x)
      implicit none
      double precision x

       if (dabs(x-1.d0).ge.0.001d0) then
        F4 =((1.d0+x)/(2.d0*(1.d0-x)**2.d0))+
     .      (x/((1.d0-x)**3.d0))*dLog(x)
       else
        F4 = 0.1667d0
       endif
      end function


      double precision function j6(x)
      implicit none
      double precision x

        if (dabs(x-1.d0).ge.0.001d0) then
        j6 = ((2.d0*(1.d0+x)*dlog(x))/((x-1.d0)**5.d0)-
     .       (1.d0+10.d0*x+x*x)/(3.d0*x*(x-1.d0)**4.d0))
        else
        j6 = -0.0333d0
        endif

      end function

cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc

      double precision function F7pr(x) 
      implicit none
      double precision x 

        if (dabs(x-1.d0).ge.0.001d0) then
        F7pr = ((7.d0-13.d0*x)/(12.d0*(1.d0-x)**3.d0))+
     .  ((-3.d0*x**2.d0-2.d0*x+2.d0)/(6.d0*(x-1.d0)**4.d0))*dLog(x)
        else
        F7pr = -0.06945d0
        endif

      end function

cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc

      double precision function F8pr(x) 
      implicit none
      double precision x 

        if (dabs(x-1.d0).ge.0.001d0) then
        F8pr = ((3.d0+x)/(4.d0*(1.d0-x)**3.d0))+
     .  ((-x+1.d0+(2.d0*x+1.d0)*dLog(x))/(2.d0*(x-1.d0)**4.d0))
        else
        F8pr = -0.041672d0
        endif

      end function

cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc

      double precision function F7(x) 
      implicit none
      double precision x 

        if (dabs(x-1.d0).ge.0.001d0) then
        F7 =(x*(3.d0-5.d0*x)/(12.d0*(x-1.d0)**2.d0))+
     .      (x*(3.d0*x-2.d0)/(6.d0*(x-1.d0)**3.d0))*dLog(x)
       else
        F7 = -0.1944d0
       endif

      end function

cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc

      double precision function F8(x)
      implicit none
      double precision x
        if (dabs(x-1.d0).ge.0.001d0) then

        F8 =(x*(3.d0-x)/(4.d0*(x-1.d0)**2.d0))-
     .      (x/(2.d0*(x-1.d0)**3.d0))*dLog(x)
        else
        F8 = -0.1667d0
        endif

      end function

cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc

       double precision function f2(x)
       implicit none
       double precision x 

       if (dabs(x-1.d0).ge.0.001d0) then
        f2 = (1.d0/(x-1.d0))*(x*dLog(x)/(x-1.d0)-1.d0)
       else
        f2 = 1.d0/2.d0
       endif

       end function

cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc

       double precision function I3(x,y)
      implicit none
      double precision x,y

       if(dabs(x-1.d0).ge.0.001d0.and.dabs(y-1.d0).ge.0.001d0.and.
     .    dabs(x-y).ge.0.001d0)then

        I3 =  (x*y*dLog(x/y)+y*dLog(y)-x*dLog(x))/
     .        ((x-y)*(1.d0-x)*(1.d0-y))

       elseif(dabs(x-1.d0).ge.0.001d0.and.dabs(y-1.d0).ge.0.001d0.and.
     .        dabs(x-y).le.0.001d0)then

        I3 = -(1.d0/(1.d0-x))*(dLog(x)/(1.d0-x)+1.d0)

       elseif(dabs(x-1.d0).le.0.001d0.and.dabs(y-1.d0).ge.0.001d0)then

        I3 = -(1.d0/(y-1.d0))*(1.d0+y*dLog(y)/(1.d0-y))

       elseif(dabs(y-1.d0).le.0.001d0.and.dabs(x-1.d0).ge.0.001d0)then

        I3 = -(1.d0/(x-1.d0))*(1.d0+x*dLog(x)/(1.d0-x))

       else
        I3 = 1.d0/2.d0
       endif

      end function

cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc

      double precision function F17(x)
      implicit none
      double precision x

        if (dabs(x-1.d0).ge.0.001d0) then
        F17 =((x*(7.d0-5.d0*x-8.d0*x*x))/(24.d0*(x-1.d0)**3.d0))+
     .      (x*x*(3.d0*x-2.d0)/(4.d0*(x-1.d0)**4.d0))*dLog(x)
        else
        F17 = -0.104d0
        endif

      end function

cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc

        double precision function F18(x)
      implicit none
      double precision x

        if (dabs(x-1.d0).ge.0.001d0) then
        F18 =((x*(2.d0+5.d0*x-x*x))/(8.d0*(x-1.d0)**3.d0))-
     .      ((x*x*3.d0)/(4.d0*(x-1.d0)**4.d0))*dLog(x)
        else
        F18 = -0.0625d0
        endif

      end function

cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc

      double precision function F37(x) 
      implicit none
      double precision x 

       if (dabs(x-1.d0).ge.0.001d0) then
        F37 =((5.d0-7.d0*x)/(6.d0*(x-1.d0)**2.d0))+
     .      (x*(3.d0*x-2.d0)/(3.d0*(x-1.d0)**3.d0))*dLog(x)
       else
        F37 = 0.444d0
       endif
      end function

cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc

        double precision function F38(x)
      implicit none
      double precision x

       if (dabs(x-1.d0).ge.0.001d0) then
        F38 =((1.d0+x)/(2.d0*(x-1.d0)**2.d0))-
     .       (x/((x-1.d0)**3.d0))*dLog(x)
       else
        F38 = 0.167d0
       endif
      end function

cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc

      double precision function H2(x,y)
      implicit none
      double precision x,y

       if(dabs(x-1.d0).ge.0.0001d0.and.dabs(y-1.d0).ge.0.0001d0.and.
     .    dabs(x-y).ge.0.0001d0)then

        H2 =  (x*y*dLog(x/y)+y*dLog(y)-x*dLog(x))/
     .        ((x-y)*(1.d0-x)*(1.d0-y))

       elseif(dabs(x-1.d0).ge.0.0001d0.and.dabs(y-1.d0).ge.0.0001d0
     .        .and.dabs(x-y).le.0.0001d0)then

        H2 = (1.d0/(x-1.d0))*(dLog(x)/(1.d0-x)+1.d0)

       elseif(dabs(x-1.d0).le.0.0001d0.and.dabs(y-1.d0).ge.0.0001d0
     .       .and.dabs(y-x).ge.0.0001d0)then

        H2 = (1.d0/(1.d0-y))*(1.d0+y*dLog(y)/(1.d0-y))

       elseif(dabs(y-1.d0).le.0.0001d0.and.dabs(x-1.d0).ge.0.0001d0
     .        .and.dabs(y-x).ge.0.0001d0)then

        H2 = (1.d0/(1.d0-x))*(1.d0+x*dLog(x)/(1.d0-x))

       else
        H2 = 1.d0/2.d0
       endif

      end function

ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc

        double precision function H17(x) 
      implicit none
      double precision x 

       if (dabs(x-1.d0).ge.0.001d0) then
        H17= (-3.d0*x**2.d0+2.d0*x)*dlog(x)/(6.d0*(1.d0-x)**4.d0)+
     .       (7.d0-5.d0*x-8.d0*x**2.d0)/(36.d0*(1.d0-x)**3.d0)
       else
        H17 = 5.d0/72.d0
       endif
      end function

ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc

        double precision function H27(x) 
      implicit none
      double precision x 

       if (dabs(x-1.d0).ge.0.001d0) then
        H27=(-3.d0*x**2.d0+2.d0*x)*dlog(x)/(3.d0*(1.d0-x)**3.d0)+
     .      (3.d0*x-5.d0*x**2.d0)/(6.d0*(x-1.d0)**2.d0)
       else
        H27 = -7.d0/18.d0
       endif
      end function

ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc

        double precision function H18(x)
      implicit none
      double precision x

       if (dabs(x-1.d0).ge.0.001d0) then
        H18 = x*dlog(x)/(2.d0*(1.d0-x)**4.d0)+
     .       (2.d0+5.d0*x-x**2.d0)/(12.d0*(1.d0-x)**3.d0)
       else
        H18 = 1.d0/24.d0
       endif
      end function

cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc

        double precision function H28(x)
      implicit none
      double precision x

       if (dabs(x-1.d0).ge.0.001d0) then
        H28 = x*dlog(x)/((1.d0-x)**3.d0)+
     .       (3.d0*x-x**2.d0)/(2.d0*(x-1.d0)**2.d0)
       else
        H28 = -1.d0/3.d0
       endif
      end function

ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc

        double precision function H58(x) 
      implicit none
      double precision x 

       if (dabs(x-1.d0).ge.0.001d0) then
        H58 = (9.d0*x**2.d0-x)*dlog(x)/(16.d0*(1.d0-x)**4.d0)+
     .       (-11.d0+40.d0*x+19.d0*x**2.d0)/(96.d0*(1.d0-x)**3.d0)
       else
        H58 = -5.d0/96.d0
       endif
      end function

cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc

        double precision function H68(x)
      implicit none
      double precision x

       if (dabs(x-1.d0).ge.0.001d0) then
        H68 = (9.d0*x**2.d0-x)*dlog(x)/(8.d0*(1.d0-x)**3.d0)+
     .       (-5.d0+13.d0*x)/(8.d0*(1.d0-x)**2.d0)
       else
        H68 = -19.d0/48.d0
       endif
      end function

cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc


C ****************************

       	double precision function kk(y,z)
	implicit none 
	double precision  x,y,z 

c like 3 arguments (x,y,z) but x=1

	    x=1.d0

          if(dabs(y/x-1.d0).le.(1.D-8)) then
	    y=x
	  endif
          if(dabs(z/x-1.d0).le.(1.D-8)) then
	    z=x
	  endif
	  if(dabs(z/y-1.d0).le.(1.D-8)) then
	    z=y
	  endif


        if(x.eq.y.and.x.eq.z) then
         kk = 1.5d0
         goto 556
        endif
        if(x.eq.y) then
         kk = (1.d0 - z + z**2*dlog(z))/(-1.d0 + z)**2
         goto 556
        endif
        if(x.eq.z) then
         kk = (1.d0 - y + y**2*dlog(y))/(-1.d0 + y)**2
         goto 556
        endif
        if(y.eq.z) then
         kk = (y*(-1.d0 + y + (-2.d0 + y)*dlog(y)))/(-1.d0 + y)**2
         goto 556
        endif

	kk=((y**2*dlog(y))/(-1.d0+y)-(z**2*dlog(z))/(-1.d0+z))/(y-z)


556        continue	

	end function 

       	double precision function jj(y,z)
	implicit none 
	double precision  x,y,z 

c like 3 arguments (x,y,z) but x=1

	    x=1.d0

          if(dabs(y/x-1.d0).le.(1.D-8)) then
	    y=x
	  endif
          if(dabs(z/x-1.d0).le.(1.D-8)) then
	    z=x
	  endif
	  if(dabs(z/y-1.d0).le.(1.D-8)) then
	    z=y
	  endif


        if(x.eq.y.and.x.eq.z) then
         jj = 0.5d0
         goto 556
        endif
        if(x.eq.y) then
         jj = (1.d0 - z + z*dlog(z))/(-1.d0 + z)**2
         goto 556
        endif
        if(x.eq.z) then
         jj = (1.d0 - y + y*dlog(y))/(-1.d0 + y)**2
         goto 556
        endif
        if(y.eq.z) then
         jj = (-1.d0+y-dlog(y))/(-1.d0 + y)**2
         goto 556
        endif

	jj=((y*dlog(y))/(-1.d0+y)-(z*dlog(z))/(-1.d0+z))/(y-z)


556        continue

	end function

C ****************************

       	double precision function kk3(x,y,z)
	implicit none 
	double precision  x,y,z,t,u
        integer p

        p=0

        if((dabs(y/x-1.d0).le.(1.D-5)).and.(dabs(z/x-1.d0).le.(1.D-5))) 
     &   then
          if(dabs(x-1.d0).le.(1.D-5)) then
	   kk3=1.0d0/3.0d0
           goto 599
	  endif
           kk3=(x**2.d0-4.d0*x+3.d0+2.d0*dlog(x))/(2.d0*x**3.d0
     &             -6.d0*x**2.d0+6.d0*x-2.d0)
          goto 599
        endif

        if(dabs(y/x-1.d0).le.(1.D-5)) then
           p=2
	   t=x
           u=z
        endif

        if(dabs(y/z-1.d0).le.(1.D-5)) then
           p=2
	   t=z
           u=x
        endif

        if(dabs(x/z-1.d0).le.(1.D-5)) then
           p=2
	   t=z
           u=y
        endif

        if(p.eq.2)then
          if(dabs(t-1.d0).le.(1.D-5)) then 
           kk3=(-1.d0+2.d0*u**2.d0*dlog(u)-3.d0*u**2.d0+4.d0*u)/(
     &           2.d0*u**3.d0-6.d0*u**2.d0+6.d0*u-2.d0)
           goto 599
	  endif
          if(dabs(u-1.d0).le.(1.D-5)) then
           kk3=(t**2.d0-2.d0*dlog(t)*t-1.d0)/(t**3.d0-3.d0*t**2.d0
     &          +3.d0*t-1.d0)
           goto 599
	  endif
            kk3=(t**2.d0-t**2.d0*u**2.d0+t**2.d0*dlog(t)+t*u**2.d0
     &      -2.d0*u**2.d0*dlog(u)*t+u**2.d0*dlog(u)*t**2.d0+t**3.d0*u
     &      -t*u-t**2.d0*dlog(t)*u**2.d0-t**3.d0+dlog(u)*u**2.d0
     &      +2.d0*dlog(t)*u**2.d0*t-2.d0*dlog(t)*t*u)/(t**4.d0*u
     &      -2.d0*t**3.d0*u**2.d0+t**2.d0*u**3.d0-t**4.d0
     &      +3.d0*t**2.d0*u**2.d0-2.d0*t*u**3.d0+2.d0*t**3.d0
     &      -3.d0*t**2.d0*u+u**3.d0-t**2.d0+2.d0*t*u-u**2.d0)
           goto 599
        endif

        if(dabs(x-1.d0).le.(1.D-5)) then
           p=1
	   t=y
           u=z
        endif

        if(dabs(y-1.d0).le.(1.D-5)) then
           p=1
	   t=z
           u=x
        endif

        if(dabs(z-1.d0).le.(1.D-5)) then
           p=1
	   t=x
           u=y
        endif

        if(p.eq.1)then
         kk3=(-t+u+u**2.d0*dlog(u)*t**2.d0+t**2.d0-u**2.d0
     &   +2.d0*t**2.d0*dlog(t)*u+dlog(u)*u**2.d0-t**2.d0*dlog(t)*u**2.d0
     &   -t**2.d0*dlog(t)-2.d0*u**2.d0*dlog(u)*t+t*u**2.d0-t**2.d0*u)/(
     &   -t**3.d0*u**2.d0+t**2.d0*u**3.d0+2.d0*t**3.d0*u-t**3.d0
     &   -3.d0*t**2.d0*u-2.d0*t*u**3.d0+3.d0*t*u**2.d0+2.d0*t**2.d0
     &   +u**3.d0-2.d0*u**2.d0-t+u)
         goto 599
        endif

        kk3=((x**2.d0*dlog(x)/(x-1.d0)-z**2.d0*dlog(z)/(z-1.d0))/(x-z)
     &      -(y**2.d0*dlog(y)/(y-1.d0)-z**2.d0*dlog(z)/(z-1.d0))
     &       /(y-z))/(x-y)

 599    continue	

	end function 

C *****************

       	double precision function jj3(x,y,z)
	implicit none 
	double precision  x,y,z,t,u
        integer p

        p=0

        if((dabs(y/x-1.d0).le.(1.D-5)).and.(dabs(z/x-1.d0).le.(1.D-5))) 
     &   then
          if(dabs(x-1.d0).le.(1.D-5)) then
	   jj3=-1.d0/6.d0
           goto 599
	  endif
           jj3=(1.d0 - x**2 + 2*x*dLog(x))/(2.d0*(-1.d0 + x)**3*x)
          goto 599
        endif

        if(dabs(y/x-1.d0).le.(1.D-5)) then
           p=2
	   t=x
           u=z
        endif
    
        if(dabs(y/z-1.d0).le.(1.D-5)) then
           p=2
	   t=z
           u=x
        endif    

        if(dabs(x/z-1.d0).le.(1.D-5)) then
           p=2
	   t=z
           u=y
        endif

        if(p.eq.2)then
          if(dabs(t-1.d0).le.(1.D-5)) then 
           jj3=(1.d0 - u**2 + 2.d0*u*dLog(u))/(2.d0*(-1.d0 + u)**3)
	   goto 599
	  endif
          if(dabs(u-1.d0).le.(1.D-5)) then
           jj3= (-2.d0 + 2*t - (1.d0 + t)*dLog(t))/(-1.d0 + t)**3
	   goto 599
	  endif
            jj3=(-((t**2 - u)*(-1.d0 + u)*dLog(t)) + 
     -    (-1.d0 + t)*
     -     ((t - u)*(-1.d0 + u) + 
     -       (-1.d0 + t)*u*dLog(u)))/
     -  ((-1.d0 + t)**2*(t - u)**2*(-1.d0 + u))
	    goto 599
        endif

        if(dabs(x-1.d0).le.(1.D-5)) then
           p=1
	   t=y
           u=z
        endif
    
        if(dabs(y-1.d0).le.(1.D-5)) then
           p=1
	   t=z
           u=x
        endif    

        if(dabs(z-1.d0).le.(1.D-5)) then
           p=1
	   t=x
           u=y
        endif

        if(p.eq.1)then
         jj3=(t*(-1.d0 + u)**2*dLog(t) -
     -    (-1.d0 + t)*
     -     (-((t - u)*(-1.d0 + u)) + 
     -       (-1.d0 + t)*u*Log(u)))/
     -  ((-1.d0 + t)**2*(t - u)*(-1.d0 + u)**2)
	 goto 599
        endif

        jj3=(((x*dLog(x))/(-1.d0 + x) -
     -       (z*dLog(z))/(-1.d0 + z))/(x - z) -
     -    ((y*dLog(y))/(-1.d0 + y) -
     -       (z*dLog(z))/(-1.d0 + z))/(y - z))/
     -  (x - y)

 599    continue

	end function






