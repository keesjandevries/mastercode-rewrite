//Jad Marrouche, Sep 2011, jad@cern.ch
#include <fstream>
#include <iostream>
#include "TTree.h"
#include "TFile.h"
#include "TMath.h"
#include "SLHAblock.hh"
#include "SLHAfile.hh"

int main(void)
{
  //open file containing the ttree
  TFile *ifile = new TFile("files/slhatree.root");

  //Tree in input file
  TTree *itree = (TTree *)ifile->Get("slhatree");

  //SLHAjm * testing = new SLHAjm(); //initialise the class object (for blocks)
  SLHAfile * testing = new SLHAfile(); //initialise the class object (for the file)
  //SLHAline test; //initialise the line object (for lines)

  //initialise the branch and load it from the tree
  itree->SetBranchAddress("file", &testing);
  //itree->GetBranch("bla")->SetFile("outputfileslha.root");

  int nentries = itree->GetEntries();
  
  //Loop over entries in the input tree
  for (Int_t i = 0; i < nentries; i++) {
    itree->GetEntry(i);
    std::cout << (*testing);
  }

  return 0;

}
