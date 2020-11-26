# CMSC 411
# 11/14/2020
# Nick Sica & Jack Huey

# global variables for adder, the fp_adder will be 1 if in use
fp_adder = 0
FP_ADDER_CYCLES = 2
# global multiplier variables
fp_multi = 0
FP_MULTI_CYCLES = 10

# global divider variables
fp_divider = 0
FP_DIVIDER_CYCLES = 40

# global integer unit variables
integer_unit = 0
INTEGER_CYCLES = 1

# global variable for stages
stages = ["Issue", "Read Operand", "Execution", "Write Back"]

# all 32 floating point registers
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

# all 32 integer registers
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

# all memory locations and their equivalent values
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


# readfile()
# Reads in the file by taking in a filename given by the user
# returns a list of the instructions inside of the file
def readFile(filename):
    # opens the file and reads it into the instructionList array
    ofp = open(filename, "r")
    instructionList = ofp.readlines()
    instructions_List = []

    # splits the lines at the whitespace and then strips the whitespace
    # appends the instructions to the instructions_List array
    for i in range(len(instructionList)):
        instructions = instructionList[i].split("\n")
        instructions = instructionList[i].strip("\n")

        instructions_List.append(instructions)
    # returns the instructions
    return instructions_List


# getScoreboard()
# builds the scoreboard from the rows, columns and instructions.
# The rows are the number of instructions, columns will always be 5 (1 instruction, 4 stages)
# returns the 2d scoreboard array
def getScoreboard(rows, columns, instructions):
    scoreboard = []
    # builds the scoreboard
    while len(scoreboard) < rows:
        boardRow = []
        while len(boardRow) < columns:
            boardRow.append("")

        scoreboard.append(boardRow)
    return scoreboard


# printScoreboard()
# neatly prints out the scoreboard and the cycles at each stage for each instruction
# does not return anything, just prints
def printScoreboard(scoreboard):
    print("Instruction     |    Issue    | Read Operation | Execute   | Write Back  | ")
    print("---------------------------------------------------------------------------- ")
    # goes through the length of the scoreboard
    for i in range(len(scoreboard)):
        count = 0
        # this goes through each instruction
        for j in range(len(scoreboard[i])):
            # checks if the subscript is an integer or not, this helps with printing
            int_check = isinstance(scoreboard[i][j], int)
            # if not integer then print normally
            if (int_check != True):
                print(scoreboard[i][j], end="")
            else:
                # if integer then it must print accordingly because to line up with each stage
                # the count variable name is the counter that helps with this
                if (count == 0):
                    print("        ", scoreboard[i][j], end="")
                    count += 1
                elif (count == 1):
                    print("            ", scoreboard[i][j], end="")
                    count += 1
                elif (count == 2):
                    print("             ", scoreboard[i][j], end="")
                    count += 1
                elif (count == 3):
                    print("            ", scoreboard[i][j], end="")
                    count += 1

        print()
        print("--------------------------------------------------------------------------- ")

# print_fp_registers
# prints all of the floating point registers for comparison of the arithmetic done
def print_fp_registers():
    print("FP Registers in order (1-32):", fp_reg1, fp_reg2, fp_reg3, fp_reg4, fp_reg5, fp_reg6, fp_reg7, fp_reg8, fp_reg9,
          fp_reg10, fp_reg11, fp_reg12, fp_reg13, fp_reg14, fp_reg15, fp_reg16, fp_reg17, fp_reg18, fp_reg19, fp_reg20,
          fp_reg21, fp_reg22, fp_reg23, fp_reg24, fp_reg25, fp_reg26, fp_reg27, fp_reg28, fp_reg29, fp_reg30, fp_reg31,
          fp_reg32)

# print_integer_registers
# prints all of the integer registers for comparison of the arithmetic done
def print_integer_registers():
    print("Integer Registers in order (1-32):", integer_reg1, integer_reg2, integer_reg3, integer_reg4, integer_reg5,
          integer_reg6, integer_reg7, integer_reg8, integer_reg9, integer_reg10, integer_reg11, integer_reg12, integer_reg13,
          integer_reg14, integer_reg15, integer_reg16, integer_reg17, integer_reg18, integer_reg19, integer_reg20, integer_reg21,
          integer_reg22, integer_reg23, integer_reg24, integer_reg25, integer_reg26, integer_reg27, integer_reg28, integer_reg29,
          integer_reg30, integer_reg31, integer_reg32)


# main()
#
#
def main():
    width = 5

    mipsInstructions = []
    scoreboard = []
    scoreboard_rows = []
    prev_instructions = []

    load_vals = []
    store_vals = []
    add_vals = []
    addi_vals = []
    add_d_vals = []
    sub_d_vals = []
    sub_vals = []
    mul_vals = []
    div_vals = []

    # lsa = load, store, add, length of the strings
    lsa_length = 3
    # other instructions are 4 chars long
    inst_length = 4

    ifp = input("Enter the filename of the MIPS instructions: ")

    mipsInstructions = readFile(ifp)
    num_instruction = len(mipsInstructions)

    scoreboard = getScoreboard(num_instruction, width, mipsInstructions)

    # puts instructions into scoreboard array
    for i in range(num_instruction):
        scoreboard[i][0] = (mipsInstructions[i])

    # this for loop will determine what the current instruction is and what to do with it
    for i in range(num_instruction):
        instruct_num = i
        # load instructions
        if (scoreboard[i][0][0] == "L"):
            load_vals = load_instruction(scoreboard[i][0], instruct_num, scoreboard)

            for num in range(1, len(stages) + 1):
                scoreboard[i][num] = load_vals[num - 1]

        # store instructions
        elif (scoreboard[i][0][0:3] == "S.D"):
            store_vals = store_instruction(scoreboard[i][0], instruct_num, scoreboard)

            for num in range(1, len(stages) + 1):
                scoreboard[i][num] = store_vals[num - 1]
        # multiply instructions
        elif (scoreboard[i][0][0] == "M"):
            mul_vals = multiply_instruction(scoreboard[i][0], instruct_num, scoreboard)

            for num in range(1, len(stages) + 1):
                scoreboard[i][num] = mul_vals[num - 1]

        # division instructions
        elif (scoreboard[i][0][0] == "D"):
            div_vals = division_instruction(scoreboard[i][0], instruct_num, scoreboard)

            for num in range(1, len(stages) + 1):
                scoreboard[i][num] = div_vals[num - 1]

        # Add instructions, there are conditions for each type
        elif (scoreboard[i][0][0] == "A"):
            # add immediate, gets the values for the scoreboard and puts them in the scoreboard
            if (scoreboard[i][0][3] == "I"):
                addi_vals = add_immediate(scoreboard[i][0], instruct_num, scoreboard)

                for num in range(1, len(stages) + 1):
                    scoreboard[i][num] = addi_vals[num - 1]

            # floating point add
            elif (scoreboard[i][0][4] == "D"):
                add_d_vals = add_fp(scoreboard[i][0], instruct_num, scoreboard)

                for num in range(1, len(stages) + 1):
                    scoreboard[i][num] = add_d_vals[num - 1]
            else:
                # integer add
                add_vals = add_integer(scoreboard[i][0], instruct_num, scoreboard)

                for num in range(1, len(stages) + 1):
                    scoreboard[i][num] = add_vals[num - 1]

        # subtraction instructions, there are conditions for each type
        elif (scoreboard[i][0][0:3] == "SUB"):
            if (scoreboard[i][0][4] == "D"):
                sub_d_vals = sub_fp(scoreboard[i][0], instruct_num, scoreboard)

                for num in range(1, len(stages) + 1):
                    scoreboard[i][num] = sub_d_vals[num - 1]
            # subtract integer
            else:
                sub_vals = sub_integer(scoreboard[i][0], instruct_num, scoreboard)

                for num in range(1, len(stages) + 1):
                    scoreboard[i][num] = sub_vals[num - 1]

        # appends the instruction into a list of the previous instructions
        prev_instructions.append(scoreboard[i][0])

        printScoreboard(scoreboard)
    #printing all of the registers
    print_fp_registers()
    print_integer_registers()

#
#
#
def check_mem_location(mem_val, offset):
    mem_val = mem_val + offset

    if (mem_val == 0):
        mem_val = mem_location_0
    elif (mem_val == 1):
        mem_val = mem_location_1
    elif (mem_val == 2):
        mem_val = mem_location_2
    elif (mem_val == 3):
        mem_val = mem_location_3
    elif (mem_val == 4):
        mem_val = mem_location_4
    elif (mem_val == 5):
        mem_val = mem_location_5
    elif (mem_val == 6):
        mem_val = mem_location_6
    elif (mem_val == 7):
        mem_val = mem_location_7
    elif (mem_val == 8):
        mem_val = mem_location_8
    elif (mem_val == 9):
        mem_val = mem_location_9
    elif (mem_val == 10):
        mem_val = mem_location_10
    elif (mem_val == 11):
        mem_val = mem_location_11
    elif (mem_val == 12):
        mem_val = mem_location_12
    elif (mem_val == 13):
        mem_val = mem_location_13
    elif (mem_val == 14):
        mem_val = mem_location_14
    elif (mem_val == 15):
        mem_val = mem_location_15
    elif (mem_val == 16):
        mem_val = mem_location_16
    elif (mem_val == 17):
        mem_val = mem_location_17
    elif (mem_val == 18):
        mem_val = mem_location_18

    return mem_val

#
#
#
def set_mem_location(location, mem_val):
    if (location == 0):
        global mem_location_1
        mem_location_0 = mem_val
    elif (location == 1):
        global mem_location_2
        mem_location_1 = mem_val
    elif (location == 2):
        global mem_location_2
        mem_location_2 = mem_val
    elif (location == 3):
        global mem_location_3
        mem_location_3 = mem_val
    elif (location == 4):
        global mem_location_4
        mem_location_4 = mem_val
    elif (location == 5):
        global mem_location_5
        mem_location_5 = mem_val
    elif (location == 6):
        global mem_location_6
        mem_location_6 = mem_val
    elif (location == 7):
        global mem_location_7
        mem_location_7 = mem_val
    elif (location == 8):
        global mem_location_8
        mem_location_8 = mem_val
    elif (location == 9):
        global mem_location_9
        mem_location_9 = mem_val
    elif (location == 10):
        global mem_location_10
        mem_location_10 = mem_val
    elif (location == 11):
        global mem_location_11
        mem_location_11 = mem_val
    elif (location == 12):
        global mem_location_12
        mem_location_12 = mem_val
    elif (location == 13):
        global mem_location_13
        mem_location_13 = mem_val
    elif (location == 14):
        global mem_location_14
        mem_location_14 = mem_val
    elif (location == 15):
        global mem_location_15
        mem_location_15 = mem_val
    elif (location == 16):
        global mem_location_16
        mem_location_16 = mem_val
    elif (location == 17):
        global mem_location_17
        mem_location_17 = mem_val
    elif (location == 18):
        global mem_location_18
        mem_location_18 = mem_val

#
#
#
def check_fp_reg_location(reg):
    if (reg == "F0"):
        memory = fp_reg1
    elif (reg == "F1"):
        memory = fp_reg2
    elif (reg == "F2"):
        memory = fp_reg3
    elif (reg == "F3"):
        memory = fp_reg4
    elif (reg == "F4"):
        memory = fp_reg5
    elif (reg == "F5"):
        memory = fp_reg6
    elif (reg == "F6"):
        memory = fp_reg7
    elif (reg == "F7"):
        memory = fp_reg8
    elif (reg == "F8"):
        memory = fp_reg9
    elif (reg == "F9"):
        memory = fp_reg10
    elif (reg == "F10"):
        memory = fp_reg11
    elif (reg == "F11"):
        memory = fp_reg12
    elif (reg == "F12"):
        memory = fp_reg13
    elif (reg == "F13"):
        memory = fp_reg14
    elif (reg == "F14"):
        memory = fp_reg15
    elif (reg == "F15"):
        memory = fp_reg16
    elif (reg == "F16"):
        memory = fp_reg17
    elif (reg == "F17"):
        memory = fp_reg18
    elif (reg == "F18"):
        memory = fp_reg19
    elif (reg == "F19"):
        memory = fp_reg20
    elif (reg == "F20"):
        memory = fp_reg21
    elif (reg == "F21"):
        memory = fp_reg22
    elif (reg == "F22"):
        memory = fp_reg23
    elif (reg == "F23"):
        memory = fp_reg24
    elif (reg == "F24"):
        memory = fp_reg25
    elif (reg == "F25"):
        memory = fp_reg26
    elif (reg == "F26"):
        memory = fp_reg27
    elif (reg == "F27"):
        memory = fp_reg28
    elif (reg == "F28"):
        memory = fp_reg29
    elif (reg == "F29"):
        memory = fp_reg30
    elif (reg == "F30"):
        memory = fp_reg31
    elif (reg == "F31"):
        memory = fp_reg32

    return memory

#
#
#
def check_integer_regs(reg):
    if (reg == "$0"):
        reg = integer_reg1
    elif (reg == "$1"):
        reg = integer_reg2
    elif (reg == "$2"):
        reg = integer_reg3
    elif (reg == "$3"):
        reg = integer_reg4
    elif (reg == "$4"):
        reg = integer_reg5
    elif (reg == "$5"):
        reg = integer_reg6
    elif (reg == "$6"):
        reg = integer_reg7
    elif (reg == "$7"):
        reg = integer_reg8
    elif (reg == "$8"):
        reg = integer_reg9
    elif (reg == "$9"):
        reg = integer_reg10
    elif (reg == "$10"):
        reg = integer_reg11
    elif (reg == "$11"):
        reg = integer_reg12
    elif (reg == "$12"):
        reg = integer_reg13
    elif (reg == "$13"):
        reg = integer_reg14
    elif (reg == "$14"):
        reg = integer_reg15
    elif (reg == "$15"):
        reg = integer_reg16
    elif (reg == "$16"):
        reg = integer_reg17
    elif (reg == "$17"):
        reg = integer_reg18
    elif (reg == "$18"):
        reg = integer_reg19
    elif (reg == "$19"):
        reg = integer_reg20
    elif (reg == "$20"):
        reg = integer_reg21
    elif (reg == "$21"):
        reg = integer_reg22
    elif (reg == "$22"):
        reg = integer_reg23
    elif (reg == "$23"):
        reg = integer_reg24
    elif (reg == "$24"):
        reg = integer_reg25
    elif (reg == "$25"):
        reg = integer_reg26
    elif (reg == "$26"):
        reg = integer_reg27
    elif (reg == "$27"):
        reg = integer_reg28
    elif (reg == "$28"):
        reg = integer_reg29
    elif (reg == "$29"):
        reg = integer_reg30
    elif (reg == "$30"):
        reg = integer_reg31
    elif (reg == "$31"):
        reg = integer_reg32

    return reg

#
#
#
def set_fp_reg_location(reg, memory):
    if (reg == "F0"):
        global fp_reg1
        fp_reg1 = memory
    elif (reg == "F1"):
        global fp_reg2
        fp_reg2 = memory
    elif (reg == "F2"):
        global fp_reg3
        fp_reg3 = memory
    elif (reg == "F3"):
        global fp_reg4
        fp_reg4 = memory
    elif (reg == "F4"):
        global fp_reg5
        fp_reg5 = memory
    elif (reg == "F5"):
        global fp_reg6
        fp_reg6 = memory
    elif (reg == "F6"):
        global fp_reg7
        fp_reg7 = memory
    elif (reg == "F7"):
        global fp_reg8
        fp_reg8 = memory
    elif (reg == "F8"):
        global fp_reg9
        fp_reg9 = memory
    elif (reg == "F9"):
        global fp_reg10
        fp_reg9 = memory
    elif (reg == "F10"):
        global fp_reg11
        fp_reg11 = memory
    elif (reg == "F11"):
        global fp_reg12
        fp_reg12 = memory
    elif (reg == "F12"):
        global fp_reg13
        fp_reg13 = memory
    elif (reg == "F13"):
        global fp_reg14
        fp_reg14 = memory
    elif (reg == "F14"):
        global fp_reg15
        fp_reg15 = memory
    elif (reg == "F15"):
        global fp_reg16
        fp_reg16 = memory
    elif (reg == "F16"):
        global fp_reg17
        fp_reg17 = memory
    elif (reg == "F17"):
        global fp_reg18
        fp_reg18 = memory
    elif (reg == "F18"):
        global fp_reg19
        fp_reg19 = memory
    elif (reg == "F19"):
        global fp_reg20
        fp_reg20 = memory
    elif (reg == "F20"):
        global fp_reg21
        fp_reg21 = memory
    elif (reg == "F21"):
        global fp_reg22
        fp_reg22 = memory
    elif (reg == "F22"):
        global fp_reg23
        fp_reg23 = memory
    elif (reg == "F23"):
        global fp_reg24
        fp_reg24 = memory
    elif (reg == "F24"):
        global fp_reg25
        fp_reg25 = memory
    elif (reg == "F25"):
        global fp_reg26
        fp_reg26 = memory
    elif (reg == "F26"):
        global fp_reg27
        fp_reg27 = memory
    elif (reg == "F27"):
        global fp_reg28
        fp_reg28 = memory
    elif (reg == "F28"):
        global fp_reg29
        fp_reg29 = memory
    elif (reg == "F29"):
        global fp_reg30
        fp_reg30 = memory
    elif (reg == "F30"):
        global fp_reg31
        fp_reg31 = memory
    elif (reg == "F31"):
        global fp_reg32
        fp_reg32 = memory

#
#
#
def set_int_reg_location(reg, memory):
    if (reg == "$0"):
        global integer_reg1
        integer_reg1 = memory
    elif (reg == "$1"):
        global integer_reg2
        integer_reg2 = memory
    elif (reg == "$2"):
        global integer_reg3
        integer_reg3 = memory
    elif (reg == "$3"):
        global integer_reg4
        integer_reg4 = memory
    elif (reg == "$4"):
        global integer_reg5
        integer_reg5 = memory
    elif (reg == "$5"):
        global integer_reg6
        integer_reg6 = memory
    elif (reg == "$6"):
        global integer_reg7
        integer_reg7 = memory
    elif (reg == "$7"):
        global integer_reg8
        integer_reg8 = memory
    elif (reg == "$8"):
        global integer_reg9
        integer_reg9 = memory
    elif (reg == "$9"):
        global integer_reg10
        integer_reg10 = memory
    elif (reg == "$10"):
        global integer_reg11
        integer_reg11 = memory
    elif (reg == "$11"):
        global integer_reg12
        integer_reg12 = memory
    elif (reg == "$12"):
        global integer_reg13
        integer_reg3 = memory
        reg = memory
    elif (reg == "$13"):
        global integer_reg14
        integer_reg14 = memory
    elif (reg == "$14"):
        global integer_reg15
        integer_reg15 = memory
    elif (reg == "$15"):
        global integer_reg16
        integer_reg16 = memory
    elif (reg == "$16"):
        global integer_reg17
        integer_reg17 = memory
    elif (reg == "$17"):
        global integer_reg18
        integer_reg3 = memory
        reg = memory
    elif (reg == "$18"):
        global integer_reg19
        integer_reg19 = memory
    elif (reg == "$19"):
        global integer_reg20
        integer_reg20 = memory
    elif (reg == "$20"):
        global integer_reg21
        integer_reg21 = memory
    elif (reg == "$21"):
        global integer_reg22
        integer_reg3 = memory
        reg = memory
    elif (reg == "$22"):
        global integer_reg23
        integer_reg23 = memory
    elif (reg == "$23"):
        global integer_reg24
        integer_reg24 = memory
    elif (reg == "$24"):
        global integer_reg25
        integer_reg25 = memory
    elif (reg == "$25"):
        global integer_reg26
        integer_reg26 = memory
    elif (reg == "$26"):
        global integer_reg27
        integer_reg27 = memory
    elif (reg == "$27"):
        global integer_reg28
        integer_reg28 = memory
    elif (reg == "$28"):
        global integer_reg29
        integer_reg29 = memory
    elif (reg == "$29"):
        global integer_reg30
        integer_reg30 = memory
    elif (reg == "$30"):
        global integer_reg31
        integer_reg31 = memory
    elif (reg == "$31"):
        global integer_reg32
        integer_reg32 = memory

    return reg

# load_instruction()
# Input: takes in a Load instruction and does the arithmetic necessary
# Output: returns a list of the cycles to be put into the scoreboard
def load_instruction(instruction, num, scoreboard):
    # holds the values of the scoreboard for this instruction
    scoreboard_vals = []

    # counters for the stages
    issue_timer = 0
    read_operand_timer = 0
    execution_timer = 0
    write_back_timer = 0

    print("load")
    # gets the registers, offset and memory value for the load instruction
    for i in range(len(instruction)):
        if (instruction[i] == "F"):
            reg = instruction[i:i + 2]

        if (instruction[i] == "("):
            offset = int(instruction[i - 1])
            if (instruction[i + 2] == ")"):
                mem_val = int(instruction[i + 1])
            else:
                mem_val = int(instruction[i + 1:i + 3])

    # gets the right memory value accounting for the offset
    mem_val = check_mem_location(mem_val, offset)
    # gets the right register for the instruction
    load_reg = check_fp_reg_location(reg)

    # if this instruction is the first instruction to be ran
    # this is an edge case that makes life easy because then calculating the cycles is easy
    if (num == 0):
        issue_timer += INTEGER_CYCLES
        scoreboard_vals.append(issue_timer)

        read_operand_timer = issue_timer + INTEGER_CYCLES
        scoreboard_vals.append(read_operand_timer)

        execution_timer = read_operand_timer + INTEGER_CYCLES
        scoreboard_vals.append(execution_timer)

        write_back_timer = execution_timer + INTEGER_CYCLES
        scoreboard_vals.append(write_back_timer)

        # sets the register value
        set_fp_reg_location(reg, mem_val)
        return scoreboard_vals

    else:
        scoreboard_vals = calc_load_scoreboard(num, mem_val,
                                                  reg, scoreboard)

        return scoreboard_vals

#
#
#
def store_instruction(instruction, num, scoreboard):
    print("store")
    store_vals = []

    issue_timer = 0
    read_operand_timer = 0
    execution_timer = 0
    write_back_timer = 0
    # gets the registers, offset and memory value for the load instruction
    for i in range(len(instruction)):
        if (instruction[i] == "F"):
            reg = instruction[i:i + 2]

        if (instruction[i] == "("):
            offset = int(instruction[i - 1])
            if (instruction[i + 2] == ")"):
                mem_val = int(instruction[i + 1])
            else:
                mem_val = int(instruction[i + 1:i + 3])

    # gets the right memory location for the store
    location = mem_val + offset

    # gets the right register for the instruction
    load_reg = check_fp_reg_location(reg)

    # if this instruction is the first instruction to be ran
    # this is an edge case that makes life easy because then calculating the cycles is easy
    if (num == 0):
        issue_timer += INTEGER_CYCLES
        store_vals.append(issue_timer)

        read_operand_timer = issue_timer + INTEGER_CYCLES
        store_vals.append(read_operand_timer)

        execution_timer = read_operand_timer + INTEGER_CYCLES
        store_vals.append(execution_timer)

        write_back_timer = execution_timer + INTEGER_CYCLES
        store_vals.append(write_back_timer)

        # sets the register value
        set_mem_location(location,load_reg)

        return store_vals

    else:
        scoreboard_vals = calc_store_scoreboard(num, location,load_reg,reg, scoreboard)
        return scoreboard_vals


def add_integer(instruction, num, scoreboard):
    print("add_integer")
    add_vals = []
    registers = []

    issue_timer = 0
    read_operand_timer = 0
    execution_timer = 0
    write_back_timer = 0

    for i in range(len(instruction)):
        if (instruction[i] == "$"):
            registers.append(instruction[i:i + 2])
        if (i == len(instruction) - 1):
            registers.append(instruction[i - 1:i + 1])

    reg_dest = registers[0]
    reg_source = registers[1]
    reg_source2 = registers[2]

    dest_reg = check_integer_regs(reg_dest)
    source_reg = check_integer_regs(reg_source)
    source_reg2 = check_integer_regs(reg_source2)

    memory = source_reg + source_reg2

    if (num == 0):
        issue_timer += INTEGER_CYCLES
        add_vals.append(issue_timer)

        read_operand_timer = issue_timer + INTEGER_CYCLES
        add_vals.append(read_operand_timer)

        execution_timer = read_operand_timer + INTEGER_CYCLES
        add_vals.append(execution_timer)

        write_back_timer = execution_timer + INTEGER_CYCLES
        add_vals.append(write_back_timer)

        set_int_reg_location(reg_dest, memory)

        return add_vals

    else:
        add_vals = calc_immediates_scoreboard(num, memory, registers, scoreboard)

        return add_vals


def add_immediate(instruction, num, scoreboard):
    print("add_immediate")
    add_vals = []
    registers = []

    issue_timer = 0
    read_operand_timer = 0
    execution_timer = 0
    write_back_timer = 0

    for i in range(len(instruction)):
        if (instruction[i] == "$"):
            registers.append(instruction[i:i + 2])
        if (i == len(instruction) - 1):
            registers.append(instruction[i - 1:i + 1])

    reg_dest = registers[0]
    reg_source = registers[1]
    value = int(registers[2])

    dest_reg = check_integer_regs(reg_dest)
    source_reg = check_integer_regs(reg_source)

    memory = source_reg + value

    if (num == 0):
        issue_timer += INTEGER_CYCLES
        add_vals.append(issue_timer)

        read_operand_timer = issue_timer + INTEGER_CYCLES
        add_vals.append(read_operand_timer)

        execution_timer = read_operand_timer + INTEGER_CYCLES
        add_vals.append(execution_timer)

        write_back_timer = execution_timer + INTEGER_CYCLES
        add_vals.append(write_back_timer)

        set_int_reg_location(reg_dest, memory)

        return add_vals

    else:
        add_vals = calc_immediates_scoreboard(num, memory, registers, scoreboard)

        return add_vals


def add_fp(instruction, num, scoreboard):
    print("add_fp")
    add_vals = []
    registers = []

    issue_timer = 0
    read_operand_timer = 0
    execution_timer = 0
    write_back_timer = 0

    for i in range(len(instruction)):
        if (instruction[i] == "F"):
            registers.append(instruction[i:i + 2])
        if (i == len(instruction) - 1):
            registers.append(instruction[i - 1:i + 1])

    reg_dest = registers[0]
    reg_source = registers[1]
    reg_source2 = registers[2]

    dest_reg = check_fp_reg_location(reg_dest)
    source_reg = check_fp_reg_location(reg_source)
    source_reg2 = check_fp_reg_location(reg_source2)

    memory = source_reg + source_reg2

    if (num == 0):
        issue_timer += 1
        add_vals.append(issue_timer)

        read_operand_timer = issue_timer + 1
        add_vals.append(read_operand_timer)

        execution_timer = read_operand_timer + FP_ADDER_CYCLES
        add_vals.append(execution_timer)

        write_back_timer = execution_timer + 1
        add_vals.append(write_back_timer)

        set_fp_reg_location(reg_dest, memory)

        return add_vals

    else:
        add_vals = calc_add_sub_scoreboard(num, memory, registers, scoreboard)

        return add_vals


def sub_fp(instruction, num, scoreboard):
    print("sub_fp")
    sub_vals = []
    registers = []

    issue_timer = 0
    read_operand_timer = 0
    execution_timer = 0
    write_back_timer = 0

    for i in range(len(instruction)):
        if (instruction[i] == "F"):
            registers.append(instruction[i:i + 2])
        if (i == len(instruction) - 1):
            registers.append(instruction[i - 1:i + 1])

    reg_dest = registers[0]
    reg_source = registers[1]
    reg_source2 = registers[2]

    dest_reg = check_fp_reg_location(reg_dest)
    source_reg = check_fp_reg_location(reg_source)
    source_reg2 = check_fp_reg_location(reg_source2)

    memory = source_reg - source_reg2

    if (num == 0):
        issue_timer += 1
        sub_vals.append(issue_timer)

        read_operand_timer = issue_timer + 1
        sub_vals.append(read_operand_timer)

        execution_timer = read_operand_timer + FP_ADDER_CYCLES
        sub_vals.append(execution_timer)

        write_back_timer = execution_timer + 1
        sub_vals.append(write_back_timer)

        set_fp_reg_location(reg_dest, memory)

        return sub_vals
    else:
        sub_vals = calc_add_sub_scoreboard(num, memory, registers, scoreboard)

        return sub_vals


def sub_integer(instruction, num, scoreboard):
    print("sub_integer")
    sub_vals = []
    registers = []

    issue_timer = 0
    read_operand_timer = 0
    execution_timer = 0
    write_back_timer = 0

    for i in range(len(instruction)):
        if (instruction[i] == "$"):
            registers.append(instruction[i:i + 2])
        if (i == len(instruction) - 1):
            registers.append(instruction[i - 1:i + 1])

    reg_dest = registers[0]
    reg_source = registers[1]
    reg_source2 = registers[2]

    dest_reg = check_integer_regs(reg_dest)
    source_reg = check_integer_regs(reg_source)
    source_reg2 = check_integer_regs(reg_source2)

    memory = source_reg - source_reg2

    if (num == 0):
        issue_timer += INTEGER_CYCLES
        sub_vals.append(issue_timer)

        read_operand_timer = issue_timer + INTEGER_CYCLES
        sub_vals.append(read_operand_timer)

        execution_timer = read_operand_timer + INTEGER_CYCLES
        sub_vals.append(execution_timer)

        write_back_timer = execution_timer + INTEGER_CYCLES
        sub_vals.append(write_back_timer)

        set_int_reg_location(reg_dest, memory)

        return sub_vals

    else:
        sub_vals = calc_immediates_scoreboard(num, memory, registers, scoreboard)

        return sub_vals


def multiply_instruction(instruction, num, scoreboard):
    print("multiply")
    mul_vals = []
    registers = []

    issue_timer = 0
    read_operand_timer = 0
    execution_timer = 0
    write_back_timer = 0

    for i in range(len(instruction)):
        if (instruction[i] == "F"):
            registers.append(instruction[i:i + 2])

    reg_dest = registers[0]
    reg_source = registers[1]
    reg_source2 = registers[2]

    dest_reg = check_fp_reg_location(reg_dest)
    source_reg = check_fp_reg_location(reg_source)
    source_reg2 = check_fp_reg_location(reg_source2)

    memory = (source_reg * source_reg2)

    if (num == 0):
        issue_timer += 1
        mul_vals.append(issue_timer)

        read_operand_timer = issue_timer + 1
        mul_vals.append(read_operand_timer)

        execution_timer = read_operand_timer + FP_MULTI_CYCLES
        mul_vals.append(execution_timer)

        write_back_timer = execution_timer + 1
        mul_vals.append(write_back_timer)

        set_fp_reg_location(reg_dest, memory)

        return mul_vals

    else:
        mul_vals = calc_multiply_scoreboard(num, memory, registers, scoreboard)


        return mul_vals


def division_instruction(instruction, num, scoreboard):
    print("division")
    div_vals = []
    registers = []

    issue_timer = 0
    read_operand_timer = 0
    execution_timer = 0
    write_back_timer = 0

    for i in range(len(instruction)):
        if (instruction[i] == "F"):
            registers.append(instruction[i:i + 2])

    reg_dest = registers[0]
    reg_source = registers[1]
    reg_source2 = registers[2]

    dest_reg = check_fp_reg_location(reg_dest)
    source_reg = check_fp_reg_location(reg_source)
    source_reg2 = check_fp_reg_location(reg_source2)

    memory = source_reg / source_reg2

    if (num == 0):
        issue_timer += 1
        div_vals.append(issue_timer)

        read_operand_timer = issue_timer + 1
        div_vals.append(read_operand_timer)

        execution_timer = read_operand_timer + FP_DIVIDER_CYCLES
        div_vals.append(execution_timer)

        write_back_timer = execution_timer + 1
        div_vals.append(write_back_timer)

        set_fp_reg_location(reg_dest, memory)

        print(fp_reg4)

        return div_vals
    else:
        div_vals = calc_division_scoreboard(num, memory, registers, scoreboard)

        return div_vals


# standard scoreboard operation for start, and in instances where there are no hazards
def calc_load_scoreboard(inst_num, mem_val, load_reg, scoreboard):
    scoreboard_vals = []
    issue_timer = 0
    issue_timer_check = 0
    read_operand_timer = 0
    execution_timer = 0
    write_back_timer = 0


    # checks if other integer units are being used
    prev_loads_wb_times = []
    for i in range(inst_num, 0, -1):
        instruction = scoreboard[inst_num - 1][0]
        if (scoreboard[i - 1][0][0] == "L" or scoreboard[i - 1][0][0:3] == "S.D"
            or scoreboard[i - 1][0][0:4] == "ADDI" or scoreboard[i - 1][0][0:4] == "ADD"
            or scoreboard[i - 1][0][0:4] == "SUB"):

            prev_loads_wb_times.append(scoreboard[i - 1][4])

    prev_inst_issue = scoreboard[inst_num - 1][1]
    print(prev_loads_wb_times)
    if (prev_loads_wb_times != []):
        if (max(prev_loads_wb_times) > prev_inst_issue):
            issue_timer_check = max(prev_loads_wb_times) + INTEGER_CYCLES
        else:
            issue_timer_check = prev_inst_issue + INTEGER_CYCLES
    else:
        issue_timer_check = prev_inst_issue + INTEGER_CYCLES

    prev_ins_wb_times = []
    prev_reg = []
    prev_inst_wb = 0
    #checks for WAW Hazards
    for i in range(inst_num, 0, -1):
        instruction = scoreboard[i - 1][0]
        len_instruction = len(instruction)
        # goes through the instruction and grabs the registers
        for j in range(len_instruction):
            if (instruction[j] == "F"):
                dest_reg = instruction[j:j + 2]

        if (load_reg == dest_reg):
            prev_ins_wb_times.append(int(scoreboard[i - 1][4]))

    if (prev_ins_wb_times != []):
        prev_inst_wb = max(prev_ins_wb_times)

    prev_inst_read = int(scoreboard[inst_num - 1][2])
    if (prev_inst_read > prev_inst_wb):
        issue_timer = prev_inst_read

    else:
        issue_timer = prev_inst_wb + 1

    if(issue_timer_check > issue_timer):
        issue_timer = issue_timer_check

    scoreboard_vals.append(issue_timer)

    read_operand_timer = issue_timer + INTEGER_CYCLES
    scoreboard_vals.append(read_operand_timer)

    execution_timer = read_operand_timer + INTEGER_CYCLES
    scoreboard_vals.append(execution_timer)

    #checks for WAR hazards
    prev_inst_read = 0
    prev_instruction = scoreboard[inst_num - 1][0]
    for i in range(len(prev_instruction)):
        if (prev_instruction[i] == "F"):
            prev_reg.append(prev_instruction[i:i + 2])
    if(len(prev_reg) == 1):
        prev_inst_read = int(scoreboard[inst_num-1][2])

    elif(prev_reg[1] == load_reg or prev_reg[2] == load_reg):

        prev_inst_read = int(scoreboard[inst_num - 1][2])

    if (prev_inst_read > execution_timer):
        write_back_timer = prev_inst_read + INTEGER_CYCLES
    else:
        write_back_timer = execution_timer + INTEGER_CYCLES

    scoreboard_vals.append(write_back_timer)

    print(load_reg, mem_val)
    set_fp_reg_location(load_reg, mem_val)

    return scoreboard_vals

def calc_store_scoreboard(inst_num, mem_val, load_reg, register,scoreboard):
    scoreboard_vals = []
    issue_timer = 0
    read_operand_timer = 0
    execution_timer = 0
    write_back_timer = 0
    #checks if other integer units are being used
    prev_stores_wb_times = []
    for i in range(inst_num, 0, -1):
        instruction = scoreboard[inst_num-1][0]
        if(scoreboard[i - 1][0][0] == "L" or scoreboard[i - 1][0][0:3] == "S.D"
                or scoreboard[i - 1][0][0:4] == "ADDI" or scoreboard[i - 1][0][0:4] == "ADD"
                or scoreboard[i - 1][0][0:4] == "SUB"):
            prev_stores_wb_times.append(scoreboard[i-1][4])

    prev_inst_issue = scoreboard[inst_num-1][1]
    print(prev_stores_wb_times)
    if(prev_stores_wb_times != []):
        if(max(prev_stores_wb_times) > prev_inst_issue):
            issue_timer = max(prev_stores_wb_times) + INTEGER_CYCLES
        else:
            issue_timer = prev_inst_issue + INTEGER_CYCLES
    else:
        issue_timer = prev_inst_issue + INTEGER_CYCLES

    scoreboard_vals.append(issue_timer)

    # checking for RAW
    prev_wb_time = 0
    for i in range(inst_num, 0, -1):
        prev_reg = []
        instruction = scoreboard[i - 1][0]
        len_instruction = len(instruction)

        for j in range(len_instruction):
            if (instruction[j] == "F"):
                prev_reg.append(instruction[j:j + 2])

        if (prev_reg == []):
            continue

        if (register == prev_reg[0]):
            prev_wb_time = int(scoreboard[i-1][4])
            break
        else:
            continue

    if (prev_wb_time > issue_timer):
        read_operand_timer = prev_wb_time + INTEGER_CYCLES
    else:
        read_operand_timer = issue_timer + INTEGER_CYCLES

    scoreboard_vals.append(read_operand_timer)

    execution_timer = read_operand_timer + INTEGER_CYCLES
    scoreboard_vals.append(execution_timer)

    write_back_timer = execution_timer + INTEGER_CYCLES
    scoreboard_vals.append(write_back_timer)

    set_mem_location(mem_val, load_reg)

    return scoreboard_vals


def calc_add_sub_scoreboard(inst_num, mem_val, registers, scoreboard):
    scoreboard_vals = []
    issue_timer = 0
    issue_timer_check = 0
    read_operand_timer = 0
    execution_timer = 0
    write_back_timer = 0

    dest_reg = registers[0]
    source_reg1 = registers[1]
    source_reg2 = registers[2]

    #checks to see if units are being used
    prev_stores_wb_times = []
    for i in range(inst_num, 0, -1):
        instruction = scoreboard[inst_num - 1][0]
        if (scoreboard[i - 1][0][0:5] == "ADD.D" or scoreboard[i - 1][0][0:5] == "SUB.D"):
            prev_stores_wb_times.append(scoreboard[i - 1][4])

    prev_inst_issue = scoreboard[inst_num - 1][1]
    if(prev_stores_wb_times != []):
        if (max(prev_stores_wb_times) > prev_inst_issue):
            issue_timer_check = max(prev_stores_wb_times) + INTEGER_CYCLES
        else:
            issue_timer_check = prev_inst_issue + INTEGER_CYCLES
    else:
        issue_timer_check = prev_inst_issue + INTEGER_CYCLES
    prev_wb_times = 0
    #checks for WAW
    for i in range(inst_num, 0, -1):
        prev_regs = []
        instruction = scoreboard[i - 1][0]
        len_instruction = len(instruction)
        # goes through the instruction and grabs the registers
        for j in range(len_instruction):
            if (instruction[j] == "F"):
                prev_regs.append(instruction[j:j + 2])

        if(prev_regs == []):
            continue

        if (dest_reg == prev_regs[0]):
            prev_wb_times = int(scoreboard[i-1][4])
            break
        else:
            continue

    if (prev_wb_times > int(scoreboard[inst_num - 1][1])):
        issue_timer = prev_wb_times + INTEGER_CYCLES
    else:
        issue_timer = int(scoreboard[inst_num - 1][1]) + INTEGER_CYCLES
    if(issue_timer_check > issue_timer):
        issue_timer = issue_timer_check

    scoreboard_vals.append(issue_timer)
    prev_wb_time = 0
    for i in range(inst_num, 0, -1):
        prev_reg = []
        instruction = scoreboard[i - 1][0]
        len_instruction = len(instruction)

        for j in range(len_instruction):
            if (instruction[j] == "F"):
                prev_reg.append(instruction[j:j + 2])

        if(prev_reg == [] or instruction[0:3] == "S.D"):
            continue


        if (source_reg1 == prev_reg[0] or source_reg2 == prev_reg[0]):
            prev_wb_time = int(scoreboard[i - 1][4])
            break
        else:
            continue

    if (prev_wb_time > issue_timer):
        read_operand_timer = prev_wb_time + INTEGER_CYCLES
    else:
        read_operand_timer = issue_timer + INTEGER_CYCLES

    scoreboard_vals.append(read_operand_timer)

    execution_timer = read_operand_timer + FP_ADDER_CYCLES
    scoreboard_vals.append(execution_timer)

    prev_read_time = 0
    # checks for WAR
    if (scoreboard[inst_num - 1][0][0] == "L" or scoreboard[inst_num - 1][0][0:3] == "S.D"):
        write_back_timer = execution_timer + INTEGER_CYCLES
    else:
        for i in range(inst_num, 0, -1):
            prev_reg_war = []
            instruction = scoreboard[i - 1][0]
            len_instruction = len(instruction)

            for j in range(len_instruction):
                if (instruction[j] == "F"):
                    prev_reg_war.append(instruction[j:j + 2])

            if(prev_reg_war == [] or len(prev_reg_war) == 1):
                continue

            if (dest_reg == prev_reg_war[1] or dest_reg == prev_reg_war[2]):
                prev_read_time = int(scoreboard[i-1][2])
                break
            else:
                continue

        if (prev_read_time > execution_timer):
            write_back_timer = prev_read_time + INTEGER_CYCLES
        else:
            write_back_timer = execution_timer + INTEGER_CYCLES

    scoreboard_vals.append(write_back_timer)

    set_fp_reg_location(dest_reg, mem_val)

    return scoreboard_vals


def calc_immediates_scoreboard(inst_num, mem_val, registers, scoreboard):
    # intitalizes variables
    scoreboard_vals = []
    immediate_tell = False
    # values for the scoreboard
    issue_timer = 0
    issue_timer_check = 0
    read_operand_timer = 0
    execution_timer = 0
    write_back_timer = 0

    # registers
    dest_reg = registers[0]
    source_reg1 = registers[1]

    # if statement in case it is an add immediate, it can handle that
    if (registers[2][0] != "$"):
        value = registers[2]
        immediate_tell = True
    else:
        source_reg2 = registers[2]

        # checks to see if units are being used
    prev_stores_wb_times = []
    for i in range(inst_num, 0, -1):
        instruction = scoreboard[inst_num - 1][0]
        if (scoreboard[i - 1][0][0] == "L" or scoreboard[i - 1][0][0:3] == "S.D" or
            scoreboard[i - 1][0][0:4] == "ADDI" or scoreboard[i - 1][0][0:4] == "ADD"
            or scoreboard[i - 1][0][0:4] == "SUB"):

            prev_stores_wb_times.append(scoreboard[i - 1][4])

    prev_inst_issue = scoreboard[inst_num - 1][1]
    if (prev_stores_wb_times != []):
        if (max(prev_stores_wb_times) > prev_inst_issue):
            issue_timer_check = max(prev_stores_wb_times) + INTEGER_CYCLES
        else:
            issue_timer_check = prev_inst_issue + INTEGER_CYCLES
    else:
        issue_timer_check = prev_inst_issue + INTEGER_CYCLES

    # checks for WAW hazards
    prev_wb_waw_times = 0
    for i in range(inst_num, 0, -1):
        prev_regs = []
        instruction = scoreboard[i - 1][0]
        len_instruction = len(instruction)
        # goes through the instruction and grabs the registers
        for j in range(len_instruction):
            if (instruction[j] == "$"):
                prev_regs.append(instruction[j:j + 2])

        if(prev_regs == []):
            continue

        if (dest_reg == prev_regs[0]):
            prev_wb_times = int(scoreboard[i][4])
            break
        else:
            continue

    if (prev_wb_waw_times > int(scoreboard[inst_num - 1][1])):
        issue_timer = prev_wb_waw_times + INTEGER_CYCLES
    else:
        issue_timer = int(scoreboard[inst_num - 1][1])

    if(issue_timer_check > issue_timer):
        issue_timer = issue_timer_check

    scoreboard_vals.append(issue_timer)

    prev_wb_raw_time = 0
    # checks for RAW hazard, goes through the previous instructions and checks if there is a read
    # after write hazard and sets the values necessary for the scoreboard
    for i in range(inst_num, 0, -1):
        instruction = scoreboard[i - 1][0]
        prev_reg = []
        len_instruction = len(instruction)

        for j in range(len_instruction):
            if (instruction == "$"):
                prev_reg.append(instruction[j:j + 2])

        if (prev_reg == []):
            continue

        if (immediate_tell == True):
            if (source_reg1 == prev_reg[0]):
                prev_wb_time = int(scoreboard[i][4])
                break
            else:
                continue
        else:
            if (source_reg1 == prev_reg[0] or source_reg2[0] == prev_reg[0]):
                prev_wb_time = int(scoreboard[i][4])
                break
            else:
                continue
    # sets the read operand clock cycle
    if (prev_wb_raw_time > issue_timer):
        read_operand_timer = prev_wb_raw_time + INTEGER_CYCLES
    else:
        read_operand_timer = issue_timer + INTEGER_CYCLES

    scoreboard_vals.append(read_operand_timer)
    execution_timer = read_operand_timer + INTEGER_CYCLES
    scoreboard_vals.append(execution_timer)

    prev_read_time = 0
    # checks for WAR
    for i in range(inst_num, 0, -1):
        prev_reg_war = []
        instruction = scoreboard[i - 1][0]
        len_instruction = len(instruction)

        for j in range(len_instruction):
            if (instruction[j] == "$"):
                prev_reg_war.append(instruction[j:j + 2])

        if (prev_reg_war == [] or len(prev_reg_war) == 1):
            continue

        if (dest_reg == prev_reg_war[1] or dest_reg == prev_reg_war[2]):
            prev_read_time = int(scoreboard[i-1][2])
            break
        else:
            continue

    if (prev_read_time > execution_timer):
        write_back_timer = prev_read_time + INTEGER_CYCLES
    else:
        write_back_timer = execution_timer + INTEGER_CYCLES

    scoreboard_vals.append(write_back_timer)

    set_int_reg_location(dest_reg, mem_val)

    return scoreboard_vals


def calc_multiply_scoreboard(inst_num, mem_val, registers, scoreboard):
    scoreboard_vals = []
    issue_timer = 0
    issue_timer_check = 0
    read_operand_timer = 0
    execution_timer = 0
    write_back_timer = 0

    dest_reg = registers[0]
    source_reg1 = registers[1]
    source_reg2 = registers[2]

    # checks to see if units are being used
    prev_stores_wb_times = []
    for i in range(inst_num, 0, -1):
        instruction = scoreboard[inst_num - 1][0]
        if (scoreboard[i - 1][0][0:5] == "MUL.D"):
            prev_stores_wb_times.append(scoreboard[i - 1][4])

    prev_inst_issue = scoreboard[inst_num - 1][1]
    if (prev_stores_wb_times != []):
        if (max(prev_stores_wb_times) > prev_inst_issue):
            issue_timer_check = max(prev_stores_wb_times) + INTEGER_CYCLES
        else:
            issue_timer_check = prev_inst_issue + INTEGER_CYCLES
    else:
        issue_timer_check = prev_inst_issue + INTEGER_CYCLES

    prev_wb_waw_times = 0
    #checks for WAW hazards
    for i in range(inst_num, 0, -1):
        prev_regs = []
        instruction = scoreboard[i - 1][0]
        len_instruction = len(instruction)
        for j in range(len_instruction):
            if (instruction[j] == "F"):
                prev_regs.append(instruction[j:j + 2])

        if (prev_regs == []):
            continue

        if (dest_reg == prev_regs[0]):
            prev_wb_waw_times = int(scoreboard[i][4])
            break
        else:
            continue

    if (prev_wb_waw_times > int(scoreboard[inst_num - 1][1])):
        issue_timer = prev_wb_waw_times + INTEGER_CYCLES
    else:
        issue_timer = int(scoreboard[inst_num - 1][1])

    if(issue_timer_check > issue_timer):
        issue_timer = issue_timer_check

    scoreboard_vals.append(issue_timer)
    prev_wb_raw_time = 0
    #checks for RAW hazards
    for i in range(inst_num, 0, -1):
        prev_reg = []
        instruction = scoreboard[i - 1][0]
        len_instruction = len(instruction)

        for j in range(len_instruction):
            if (instruction[j] == "F"):
                prev_reg.append(instruction[j:j + 2])
        if (prev_reg == [] or instruction[i-1][0][0:3] == "S.D"):
            continue

        if (source_reg1 == prev_reg[0] or source_reg2 == prev_reg[0]):
            prev_wb_raw_time = int(scoreboard[i - 1][4])
            break
        else:
            continue
    if (prev_wb_raw_time > issue_timer):
        read_operand_timer = prev_wb_raw_time + INTEGER_CYCLES
    else:
        read_operand_timer = issue_timer + INTEGER_CYCLES

    scoreboard_vals.append(read_operand_timer)

    execution_timer = read_operand_timer + FP_MULTI_CYCLES
    scoreboard_vals.append(execution_timer)

    prev_read_time = 0
    # checks for WAR
    if (scoreboard[inst_num - 1][0][0] == "L" or scoreboard[inst_num - 1][0][0:3] == "S.D"):
        write_back_timer = execution_timer + INTEGER_CYCLES
    else:
        for i in range(inst_num, 0, -1):
            prev_reg_war = []
            instruction = scoreboard[i-1][0]
            len_instruction = len(instruction)

            for j in range(len_instruction):
                if (instruction[j] == "F"):
                    prev_reg_war.append(instruction[j:j + 2])

            if (prev_reg_war == [] or len(prev_reg_war) == 1):
                continue

            if(dest_reg == prev_reg_war[1] or dest_reg == prev_reg_war[2]):
                prev_read_time = int(scoreboard[i-1][2])
                break
            else:
                continue

        if (prev_read_time > execution_timer):
            write_back_timer = prev_read_time + INTEGER_CYCLES
        else:
            write_back_timer = execution_timer + INTEGER_CYCLES

    scoreboard_vals.append(write_back_timer)

    set_fp_reg_location(dest_reg, mem_val)

    return scoreboard_vals

def calc_division_scoreboard(inst_num, mem_val, registers, scoreboard):
    scoreboard_vals = []
    issue_timer = 0
    issue_timer_check = 0
    read_operand_timer = 0
    execution_timer = 0
    write_back_timer = 0

    dest_reg = registers[0]
    source_reg1 = registers[1]
    source_reg2 = registers[2]

    # checks to see if units are being used
    prev_stores_wb_times = []
    for i in range(inst_num, 0, -1):
        instruction = scoreboard[inst_num - 1][0]
        if (scoreboard[i - 1][0][0:5] == "DIV.D"):
            prev_stores_wb_times.append(scoreboard[i - 1][4])

    prev_inst_issue = scoreboard[inst_num - 1][1]
    if (prev_stores_wb_times != []):
        if (max(prev_stores_wb_times) > prev_inst_issue):
            issue_timer_check = max(prev_stores_wb_times) + INTEGER_CYCLES
        else:
            issue_timer_check = prev_inst_issue + INTEGER_CYCLES
    else:
        issue_timer_check = prev_inst_issue + INTEGER_CYCLES

    prev_wb_waw_times = 0
    # checks for WAW hazards
    for i in range(inst_num, 0, -1):
        prev_regs = []
        instruction = scoreboard[i - 1][0]
        len_instruction = len(instruction)
        for j in range(len_instruction):
            if (instruction[j] == "F"):
                prev_regs.append(instruction[j:j + 2])

        if (prev_regs == []):
            continue

        if (dest_reg == prev_regs[0]):
            prev_wb_waw_times = int(scoreboard[i][4])
            break
        else:
            continue

    if (prev_wb_waw_times > int(scoreboard[inst_num - 1][1])):
        issue_timer = prev_wb_waw_times + INTEGER_CYCLES
    else:
        issue_timer = int(scoreboard[inst_num - 1][1])

    if (issue_timer_check > issue_timer):
        issue_timer = issue_timer_check

    scoreboard_vals.append(issue_timer)
    prev_wb_raw_time = 0
    # checks for RAW hazards
    for i in range(inst_num, 0, -1):
        prev_reg = []
        instruction = scoreboard[i - 1][0]
        len_instruction = len(instruction)

        for j in range(len_instruction):
            if (instruction[j] == "F"):
                prev_reg.append(instruction[j:j + 2])
        if (prev_reg == [] or instruction[i - 1][0][0:3] == "S.D"):
            continue

        if (source_reg1 == prev_reg[0] or source_reg2 == prev_reg[0]):
            prev_wb_raw_time = int(scoreboard[i - 1][4])
            break
        else:
            continue
    if (prev_wb_raw_time > issue_timer):
        read_operand_timer = prev_wb_raw_time + INTEGER_CYCLES
    else:
        read_operand_timer = issue_timer + INTEGER_CYCLES

    scoreboard_vals.append(read_operand_timer)

    execution_timer = read_operand_timer + FP_DIVIDER_CYCLES
    scoreboard_vals.append(execution_timer)

    prev_read_time = 0
    # checks for WAR
    if (scoreboard[inst_num - 1][0][0] == "L" or scoreboard[inst_num - 1][0][0:3] == "S.D"):
        write_back_timer = execution_timer + INTEGER_CYCLES
    else:
        for i in range(inst_num, 0, -1):
            prev_reg_war = []
            instruction = scoreboard[i - 1][0]
            len_instruction = len(instruction)

            for j in range(len_instruction):
                if (instruction[j] == "F"):
                    prev_reg_war.append(instruction[j:j + 2])

            if (prev_reg_war == [] or len(prev_reg_war) == 1):
                continue

            if (dest_reg == prev_reg_war[1] or dest_reg == prev_reg_war[2]):
                prev_read_time = int(scoreboard[i-1][2])
                break
            else:
                continue

        if (prev_read_time > execution_timer):
            write_back_timer = prev_read_time + INTEGER_CYCLES
        else:
            write_back_timer = execution_timer + INTEGER_CYCLES

    scoreboard_vals.append(write_back_timer)

    set_fp_reg_location(dest_reg, mem_val)

    return scoreboard_vals


main()
