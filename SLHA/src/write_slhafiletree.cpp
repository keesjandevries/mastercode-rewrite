//Jad Marrouche, Sep 2011, jad@cern.ch
#include <fstream>
#include <iostream>
#include "TTree.h"
#include "TFile.h"
#include "TMath.h"
#include "SLHAblock.hh"
#include "SLHAfile.hh"

int main(int argc, char *argv[])
{

  SLHAfile file;
  TFile *ofile = new TFile("files/slhatree.root","RECREATE");
  TTree *newtree = new TTree("slhatree","SLHA file tree");
  newtree->Branch("file", &file);

  //pass the list of slha output files as command line arguments to store in the root tree
  for (int n = 1; n < argc; n++) {
    std::string filename(argv[n]);
    if(file.ReadFile(filename)) newtree->Fill();
    else std::cout << "cp " << filename << " ~/public_html/SLHABADfiles" << std::endl;
  }
  // Make sure ROOT knows we want to write to the output file
  ofile->cd();

  // Write the tree to the file
  newtree->Write();

  // Close the output file
  ofile->Close();


  return 0;

}
