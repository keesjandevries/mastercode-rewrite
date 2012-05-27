#include "SLHAfile.hh"

extern "C" {
    SLHAfile* SLHAfile_new(){ 
        return new SLHAfile(); 
    }
    
    bool SLHAfile_ReadStream( SLHAfile* sf, std::istream& mfile, 
                              bool mVerbose = false ) {
        sf->ReadStream(mfile,mVerbose);
    }

    bool SLHAfile_ReadFile(SLHAfile* sf, const char* f) {
        std::string s(f);
        return sf->ReadFile(s);
    }

    void SLHAfile_print(SLHAfile* sf) { 
        std::cout << (*sf);
    }
}
