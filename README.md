# 411-Scoreboarding
CMSC 411 @ UMBC Scoreboarding project for Ivan
Nick Sica and Jack Huey

General Summary + User Instructions:
The way we designed the program requires users to enter in
the proper text file containing the MIPS code to be read in, and then
it will proceed to read in the file and calculate the scoreboard
The resulting scoreboard will be represented via a 2D array and printed out for the user to see
The resulting register values are also printed.

The way the scoreboard is first built is by creating a 2D array of the amount of instructions (rows)
and 5 columns. Once it is read in, each instruction is handled and given the correct clock cycles 
on the scoreboard.The program handles the scoreboard by instruction. There is a different function for each type of instruction
which allows for versatility and effectiveness. While this would hamper efficiency, tracking efficiency is unnecessary for this project. 

Specifics: The MIPS text file MUST be in the same directory. TESTED ON LINUX USING GL.

