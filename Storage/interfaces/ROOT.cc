//
// Fortran interface to ROOT I/O
//
// $Id: root_interface.cc,v 1.1 2008/09/30 13:58:09 fronga Exp $

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
    void rootwrite(  double* vars, int nvars )
    {
      // Define tree the first time
      if ( first ) {
            first = false;
            std::ostringstream varName;
            varName << "vars[" << nvars << "]/D";
            outputFile->cd();
            tree->SetAutoSave(500000); // Save every ~1000 events
            tree->Branch("vars",vars,varName.str().c_str());
      } 
      else {
            // Check number of variables
            int cnVars = tree->GetLeaf("vars")->GetLen();
            tree->SetBranchAddress("vars",vars);
            if ( cnVars != nvars ) {
                std::cerr << "*** ERROR *** ("__FILE__" - " << __LINE__ << "): "
                          << "expecting " << cnVars << " variables, got " << nvars << std::endl;
                rootclose();
                exit(-1);
        }
      }
      tree->Fill();
    }
}
