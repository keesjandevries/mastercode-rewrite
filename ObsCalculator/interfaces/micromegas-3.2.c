#include"../sources/micromegas.h"
#include"../sources/micromegas_aux.h"
#include"lib/pmodel.h"

//NOTE: This is entirely based on MSSM/main.c .
//Howerer everything that is not needed for calculation of Omega and sigma_p_si is stripped off

int main(int argc,char** argv){   
    int err;
    char cdmName[10];
    int spin2, charge3,cdim;

    ForceUG=0;  /* to Force Unitary Gauge assign 1 */

    // Check number of arguments
    if(argc <2) 
    {  printf("The program needs one argument:the name of SLHA input file.\n"
             "Example: ./main suspect2_lha.out \n");
       exit(1);
    }  
      
    // Read in slha
    err=lesHinput(argv[1]);
    if(err) exit(2);
     
    // Check for slha warnings
    slhaWarnings(stdout);
    if(err) exit(1);

    // Sort Particles
    err=sortOddParticles(cdmName);
    if(err) { printf("Can't calculate %s\n",cdmName); return 1;}

    qNumbers(cdmName,&spin2, &charge3, &cdim);
  
    // This shouldn't happen
    if(charge3) { printf("Dark Matter has electric charge %d/3\n",charge3); exit(1);}
    if(cdim!=1) { printf("Dark Matter is a color particle\n"); exit(1);}
    if(strcmp(cdmName,"~o1")) printf(" ~o1 is not CDM\n"); 
                             
    // Calculation of Omega, i.e. dark matter density
    int fast=1;
    double Beps=1.E-5;
    double Omega,Xf;   
    Omega=darkOmega(&Xf,fast,Beps);
    // print value
    printf("[\"MastercodeTag\", \"Omega\", %f  ]\n",Omega);

    // Calculation of sigma_p_si
    double pA0[2],pA5[2],nA0[2],nA5[2];
    double Nmass=0.939; /*nucleon mass*/
    double SCcoeff;        
    nucleonAmplitudes(FeScLoop, pA0,pA5,nA0,nA5);
    SCcoeff=4/M_PI*3.8937966E8*pow(Nmass*Mcdm/(Nmass+ Mcdm),2.);
    double proton_sigma_si=SCcoeff*pA0[0]*pA0[0];
    // print value
    printf("[\"MastercodeTag\", \"sigma_p_si\", %e ] \n",proton_sigma_si);
    // if all went fine, then return 0 
    return 0;
}
