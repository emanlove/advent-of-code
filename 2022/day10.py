import sys

def read_instructions(filename):
    with open(filename,'r') as fh:
        instructions = [line.rstrip('\n') for line in fh]

    return instructions

def run_program(program):
    # import pdb; pdb.set_trace()    
    X = [None, 1]

    for instr in program:
        cmd,*args = instr.split(' ')

        if cmd == 'noop':
            X.append(X[-1])
        elif cmd == 'addx':
            X.append(X[-1])
            # X.append(X[-1]) # should only be two cycles
            register = X[-1] + int(args[0])
            X.append(register)

    return X

def get_signal_strength(reg, cycles):
    signal_strengths = {}
    for cycle in cycles:
        reg_value = reg[cycle]
        strength = cycle * reg_value
        signal_strengths[cycle] = strength
        print(f"cycle: {cycle}  register: {reg_value}  signal_strength: {strength} ")

    return signal_strengths

def crt_draw(cycles):
    screen = [None for _ in range(240)]
    for pixel,reg_value in enumerate(cycles[1:241]):
        cycle = pixel+1
        # print(f"{cycle}")
        pos = pixel % 40
        # print(f"p{pixel}  v{reg_value}")
        # if reg_value-1 <= pixel <= reg_value+1:
        if pos in range(reg_value-1,reg_value+2):
            screen[pixel] = '#'
        else:
            screen[pixel] = '.'

    crt = [screen[x:x+40] for x in range(0,len(screen),40)]
    crt = [''.join(line) for line in crt]

    for line in crt:
        print(f"{line}")
    # import pdb; pdb.set_trace()

if __name__ == "__main__":
    file = sys.argv[1]

    program = read_instructions(file)

    cycles = run_program(program)

    # print(f"{cycles}")

    # import pdb;pdb.set_trace()
    signal_strengths = get_signal_strength(cycles, [20, 60, 100, 140, 180, 220])
    total_strengths = sum(list(signal_strengths.values()))
    print(f"The sum of the signal strengths is {total_strengths}")
    part1_ans = total_strengths

    # print(f"The total number of unique positions the last knot visited is {num_unique_pos_last_knot_visited}")
    # part2_ans = num_unique_pos_last_knot_visited

    crt_draw(cycles)

    if len(sys.argv) >= 3:
        if int(sys.argv[2]) == part1_ans:
            print(f"Answer for part 1 is correct!")
    if len(sys.argv) == 4:
        if int(sys.argv[3]) == part2_ans:
            print(f"Answer for part 2 is correct!")

