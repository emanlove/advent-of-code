import sys

def read_document(filename):
    with open(filename,'r') as fh:
        lines = [line.rstrip('\n') for line in fh]
    
    lr_instructions = [c for c in lines[0]]
    map = {}
    for line in lines[2:]:
        node, next_elements = line.split(' = ')
        left, right = next_elements[1:-1].split(', ')
        map[node] = {'L':left, 'R':right}

    return lr_instructions, map

if __name__ == "__main__":
    file = sys.argv[1]

    lr_instructions,map = read_document(file)

    node = 'AAA'
    len_inst = len(lr_instructions)
    inst_indx = 0
    steps = 0
    while node != 'ZZZ':
        move_direction = lr_instructions[inst_indx]
        node = map[node][move_direction]
        steps += 1
        inst_indx +=1
        if inst_indx == len_inst:
            inst_indx = 0
    
    print(f"The number of steps required to reach ZZZ is {steps}")
