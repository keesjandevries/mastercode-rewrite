CC=g++
CFLAGS=-c -Wall -fPIC
LD_FLAGS=-static

LIB_DIR=$(PWD)/../../json-local/lib
SRC_DIR=$(PWD)/src
OBJ_DIR=$(PWD)/obj
INC_DIR=$(PWD)/inc
INC_JSON=$(PWD)/../../json-local/include/



MAIN_SRC=$(PWD)/main.cc
MAIN_OBJ=$(OBJ_DIR)/main.o
SRCS=$(wildcard $(SRC_DIR)/*.cc)
OBJS=$(addprefix $(OBJ_DIR)/,$(notdir $(SRCS:.cc=.o)))

TARGET=test.x

$(TARGET): $(MAIN_OBJ) $(OBJS) 
	$(CC) $(LD_FLAGS)  $^ -o $@ -L$(LIB_DIR) -ljansson

$(MAIN_OBJ) : $(MAIN_SRC)
	$(CC) $(CFLAGS) $< -o $@ -I$(INC_DIR) -I$(INC_JSON)

#NOTE: this is the proper way expand things 
$(OBJ_DIR)/%.o: $(SRC_DIR)/%.cc $(INC_DIR)/%.h
	$(CC) $(CFLAGS) $< -o $@ -I$(INC_DIR) -I$(INC_JSON)

clean :
	rm -f $(OBJ_DIR)/*o $(TARGET)
