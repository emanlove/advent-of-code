import sys


def read_content(filename):
    with open(filename,'r') as fh:
        rucksacks = [line.rstrip('\n') for line in fh]

    return rucksacks

def read_elf_groups(filename):
    with open(filename,'r') as fh:
        groups=[ [] ]
        indx=0
        for line in fh:
            #import pdb;pdb.set_trace()
            line = line.rstrip('\n')
            if line == '':
                groups.append([])
                indx += 1
            else:
                groups[indx].append(line)

    return groups

def read_content_of_N_elf_groups(filename, N):
    ungrouped = read_content(filename)

    # ToDo check length is even divisble by N
    rucksacks_N_elves = [ungrouped[x:x+N] for x in range(0,len(ungrouped), N)]
    #import pdb;pdb.set_trace()
    sack_as_individual_content = [[c for c in sack] for elf_group in rucksacks_N_elves for sack in elf_group]
    rucksacks_N_elves_with_content = [sack_as_individual_content[x:x+N] for x in range(0,len(sack_as_individual_content), N)]

    return rucksacks_N_elves_with_content

def sort_contents_of_rucksacks(sack):
    num_items = len(sack)
    if num_items % 2 != 0:
        print("Sack has odd number of contents")
    items_per_sack = num_items//2
    first = sack[:items_per_sack]
    second = sack[items_per_sack:]

    return first, second

def prioritize_common_item(first, second):
    first_set = set([c for c in first])
    second_set = set([c for c in second])

    common = first_set & second_set

    if len(common) != 1:
        print(f"Expecting one common element but found {len(common)}: {common}")

    common_char = list(common)[0]

    ascii_code = ord(common_char)

    if ascii_code > 96:  # lowercase letters
        priority = ascii_code - 96
    else:  # uppercase letters
        priority = ascii_code - 64 + 26

    return priority

def ascii_to_elf_priority(char):
    ascii_code = ord(char)

    if ascii_code > 96:  # lowercase letters
        elf_priority = ascii_code - 96
    else:  # uppercase letters
        elf_priority = ascii_code - 64 + 26

    return elf_priority


def prioritize_common_item_amongst_N_elf_groups(*groups):
    common = set(group[0]).intersection(*group[1:])

    if len(common) != 1:
        print(f"Expecting one common element but found {len(common)}: {common}")

    common_char = list(common)[0]

    priority = ascii_to_elf_priority(common_char)

    return priority

def extract_assigned_sections():
    pass

def is_exclusively_cleaning_sections(group):
    elf_assignment_sets = []
    for assignment in group:
        try:
            num_notation = assignment.split('  ')[1]
        except:
            import pdb;pdb.set_trace()
        start, end = num_notation.split('-')
        elf_assignment_sets.append(set(range(int(start),int(end)+1)))
        
    # basing this off of only two in group
    return ( (elf_assignment_sets[0] <= elf_assignment_sets[1]) or (elf_assignment_sets[1] <= elf_assignment_sets[0]) )

if __name__ == "__main__":
    file = sys.argv[1]

    elf_groups = read_elf_groups(file)
    total_exclusive_groups = 0
    for group in elf_groups:
        if is_exclusively_cleaning_sections(group):
            total_exclusive_groups += 1

    # import pdb;pdb.set_trace()

    # total_priorities = 0
    # for sack in rucksacks:
    #     f,s = sort_contents_of_rucksacks(sack)
    #     priority = prioritize_common_item(f,s)
    #     total_priorities += priority

    print(f"The total number of exclusive elf groups is {total_exclusive_groups}")
    part1_ans = total_exclusive_groups

    # # Three elf groups in consective "sacks" or lines
    # total_priorities_amongst_3_elves = 0
    # n_rucksack_groups = read_content_of_N_elf_groups(file, 3)
    # for group in n_rucksack_groups:
    #     priority = prioritize_common_item_amongst_N_elf_groups(group)
    #     total_priorities_amongst_3_elves += priority

    # print(f"The total sum of priorities for three elves in a group is {total_priorities_amongst_3_elves}")
    # part2_ans = total_priorities_amongst_3_elves

    if len(sys.argv) == 3:
        if int(sys.argv[2]) == part1_ans:
            print(f"Answer for part 1 is correct!")
    # if len(sys.argv) == 4:
    #     if int(sys.argv[3]) == part2_ans:
    #         print(f"Answer for part 2 is correct!")
