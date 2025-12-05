import sys


def read_fresh_spoiled_list(filename):

    with open(filename, 'r') as fh:
        lines = [line.rstrip('\n') for line in fh]

    num_fresh_ingredients = 0
    fresh_ranges = []
    check_ingredients = []
    for line in lines:
        if '-' in line:
            start,end = line.split('-')
            # fresh_ranges += list(range(int(start),int(end)+1))
            fresh_ranges += range(int(start),int(end)+1)
        elif line != '':
            check_ingredients.append(int(line))

    fresh_ingredients = set(fresh_ranges) & set(check_ingredients)
    # print(f"{fresh_ranges} {check_ingredients}")
    return len(fresh_ingredients)


if __name__ == "__main__":
    file = sys.argv[1]

    num_fresh_ingredients = read_fresh_spoiled_list(file)
    print(f"The total number of fresh ingredients is {num_fresh_ingredients}")
