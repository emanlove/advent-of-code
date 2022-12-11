import sys

TOTAL_NUM_ROUNDS = 1 # 20

def read_notes(filename):
    with open(filename,'r') as fh:
        notes = [line.rstrip('\n') for line in fh]

    notes.append('')  #added line at end for parsing last monkey in notes
    return notes

def parse_notes(notes):
    notes_on_monkeys = [notes[indx-6:indx] for indx,line in enumerate(notes) if line=='']

    monkeys = []
    for note in notes_on_monkeys:
        # Extract worry levels
        worry_levelSTR = note[1].split('  Starting items: ')[1].split(', ')
        worry_level = [int(_) for _ in worry_levelSTR]
        # print(f"{worry_level}")
        # Extract Operation
        oper = note[2].split('  Operation: new = ')[1]
        operand,operator,modifier = oper.split(' ')
        operation = {'operand':operand,'operator':operator,'modifier':modifier}
        # Extract Test
        test = int(note[3].split('  Test: divisible by ')[1])
        if_true = int(note[4].split('    If true: throw to monkey ')[1])
        if_false = int(note[5].split('    If false: throw to monkey ')[1])
        # print(f"{test}  {if_true}  {if_false}")

        attr = {'worry_levels':worry_level, 'operation':operation, 'test':test, 'if_true':if_true, 'if_false':if_false, 'activity':0}
        monkeys.append(attr)
    
    # print(f"{len(monkeys)}")
    return monkeys

def inspect_item(level,oper):
    # print(f"{level}  {oper}")
    new_level = None

    if oper['operand'] == 'old':
        operand = level
    else:
        operand = int(oper['operand'])

    if oper['modifier'] == 'old':
        modifier = level
    else:
        modifier = int(oper['modifier'])

    if oper['operator'] == '+':
        new_level = operand + modifier
        print(f"    Worry level increases by {oper['modifier']} to {new_level}.")
    elif oper['operator'] == '*':
        new_level = operand * modifier
        print(f"    Worry level is multiplied by {oper['modifier']} to {new_level}.")
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

    # display_items_held(-1,monkeys)
    for round in range(TOTAL_NUM_ROUNDS):
        for indx,monkey in enumerate(monkeys):
            print(f"Monkey {indx}:")
            for item in monkey['worry_levels']:
                # inspects an item
                print(f"  Monkey inspects an item with a worry level of {item}.")
                inspected_level = inspect_item(item, monkey['operation'])
                # factor in my relief
                relief_level = inspected_level//3
                print(f"    Monkey gets bored with item. Worry level is divided by 3 to {relief_level}.")
                # monkey tests your worry level and throws item
                if relief_level % monkey['test'] == 0:
                    monkeys[monkey['if_true']]['worry_levels'].append(relief_level)
                    print(f"    Current worry level is divisible by {monkey['test']}.")
                    print(f"    Item with worry level {relief_level} is thrown to monkey {monkey['if_true']}.")                    
                else:
                    monkeys[monkey['if_false']]['worry_levels'].append(relief_level)
                    print(f"    Current worry level is not divisible by {monkey['test']}.")
                    print(f"    Item with worry level {relief_level} is thrown to monkey {monkey['if_false']}.")                    
            monkey['activity'] += len(monkey['worry_levels'])
            monkey['worry_levels'] = []
        display_items_held(round,monkeys)

    return monkeys

def display_monkey_total_activity(monkeys):
    for indx,monkey in enumerate(monkeys):
        print(f"Monkey {indx} inspected items {monkey['activity']} times.")

def display_items_held(round,monkeys):
    print("")
    print(f"After round {round+1}, the monkeys are holding items with these worry levels:")
    for indx,monkey in enumerate(monkeys):
        print(f"Monkey {indx}: {monkey['worry_levels']}")

if __name__ == "__main__":
    file = sys.argv[1]

    notes = read_notes(file)
    notes_about_monkeys = parse_notes(notes)
    monkeys = play_keep_away(notes_about_monkeys)
    display_monkey_total_activity(monkeys)

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

