# CMSC 411
# 11/14/2020
# Nick Sica & Jack Huey

# global variables for adder,
FP_ADDER_CYCLES = 2
# global multiplier variables
FP_MULTI_CYCLES = 10
# global divider variables
FP_DIVIDER_CYCLES = 40
# global integer unit variables
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
    print("Instruction       |  Issue  |  Read  |  Execute |  Write Back  | ")
    print("----------------------------------------------------------------")

    # goes through the scoreboard and prints each row and column and formats it.
    # we tried to make it pretty but it's not perfect
    for i in range(len(scoreboard)):
        counter = 0
        for j in range(len(scoreboard[i])):
            print("{}   |".format(scoreboard[i][j]), end="     ")
            counter += 1

            if (counter == 5):
                print()

        print("---------------------------------------------------------------- ")


# print_fp_registers
# prints all of the floating point registers for comparison of the arithmetic done
def print_fp_registers():
    print("FP Registers in order (0-31):", fp_reg1, fp_reg2, fp_reg3, fp_reg4, fp_reg5, fp_reg6, fp_reg7, fp_reg8,
          fp_reg9,
          fp_reg10, fp_reg11, fp_reg12, fp_reg13, fp_reg14, fp_reg15, fp_reg16, fp_reg17, fp_reg18, fp_reg19, fp_reg20,
          fp_reg21, fp_reg22, fp_reg23, fp_reg24, fp_reg25, fp_reg26, fp_reg27, fp_reg28, fp_reg29, fp_reg30, fp_reg31,
          fp_reg32)


# print_integer_registers
# prints all of the integer registers for comparison of the arithmetic done
def print_integer_registers():
    print("Integer Registers in order (0-31):", integer_reg1, integer_reg2, integer_reg3, integer_reg4, integer_reg5,
          integer_reg6, integer_reg7, integer_reg8, integer_reg9, integer_reg10, integer_reg11, integer_reg12,
          integer_reg13,
          integer_reg14, integer_reg15, integer_reg16, integer_reg17, integer_reg18, integer_reg19, integer_reg20,
          integer_reg21,
          integer_reg22, integer_reg23, integer_reg24, integer_reg25, integer_reg26, integer_reg27, integer_reg28,
          integer_reg29,
          integer_reg30, integer_reg31, integer_reg32)


# main()
# Builds the scoreboard and handles reading in the instructions
# Prints the scoreboard and registers at the end
def main():
    # width of the scoreboard will always be 5
    width = 5
    # arrays to store some of the instruction and the scoreboard
    mipsInstructions = []
    scoreboard = []
    scoreboard_rows = []
    prev_instructions = []

    # gets the filename of the text MIPS file
    ifp = input("Enter the filename of the MIPS instructions: ")

    # reads the files
    mipsInstructions = readFile(ifp)
    num_instruction = len(mipsInstructions)

    # builds the scoreboard
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

    # prints the scoreboard
    printScoreboard(scoreboard)
    # printing all of the registers
    print_fp_registers()
    print_integer_registers()


# check_mem_location()
# Takes in a memory value and the offset
# Returns the memory value at the specific location
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


# set_mem_location
# Takes in the location and the new value
# Sets the new value to the location, does not return
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


# check_fp_reg_location
# Takes in the FP register
# returns the value inside of the FP register
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


# check_integer_regs
# Takes in the integer register
# Returns the value inside the integer register
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


# set_fp_reg_location
# Takes in the FP register and the memory value
# Sets the register to the memory value
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


# set_int_reg_location
# Takes in the integer register and the memory value
# Sets the integer register to the memory value
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

    # gets the registers, offset and memory value for the load instruction
    for i in range(len(instruction)):
        if (instruction[i] == "F"):
            reg = instruction[i:i + 3]
            reg = reg.strip(",")

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
        # gets the right clock cycle values if the instruction is not the first
        scoreboard_vals = calc_load_scoreboard(num, mem_val,
                                               reg, scoreboard)
        return scoreboard_vals


# store_instruction
# Takes in the instruction, the instruction number and the scoreboard
# Returns a list of the cycles to be put into the scoreboard
def store_instruction(instruction, num, scoreboard):
    # array to put the values in
    store_vals = []
    # values for the stages
    issue_timer = 0
    read_operand_timer = 0
    execution_timer = 0
    write_back_timer = 0

    # gets the registers, offset and memory value for the load instruction
    for i in range(len(instruction)):
        if (instruction[i] == "F"):
            reg = instruction[i:i + 3]
            reg = reg.strip(",")

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

        # sets the memory value to what was in the register
        set_mem_location(location, load_reg)

        return store_vals

    else:
        # gets the clock cycle values and puts them in the array
        scoreboard_vals = calc_store_scoreboard(num, location, load_reg, reg, scoreboard)
        return scoreboard_vals


# add_integer
# Takes in the add integer instruction, the instruction number and the scoreboard
# returns a list of the cycles to be put into the scoreboard
def add_integer(instruction, num, scoreboard):
    # arrays for the values and the registers
    add_vals = []
    registers = []

    # values for the stages
    issue_timer = 0
    read_operand_timer = 0
    execution_timer = 0
    write_back_timer = 0

    # gets the registers and puts them in the array
    for i in range(len(instruction)):
        if (instruction[i] == "$"):
            regs = instruction[i:i + 3]
            regs = regs.strip(",")
            registers.append(regs)

    # gets the destination register, and the sources
    reg_dest = registers[0]
    reg_source = registers[1]
    reg_source2 = registers[2]

    # gets the values from the registers
    dest_reg = check_integer_regs(reg_dest)
    source_reg = check_integer_regs(reg_source)
    source_reg2 = check_integer_regs(reg_source2)

    # does the addition
    memory = source_reg + source_reg2

    # if the instruction is first
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
        # calculates the clock cycles and puts them into an array
        add_vals = calc_immediates_scoreboard(num, memory, registers, scoreboard)

        return add_vals

# add_immediate
# Takes in the add immediate instruction, the instruction number and the scoreboard
# returns a list of the cycles to be put into the scoreboard
def add_immediate(instruction, num, scoreboard):
    # arrays for the values
    add_vals = []
    registers = []

    # values for the stages
    issue_timer = 0
    read_operand_timer = 0
    execution_timer = 0
    write_back_timer = 0

    # gets the registers from the instruction
    for i in range(len(instruction)):
        if (instruction[i] == "$"):
            regs = instruction[i:i + 3]
            regs = regs.strip(",")
            registers.append(regs)
        if (i == len(instruction) - 1):
            registers.append(instruction[i - 1:i + 1])

    # gets the destination and source register. As well as the immediate value
    reg_dest = registers[0]
    reg_source = registers[1]
    value = int(registers[2])

    # gets the values from the registers
    dest_reg = check_integer_regs(reg_dest)
    source_reg = check_integer_regs(reg_source)

    # does the add
    memory = source_reg + value

    # if the instruction is the first instruction
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
        # gets the clock cycles and puts them in an array
        add_vals = calc_immediates_scoreboard(num, memory, registers, scoreboard)

        return add_vals

# add_fp
# Takes in the floating point add instruction, instruction number, scoreboard
# returns a list of the cycles to be put into the scoreboard
def add_fp(instruction, num, scoreboard):
    # arrays for the registers
    add_vals = []
    registers = []

    # values for the stages
    issue_timer = 0
    read_operand_timer = 0
    execution_timer = 0
    write_back_timer = 0

    # gets the registers
    for i in range(len(instruction)):
        if (instruction[i] == "F"):
            regs = instruction[i:i + 3]
            regs = regs.strip(",")
            registers.append(regs)

    # gets the destination registers, the source registers
    reg_dest = registers[0]
    reg_source = registers[1]
    reg_source2 = registers[2]

    # gets the values of the registers
    dest_reg = check_fp_reg_location(reg_dest)
    source_reg = check_fp_reg_location(reg_source)
    source_reg2 = check_fp_reg_location(reg_source2)

    # does the add
    memory = source_reg + source_reg2

    # if the instruction is the first instruction
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
        # gets the clock cycle values and puts them into an array
        add_vals = calc_add_sub_scoreboard(num, memory, registers, scoreboard)

        return add_vals

# sub_fp
# takes in the sub floating point instruction, instruction number and the scoreboard
# returns a list of the cycles to be put into the scoreboard
def sub_fp(instruction, num, scoreboard):
    # arrays for the values and registers
    sub_vals = []
    registers = []

    # values for the stages
    issue_timer = 0
    read_operand_timer = 0
    execution_timer = 0
    write_back_timer = 0

    # gets the registers
    for i in range(len(instruction)):
        if (instruction[i] == "F"):
            regs = instruction[i:i + 3]
            regs = regs.strip(",")
            registers.append(regs)

    # gets the destination and source registers
    reg_dest = registers[0]
    reg_source = registers[1]
    reg_source2 = registers[2]

    # gets the value of the registers
    dest_reg = check_fp_reg_location(reg_dest)
    source_reg = check_fp_reg_location(reg_source)
    source_reg2 = check_fp_reg_location(reg_source2)

    # does the subtract
    memory = source_reg - source_reg2

    # if the instruction is the first instruction
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
        # gets the clock cycle values and puts them in an array
        sub_vals = calc_add_sub_scoreboard(num, memory, registers, scoreboard)

        return sub_vals
# sub_integer
# Takes in the subtract integer instruction and the instruction number, scoreboard
# returns a list of the cycles to be put into the scoreboard
def sub_integer(instruction, num, scoreboard):
    # arrays for the values and registers
    sub_vals = []
    registers = []

    # values for the stages
    issue_timer = 0
    read_operand_timer = 0
    execution_timer = 0
    write_back_timer = 0

    # gets the registers
    for i in range(len(instruction)):
        if (instruction[i] == "$"):
            regs = instruction[i:i + 3]
            regs = regs.strip(",")
            registers.append(regs)

    # gets the destination and source registers
    reg_dest = registers[0]
    reg_source = registers[1]
    reg_source2 = registers[2]

    # gets the values for the registers
    dest_reg = check_integer_regs(reg_dest)
    source_reg = check_integer_regs(reg_source)
    source_reg2 = check_integer_regs(reg_source2)

    # does the subtraction
    memory = source_reg - source_reg2

    # if the instruction is the first instruction
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
        # gets the clock cycle values
        sub_vals = calc_immediates_scoreboard(num, memory, registers, scoreboard)

        return sub_vals

# multiply_instruction
# Takes in the multiply instruction, the instruction number and the scoreboard
# returns a list of the cycles to be put into the scoreboard
def multiply_instruction(instruction, num, scoreboard):
    # arrays for the values and the registers
    mul_vals = []
    registers = []

    # values for the stages
    issue_timer = 0
    read_operand_timer = 0
    execution_timer = 0
    write_back_timer = 0

    # gets the registers
    for i in range(len(instruction)):
        if (instruction[i] == "F"):
            regs = instruction[i:i + 3]
            regs = regs.strip(",")
            registers.append(regs)

    # gets the destination and source registers
    reg_dest = registers[0]
    reg_source = registers[1]
    reg_source2 = registers[2]

    # gets the values for the registers
    dest_reg = check_fp_reg_location(reg_dest)
    source_reg = check_fp_reg_location(reg_source)
    source_reg2 = check_fp_reg_location(reg_source2)

    # does the multiply arithmetic
    memory = (source_reg * source_reg2)

    # if the instruction is the first instruction
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
        # gets the clock cycle values and puts them into the array
        mul_vals = calc_multiply_scoreboard(num, memory, registers, scoreboard)

        return mul_vals

# division_instruction
# Takes in the division instruction, the instruction number, and the scoreboard
# returns a list of the cycles to be put into the scoreboard
def division_instruction(instruction, num, scoreboard):
    # arrays for the registers and the clock cycle values
    div_vals = []
    registers = []

    # values for the stages
    issue_timer = 0
    read_operand_timer = 0
    execution_timer = 0
    write_back_timer = 0

    # gets the registers
    for i in range(len(instruction)):
        if (instruction[i] == "F"):
            regs = instruction[i:i + 3]
            regs = regs.strip(",")
            registers.append(regs)

    # gets the destination and source registers
    reg_dest = registers[0]
    reg_source = registers[1]
    reg_source2 = registers[2]

    # gets the values for the registers
    dest_reg = check_fp_reg_location(reg_dest)
    source_reg = check_fp_reg_location(reg_source)
    source_reg2 = check_fp_reg_location(reg_source2)

    # does the division arithmetic unless there is a divide by zero error
    try:
        memory = source_reg / source_reg2
    except ZeroDivisionError:
        print("Divide by zero error, try a different register")

    # if the instruction is the first instruction
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

        return div_vals
    else:
        # gets the clock cycle values and puts them into the array
        div_vals = calc_division_scoreboard(num, memory, registers, scoreboard)

        return div_vals

# calc_load_scoreboard
# Takes in the instruction number, memory value, the destination register and the scoreboard
# Returns the clock cycle values - checks for hazards
def calc_load_scoreboard(inst_num, mem_val, load_reg, scoreboard):
    # array for the values
    scoreboard_vals = []
    # values for the clock cycle values, the issue_timer_check is to help with the
    # hazards and check the unit
    issue_timer = 0
    issue_timer_check = 0
    read_operand_timer = 0
    execution_timer = 0
    write_back_timer = 0

    # checks if other integer units are being used
    prev_loads_wb_times = []
    # goes through the previous instructions, checks if the units are the same and if they are then it appends the
    # write back time
    for i in range(inst_num, 0, -1):
        instruction = scoreboard[inst_num - 1][0]
        if (scoreboard[i - 1][0][0] == "L" or scoreboard[i - 1][0][0:3] == "S.D"
                or scoreboard[i - 1][0][0:4] == "ADDI" or scoreboard[i - 1][0][0:4] == "ADD"
                or scoreboard[i - 1][0][0:4] == "SUB"):
            prev_loads_wb_times.append(scoreboard[i - 1][4])

    # gets the previous instruction's issue time
    prev_inst_issue = scoreboard[inst_num - 1][1]
    # if there are other instructions with the same unit then it will take the highest write back value
    # if not then it will take the previous instruction issue
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
    # checks for WAW Hazards
    for i in range(inst_num, 0, -1):
        instruction = scoreboard[i - 1][0]
        len_instruction = len(instruction)
        # goes through the instruction and grabs the registers
        for j in range(len_instruction):
            if (instruction[j] == "F"):
                dest_reg = instruction[j:j + 2]
        # the destination registers are the same
        if (load_reg == dest_reg):
            prev_ins_wb_times.append(int(scoreboard[i - 1][4]))
    # if there are values that had the same destination registers then it gets the max write back time
    if (prev_ins_wb_times != []):
        prev_inst_wb = max(prev_ins_wb_times)

    # gets the previous instructions read and compares it to the
    # previous instructions write back times
    prev_inst_read = int(scoreboard[inst_num - 1][2])
    if (prev_inst_read > prev_inst_wb):
        issue_timer = prev_inst_read

    else:
        issue_timer = prev_inst_wb + 1

    # compares the structural hazard with the WAW hazard and sets the issue value to the highest
    if (issue_timer_check > issue_timer):
        issue_timer = issue_timer_check

    scoreboard_vals.append(issue_timer)

    # sets the read operand timer- there are no RAWs for a Load instruction
    read_operand_timer = issue_timer + INTEGER_CYCLES
    scoreboard_vals.append(read_operand_timer)

    # sets the execution timer
    execution_timer = read_operand_timer + INTEGER_CYCLES
    scoreboard_vals.append(execution_timer)

    # checks for WAR hazards
    prev_inst_read = 0
    prev_instruction = scoreboard[inst_num - 1][0]
    # goes through the previous instruction and gets the registers
    for i in range(len(prev_instruction)):
        if (prev_instruction[i] == "F"):
            prev_reg.append(prev_instruction[i:i + 2])
    #if the previous instruction only has one register then we know it is a read or store so it gets the read value
    # since it would break based on our second condition
    if (len(prev_reg) == 1):
        prev_inst_read = int(scoreboard[inst_num - 1][2])

    #if the source registers of the previous instruction are equal to the destination register then it gets the read val
    elif (prev_reg[1] == load_reg or prev_reg[2] == load_reg):

        prev_inst_read = int(scoreboard[inst_num - 1][2])

    # if the reads are greater than the execution timer then it stalls and sets the write back timer to the read + 1
    if (prev_inst_read > execution_timer):
        write_back_timer = prev_inst_read + INTEGER_CYCLES
    else:
        write_back_timer = execution_timer + INTEGER_CYCLES

    # puts the values in an array
    scoreboard_vals.append(write_back_timer)

    # sets the registers to the right values
    set_fp_reg_location(load_reg,mem_val)

    return scoreboard_vals


# calc_store_scoreboard
# Takes in the instruction number, the location, the value of the register, the register and the scoreboard
# Returns the clock cycle values - checks for hazards
def calc_store_scoreboard(inst_num, mem_val, load_reg, register, scoreboard):
    # initalizes values for the cycles and such
    scoreboard_vals = []
    issue_timer = 0
    read_operand_timer = 0
    execution_timer = 0
    write_back_timer = 0

    # checks if other integer units are being used
    prev_stores_wb_times = []
    # goes through all of the previous instructions to check for structural hazards
    for i in range(inst_num, 0, -1):
        instruction = scoreboard[inst_num - 1][0]
        if (scoreboard[i - 1][0][0] == "L" or scoreboard[i - 1][0][0:3] == "S.D"
                or scoreboard[i - 1][0][0:4] == "ADDI" or scoreboard[i - 1][0][0:4] == "ADD"
                or scoreboard[i - 1][0][0:4] == "SUB"):
            prev_stores_wb_times.append(scoreboard[i - 1][4])


    prev_inst_issue = scoreboard[inst_num - 1][1]
    # does some arithmetic to check if the previous write back timers are greater than the previous instruction
    # issue which dictates where to start for the store instruction
    if (prev_stores_wb_times != []):
        if (max(prev_stores_wb_times) > prev_inst_issue):
            issue_timer = max(prev_stores_wb_times) + INTEGER_CYCLES
        else:
            issue_timer = prev_inst_issue + INTEGER_CYCLES
    else:
        issue_timer = prev_inst_issue + INTEGER_CYCLES

    # there is no WAW hazards for a store because a store does not write only reads
    scoreboard_vals.append(issue_timer)

    # checking for RAW
    prev_wb_time = 0
    for i in range(inst_num, 0, -1):
        prev_reg = []
        instruction = scoreboard[i - 1][0]
        len_instruction = len(instruction)

        #gets the previous instructions' registers
        for j in range(len_instruction):
            if (instruction[j] == "F"):
                prev_reg.append(instruction[j:j + 2])

        # if there are no floating point registers then skip
        if (prev_reg == []):
            continue

        # if the register is equal to the destination register of the previous
        # then it gets that instruction's write back time
        if (register == prev_reg[0]):
            prev_wb_time = int(scoreboard[i - 1][4])
            break
        else:
            continue

    # if the previous write back is greater than the issue then we have to stall otherwise just keep going
    if (prev_wb_time > issue_timer):
        read_operand_timer = prev_wb_time + INTEGER_CYCLES
    else:
        read_operand_timer = issue_timer + INTEGER_CYCLES

    scoreboard_vals.append(read_operand_timer)

    execution_timer = read_operand_timer + INTEGER_CYCLES
    scoreboard_vals.append(execution_timer)

    write_back_timer = execution_timer + INTEGER_CYCLES
    scoreboard_vals.append(write_back_timer)

    # sets the memory location's new value
    set_mem_location(mem_val, load_reg)

    return scoreboard_vals

# calc_add_sub_scoreboard
# checks for hazards for the add and subs- takes in instruction number, the memory value, the registers
# and the scoreboard
# Returns the clock cycle values - checks for hazards
def calc_add_sub_scoreboard(inst_num, mem_val, registers, scoreboard):
    # initializes the variables for the cycle values
    scoreboard_vals = []
    issue_timer = 0
    issue_timer_check = 0
    read_operand_timer = 0
    execution_timer = 0
    write_back_timer = 0

    # gets the destination and source registers
    dest_reg = registers[0]
    source_reg1 = registers[1]
    source_reg2 = registers[2]

    # checks to see if units are being used
    prev_stores_wb_times = []
    # goes through all of the previous instructions to check for structural hazards
    for i in range(inst_num, 0, -1):
        instruction = scoreboard[inst_num - 1][0]
        if (scoreboard[i - 1][0][0:5] == "ADD.D" or scoreboard[i - 1][0][0:5] == "SUB.D"):
            prev_stores_wb_times.append(scoreboard[i - 1][4])

    prev_inst_issue = scoreboard[inst_num - 1][1]
    # gets the largest write back time of the previous instructions with the add unit
    if (prev_stores_wb_times != []):
        if (max(prev_stores_wb_times) > prev_inst_issue):
            issue_timer_check = max(prev_stores_wb_times) + INTEGER_CYCLES
        else:
            issue_timer_check = prev_inst_issue + INTEGER_CYCLES
    else:
        issue_timer_check = prev_inst_issue + INTEGER_CYCLES
    prev_wb_times = 0

    # checks for WAW hazards by going through the previous instructions and checking for
    # the same destination registers
    for i in range(inst_num, 0, -1):
        prev_regs = []
        instruction = scoreboard[i - 1][0]
        len_instruction = len(instruction)
        # goes through the instruction and grabs the registers
        for j in range(len_instruction):
            if (instruction[j] == "F"):
                prev_regs.append(instruction[j:j + 2])

        if (prev_regs == []):
            continue

        if (dest_reg == prev_regs[0]):
            prev_wb_times = int(scoreboard[i - 1][4])
            break
        else:
            continue

    # checks whether it needs to stall or not
    if (prev_wb_times > int(scoreboard[inst_num - 1][1])):
        issue_timer = prev_wb_times + INTEGER_CYCLES
    else:
        issue_timer = int(scoreboard[inst_num - 1][1]) + INTEGER_CYCLES
    # checks whether to stall the longest for the WAW or structural hazard
    if (issue_timer_check > issue_timer):
        issue_timer = issue_timer_check

    scoreboard_vals.append(issue_timer)
    # Checks for RAW hazards by going through the previous instructions and comparing the source registers with
    # the previous destination registers
    prev_wb_time = 0
    for i in range(inst_num, 0, -1):
        prev_reg = []
        instruction = scoreboard[i - 1][0]
        len_instruction = len(instruction)

        for j in range(len_instruction):
            if (instruction[j] == "F"):
                prev_reg.append(instruction[j:j + 2])

        # if the previous registers were integer registers or it was a store instruction then skip
        # the reason for the store instruction was because a store does not write
        if (prev_reg == [] or instruction[0:3] == "S.D"):
            continue

        # compares the source registers and the previous destination register, if there is a ht
        # then it gets the previous write back time for more checks
        if (source_reg1 == prev_reg[0] or source_reg2 == prev_reg[0]):
            prev_wb_time = int(scoreboard[i - 1][4])
            break
        else:
            continue
    # if the previous write back timer is greater than the issue value then it has to stall
    if (prev_wb_time > issue_timer):
        read_operand_timer = prev_wb_time + INTEGER_CYCLES
    else:
        read_operand_timer = issue_timer + INTEGER_CYCLES

    scoreboard_vals.append(read_operand_timer)

    execution_timer = read_operand_timer + FP_ADDER_CYCLES
    scoreboard_vals.append(execution_timer)

    prev_read_time = 0
    # checks for WAR hazards by going through the previous instructions and comparing the destination registers
    # with the source registers
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

            # if the array was integer registers or it only has 1 register then it skips
            if (prev_reg_war == [] or len(prev_reg_war) == 1):
                continue

            # if there is a hit then it gets the previous read time
            if (dest_reg == prev_reg_war[1] or dest_reg == prev_reg_war[2]):
                prev_read_time = int(scoreboard[i - 1][2])
                break
            else:
                continue
        # compares and decides whether to stall or not
        if (prev_read_time > execution_timer):
            write_back_timer = prev_read_time + INTEGER_CYCLES
        else:
            write_back_timer = execution_timer + INTEGER_CYCLES

    scoreboard_vals.append(write_back_timer)
    # sets the registers to the correct values
    set_fp_reg_location(dest_reg, mem_val)

    return scoreboard_vals

# calc_immediates_scoreboard
# Checks for hazards for integer adds and subs- takes in the instruction number, memory value, the registers
# and the scoreboard
# Returns the clock cycle values - checks for hazards
def calc_immediates_scoreboard(inst_num, mem_val, registers, scoreboard):
    # initializes variables
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

    # checks to see if units are being used by going through the previous instructions and checking whether
    # they are the same unit, if there are other instructions using the integer unit then it gets the write back time
    # for comparison
    prev_stores_wb_times = []
    for i in range(inst_num, 0, -1):
        instruction = scoreboard[inst_num - 1][0]
        if (scoreboard[i - 1][0][0] == "L" or scoreboard[i - 1][0][0:3] == "S.D" or
                scoreboard[i - 1][0][0:4] == "ADDI" or scoreboard[i - 1][0][0:4] == "ADD"
                or scoreboard[i - 1][0][0:4] == "SUB"):
            prev_stores_wb_times.append(scoreboard[i - 1][4])

    prev_inst_issue = scoreboard[inst_num - 1][1]
    # gets the highest write back to decide if there is a structural hazard or not
    if (prev_stores_wb_times != []):
        if (max(prev_stores_wb_times) > prev_inst_issue):
            issue_timer_check = max(prev_stores_wb_times) + INTEGER_CYCLES
        else:
            issue_timer_check = prev_inst_issue + INTEGER_CYCLES
    else:
        issue_timer_check = prev_inst_issue + INTEGER_CYCLES

    # checks for WAW hazards by going through the previous instructions and checking the destination registers
    prev_wb_waw_times = 0
    for i in range(inst_num, 0, -1):
        prev_regs = []
        instruction = scoreboard[i - 1][0]
        len_instruction = len(instruction)
        # goes through the instruction and grabs the registers
        for j in range(len_instruction):
            if (instruction[j] == "$"):
                prev_regs.append(instruction[j:j + 2])

        if (prev_regs == []):
            continue

        if (dest_reg == prev_regs[0]):
            prev_wb_times = int(scoreboard[i][4])
            break
        else:
            continue
    # checks if there is a reason to stall or not
    if (prev_wb_waw_times > int(scoreboard[inst_num - 1][1])):
        issue_timer = prev_wb_waw_times + INTEGER_CYCLES
    else:
        issue_timer = int(scoreboard[inst_num - 1][1])
    # comparison to see how long to stall based on the WAW hazard or the structural hazard
    if (issue_timer_check > issue_timer):
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
        # this is here to tell whether the instruction is an ADDI. if it is then it handles it here so there is no
        # error with our other conditions
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
    # sets the read operand clock cycle by deciding whether we need to stall or not
    if (prev_wb_raw_time > issue_timer):
        read_operand_timer = prev_wb_raw_time + INTEGER_CYCLES
    else:
        read_operand_timer = issue_timer + INTEGER_CYCLES

    scoreboard_vals.append(read_operand_timer)
    execution_timer = read_operand_timer + INTEGER_CYCLES
    scoreboard_vals.append(execution_timer)

    prev_read_time = 0
    # checks for WAR by comparing the the previous instructions source registers with the current instruction's
    # destination register
    for i in range(inst_num, 0, -1):
        prev_reg_war = []
        instruction = scoreboard[i - 1][0]
        len_instruction = len(instruction)

        for j in range(len_instruction):
            if (instruction[j] == "$"):
                prev_reg_war.append(instruction[j:j + 2])

        if (prev_reg_war == [] or len(prev_reg_war) == 1):
            continue

        # in case there is an ADDI, condition to check so that it can handle the ADDI and not break
        if(len(prev_reg_war) == 2):
            if(dest_reg == prev_reg_war[1]):
                prev_read_time = int(scoreboard[i-1][2])
                break
            else:
                continue

        # gets the read times of the previous instructions if there is a hit
        if (dest_reg == prev_reg_war[1] or dest_reg == prev_reg_war[2]):
            prev_read_time = int(scoreboard[i - 1][2])
            break
        else:
            continue
    # decides whether to stall or not
    if (prev_read_time > execution_timer):
        write_back_timer = prev_read_time + INTEGER_CYCLES
    else:
        write_back_timer = execution_timer + INTEGER_CYCLES

    scoreboard_vals.append(write_back_timer)
    # sets the integer registers values
    set_int_reg_location(dest_reg, mem_val)

    return scoreboard_vals

# calc_multiply scoreboard
# Checks for hazards for the multiply instruction- takes in the instruction number, the memory value, the registers
# and the scoreboard
# Returns the clock cycle values - checks for hazards
def calc_multiply_scoreboard(inst_num, mem_val, registers, scoreboard):
    # initializes variables
    scoreboard_vals = []
    issue_timer = 0
    issue_timer_check = 0
    read_operand_timer = 0
    execution_timer = 0
    write_back_timer = 0

    # gets the registers
    dest_reg = registers[0]
    source_reg1 = registers[1]
    source_reg2 = registers[2]

    # checks to see if units are being used by going through the previous instructions and seeing if another MUL.D has
    # occured
    prev_stores_wb_times = []
    for i in range(inst_num, 0, -1):
        instruction = scoreboard[inst_num - 1][0]
        if (scoreboard[i - 1][0][0:5] == "MUL.D"):
            prev_stores_wb_times.append(scoreboard[i - 1][4])

    prev_inst_issue = scoreboard[inst_num - 1][1]
    if (prev_stores_wb_times != []):
        # if there is a hit it gets the highest write back time to compare to the current instruction
        if (max(prev_stores_wb_times) > prev_inst_issue):
            issue_timer_check = max(prev_stores_wb_times) + INTEGER_CYCLES
        else:
            issue_timer_check = prev_inst_issue + INTEGER_CYCLES
    else:
        issue_timer_check = prev_inst_issue + INTEGER_CYCLES

    prev_wb_waw_times = 0
    # checks for WAW hazards by looping through the previous instructions and comparing the destination registers
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
    # checks whether to stall or not
    if (prev_wb_waw_times > int(scoreboard[inst_num - 1][1])):
        issue_timer = prev_wb_waw_times + INTEGER_CYCLES
    else:
        issue_timer = int(scoreboard[inst_num - 1][1])

    # decides whether to stall for the WAW or structural hazard
    if (issue_timer_check > issue_timer):
        issue_timer = issue_timer_check

    scoreboard_vals.append(issue_timer)
    prev_wb_raw_time = 0
    # checks for RAW hazards by looping through the previous instruction and compares the source registers of the
    # current instruction to the previous registers' destination register
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
    # decides whether to stall or not
    if (prev_wb_raw_time > issue_timer):
        read_operand_timer = prev_wb_raw_time + INTEGER_CYCLES
    else:
        read_operand_timer = issue_timer + INTEGER_CYCLES

    scoreboard_vals.append(read_operand_timer)

    execution_timer = read_operand_timer + FP_MULTI_CYCLES
    scoreboard_vals.append(execution_timer)

    prev_read_time = 0
    # checks for WAR hazards by looping through the previous instructions and comparing the current instruction's
    # destination register with the previous instructions' source registers
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
                prev_read_time = int(scoreboard[i - 1][2])
                break
            else:
                continue
        # decides whether to stall or not
        if (prev_read_time > execution_timer):
            write_back_timer = prev_read_time + INTEGER_CYCLES
        else:
            write_back_timer = execution_timer + INTEGER_CYCLES

    scoreboard_vals.append(write_back_timer)
    # sets the register values
    set_fp_reg_location(dest_reg, mem_val)

    return scoreboard_vals

# calc_division_scoreboard
# Checks for hazards and gets the clock cycle values- takes in the instruction number, the memory value, the registers,
# and the scoreboard
# Returns the clock cycle values - checks for hazards
def calc_division_scoreboard(inst_num, mem_val, registers, scoreboard):
    # initializes the array and the values
    scoreboard_vals = []
    issue_timer = 0
    issue_timer_check = 0
    read_operand_timer = 0
    execution_timer = 0
    write_back_timer = 0
    # gets the registers
    dest_reg = registers[0]
    source_reg1 = registers[1]
    source_reg2 = registers[2]

    # checks to see if units are being used (structural hazard) by looping through the previous instructions
    # and getting the write back times of the previous instructions that is the same as the current
    prev_stores_wb_times = []
    for i in range(inst_num, 0, -1):
        instruction = scoreboard[inst_num - 1][0]
        if (scoreboard[i - 1][0][0:5] == "DIV.D"):
            prev_stores_wb_times.append(scoreboard[i - 1][4])

    prev_inst_issue = scoreboard[inst_num - 1][1]
    # decides whether to stall or not
    if (prev_stores_wb_times != []):
        if (max(prev_stores_wb_times) > prev_inst_issue):
            issue_timer_check = max(prev_stores_wb_times) + INTEGER_CYCLES
        else:
            issue_timer_check = prev_inst_issue + INTEGER_CYCLES
    else:
        issue_timer_check = prev_inst_issue + INTEGER_CYCLES

    prev_wb_waw_times = 0
    # checks for WAW hazards by looping through the previous instructions and comparing their destination registers
    # with the destination register of the current instruction
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
    # decides whether to stall or not
    if (prev_wb_waw_times > int(scoreboard[inst_num - 1][1])):
        issue_timer = prev_wb_waw_times + INTEGER_CYCLES
    else:
        issue_timer = int(scoreboard[inst_num - 1][1])

    # decides whether to stall due to WAW or structural hazard
    if (issue_timer_check > issue_timer):
        issue_timer = issue_timer_check

    scoreboard_vals.append(issue_timer)
    prev_wb_raw_time = 0
    # checks for RAW hazards by looping through the previous instructions and comparing their destination registers
    # with the source registers of the current instruction
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
    # decides whether to stall or not
    if (prev_wb_raw_time > issue_timer):
        read_operand_timer = prev_wb_raw_time + INTEGER_CYCLES
    else:
        read_operand_timer = issue_timer + INTEGER_CYCLES

    scoreboard_vals.append(read_operand_timer)

    execution_timer = read_operand_timer + FP_DIVIDER_CYCLES
    scoreboard_vals.append(execution_timer)

    prev_read_time = 0
    # checks for WAR hazards by looping through the previous instructions and comparing their source registers
    # with the destination register of the current instruction
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
                prev_read_time = int(scoreboard[i - 1][2])
                break
            else:
                continue
        # decides whether to stall or not
        if (prev_read_time > execution_timer):
            write_back_timer = prev_read_time + INTEGER_CYCLES
        else:
            write_back_timer = execution_timer + INTEGER_CYCLES

    scoreboard_vals.append(write_back_timer)
    # sets the registers values
    set_fp_reg_location(dest_reg, mem_val)

    return scoreboard_vals

# call to main
main()
