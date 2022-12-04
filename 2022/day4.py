import sys

def read_elf_groups(filename):
    with open(filename,'r') as fh:
        groups = [line.rstrip('\n') for line in fh]

    return groups

def extract_assigned_sections():
    pass

def is_exclusively_cleaning_sections(group):
    elf_assignment_sets = []
    elves = group.split(',')
    for elf in elves:
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

    print(f"The total number of exclusive elf groups is {total_exclusive_groups}")
    part1_ans = total_exclusive_groups

    # print(f"The total sum of priorities for three elves in a group is {total_priorities_amongst_3_elves}")
    # part2_ans = total_priorities_amongst_3_elves

    if len(sys.argv) == 3:
        if int(sys.argv[2]) == part1_ans:
            print(f"Answer for part 1 is correct!")
    # if len(sys.argv) == 4:
    #     if int(sys.argv[3]) == part2_ans:
    #         print(f"Answer for part 2 is correct!")
