import sys

def executeProgram(program):

    for oindx,original_opcode in enumerate(program[::4]):
        pindx=oindx*4
        opcode=program[pindx]
        if opcode==1:
            program[program[pindx+3]] = program[program[pindx+1]] + program[program[pindx+2]]
        elif opcode==2:
            program[program[pindx+3]] = program[program[pindx+1]] * program[program[pindx+2]]
        elif opcode==99:
            break
        else:
            print(f"Error - Illegal opcode:{opcode}")

    return program

def loadProgram(pfile):
    with open(pfile,'r') as fh:
        program = fh.readlines()

    programStr = program[0].rstrip('\n')
    programInt = [int(pos) for pos in programStr.split(',')]
    
    return programInt

if __name__ == "__main__":
    progfile = sys.argv[1]

    program = loadProgram(progfile)
    program[1] = 12
    program[2] = 2
    result = executeProgram(program)

    print(f"The Intcode program results with {result[0]} in position 0.")
