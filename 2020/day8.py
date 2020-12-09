import sys,copy

def read_boot_code(filename):
    with open(filename,'r') as fh:
        boot_code = [line.rstrip('\n') for line in fh]

    return boot_code

def _operation(line,program):
    operation,argument = program[line].split()
    return operation

def replaceOperation(operation,line,program):
    alt_program = copy.deepcopy(program)
    old_operation = _operation(line,alt_program)
    alt_program[line] = operation + alt_program[line][3:]
    return alt_program

def executeCode(code):
    accumulator = 0
    visited_line = [0] * len(code)

    ipntr = 0
    while True:
        if ipntr == len(code):
            print(f"COMPLETED: Boot code completed execution!  accumulator:{accumulator}")
            break
        if visited_line[ipntr]:
            print(f"WARNING: Infinite Loop discovered! accumulator:{accumulator}")
            break

        visited_line[ipntr] = 1
        operation,argument = code[ipntr].split()

        if operation=='nop':
            ipntr += 1
        elif operation=='acc':
            accumulator += int(argument)
            ipntr += 1
        elif operation=='jmp':
            ipntr += int(argument)
            if ipntr > len(code) or ipntr < 0:
                print(f"ERROR: jmp operation out of bounds - {ipntr-int(argument)}->{ipntr}")
                break
        else:
            print(f"ERROR: Unknown operation - {ipntr}:{operation}")
            break

    return accumulator, visited_line

if __name__ == "__main__":
    file = sys.argv[1]
    boot_code = read_boot_code(file)

    print("\nPart One:")
    acummulator,visited_line = executeCode(boot_code)

    print("\nPart Two:")
    nop_before_infinite_loop = [line for line,visited in enumerate(visited_line) if _operation(line,boot_code)=='nop']

    for nop_line in nop_before_infinite_loop:
        modified_boot_code = replaceOperation('jmp',nop_line,boot_code)
        acummulator,visited_line = executeCode(modified_boot_code)

    jmp_before_infinite_loop = [line for line,visited in enumerate(visited_line) if _operation(line,boot_code)=='jmp']

    for jmp_line in jmp_before_infinite_loop:
        modified_boot_code = replaceOperation('nop',jmp_line,boot_code)
        acummulator,visited_line = executeCode(modified_boot_code)
