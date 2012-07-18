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

    int SLHAfile_getstr(SLHAfile* sf, char* buf, int len) {
        std::stringstream ss_out( std::stringstream::in |
                                  std::stringstream::out );
        ss_out << (*sf);
        std::string sf_str = ss_out.str();
        const char* lol_str = sf_str.c_str();
        strncpy(buf,lol_str,len-1);
        buf[len-1]=0;
        return strlen(buf);
    }
}
