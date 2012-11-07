      program main 

      IMPLICIT NONE

#include "SLHA.h"

      integer error
      DOUBLE COMPLEX slhadata(nslhadata)
      DOUBLE PRECISION BRBSG,BRKPNN,RDMB,RDMS,RDMK,BRXSLL,
     &     BRBTN,BRKL2,PSLL,PDLL,PLLSAPX

      call slharead(error,slhadata,"ss.slha",0)
      if(error.ne.0) stop "Read error"

      call BPHYSICSINTERFACE( ERROR, slhadata, BRbsg,BRKpnn, RDMb,RDMs,RDMK,BRXsll,
     &     BRbtn,BRKl2,Psll,Pdll,Pllsapx )
      end

