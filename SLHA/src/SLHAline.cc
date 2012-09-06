//Jad Marrouche, Sep 2011, jad@cern.ch
#include "SLHAline.hh"

SLHAline::SLHAline() {mIndexInfo=0;mValue=0.0;mComment="";}
SLHAline::~SLHAline() {}

UInt_t SLHAline::GetFullIndex() const {
  return mIndexInfo; //method to get the full index
}

void SLHAline::SetFullIndex(Long_t index) {
  //we take 64 bits in order to be able to warn if number is >32 bits or <0
  //otherwise bottom bits are stripped off without warning
  if(index >=0 && index <= 0xFFFFFFFF) {
    mIndexInfo = index; //set index
  } else { 
    std::cout << "The indexinfo must be UInt_32. You gave " << index << std::endl;
    throw 0;   
  }
  return;
}

UInt_t SLHAline::GetNumIndices() const {
  //mask off the top 2 bits and shift them to return 
  //a number between 0-3 inclusive
  return ((mIndexInfo & 0xC0000000) >> 30);
}

void SLHAline::SetNumIndices(Long_t numindices) {
  //do some range checking on the index passed to prevent debugging nightmares
  if(numindices <= 0x3 && numindices >= 0 ) {
    //first, copy the index info to a temp long
    UInt_t newindexinfo = mIndexInfo;
    newindexinfo = (newindexinfo & 0x3FFFFFFF); //mask off the top 2 bits
    UInt_t numindex = numindices << 30; //move the numindices to the top 2 bits
    newindexinfo = newindexinfo | numindex; //merge with existing info via OR
    mIndexInfo = newindexinfo; //set new index
  } else {
    std::cout << "The number of indices must be between 0-3 inclusive. You gave " << numindices << std::endl;
    throw 0;
  }
  return;

}

UInt_t SLHAline::GetIndex1() const {
  return (mIndexInfo & 0x00FFFFFF); //method to return Index1 from 32 bits
}

void SLHAline::SetIndex1(Long_t index1) {
  //do some range checking on the index passed to prevent debugging nightmares
  if(index1 <= 0xFFFFFF && index1 >= 0 ) {
    //first, copy the index info to a temp long
    UInt_t newindexinfo = mIndexInfo;
    newindexinfo = (newindexinfo & 0xFF000000); //mask off the bottom 20 bits
    newindexinfo = newindexinfo | index1; //logical OR with passed index
    mIndexInfo = newindexinfo; //set new index
    if( this->GetNumIndices() == 0 ){
        this->SetNumIndices(1);
    }
  } else {
    std::cout << "The range for index1 must be between 0 and 0xFFFFFF inclusive. You gave " << index1 << std::endl;
    throw 0;
  }

  return;
}

UInt_t SLHAline::GetIndex2() const {
  return ((mIndexInfo & 0x3F000000) >> 24); //method to return Index2 from 32 bits
}

void SLHAline::SetIndex2(Long_t index2) {
  //do some range checking on the index passed to prevent debugging nightmares
  if(index2 <= 0x3F && index2 >= 0 ) {
    //first, copy the index info to a temp integer
    UInt_t newindexinfo = mIndexInfo;
    newindexinfo = (newindexinfo & 0xC0FFFFFF); //mask off bits 24-30
    UInt_t ind2 = index2 << 24; //move index 2 to occupy bits 24-30
    newindexinfo = newindexinfo | ind2; //merge back with other info
    mIndexInfo = newindexinfo; //set mIndexInfo to new value
    if( this->GetNumIndices() == 0 ){
        throw 0;
    }
    if( this->GetNumIndices() == 1 ){
        this->SetNumIndices(2);
    }
  } else {
    std::cout << "The range for index2 must be between 0 and 0x3F inclusive. You gave " << index2 << std::endl;
    throw 0;
  }
  return;
}

Double_t SLHAline::GetValue() const {
  return mValue; //method to get the value of a line
}

void SLHAline::SetValue(Double_t value) {
  mValue = value; //method to set the value of a line
  return;
}

std::string SLHAline::GetComment() const {
  return mComment; //method to get the comment of a line
}

void SLHAline::SetComment(std::string comment) {
  mComment = comment; //method to set the comment of a line
  return;
}

std::ostream &operator<<(std::ostream &os, const SLHAline &sl) {
  //overloading the << operator to match the SLHA line formatting
  //the style of output depends on the number of indices
  std::cout.precision(8);
  if(sl.GetNumIndices() == 0) {
    os << "\t" << std::scientific << sl.GetValue()
       << "\t" << "#" << sl.GetComment()
       << std::endl;
  } else if(sl.GetNumIndices() == 1) {
    os << "\t" << sl.GetIndex1() 
       << "\t" << std::scientific << sl.GetValue() 
       << "\t" << "#" << sl.GetComment() 
       << std::endl;
  } else if(sl.GetNumIndices() == 2) {
    os << "\t" << sl.GetIndex1() 
       << "\t" << sl.GetIndex2() 
       << "\t" << std::scientific << sl.GetValue()
       << "\t" << "#" << sl.GetComment()
       << std::endl;
  }
  return os;
}
