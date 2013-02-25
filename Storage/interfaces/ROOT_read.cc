#include <sstream>
#include <iostream>
#include <cstdlib>

#include "TFile.h"
#include "TTree.h"
#include "TLeaf.h"

static TFile* inputFile;
static TTree* tree;

extern "C" 
{
    //____________________________________________________________________
    void rootopen( char* infile )
    {
        inputFile = new TFile(infile,"UPDATE");  
        tree = (TTree*)inputFile->Get("tree");
    }
    //____________________________________________________________________
    int getNvars(){
        return tree->GetLeaf("vars")->GetLen();
    }
    //____________________________________________________________________
    int getEntries(){
        return tree->GetEntries();
    }
    //____________________________________________________________________
    void rootclose()
    {
      inputFile->Close();
    }
    //____________________________________________________________________
    void rootread(  double* vars, int entry )
    {
        tree->SetBranchAddress("vars",vars);
        tree->GetEntry(entry);
    }
}
