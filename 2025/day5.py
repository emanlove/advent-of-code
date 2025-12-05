import sys


def read_fresh_spoiled_list(filename):

    with open(filename, 'r') as fh:
        lines = [line.rstrip('\n') for line in fh]

    num_fresh_ingredients = 0
    fresh_ingredients = []
    fresh_ranges = []
    for line in lines:
        if '-' in line:
            start,end = line.split('-')
            fresh_ranges += list(range(int(start),int(end)+1))
        elif line != '':
            check_ingredient = int(line)
            # print(f"{check_ingredient} {fresh_ranges}")
            if check_ingredient in fresh_ranges:
                num_fresh_ingredients += 1

    return num_fresh_ingredients


if __name__ == "__main__":
    file = sys.argv[1]

    num_fresh_ingredients = read_fresh_spoiled_list(file)
    print(f"The total number of fresh ingredients is {num_fresh_ingredients}")
