CXX=g++
LD=g++

UNAME := $(shell uname)

ifeq ($(UNAME),Darwin)
	SONAME := -install_name
else
	SONAME := -soname
endif

INCDIR=\
	-Iinc

CXXFLAGS=-c --std=c++11 -fPIC -g -D$(UNAME)

LDFLAGS=
LINK=
LIBS=

SRCDIR=src
OBJDIR=obj
EXEDIR=exe
LIBDIR=libs

SRC=$(wildcard src/*.cc)
SRCEXE=$(wildcard src/*.cpp)
OBJ=$(subst $(SRCDIR), $(OBJDIR),$(subst cc,o,$(SRC)))
OBJEXE=$(subst $(SRCDIR), $(OBJDIR),$(subst cpp,eo,$(SRCEXE)))
SLHALIBS=libSLHAfile.so

TARGETS=$(subst .cpp,,$(subst $(SRCDIR)/,,$(SRCEXE)))

all:$(TARGETS) $(OBJ) $(SLHALIBS)

$(TARGETS): $(OBJEXE) $(OBJ)
	$(LD) -o exe/$@ $(OBJ) obj/$@.eo  $(LDFLAGS) $(LIBS) $(LIBOBJS)

$(OBJEXE):$(SRCEXE)
	$(CXX) $(CXXFLAGS) $(INCDIR) $(subst .eo,.cpp,$(subst obj,src,$@)) -o $@

$(OBJ):$(SRC)
	$(CXX) $(CXXFLAGS) $(INCDIR) $(subst .o,.cc,$(subst obj,src,$@)) -o $@

$(SLHALIBS):$(OBJ)
	$(CXX) -shared -Wl,$(SONAME),$@ -o $(LIBDIR)/$@ $(OBJ) $(LIBS)

clean:
	@rm obj/*
	@rm libs/*

force:
	@make clean
	@make
