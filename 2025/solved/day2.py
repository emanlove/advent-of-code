import sys

"""
2 [(1,1)]
3 [(1,1,1)]
4 [(1,1,1,1),(2,2))]
5 [(1,1,1,1,1)]
6 [(1,1,1,1,1,1),(2,2,2),(3,3)]
7 [(1,1,1,1,1,1,1)]
8 [(1,1,1,1,1,1,1,1),(2,2,2,2),(4,4)]
9 [(1,1,1,1,1,1,1,1,1),(3,3,3)]
10 [(1,1,1,1,1,1,1,1,1,1),(2,2,2,2,2),(5,5)]

factors of length
all factors are prime numbers
"""


from functools import reduce

def factors_of_n(n):
    # Source - https://stackoverflow.com/a
    # Posted by agf, modified by community. See post 'Timeline' for change history
    # Retrieved 2025-12-02, License - CC BY-SA 4.0
    return set(reduce(
        list.__add__,
        ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


def part_2(filename):
    invalid_ids = []
    pairs = get_first_last_pairs(filename)
    for pair in pairs:
        # get first and last as integers and strings
        first,last = pair[0],pair[1]
        first_str,last_str = str(first),str(last)
        # get length of
        len_pair = len(first_str)
        # get factors of length
        factors = factors_of_n(len_pair) - set([len_pair])

        for factor in factors:
            lower_digits = int(first_str[:factor])
            upper_digits = int(last_str[:factor])
            # print(f"lower: {lower_double}  upper: {upper_double}")
            num_seqs = len_pair // factor
            lower_bound_digits = lower_digits if int(str(lower_digits) * num_seqs) >= first else lower_digits + 1
            upper_bound_digits = upper_digits if int(str(upper_digits) * num_seqs) <= last else upper_digits - 1
            for digit in range(lower_bound_digits, upper_bound_digits + 1):
                # print(f"{int(str(digit) * num_seqs)}")
                invalid_ids.append(int(str(digit) * num_seqs))

    invalid_ids = list(set(invalid_ids))
    return sum(invalid_ids)

def get_first_last_pairs(filename):
    with open(filename, 'r') as fh:
        lines = [line.rstrip('\n') for line in fh]

    pairs = []
    all_ids = lines[0]
    id_pairs = all_ids.split(',')
    for pair in id_pairs:
        first, last = pair.split('-')
        len_first = len(first); len_last = len(last)

        if len_first == len_last:
            pairs.append( (int(first), int(last)) )
        else:
            lengths = range(len_first,len_last+1)
            # first
            pairs.append( (int(first), int('9'*lengths[0])) )
            # last
            pairs.append( (10**(lengths[-1]-1), int(last)) )
            # the in-betweens
            for lngth in lengths[1:-1]:
                pairs.append( (10**(lngth-1), int('9'*lngth)) )

    return pairs


def read_ids(filename):
    with open(filename, 'r') as fh:
        lines = [line.rstrip('\n') for line in fh]

    invalid_ids = []
    all_ids = lines[0]
    id_pairs = all_ids.split(',')
    for pair in id_pairs:
        first, last = pair.split('-')

        first_int = int(first); last_int=int(last)

        for id in range(first_int,last_int+1):
            id_str = str(id)
            id_len = len(id_str)
            if id_len % 2:
                continue
            if id_str[:id_len//2] != id_str[id_len//2:]:
                continue
            invalid_ids.append(id)

    return sum(invalid_ids)

if __name__ == "__main__":
    file = sys.argv[1]

    # sum_invalid_ids = read_ids(file)
    sum_invalid_ids  = part_2(file)
    print(f"The sum of all invalid ids is {sum_invalid_ids}")
