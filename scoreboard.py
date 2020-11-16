# CMSC 411
# 11/14/2020
# Nick Sica & Jack Huey

fp_adder = 0
FP_ADDER_CYCLES = 2

fp_multi = 0
FP_MULTI_CYCLES = 10

fp_divider = 0
FP_DIVIDER_CYCLES = 40

integer_unit = 0
INTEGER_CYCLES = 1

fp_reg1 = 0
fp_reg2 = 0
fp_reg3 = 0
fp_reg4 = 0
fp_reg5 = 0
fp_reg6 = 0
fp_reg7 = 0
fp_reg8 = 0
fp_reg9 = 0
fp_reg10 = 0
fp_reg11 = 0
fp_reg12 = 0
fp_reg13 = 0
fp_reg14 = 0
fp_reg15 = 0
fp_reg16 = 0
fp_reg17 = 0
fp_reg18 = 0
fp_reg19 = 0
fp_reg20 = 0
fp_reg21 = 0
fp_reg22 = 0
fp_reg23 = 0
fp_reg24 = 0
fp_reg25 = 0
fp_reg26 = 0
fp_reg27 = 0
fp_reg28 = 0
fp_reg29 = 0
fp_reg30 = 0
fp_reg31 = 0
fp_reg32 = 0

integer_reg1 = 0
integer_reg2 = 0
integer_reg3 = 0
integer_reg4 = 0
integer_reg5 = 0
integer_reg6 = 0
integer_reg7 = 0
integer_reg8 = 0
integer_reg9 = 0
integer_reg10 = 0
integer_reg11 = 0
integer_reg12 = 0
integer_reg13 = 0
integer_reg14 = 0
integer_reg15 = 0
integer_reg16 = 0
integer_reg17 = 0
integer_reg18 = 0
integer_reg19 = 0
integer_reg20 = 0
integer_reg21 = 0
integer_reg22 = 0
integer_reg23 = 0
integer_reg24 = 0
integer_reg25 = 0
integer_reg26 = 0
integer_reg27 = 0
integer_reg28 = 0
integer_reg29 = 0
integer_reg30 = 0
integer_reg31 = 0
integer_reg32 = 0

mem_location_0 = 45
mem_location_1 = 12
mem_location_2 = 0
mem_location_3 = 0
mem_location_4 = 10
mem_location_5 = 135
mem_location_6 = 254
mem_location_7 = 127
mem_location_8 = 18
mem_location_9 = 4
mem_location_10 = 55
mem_location_11 = 8
mem_location_12 = 2
mem_location_13 = 98
mem_location_14 = 13
mem_location_15 = 5
mem_location_16 = 233
mem_location_17 = 158
mem_location_18 = 167


def readFile(filename):
    ofp = open(filename, "r")
    instructionList = ofp.readlines()
    instructions_List = []
    
    for i in range(len(instructionList)):
        instructions = instructionList[i].split("\n")
        instructions = instructionList[i].strip("\n")

        instructions_List.append(instructions)
    
    return instructions_List


def printScoreboard(scoreboard):
    print("\n  Instruction        |  Issue  | Read Operand | Execute | Write Back | ")

    print(scoreboard)
    
def main():
    mipsInstructions = []
    scoreboard = []
     
    mipsToPython = {"Load" : "L.D", "Store": "S.D", "Add":"ADD", "AddImediate":"ADDI",
                    "Add.d": "ADD.D", "Sub.d" : "SUB.d", "Sub" : "SUB.D", "Mul.d": "MUL.D",
                    "Div.d": "DIV.D" }
    #lsa = load, store, add, length of the strings
    lsa_length = 3
    #other instructions are 4 chars long
    inst_length = 4
    
    ifp = input("Enter the filename of the MIPS instructions: ")
    
    mipsInstructions = readFile(ifp)

    num_instruction = len(mipsInstructions)

    #puts instructions into scoreboard array
    for i in range(num_instruction):
        scoreboard.append(mipsInstructions[i])

    #this for loop will determine what the current instruction is and what to do with it
    for i in range(num_instruction):
        #load instructions
        if(scoreboard[i][0] == "L"):
            load_instruction(scoreboard[i])
            
        #store instructions
        elif(scoreboard[i][0:3] == "S.D"):
            store_instruction(scoreboard[i])

        #multiply instructions
        elif(scoreboard[i][0] == "M"):
            multiply_instruction(scoreboard[i])

        #division instructions
        elif(scoreboard[i][0] == "D"):
            division_instruction(scoreboard[i])

        #Add instructions, there are conditions for each type
        elif(scoreboard[i][0] == "A"):
            if(scoreboard[i][3] == "I"):
                add_immediate(scoreboard[i])
            elif(scoreboard[i][4] == "D"):
                add_fp(scoreboard[i])
            else:
                add_integer(scoreboard[i])

        #subtraction instructions, there are conditions for each type
        elif(scoreboard[i][0:3] == "SUB"):
            if(scoreboard[i][4] == "D"):
                sub_fp(scoreboard[i])
            else:
                sub_integer(scoreboard[i])
            
        
        
    
 #   printScoreboard(scoreboard)

# 
# Input: takes in a Load instruction and does the arithmetic
# Output: idk yet
def load_instruction(instruction):
    issue_timer = 0
    read_operand_timer = 0
    execution_timer = 0
    write_back_timer = 0
    
    print("load")
    for i in range(len(instruction)):
        if(instruction[i] == "F"):
            reg = instruction[i:i+2]
            
    print(reg)
            
    
def store_instruction(instruction):
    print("store")
    
def add_integer(instruction):
    print("add_integer")

def add_immediate(instruction):
     print("add_immediate")
def add_fp(instruction):
     print("add_fp")

def sub_fp(instruction):
     print("sub_fp")

def sub_integer(instruction):
    print("sub_integer")
def multiply_instruction(instruction):
     print("multiply")

def division_instruction(instruction):
     print("division")

main()
    

 

    
