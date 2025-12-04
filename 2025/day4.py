import sys

"""
pos-ncols-1  pos-ncols  pos-ncols+1
pos-1        pos        pos+1
pos+ncols-1  pos+ncols  pos+ncols+1
"""

def read_paper_roll_map(filename):

    accessible_rolls = []

    with open(filename, 'r') as fh:
        lines = [line.rstrip('\n') for line in fh]

    nrows = len(lines)
    ncols = len(lines[0])

    indx_around = [-ncols-1, -ncols, -ncols+1, -1, +1, +ncols-1, +ncols, +ncols+1]

    flattened_map = ''.join(lines)
    len_map = len(flattened_map)

    for pos,item in enumerate(flattened_map):
        if item == '.':
            accessible_rolls.append(0)
            continue
        surrounding_spots = []
        for indx in indx_around:
            check = pos+indx
            # print(f"{pos}: {check}")
            if check>-1 and check<len_map and flattened_map[check]=='@':
                surrounding_spots.append(1)
            else:
                surrounding_spots.append(0)
        # print(f"{surrounding_spots}")

        if sum(surrounding_spots) < 4:
            accessible_rolls.append(1)
        else:
            accessible_rolls.append(0)

    print_map(accessible_rolls, nrows, ncols)
    return sum(accessible_rolls)

def print_map(flattened_map,nrows, ncols):
    for row in range(nrows):
        print(f"{flattened_map[row*ncols:(row*ncols+ncols)]}")

if __name__ == "__main__":
    file = sys.argv[1]

    num_accessible_rolls = read_paper_roll_map(file)
    print(f"The total number of accessible rolls is {num_accessible_rolls}")
