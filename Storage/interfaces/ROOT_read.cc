#include <sstream>
#include <iostream>
#include <cstdlib>

#include "TFile.h"
#include "TTree.h"
#include "TLeaf.h"

//static bool first = true;

static TFile* inputFile;
static TTree* tree;

extern "C" 
{
  
  
    //____________________________________________________________________
    void rootopen( char* infile )
    {
//      outputFile = TFile::Open(outfile,"RECREATE");
//      tree = new TTree("tree","MasterCode tree");
    inputFile = new TFile(infile,"UPDATE");  
// Tree
    tree = (TTree*)f->Get("tree");
// number of entries
    int nentries = t->GetEntries();
// branch to loop over
    Int_t nTotVars = t->GetLeaf("vars")->GetLen();
//    double* invars = new double[nTotVars];
//    t->SetBranchAddress("vars",invars);
    }


    //____________________________________________________________________
    void rootclose()
    {
        // this function relies on rootopen to be called
//      tree->Write();dd
      inputFile->Close();
    }


    //____________________________________________________________________
//    void rootwrite(  double* vars, int nvars )
    void rootread(  double* vars, int entry )
    {
        tree->GetEntry(entry);
        tree->SetBranchAddress("vars",vars);
    }
}
      // Define tree the first time
//      if ( first ) {
//            first = false;
//            std::ostringstream varName;
//            varName << "vars[" << nvars << "]/D";
//            inputFile->cd();
//            tree->SetAutoSave(500000); // Save every ~1000 events
//            tree->Branch("vars",vars,varName.str().c_str());
//      } 
//      else {
//            // Check number of variables
//            int cnVars = tree->GetLeaf("vars")->GetLen();
//            tree->SetBranchAddress("vars",vars);
//            if ( cnVars != nvars ) {
//                std::cerr << "*** ERROR *** ("__FILE__" - " << __LINE__ << "): "
//                          << "expecting " << cnVars << " variables, got " << nvars << std::endl;
//                rootclose();
//                exit(-1);
//        }
//      }
//      tree->Fill();
