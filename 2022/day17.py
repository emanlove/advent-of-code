"""
####

.#.
###
.#.

..#
..#
###

#
#
#
#

##
##
"""
import sys

def read_gas_jets(filename):
    with open(filename,'r') as fh:
        jets = [line.rstrip('\n') for line in fh]

    return jets

if __name__ == "__main__":
    file = sys.argv[1]

    the_way_the_jets_blow = read_gas_jets(file)

    print(f"The answer to part one is {1}")
    part1_ans = 1

    # print(f"The answer to part two is {0}")
    # part2_ans = 0

    if len(sys.argv) >= 3:
        if int(sys.argv[2]) == part1_ans:
            print(f"Answer for part 1 is correct!")
    if len(sys.argv) == 4:
        if int(sys.argv[3]) == part2_ans:
            print(f"Answer for part 2 is correct!")

