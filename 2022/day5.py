import sys

NUM_STACKS = 9

def read_stacks_and_procedures(filename):
    with open(filename,'r') as fh:
        s_and_p = [line.rstrip('\n') for line in fh]

    return s_and_p

def extract_stacks_and_procedures(s_and_p):

    # find line seperating stacks from procedures
    indx_break = s_and_p.index('')

    stacks = s_and_p[:indx_break]
    procedures = s_and_p[indx_break+1:]

    return stacks, procedures

def parse_procedures(lines):
    procedures = []
    # import pdb;pdb.set_trace()

    for line in lines:
        mv_frm, to = line.split(' to ')
        mv_cnt, frm = mv_frm.split(' from ')
        _, count = mv_cnt.split('move ')
        procedures.append({'move':int(count), 'from':int(frm), 'to':int(to)})

    return procedures

def parse_stacks(lines):
    """ Based upon the input data of nine stacks this method will be highly specific to
        that data.
    """
    STACK_INDXS = [1+(col*4) for col in range(NUM_STACKS)]

    stacks = [[] for _ in range(NUM_STACKS+1)]

    # import pdb;pdb.set_trace()
    for line in lines[-2::-1]:
        for stack,data_col in enumerate(STACK_INDXS):
            if line[data_col] != ' ':
                stacks[stack+1].append(line[data_col])

    return stacks

def move(stacks,count,frm,to):
    for _ in range(count):
        crate = stacks[frm].pop()
        stacks[to].append(crate)

    return stacks

def move_9001(stacks,count,frm,to):
    temp = []
    for _ in range(count):
        crate = stacks[frm].pop()
        temp.insert(0,crate)

    stacks[to] += temp

    return stacks

def top_of_stacks(stacks):
    tops = ''
    for indx in range(1,NUM_STACKS+1):
        stack_top = stacks[indx].pop()
        tops += stack_top
    
    return tops

if __name__ == "__main__":
    file = sys.argv[1]

    stacks_and_procedures = read_stacks_and_procedures(file)
    s_data, p_data = extract_stacks_and_procedures(stacks_and_procedures)
    procedures = parse_procedures(p_data)
    stacks = parse_stacks(s_data)

    for proc in procedures:
        move_9001(stacks,proc['move'],proc['from'],proc['to'])

    tops = top_of_stacks(stacks)

    print(f"The top of the stacks is {tops}")
    part1_ans = tops

    # print(f"The total sum of priorities for three elves in a group is {total_priorities_amongst_3_elves}")
    # part2_ans = total_priorities_amongst_3_elves

    if len(sys.argv) == 3:
        if sys.argv[2] == part1_ans:
            print(f"Answer for part 1 is correct!")
    # if len(sys.argv) == 4:
    #     if int(sys.argv[3]) == part2_ans:
    #         print(f"Answer for part 2 is correct!")
