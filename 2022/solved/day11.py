import sys
import math

TOTAL_NUM_ROUNDS = 10000

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
        # operand,operator,modifier = oper.split(' ')
        # operation = {'operand':operand,'operator':operator,'modifier':modifier}
        operation = (lambda old,oper=oper:eval(oper))
        # Extract Test
        test = int(note[3].split('  Test: divisible by ')[1])
        if_true = int(note[4].split('    If true: throw to monkey ')[1])
        if_false = int(note[5].split('    If false: throw to monkey ')[1])
        # print(f"{test}  {if_true}  {if_false}")

        attr = {'worry_levels':worry_level, 'operation':operation, 'test':test, 'if_true':if_true, 'if_false':if_false, 'activity':0}
        monkeys.append(attr)
    
    # print(f"{len(monkeys)}")
    return monkeys

def modify_worry_level_list(monkeys):
    total_num_items = sum([len(m['worry_levels']) for m in monkeys])

    for monkey in monkeys:
        num_items_per_monkey = len(monkey['worry_levels'])
        monkey['last_item'] = num_items_per_monkey
        monkey['worry_levels'] = monkey['worry_levels'] + [None for _ in range(total_num_items - num_items_per_monkey)]

    return monkeys

def inspect_item(level,oper):
    # print(f"{level}  {oper}")
    if level == None:
        import pdb;pdb.set_trace()
        return None

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
        # print(f"    Worry level increases by {oper['modifier']} to {new_level}.")
    elif oper['operator'] == '*':
        new_level = operand * modifier
        # print(f"    Worry level is multiplied by {oper['modifier']} to {new_level}.")
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

    # change divider
    lcm = 1
    for m in monkeys:
        lcm *= (lcm*m['test'])//math.gcd(lcm,m['test'])
    # display_items_held(-1,monkeys)
    for round in range(TOTAL_NUM_ROUNDS):
        # for monkey in monkeys:
        for indx,monkey in enumerate(monkeys):
            # print(f"Monkey {indx}:")
            # import pdb; pdb.set_trace()
            # for item in monkey['worry_levels'][:monkey['last_item']]:
            for item in monkey['worry_levels']:
                # inspects an item
                # print(f"  Monkey inspects an item with a worry level of {item}.")
                # inspected_level = inspect_item(item, monkey['operation'])
                inspected_level = monkey['operation'](item)
                # print(f"    Worry level changes to {inspected_level}.")
                # factor in my relief
                # relief_level = inspected_level//3
                relief_level = (inspected_level) % lcm
                # relief_level = inspected_level
                # print(f"    Monkey gets bored with item. Worry level is divided by 3 to {relief_level}.")
                # monkey tests your worry level and throws item
                if relief_level % monkey['test'] == 0:
                # if relief_level % lcm == 0:
                    monkeys[monkey['if_true']]['worry_levels'].append(relief_level)
                    # monkeys[monkey['if_true']]['worry_levels'][monkeys[monkey['if_true']]['last_item']] = relief_level
                    # monkeys[monkey['if_true']]['last_item'] += 1
                    # print(f"    Current worry level is divisible by {monkey['test']}.")
                    # print(f"    Item with worry level {relief_level} is thrown to monkey {monkey['if_true']}.")                    
                else:
                    # import pdb;pdb.set_trace()
                    monkeys[monkey['if_false']]['worry_levels'].append(relief_level)                    
                    # monkeys[monkey['if_false']]['worry_levels'][monkeys[monkey['if_false']]['last_item']] = relief_level
                    # monkeys[monkey['if_false']]['last_item'] += 1
                    # print(f"    Current worry level is not divisible by {monkey['test']}.")
                    # print(f"    Item with worry level {relief_level} is thrown to monkey {monkey['if_false']}.")                    
            monkey['activity'] += len(monkey['worry_levels'])
            monkey['worry_levels'] = []
            # monkey['activity'] += monkey['last_item']
            # monkey['last_item'] = 0
        # display_items_held(round,monkeys)

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
    # monkeys = modify_worry_level_list(notes_about_monkeys)
    monkeys = play_keep_away(notes_about_monkeys)
    display_monkey_total_activity(monkeys)

    activity = [m['activity'] for m in monkeys]
    highest_two_activities = sorted(activity, reverse=True)[:2]
    monkey_business_level = highest_two_activities[0] * highest_two_activities[1]
    print(f"The level of monkey business is {monkey_business_level}")
    part1_ans = monkey_business_level

    # print(f"The total number of unique positions the last knot visited is {num_unique_pos_last_knot_visited}")
    # part2_ans = num_unique_pos_last_knot_visited

    if len(sys.argv) >= 3:
        if int(sys.argv[2]) == part1_ans:
            print(f"Answer for part 1 is correct!")
    if len(sys.argv) == 4:
        if int(sys.argv[3]) == part2_ans:
            print(f"Answer for part 2 is correct!")

