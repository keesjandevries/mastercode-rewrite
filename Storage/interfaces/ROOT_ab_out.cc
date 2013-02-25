#include <sstream>
#include <iostream>
#include <cstdlib>

#include "TFile.h"
#include "TTree.h"
#include "TLeaf.h"

static bool first = true;

static TFile* outputFile;
static TTree* tree;

extern "C" 
{
  
  
    //____________________________________________________________________
    void rootopen( char* outfile )
    {
      outputFile = TFile::Open(outfile,"RECREATE");
      tree = new TTree("tree","MasterCode tree");
    }


    //____________________________________________________________________
    void rootclose()
    {
        // this function relies on rootopen to be called
      tree->Write();
      outputFile->Close();
    }


    //____________________________________________________________________
    void rootwrite(  double* invars, double* outvars, int nvars )
    {
        // Define tree the first time
        if ( first ) {
              first = false;
              std::ostringstream invarName;
              std::ostringstream outvarName;
              invarName << "invars[" << nvars << "]/D";
              outvarName << "outvars[" << nvars << "]/D";
              outputFile->cd();
              tree->SetAutoSave(500000); // Save every ~1000 events
              tree->Branch("invars",invars,invarName.str().c_str());
              tree->Branch("outvars",outvars,outvarName.str().c_str());
        } 
        else {
              tree->SetBranchAddress("invars",invars);
              tree->SetBranchAddress("outvars",outvars);
        }
        tree->Fill();
    }
}
