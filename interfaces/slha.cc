#include "SLHAfile.hh"
#include "SLHAblock.hh"

extern "C" {
    //SLHA file
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
    
    // SLHA block
    SLHAblock* SLHAblock_new(const char* name){ 
        return new SLHAblock(name); 
    }

    int SLHAblock_getstr(SLHAblock* sb, char* buf, int len) {
        std::stringstream ss_out( std::stringstream::in |
                                  std::stringstream::out );
        ss_out << (*sb);
        std::string bn_str = ss_out.str();
        const char* sb_cstr = sb_str.c_str();
        strncpy(buf,sb_cstr,len-1);
        buf[len-1]=0;
        return strlen(buf);
    }
}
