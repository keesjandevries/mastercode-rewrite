#include <string.h>
#include "SLHAfile.hh"
#include "SLHAblock.hh"

extern "C" {
    //SLHA file
    SLHAfile* SLHAfile_new(){ 
        return new SLHAfile(); 
    }
    
    bool SLHAfile_readstream( SLHAfile* sf, std::istream& mfile, 
                              bool mVerbose = false ) {
        sf->ReadStream(mfile,mVerbose);
    }

    bool SLHAfile_readfile(SLHAfile* sf, const char* f) {
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

    SLHAblock* SLHAfile_getblock(SLHAfile* sf, const char* blockname) {
        return new SLHAblock((*sf)[blockname]);
    }
    
    // SLHA block
    SLHAblock* SLHAblock_new(const char* name) { 
        return new SLHAblock(name); 
    }

    int SLHAblock_getstr(SLHAblock* sb, char* buf, int len) {
        std::stringstream ss_out( std::stringstream::in |
                                  std::stringstream::out );
        ss_out << (*sb);
        std::string bn_str = ss_out.str();
        const char* sb_cstr = bn_str.c_str();
        strncpy(buf,sb_cstr,len-1);
        buf[len-1]=0;
        return strlen(buf);
    }

    SLHAline* SLHAblock_getline(SLHAblock* sb, const char* comment) {
        return new SLHAline(sb->FindComment(comment));
    }

    // SLHA line
    SLHAline* SLHAline_new(double val=0., const char* comment="") {
        SLHAline* sl = new SLHAline;
        sl->SetValue(val);
        sl->SetComment(comment);
        return sl;
    }

    void SLHAline_setvalue(SLHAline* sl, double val) {
        sl->SetValue(val);
    }

    double SLHAline_getvalue(SLHAline* sl) {
        return sl->GetValue();
    }

    void SLHAline_setcomment(SLHAline* sl, const char* comment) {
        sl->SetComment(comment);
    }

    int SLHAline_getcomment(SLHAline* sl, char* buf, int len) {
        std::string comment_str = sl->GetComment();
        const char* sl_cstr = comment_str.c_str();
        strncpy(buf,sl_cstr,len-1);
        buf[len-1]=0;
        return strlen(buf);
    }

    void SLHAline_setindex1(SLHAline* sl, int index) {
        sl->SetIndex1(index);
    }

    void SLHAline_getindex1(SLHAline* sl) {
        sl->GetIndex1();
    }

    void SLHAline_setindex2(SLHAline* sl, int index) {
        sl->SetIndex2(index);
    }

    void SLHAline_getindex2(SLHAline* sl) {
        sl->GetIndex2();
    }

    int SLHAline_getstr(SLHAline* sl, char* buf, int len) {
        std::stringstream ss_out( std::stringstream::in |
                                  std::stringstream::out );
        ss_out << (*sl);
        std::string bn_str = ss_out.str();
        const char* sl_cstr = bn_str.c_str();
        strncpy(buf,sl_cstr,len-1);
        buf[len-1]=0;
        return strlen(buf);
    }

    int SLHAline_getnumindices(SLHAline* sl) {
        return sl->GetNumIndices();
    }

    int SLHAline_getfullindex(SLHAline* sl) {
        return sl->GetFullIndex();
    }

    // Multiple
    void SLHAfile_addblock(SLHAfile* sf, SLHAblock *sb) {
        sf->AddBlock(*sb);
    }

    void SLHAblock_addline(SLHAblock *sb, SLHAline *sl) {
        sb->AddLine(*sl);
    }

}
