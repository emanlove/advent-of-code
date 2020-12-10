import sys, math
from collections import Counter
from math import factorial

def read_joltage_ratings(filename):
    with open(filename,'r') as fh:
        joltage_ratings = [int(line.rstrip('\n')) for line in fh]

    return joltage_ratings

def count_repeated_ones(diffs):
    counts={}
    ocounter = 0
    for diff in diffs:
        if diff == 3:
            if ocounter:
                if ocounter not in counts:
                    counts[ocounter] = 1
                else:
                    counts[ocounter] += 1
            ocounter = 0
        else:
            ocounter += 1

    import pdb;pdb.set_trace()
    return counts

def get_num_arrangements(counts):
    total_arrangements = 0

    counts.pop(1)

    for count in counts:
        total_arrangements += math.factorial(count) * counts[count]

    return total_arrangements

if __name__ == "__main__":
    file = sys.argv[1]

    ratings = read_joltage_ratings(file)

    sorted_ratings = sorted(ratings)
    adapters_plugs = [0]+sorted_ratings+[sorted_ratings[-1]+3]
    next_rating_pairs = zip(adapters_plugs[:-1],adapters_plugs[1:])
    differences = [pair[1]-pair[0] for pair in next_rating_pairs]
    groups_of_ones = count_repeated_ones(differences)
    num_arrangements = get_num_arrangements(groups_of_ones)
    count_of_differences = Counter(differences)

    num_diff1 = count_of_differences[1]
    num_diff3 = count_of_differences[3]
    
    print(f"Number of 1's:{num_diff1}   Number of 3's:{num_diff3}")
    print(f"Product of number of 1's and 3's: {num_diff1*num_diff3}")
    print(f"The total number of arrangements is {num_arrangements}")
