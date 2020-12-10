"""
Notes:
Working out the solution for Part Two. I realized that distinct arrangements come from the spots
where there are more than one difference of ones. At first glance I was thinking it was a factorial
of the number of consecutive ones (Test suite A - 3! + 2! = 8). But further investigation this is not
correct. (Test Suite B - 4! + 4! + 4! + 4! + 3! + 2! != 19208 nor if *).

Thinking more I started to draw out the combinations based upon the number of ones. For example, started with
this

3   1   1   1   3

where this is a set of 1 differences. To give more of the picture I put in somewhat arbitrary numbers which would cause this set of differences

  3   4   5   6   9
3   1   1   1   3

Going with these this is the possible valid combinations

  3   4   5   6   9
3   1   1   1   3
  3   4   5   6
  3   4       6
  3       5   6
  3           6

or 4. Looking at sequences of two ones we see

  3   4   5   8
3   1   1   3
  3   4   5
  3       5

the total combinations to be 2. At this point I see a couple of things. I need
those outside numbers. And this is starting to looking this the ones and zeros
in a sequence of binary numbers .. (maybe combinatorics ..? .. which makes sense).
Looking at a set of four one difference, I am expecting an issue with gaps of three
(or more as were move to five ones).

  3   4   5   6   7   10
3   1   1   1   1   3
  3   4   5   6   7
  3   4           7
  3       5       7
  3           6   7
  3   4   5       7
  3   4       6   7
  3       5   6   7

or 7. So yes this is very much looking like binary .. which makes complete sense. If you have
K number of binary options the total number of combinations would be 2**K. So looking at the
next one, five ones

  3   4   5   6   7   8   11
3   1   1   1   1   1   3
  3   4   5   6   7   8
  3   4           7   8
  3       5       7   8
  3           6   7   8
  3   4   5       7   8
  3   4       6   7   8
  3       5   6   7   8
  3           6       8
  3   4       6       8
  3       5   6       8
  3   4   5   6       8
  3       5           8
  3   4   5           8

wich is 13 out of the 16. So if n is the number of ones in a group then the number of combinations
is something like

2**(n-1) - ??

At this point I tired to find out what ?? was. I was guessing it had something to do with 3 (or
whatever the greatest gap). At this point I thought about this, and thought about it, and thought about it,
and thought about it some more. Then I pulled in my son and discussed it with him for a while. I walked him
though the problem and my thoughts above for which we discussed for a while. After trying to work though the
problem for a while I ran the script .. *** Spoiler Alert ***

the input set has no sets of ones with more than four. Thus I had everything from hand calculations.


... Still wonering about that question of how to calculate by formula the number of sets within a binary set.
"""
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
