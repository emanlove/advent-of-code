import sys, re

def read_init_program(filename):
    with open(filename,'r') as fh:
        program = [line.rstrip('\n') for line in fh]

    maskStr = program[0]
    _,mask = maskStr.split(' = ')
    ones=[indx for indx,bit in enumerate(mask[::-1]) if bit=='1']
    zeros=[indx for indx,bit in enumerate(mask[::-1]) if bit=='0']
    
    instructions = []
    for instr in program[1:]:
        addrStr,valStr=instr.split(' = ')
        matches = re.findall(r'[(\d*)]',addrStr)
        addr = int(matches[0])
        #val = int(valStr,base=2)
        val = int(valStr)
        instructions.append((addr,val))

    return ones,zeros,instructions

# `setbit` and `clear_bit` are from RealPython
# https://realpython.com/python-bitwise-operators/#bitmasks

def set_bit(value, bit_index):
    return value | (1 << bit_index)

def clear_bit(value, bit_index):
    return value & ~(1 << bit_index)

if __name__ == "__main__":
    file = sys.argv[1]

    ones,zeros,instructions = read_init_program(file)

    memory = {}
    for instr in instructions:
        value = int(instr[1])
        print(f"{value:036b}")
        for one in ones:
            value = set_bit(value,one)
            print(f"{value:036b}")
        for zero in zeros:
            value = clear_bit(value,zero)
            print(f"{value:036b}")

        addr = instr[0]

        print(f"{addr}:{value}")
        memory[addr] = value

    mem_total = sum(memory[a] for a in memory)
    print(f"The total in the memory is {mem_total}")
