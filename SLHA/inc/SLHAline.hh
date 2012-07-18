//Jad Marrouche, Sep 2011, jad@cern.ch
#ifndef __SLHALINE__
#define __SLHALINE__
#include <iostream>
#include <string>
#include "Rtypes.h"

//we include Rtypes.h which is a bunch of ROOT typedefs to ensure
//we always get the same number of bits for int/long etc
//UInt_t = 32 bits unsigned
//Double_t = 64 bits signed
//Long_t = 64 bits signed

//the structure of the indexinfo: 32 bits, unsigned int
// 2 bits | 6 bits | 24 bits
// 11 | 11 1111 | 1111 1111 1111 1111 1111 1111
// the top 2 bits (0-3) determine how many indices the line has
// the next 6 bits (0-63) are the secondary index for e.g. matrices
// the last 24 bits (0-0xFFFFFF) represent the primary index and account
// for the PDG indices which can be e.g. 9331122 for pentaquarks...

class SLHAline {

 public:
  SLHAline();
  ~SLHAline();

  UInt_t GetNumIndices() const; //since read-only function
  void SetNumIndices(Long_t);

  UInt_t GetIndex1() const; //read-only
  void SetIndex1(Long_t);

  UInt_t GetIndex2() const; //read-only
  void SetIndex2(Long_t);
  
  UInt_t GetFullIndex() const; //read-only
  void SetFullIndex(Long_t); 

  Double_t GetValue() const; //read-only
  void SetValue(Double_t);

  std::string GetComment() const; //read-only
  void SetComment(std::string);

  //we use 64 bits for all Set Functions in order to be able to catch cases
  //where a user/program may pass > 32 bits etc OR a value < 0
  //Case 1: This would cause the bottom bits to be cut off without warning!
  //Case 2: If the signature was an unsigned int, the compiler would cast
  //a negative number to a UInt which might put it in the range since
  // e.g. -1 = 2^n - 2
  //At least this provides a way to catch such cases

 private:
  UInt_t mIndexInfo;
  Double_t mValue;
  std::string mComment;
};

//define the ostream for pretty printing!
std::ostream &operator<<(std::ostream &os, const SLHAline &sl);

#endif
