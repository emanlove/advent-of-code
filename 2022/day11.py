import sys

TOTAL_NUM_ROUNDS = 20

def read_notes(filename):
    with open(filename,'r') as fh:
        notes = [line.rstrip('\n') for line in fh]

    return notes

def parse_notes(notes):
    import pdb;pdb.set_trace()
    notes_on_monkeys = [notes[indx-6:indx] for indx,line in enumerate(notes) if line=='']

    monkeys = []
    for note in notes_on_monkeys:
        # Extract worry levels
        worry_levelSTR = note[1].lstrip('  Starting items: ').split(', ')
        worry_level = [int(_) for _ in worry_levelSTR]
        # Extract Operation
        oper = note[2].lstrip('  Operation: new = ')
        operand,operator,modifier = oper.split(' ')
        operation = {'operand':operand,'operator':operator,'modifier':modifier}
        # Extract Test
        test = int(note[3].lstrip('  Test: divisible by '))
        if_true = int(note[4].lstrip('    If true: throw to monkey '))
        if_false = int(note[5].lstrip('    If false: throw to monkey '))

        attr = {'worry_levels':worry_level, 'operation':operation, 'test':test, 'if_true':if_true, 'if_false':if_false}
        monkeys.append(attr)
    
    return monkeys

def inspect_item(level,oper):
    new_level = None

    if oper['operand'] == 'old':
        oper['operand'] = level
    else:
        oper['operand'] = int(oper['operand'])

    if oper['modifier'] == 'old':
        oper['modifier'] = level
    else:
        oper['modifier'] = int(oper['modifier'])

    if oper['operater'] == '+':
        new_level = oper['operand'] + oper['modifier']
    elif oper['operater'] == '*':
        new_level = oper['operand'] * oper['modifier']
    else:
        print(f"WARNING: Unkown operator!")
    
    return new_level

def throw_item(test):
    pass

# inspects an item
# factor in my relief
# tests your worry level
# monkey throws item

def play_keep_away(monkeys):
    monkey_activity = [0 for _ in range(len(monkeys))]

    for round in range(TOTAL_NUM_ROUNDS):
        for monkey in monkeys:
            for item in monkey['worry_level']:
                # inspects an item
                inspected_level = inspect_item(item, monkey['operation'])
                # factor in my relief
                relief_level = inspected_level//3
                # monkey tests your worry level and throws item
                if relief_level % monkey['test']:
                    monkeys[monkey['if_true']]['worry_level'] = relief_level
                else:
                    monkeys[monkey['if_false']]['worry_level'] = relief_level            
            monkey['worry_level'] = []

if __name__ == "__main__":
    file = sys.argv[1]

    notes = read_notes(file)
    notes_about_monkeys = parse_notes(notes)

    # print(f"The sum of the signal strengths is {total_strengths}")
    # part1_ans = total_strengths

    # print(f"The total number of unique positions the last knot visited is {num_unique_pos_last_knot_visited}")
    # part2_ans = num_unique_pos_last_knot_visited

    if len(sys.argv) >= 3:
        if int(sys.argv[2]) == part1_ans:
            print(f"Answer for part 1 is correct!")
    if len(sys.argv) == 4:
        if int(sys.argv[3]) == part2_ans:
            print(f"Answer for part 2 is correct!")

