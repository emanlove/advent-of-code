import sys

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

    # zeros = read_rotations(file)
    sum_invalid_ids = read_ids(file)
    print(f"The sum of all invalid ids is {sum_invalid_ids}")
