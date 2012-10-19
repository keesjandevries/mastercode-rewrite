#include <iostream>
#include <fstream>
#include "SLHAline.hh"
#include "SLHAblock.hh"
#include "SLHAfile.hh"

int main(void) {

  SLHAline line;
 
  std::cout << "initial value is " << line.GetFullIndex() << std::endl;

  line.SetFullIndex(0xC3100001);

  std::cout << "line index is now " << line.GetFullIndex() << std::endl;
  std::cout << "num line indices is " << line.GetNumIndices() << std::endl;

  line.SetNumIndices(2);

  std::cout << "num line indices is " << line.GetNumIndices() << std::endl;

  std::cout << "index 1 is: " << line.GetIndex1() << std::endl;
  line.SetIndex1(0xFFFFFF);
  std::cout << "index 1 is now: " << line.GetIndex1() << std::endl;

  std::cout << "index 2 is: " << line.GetIndex2() << std::endl;
  line.SetIndex2(63);
  std::cout << "index 2 is now: " << line.GetIndex2() << std::endl;

  line.SetComment("hello world!");
  line.SetValue(54444444444444444444444444444444444444.);
  std::cout << line;

  SLHAblock block("myblock");
  block.AddLine(line);
  block.AddLine(line);
  block.AddLine(line);
  block.AddLine(line);
  block.AddLine(line);

  std::cout << block;

  SLHAline line2;
  line2 = block.FindComment("hello world");
  std::cout << "looking for line2" << std::endl;
  std::cout <<line2;

  line2 = block.FindIndex(std::make_pair(16777215,63),1);
  std::cout << line2;


  SLHAfile file;

  //read in some SLHA file
  if(file.ReadFile("files/001136-slha.out")) std::cout << "yay" << std::endl << file;
  else std::cout << "bummer" << std::endl;

  //search for a particular blockname within the file
  SLHAblock searchblock;
  searchblock = file["STAUMIX"];
  std::cout << searchblock;

  //write back the SLHA file to a new text file
  std::ofstream myfile("files/SLHA-out.txt");
  myfile << file;
  myfile.close();

  //the two lines below are equivalent
  //std::cout << file;
  //operator<<(std::cout, file);
 
  return 0;

}
