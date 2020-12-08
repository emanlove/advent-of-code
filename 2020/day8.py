import sys

def read_boot_code(filename):
    with open(filename,'r') as fh:
        boot_code = [line.rstrip('\n') for line in fh]

    return boot_code

if __name__ == "__main__":
    file = sys.argv[1]
    boot_code = read_boot_code(file)

    accumulator = 0
    visited_line = [0] * len(boot_code)

    ipntr = 0
    while True:
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
        else:
            print(f"ERROR: Unknown operation - {ipntr}:{operation}")
            break
