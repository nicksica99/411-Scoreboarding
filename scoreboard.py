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
    prev_instructions = []
     
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
        instruct_num = i
        #load instructions
        if(scoreboard[i][0] == "L"):
            load_instruction(scoreboard[i], instruct_num, scoreboard)
            
        #store instructions
        elif(scoreboard[i][0:3] == "S.D"):
            store_instruction(scoreboard[i], instruct_num, scoreboard)

        #multiply instructions
        elif(scoreboard[i][0] == "M"):
            multiply_instruction(scoreboard[i], instruct_num, scoreboard)

        #division instructions
        elif(scoreboard[i][0] == "D"):
            division_instruction(scoreboard[i], instruct_num, scoreboard)

        #Add instructions, there are conditions for each type
        elif(scoreboard[i][0] == "A"):
            if(scoreboard[i][3] == "I"):
                add_immediate(scoreboard[i], instruct_num, scoreboard)
            elif(scoreboard[i][4] == "D"):
                add_fp(scoreboard[i], instruct_num, scoreboard)
            else:
                add_integer(scoreboard[i], instruct_num, scoreboard)

        #subtraction instructions, there are conditions for each type
        elif(scoreboard[i][0:3] == "SUB"):
            if(scoreboard[i][4] == "D"):
                sub_fp(scoreboard[i], instruct_num, scoreboard)
            else:
                sub_integer(scoreboard[i], instruct_num, scoreboard)
                
        #appends the instruction into a list of the previous instructions
        prev_instructions.append(scoreboard[i])
        
    
 #   printScoreboard(scoreboard)

# 
# Input: takes in a Load instruction and does the arithmetic
# Output: idk yet
def load_instruction(instruction, num, scoreboard):
    scoreboard_vals = []
    issue_timer = 0
    read_operand_timer = 0
    execution_timer = 0
    write_back_timer = 0

    
    
    print("load")
    for i in range(len(instruction)):
        if(instruction[i] == "F"):
            reg = instruction[i:i+2]
            
        if(instruction[i] == "("):
            offset = int(instruction[i-1])
            if(instruction[i+2] == ")"):
                mem_val = int(instruction[i+1])
            else:
                mem_val = int(instruction[i+1:i+3])
                

    mem_val = check_mem_location(mem_val, offset)
    
    load_reg = check_fp_reg_location(reg)
    
    if(num == 0):
        issue_timer += INTEGER_CYCLES
        scoreboard_vals.append(issue_timer)

        read_operand_timer = issue_timer + INTEGER_CYCLES
        scoreboard_vals.append(read_operand_timer)

        execution_timer =  read_operand_timer + INTEGER_CYCLES
        scoreboard_vals.append(execution_timer)

        write_back_timer = execution_timer + INTEGER_CYCLES
        scoreboard_vals.append(write_back_timer)

        
        set_fp_reg_location(reg, mem_val)
        
 
    
def check_mem_location(mem_val, offset):
    mem_val = mem_val + offset
    
    if(mem_val == 0):
        mem_val = mem_location_0
    elif(mem_val == 1):
        mem_val = mem_location_1
    elif(mem_val == 2):
        mem_val = mem_location_2
    elif(mem_val == 3):
        mem_val = mem_location_3
    elif(mem_val == 4):
        mem_val = mem_location_4
    elif(mem_val == 5):
        mem_val = mem_location_5
    elif(mem_val == 6):
        mem_val = mem_location_6
    elif(mem_val == 7):
        mem_val = mem_location_7
    elif(mem_val == 8):
        mem_val = mem_location_8
    elif(mem_val == 9):
        mem_val = mem_location_9
    elif(mem_val == 10):
        mem_val = mem_location_10
    elif(mem_val == 11):
        mem_val = mem_location_11
    elif(mem_val == 12):
       mem_val = mem_location_12
    elif(mem_val == 13):
       mem_val = mem_location_13
    elif(mem_val == 14):
       mem_val = mem_location_14
    elif(mem_val == 15):
       mem_val = mem_location_15
    elif(mem_val == 16):
       mem_val = mem_location_16
    elif(mem_val == 17):
       mem_val = mem_location_17
    elif(mem_val == 18):
       mem_val = mem_location_18

    return mem_val

def check_fp_reg_location(reg):
    if(reg == "F0"):
        memory = fp_reg1
    elif(reg == "F1"):
        memory = fp_reg2
    elif(reg == "F2"):
        memory = fp_reg3
    elif(reg == "F3"):
        memory = fp_reg4
    elif(reg == "F4"):
        memory = fp_reg5
    elif(reg == "F5"):
        memory = fp_reg6
    elif(reg == "F6"):
        memory = fp_reg7
    elif(reg == "F7"):
        memory = fp_reg8
    elif(reg == "F8"):
        memory = fp_reg9
    elif(reg == "F9"):
        memory = fp_reg10
    elif(reg == "F10"):
        memory = fp_reg11
    elif(reg == "F11"):
        memory = fp_reg12
    elif(reg == "F12"):
        memory = fp_reg13
    elif(reg == "F13"):
        memory = fp_reg14
    elif(reg == "F14"):
        memory = fp_reg15
    elif(reg == "F15"):
        memory = fp_reg16
    elif(reg == "F16"):
        memory = fp_reg17
    elif(reg == "F17"):
        memory = fp_reg18
    elif(reg == "F18"):
        memory = fp_reg19
    elif(reg == "F19"):
        memory = fp_reg20
    elif(reg == "F20"):
        memory = fp_reg21
    elif(reg == "F21"):
        memory = fp_reg22
    elif(reg == "F22"):
        memory = fp_reg23
    elif(reg == "F23"):
        memory = fp_reg24
    elif(reg == "F24"):
        memory = fp_reg25
    elif(reg == "F25"):
        memory = fp_reg26
    elif(reg == "F26"):
        memory = fp_reg27
    elif(reg == "F27"):
        memory = fp_reg28
    elif(reg == "F28"):
        memory = fp_reg29
    elif(reg == "F29"):
        memory = fp_reg30
    elif(reg == "F30"):
        memory = fp_reg31
    elif(reg == "F31"):
        memory = fp_reg32

    return memory

def check_integer_regs(reg):
    if(reg == "$0"):
        reg = integer_reg1
    elif(reg == "$1"):
        reg = integer_reg2
    elif(reg == "$2"):
        reg = integer_reg3
    elif(reg == "$3"):
        reg = integer_reg4
    elif(reg == "$4"):
        reg = integer_reg5
    elif(reg == "$5"):
        reg = integer_reg6
    elif(reg == "$6"):
        reg = integer_reg7
    elif(reg == "$7"):
        reg = integer_reg8
    elif(reg == "$8"):
        reg = integer_reg9
    elif(reg == "$9"):
        reg = integer_reg10
    elif(reg == "$10"):
        reg = integer_reg11
    elif(reg == "$11"):
        reg = integer_reg12
    elif(reg == "$12"):
        reg = integer_reg13
    elif(reg == "$13"):
        reg = integer_reg14
    elif(reg == "$14"):
        reg = integer_reg15
    elif(reg == "$15"):
        reg = integer_reg16
    elif(reg == "$16"):
        reg = integer_reg17
    elif(reg == "$17"):
        reg = integer_reg18
    elif(reg == "$18"):
        reg = integer_reg19
    elif(reg == "$19"):
        reg = integer_reg20
    elif(reg == "$20"):
        reg = integer_reg21
    elif(reg == "$21"):
        reg = integer_reg22
    elif(reg == "$22"):
        reg = integer_reg23
    elif(reg == "$23"):
        reg = integer_reg24
    elif(reg == "$24"):
        reg = integer_reg25
    elif(reg == "$25"):
        reg = integer_reg26
    elif(reg == "$26"):
        reg = integer_reg27
    elif(reg == "$27"):
        reg = integer_reg28
    elif(reg == "$28"):
        reg = integer_reg29
    elif(reg == "$29"):
        reg = integer_reg30
    elif(reg == "$30"):
        reg = integer_reg31
    elif(reg == "$31"):
        reg = integer_reg32

    return reg

def set_fp_reg_location(reg, memory):
    if(reg == "F0"):
        global fp_reg1
        fp_reg1 = memory
    elif(reg == "F1"):
        global fp_reg2
        fp_reg2 = memory
    elif(reg == "F2"):
        global fp_reg3
        fp_reg3 = memory
    elif(reg == "F3"):
        global fp_reg4
        fp_reg4 = memory
    elif(reg == "F4"):
        global fp_reg5
        fp_reg5 = memory
    elif(reg == "F5"):
        global fp_reg6
        fp_reg6 = memory
    elif(reg == "F6"):
        global fp_reg7
        fp_reg7 = memory
    elif(reg == "F7"):
        global fp_reg8
        fp_reg8 = memory
    elif(reg == "F8"):
        global fp_reg9
        fp_reg9 = memory
    elif(reg == "F9"):
        global fp_reg10
        fp_reg9 = memory
    elif(reg == "F10"):
        global fp_reg11
        fp_reg11 = memory
    elif(reg == "F11"):
        global fp_reg12 
        fp_reg12 = memory
    elif(reg == "F12"):
        global fp_reg13
        fp_reg13 = memory
    elif(reg == "F13"):
        global fp_reg14
        fp_reg14 = memory
    elif(reg == "F14"):
        global fp_reg15
        fp_reg15 = memory
    elif(reg == "F15"):
        global fp_reg16
        fp_reg16 = memory
    elif(reg == "F16"):
        global fp_reg17
        fp_reg17 = memory
    elif(reg == "F17"):
        global fp_reg18
        fp_reg18 = memory
    elif(reg == "F18"):
        global fp_reg19
        fp_reg19 = memory
    elif(reg == "F19"):
        global fp_reg20
        fp_reg20 = memory
    elif(reg == "F20"):
        global fp_reg21
        fp_reg21 = memory
    elif(reg == "F21"):
        global fp_reg22
        fp_reg22 = memory
    elif(reg == "F22"):
        global fp_reg23
        fp_reg23 = memory
    elif(reg == "F23"):
        global fp_reg24
        fp_reg24 = memory
    elif(reg == "F24"):
        global fp_reg25
        fp_reg25 = memory
    elif(reg == "F25"):
        global fp_reg26
        fp_reg26 = memory
    elif(reg == "F26"):
        global fp_reg27
        fp_reg27 = memory
    elif(reg == "F27"):
        global fp_reg28
        fp_reg28 = memory
    elif(reg == "F28"):
        global fp_reg29
        fp_reg29 = memory
    elif(reg == "F29"):
        global fp_reg30
        fp_reg30 = memory
    elif(reg == "F30"):
        global fp_reg31
        fp_reg31 = memory
    elif(reg == "F31"):
        global fp_reg32
        fp_reg32 = memory

    

def store_instruction(instruction, num, scoreboard):
    print("store")
    
def add_integer(instruction, num, scoreboard):
    print("add_integer")

def add_immediate(instruction, num, scoreboard):
     print("add_immediate")
     
def add_fp(instruction, num, scoreboard):
     print("add_fp")

def sub_fp(instruction, num, scoreboard):
     print("sub_fp")

def sub_integer(instruction, num, scoreboard):
    print("sub_integer")
    
def multiply_instruction(instruction, num, scoreboard):
     print("multiply")

def division_instruction(instruction, num, scoreboard):
     print("division")


main()
    

 

    
