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

def match_nv_output(file):
    
    for noun in range(100):
        for verb in range(100):
            program = loadProgram(file)
            program[1] = noun
            program[2] = verb
            result = executeProgram(program)

            if result[0]==19690720:
                return (noun,verb)
    return (None,None)
    
if __name__ == "__main__":
    progfile = sys.argv[1]

    program = loadProgram(progfile)
    program[1] = 12
    program[2] = 2
    result = executeProgram(program)

    print(f"The Intcode program results with {result[0]} in position 0.")

    (n,v) = match_nv_output(progfile)

    print(f"Using noun [{n}] and verb [{v}] the Intcode program results with 19690720.")
    print(f"Answer: {100*n+v}")
