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

def _opcode(value):
    if isinstance(value,int):
        value=str(value)
        
    if isinstance(value,str):
        value=value.zfill(5)

        operation = value[-2:]
        firstpmode = int(value[-3])
        secondpmode = int(value[-4])
        thirdpmode = int(value[-5])

        return thirdpmode,secondpmode,firstpmode,operation
    
    
def executeMultiCodeProgram(program,input=None):
    thirdpmode,secondpmode,firstpmode,operation = _opcode(program[0])
    
    pindx = 0
    
    while operation != '99':
        if operation=='01':
            #print(f"{program[pindx:pindx+4]}")
            program[program[pindx+3]] = (program[pindx+1] if firstpmode else program[program[pindx+1]]) + \
              (program[pindx+2] if secondpmode else program[program[pindx+2]])
            #program[program[pindx+3]] = program[program[pindx+1]] + program[program[pindx+2]]
            pindx += 4
        elif operation=='02':
            #print(f"{program[pindx:pindx+4]}")
            program[program[pindx+3]] = (program[pindx+1] if firstpmode else program[program[pindx+1]]) * \
              (program[pindx+2] if secondpmode else program[program[pindx+2]])
            #program[program[pindx+3]] = program[program[pindx+1]] * program[program[pindx+2]]
            pindx += 4
        elif operation=='03':
            #print(f"{program[pindx:pindx+2]}")
            program[program[pindx+1]] = input
            pindx += 2
        elif operation=='04':
            print(f"{program[pindx:pindx+2]}")
            #print(f"output: {program[program[pindx+1]]}")
            print(f"output: {program[pindx+1] if firstpmode else program[program[pindx+1]]}")
            #if program[program[pindx+1]] != 0:
            #    print(f"{program[pindx:pindx+2]}")
            pindx += 2
        else:
            print(f"Error - Illegal opcode:{opcode}")

        thirdpmode,secondpmode,firstpmode,operation = _opcode(program[pindx])
        #print(f"new opcode: {operation}")
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
            result = executeMultiCodeProgram(program)

            if result[0]==19690720:
                return (noun,verb)
    return (None,None)
    
if __name__ == "__main__":
    progfile = sys.argv[1]

    program = loadProgram(progfile)
    #program[1] = 12
    #program[2] = 2
    result = executeMultiCodeProgram(program,1)

    #print(f"{result}")
    print(f"The Intcode program results with {result[0]} in position 0.")

    #(n,v) = match_nv_output(progfile)
    #
    #print(f"Using noun [{n}] and verb [{v}] the Intcode program results with 19690720.")
    #print(f"Answer: {100*n+v}")
