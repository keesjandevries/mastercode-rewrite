//Jad Marrouche, Sep 2011, jad@cern.ch
#include "SLHAblock.hh"

SLHAblock::SLHAblock() {}
SLHAblock::SLHAblock(std::string blockname) {
  //constructor which sets the blockname
  this->SetBlockName(blockname);
}

SLHAblock::~SLHAblock() {}

void SLHAblock::SetBlockName(std::string blockname) {
  mblockname = blockname; //set the blockname
  return;
}

void SLHAblock::AddLine(SLHAline lineval) {
  mlines.push_back(lineval); //push back a new SLHAline to the end of the block
  return;
}

void SLHAblock::clear() {
  //reset the information stored in the block object
  mlines.clear();
  mblockname = "";
  return;
}

unsigned int SLHAblock::size() const {
  return mlines.size(); //find out the size of the vector of SLHAlines
}

SLHAline SLHAblock::FindComment(std::string comment) const {

  //use the native functions instead of acting on private members
  for(unsigned int i=0; i<this->size();i++) { //loop over the vector
    if(this->GetLine(i).GetComment() == comment) { //check comments match
      return (this->GetLine(i)); //if so return the line
    }
  }

  SLHAline line;
  line.SetComment("not found"); //otherwise return a line with comment = not found
  return line;

}


SLHAline SLHAblock::FindIndex(std::pair<UInt_t, UInt_t> index, UInt_t num_indices) const {

  if(num_indices == 1 || num_indices == 2) {
    //use the native functions instead of acting on private members
    for(unsigned int i=0; i<this->size();i++) { //loop over all lines
      //now check that the line has 1 index and we want 1 index
      if(num_indices == 1 && this->GetLine(i).GetNumIndices() == 1) {
	//now check that index1 matches and if so return the line
	if(this->GetLine(i).GetIndex1() == index.first) {
	  return this->GetLine(i);
	}
      } else if(num_indices == 2 && this->GetLine(i).GetNumIndices() == 2) { //repeat for 2 index case
	if(this->GetLine(i).GetIndex1() == index.first && this->GetLine(i).GetIndex2() == index.second) {
	  return this->GetLine(i);
	}
      }
    }
  }

  SLHAline line; 
  line.SetComment("not found");
  return line;

}


SLHAline SLHAblock::GetLine(unsigned int linenum) const {
  return mlines.at(linenum); //method to access elements of SLHAline vector
}

std::string SLHAblock::GetBlockName() const {
  return mblockname; //method to get back block name
}

std::ostream &operator<<(std::ostream &os, const SLHAblock &block) {
  //overloading the << operator to match SLHA file formatting
  os << "BLOCK " << block.GetBlockName() << std::endl;
  for(unsigned int i=0; i<block.size();i++) { //loop over all lines in block
    os << block.GetLine(i); //look in SLHAline.cc for implementation
  }
  return os;
}
