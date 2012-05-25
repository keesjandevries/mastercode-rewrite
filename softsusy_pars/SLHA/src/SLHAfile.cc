//Jad Marrouche, Sep 2011, jad@cern.ch
#include "SLHAfile.hh"
#include <sstream>

SLHAfile::SLHAfile() {}
SLHAfile::~SLHAfile() {}

SLHAfile::SLHAfile(std::string mFileName) {
  //constructor which reads the file name by default
  this->ReadFile(mFileName);
}

void SLHAfile::AddBlock(SLHAblock block) {
  mblocks.push_back(block); //add a block to the file object
  return;
}

bool SLHAfile::ReadFile( std::string mFileName, bool mVerbose ) {
    if(mVerbose) std::cout << "reading file " << mFileName << std::endl;

    std::ifstream mFileStream(mFileName.c_str()); //the file to be read in
    bool state = false;
    if( mFileStream.is_open() ) {
        state = this->ReadStream( mFileStream, mVerbose );
        mFileStream.close();
    }
    else { 
        std::cout << "Unable to open file"; 
    }
    return state;
}

bool SLHAfile::ReadStream(std::istream& myfile, bool mVerbose) {
  this->clear(); //make sure when Reading a file that all existing info is erased
  
  std::string lLine; //this variable will contain the contents of a line
  
  //default constructor for our block object
  SLHAblock block;
  bool firsttimeblock(true);
  
    
    bool BlackList(true); //set up a flag for Blacklisting certain block names if relevant
    while ( myfile.good() ) { //check that the file is good for reading
      
      getline (myfile,lLine); //read the first line from myfile, copy it to lLine and advance the pointer to the next line
      std::transform( lLine.begin() , lLine.end() , lLine.begin() , ::toupper ); //capitalise all characters to make string comparison unambiguous
      std::string::iterator lItr; //define a string iterator to loop over the characters of a line
      
      for(lItr=lLine.begin();lItr!=lLine.end();++lItr) {
	if( *lItr!=' ' && *lItr!='\t' ) break; //find the first non-space-non-tab character so that lItr points to it
      }
      if(lItr == lLine.end()) continue; //i.e. read the next line as we have reached the end of the line
      if(*lItr == '#') continue; //i.e. the first non-space-non-tab character is a hash --> the line is a comment so ignore it
      
      if( lLine.substr( lItr-lLine.begin() , 5 ) == "BLOCK" ) { //compose a substring of 5 characters from the current position of lItr and compare to read BLOCK
	// is a block definition
	if(mVerbose) std::cout << lLine << "  >> is a block definition" << std::endl; //for info, print out the header block line
	lItr += 5; //advance the pointer by 5 characters
	for( ;lItr!=lLine.end();++lItr)	{
	  if( *lItr!=' ' && *lItr!='\t' ) break; //find the next non-space-non-tab character
	}
	std::string lTemp;
	
	for( ;lItr!=lLine.end();++lItr) { //go from the found character above to the end of line (or #) and make a new string. this is the block name
	  if( *lItr=='#' ) break;
	  lTemp += *lItr;
	}

	//now we strip off the whitespace at the end of the string
	lTemp.erase(lTemp.find_last_not_of(" \n\r\t")+1);

	if(mVerbose) std::cout << "the block is called: " << lTemp << std::endl;
	
	//at this point, you may wish to ignore certain blocks - do this by adding to the following:
	if( lTemp.substr(0,6) == "SPINFO" ) BlackList = true;
	else BlackList = false;
	
	//lTemp now = block name without any comments.
	//If this is the >= second time accessing this part of the code, want to do something like:
	if(!BlackList) {
	  if(firsttimeblock) {
	    firsttimeblock = false;
	  } else {
	    this->AddBlock(block);
	    block.clear(); //reset block contents;
	  }
	  //set the name of the SLHAblock object
	  block.SetBlockName(lTemp);
	}

      } else { //if the line does not begin with BLOCK, and is not a comment or blank line, then it is a data line
	if( !BlackList ) { //so long as the block name is not blacklisted, read in the line
	  std::vector< std::string > lTemp; //define vector of strings
	  bool isSpace(true);

	  for( ;lItr!=lLine.end();++lItr) { //the pointer is now pointing at the first non-space-non-tab character in the line

	    if( *lItr=='#' ) { //if that happens to be a #, the line is a comment (this is excluded by the logic above so it must be further along)
	      lTemp.push_back( std::string("") );
	      lTemp.back() += lLine.substr( lItr-lLine.begin()+2 ); //add the string from the hash (excluding it) to the end of the line and break out
	      break;
	    }
	    
	    if( isSpace ) { //isSpace is defaulted to true the first time i.e. associate all characters with a certain substring
	      if( *lItr!=' ' && *lItr!='\t' ) { //i.e. non-space-non-tab character
		isSpace = false; //reset isSpace to prevent a call to push_back
		lTemp.push_back( std::string("") );
		lTemp.back() += *lItr; //add the character to a string onto the end of the vector
	      }
	    } else {
	      if( *lItr!=' ' && *lItr!='\t' ) { //if we encounter a non-space-non-tab character which is part of the previous string
		lTemp.back() += *lItr; //add it onto the last element of the vector
	      } else {
		isSpace = true; //otherwise if we find a space or tab, reset isSpace so we push another string entry into the vector
	      }
	    }
	  }

	  std::string lIndex0("0"), lIndex1("0"), lValue("") , lComment("");

	  if( lTemp.size() == 2 ) { //if we have two elements in the vector, assume it is value + comment
	    // 0 index data entry
	    if(mVerbose) std::cout  << lLine << "  >> 0 index data entry" << std::endl;
	    lValue = lTemp[0];
	    lComment = lTemp[1];
	    
	  } else if( lTemp.size() == 3 ) { //if we have three elements, assume it is index + value + comment
	    // 1 index data entry
	    if(mVerbose) std::cout  << lLine << "  >> 1 index data entry" << std::endl;
	    lIndex0 = lTemp[0];
	    lValue = lTemp[1];
	    lComment = lTemp[2];

	  } else if( lTemp.size() == 4 ) { //if we have four elements, assume it is index + index + value + comment
	    // 2 index data entry
	    if(mVerbose) std::cout  << lLine << "  >> 2 index data entry" << std::endl;
	    lIndex0 = lTemp[0];
	    lIndex1 = lTemp[1];
	    lValue = lTemp[2];
	    lComment = lTemp[3];

	  } else {
	    if(mVerbose) std::cout << "Your config file is screwed" << std::endl;
	    //throw 0;
	    return false;
	  }

	  //define some variables and cast the strings to their values
	  std::stringstream lStr1 , lStr2 , lStr3;
	  UInt_t lIntIndex0(0) , lIntIndex1(0);
          Double_t lDoubleValue(0.0);
	  
	  lStr1 << lIndex0;
	  lStr1 >> lIntIndex0;
	  
	  lStr2 << lIndex1;
	  lStr2 >> lIntIndex1;
	  
	  if(lValue != "NAN") {
	    lStr3 << lValue;
	    lStr3 >> lDoubleValue;
	  }
	  
	  if(mVerbose) std::cout << lIntIndex1 << " | " << lIntIndex0 << " | " << std::scientific << lDoubleValue << " | " << lComment << std::endl;
	  //at this stage, we can compile an SLHAline object, ignoring lines with NAN for the time being
	  if(lValue != "NAN") {
	    //populate the SLHAline object with the above information
	    SLHAline myobject;
	    myobject.SetNumIndices((lTemp.size() - 2));
	    myobject.SetIndex1(lIntIndex0);
	    myobject.SetIndex2(lIntIndex1);
	    myobject.SetValue(lDoubleValue);
	    myobject.SetComment(lComment);
	    block.AddLine(myobject); //add the line to the block
	  }
	  
	} else {
	  if(mVerbose) std::cout  << lLine << " is in a Black-listed block" << std::endl; //ignore lines in a blacklisted block header
	}
      }
      
    }

    //add the last block to the file
    if(!BlackList) {
      this->AddBlock(block);
    }

  return true;
}

unsigned int SLHAfile::size() const {
  return mblocks.size(); //method to get number of blocks in the vector
}

void SLHAfile::clear() {
  mblocks.clear(); //method to clear contents of the vector
  return;
}

SLHAblock SLHAfile::GetBlock(unsigned int blocknum) const {
  return mblocks.at(blocknum); //method to get elements of the block vector
}

SLHAblock SLHAfile::operator[](std::string blockname) const {
  //this method overrides the [] operator to allow an easy way to search for
  //a block within the vector of blocks. It assumes that there is only one
  //occurrence of each blockname, and will return the last occurrence if more
  //than one exists
  SLHAblock temp;
  temp.SetBlockName("not found");

  for(unsigned int i=0; i<this->size(); i++) {
    if(this->GetBlock(i).GetBlockName() == blockname) {
      temp = this->GetBlock(i); //copy to the temp SLHAblock
    }
  }

  return temp;
}

std::stringstream& SLHAfile::streamer(std::stringstream& ss)
{
    if( ss ) ss.clear();
    ss << (*this);
    return ss;
}


std::ostream &operator<<(std::ostream &os, const SLHAfile &file) {
  //overload the << operator to match the SLHA file format
  for(unsigned int i=0; i<file.size(); i++) {
    os << file.GetBlock(i);
  }

  return os;
}

std::istream &operator>>(std::istream &is, SLHAfile &file) {
    file.ReadStream(is);
    return is;
}
