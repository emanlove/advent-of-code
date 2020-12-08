import sys

def read_boot_code(filename):
    with open(filename,'r') as fh:
        boot_code = [line.rstrip('\n') for line in fh]

    return boot_code

def _operation(line,program):
    operation,argument = program[line].split()
    return operation
    
if __name__ == "__main__":
    file = sys.argv[1]
    boot_code = read_boot_code(file)

    accumulator = 0
    visited_line = [0] * len(boot_code)

    ipntr = 0
    while True:
        if ipntr == len(boot_code):
            print(f"COMPLETED: Boot code completed execution!  accumulator:{accumulator}")
            break
        if visited_line[ipntr]:
            print(f"WARNING: Infinite Loop discovered! accumulator:{accumulator}")
            break

        visited_line[ipntr] = 1
        operation,argument = boot_code[ipntr].split()

        if operation=='nop':
            ipntr += 1
        elif operation=='acc':
            accumulator += int(argument)
            ipntr += 1
        elif operation=='jmp':
            ipntr += int(argument)
            if ipntr > len(boot_code) or ipntr < 0:
                print(f"ERROR: jmp operation out of bounds - {ipntr-int(argument)}->{ipntr}")
                break
        else:
            print(f"ERROR: Unknown operation - {ipntr}:{operation}")
            break

    nop_before_infinite_loop = [line for line,visited in enumerate(visited_line) if _operation(line,boot_code)=='nop']
    jmp_before_infinite_loop = [line for line,visited in enumerate(visited_line) if _operation(line,boot_code)=='jmp']
