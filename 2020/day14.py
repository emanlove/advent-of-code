import sys, re

def read_init_program(filename):
    with open(filename,'r') as fh:
        program = [line.rstrip('\n') for line in fh]

    return program

# `setbit` and `clear_bit` are from RealPython
# https://realpython.com/python-bitwise-operators/#bitmasks

def set_bit(value, bit_index):
    return value | (1 << bit_index)

def clear_bit(value, bit_index):
    return value & ~(1 << bit_index)

def isBitMaskInstruction(instruction):
    instr,val = instruction.split(' = ')
    return True if instr=='mask' else False

def updateMask(instruction):
    _,mask = instruction.split(' = ')
    ones=[indx for indx,bit in enumerate(mask[::-1]) if bit=='1']
    zeros=[indx for indx,bit in enumerate(mask[::-1]) if bit=='0']
    xes=[indx for indx,bit in enumerate(mask[::-1]) if bit=='X']

    return ones,zeros,xes

def parseMemoryInstruction(instruction):
    addrStr,valStr=instruction.split(' = ')
    matches = re.findall(r'\[(\d*)\]',addrStr)
    addr = int(matches[0])
    val = int(valStr)
    return addr,val

if __name__ == "__main__":
    file = sys.argv[1]

    program = read_init_program(file)

    ones=[]
    zeros=[]
    memory = {}
    for line in program:
        if isBitMaskInstruction(line):
            ones,zeros,xes = updateMask(line)
        else:
            address,value = parseMemoryInstruction(line)
            #print(f"{address:036b}")
            for one in ones:
                address = set_bit(address,one) 
                #print(f"{address:036b}")

            numXes = len(xes)
            addrMasks = [f'{n:0{numXes}b}' for n in range(2**numXes)]
            for mask in addrMasks:
                addr36Bin = list(f'{address:036b}')
                for bit,x in enumerate(xes):
                    addr36Bin[-x-1]=mask[bit]

                addr36Str = ''.join(addr36Bin) 
                addr = int(addr36Str,base=2)
                #print(f"{addr36Str}  {addr}:{value}")
                memory[addr] = value

    mem_total = sum(memory[a] for a in memory)
    print(f"The total in the memory is {mem_total}")
