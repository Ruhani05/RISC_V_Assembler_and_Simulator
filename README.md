# RISC-V-Assembler-and-Simulator-in a team of four IIITD students
Implementation of a subset of RV32I (RISC-V 32-bit integer) instruction set using simple assembler and simulator.
(This was a college group project)

#How to Run Sample Testcases:
1. we have simple and hard tests both at the assembler level and simulator level.

2. The tests for assembler and simulator are independent.

3. Assembler test content is within "tests/assembly/".
The folder simpleBin, hardBin, errorGen contains the files for input assembly code.
The folder bin_s contains the exact machine code file corresponding to the tests inside simpleBin. Similarly for bin_h.
The folder user_bin_s, user_bin_h contains the machine code created by student's Assembler for simpleBin, hardBin respectivly.

4. Simulator test content is within "tests/bin/", tests/traces/".
The folder "tests/traces/" contains correct expected simulator traces. 
The folder "tests/bin/" contains simultor traces generated by student's simulator.

Utilization steps (for students)
This framework is for python users only.

Assembler must take a assembly code file as input and produce a machine code file as output.
All input and output files need to be stroed with ".txt" extensions.
Format $python3 Assembler.py input_assembly_code_file_path output_machine_code_file_path
1. Rename your assembler code file as "Assembler.py"
2. Place this file inside the already created SimpleAssembler folder.
For linux users: $python3 src/main.py --no-sim --linux
For windows user: >python3 src\main.py --no-sim --windows


Simulator must take a machine code file as input and produce a trace file as output.
All input and output files need to be stored with ".txt" extentions.
Format $python3 Simulator.py input_machine_code_file_path output_trace_file_path
1. Rename your simulator code file as "Simulator.py"
2. Place this file inside the already created SimpleSimulator folder.
For linux users: $python3 src/main.py --no-asm --linux
For windows user: >python3 src\main.py --no-asm --windows

