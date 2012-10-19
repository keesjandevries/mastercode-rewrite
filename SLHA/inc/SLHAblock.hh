//Jad Marrouche, Sep 2011, jad@cern.ch
#ifndef __SLHABLOCK__
#define __SLHABLOCK__

#include <iostream>
#include <string>
#include <vector>
#include "SLHAline.hh"

class SLHAblock {
  
public:
  SLHAblock();
  SLHAblock(std::string); //constructor setting the blockname directly
  ~SLHAblock();
  void SetBlockName(std::string);
  void AddLine(SLHAline);
  void clear(); //resets the private members
  unsigned int size() const; //read-only
  SLHAline FindComment(std::string) const; //read-only
  SLHAline FindIndex(std::pair<uint32_t, uint32_t>, uint32_t) const; //read-only
  std::string GetBlockName() const; //read-only
  SLHAline GetLine(unsigned int) const; //read-only

private:
  std::vector<SLHAline> mlines; //the vector containing the SLHAline objects
  std::string mblockname; //the name of the block

};

//overload the << to allow for pretty printing!
std::ostream &operator<<(std::ostream &os, const SLHAblock &block);

#endif
