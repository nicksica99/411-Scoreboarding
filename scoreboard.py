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
    instruction_array = []

    for i in range(len(instructionList)):
        newInstruction = instructionList[i].split("\n")

        instructionList.append(newInstruction)
