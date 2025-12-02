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
            match factor:
                case 1:
                    lower_digit = int(first_str[0]); upper_digit = int(last_str[0])
                    lower_bound_digit = lower_digit if int(first_str[0]*len_pair)>first else lower_digit+1
                    upper_bound_digit = upper_digit if int(last_str[0]*len_pair)<last else upper_digit-1
                    for digit in range(lower_bound_digit,upper_bound_digit+1):
                        # print(f"{int(str(digit)*len_pair)}")
                        invalid_ids.append(int(str(digit)*len_pair))
                case 2:
                    print(f"{pair}")
                    lower_double = int(first_str[:2]); upper_double = int(last_str[:2])
                    print(f"lower: {lower_double}  upper: {upper_double}")
                    # lower_double = first_str[:1]; upper_double = last_str[:1]
                    num_pairs = len_pair // 2
                    # lower_bound_double = lower_double if int(lower_double*num_pairs)>first else str(int(lower_double)+1)
                    # upper_bound_double = upper_double if int(upper_double*num_pairs)<last else str(int(upper_double)-1)
                    lower_bound_double = lower_double if int(str(lower_double)*num_pairs)>first else lower_double+1
                    upper_bound_double = upper_double if int(str(upper_double)*num_pairs)<last else upper_double-1
                    for digit in range(lower_bound_double, upper_bound_double+1):
                        print(f"{int(str(digit)*num_pairs)}")
                        invalid_ids.append(int(str(digit)*num_pairs))
                case 3:
                    pass
                case 4:
                    pass
                case 5:
                    pass
                case _:
                    print('Unhandled factor')


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
    # print(f"The sum of all invalid ids is {sum_invalid_ids}")
    part_2(file)