//Jad Marrouche, Sep 2011, jad@cern.ch
#ifndef __SLHAFILE__
#define __SLHAFILE__

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm> //for capitalisation in the ReadFile function
#include <sstream>

#include "SLHAblock.hh"

class SLHAfile {
  
public:
  SLHAfile();
  SLHAfile(std::string); //constructor which reads file name of SLHA file
  ~SLHAfile();
  void AddBlock(SLHAblock);
  bool ReadFile(std::string, bool mVerbose=false);
  bool ReadStream(std::istream&, bool mVerbose=false);
  unsigned int size() const; //read-only
  SLHAblock GetBlock(unsigned int) const; //read-only
  void clear();
  SLHAblock operator[](std::string) const; //read-only - to allow easy search of blocknames

  // for softsusy interface
  std::stringstream& streamer(std::stringstream& ss);
private:
  std::vector<SLHAblock> mblocks; //the vector containing the collection of blocks

};

//for pretty printing!
std::ostream &operator<<(std::ostream &os, const SLHAfile &file);
std::istream &operator>>(std::istream &is, SLHAfile &file);

#endif
