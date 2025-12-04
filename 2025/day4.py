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

    # indx_around = [-ncols-1, -ncols, -ncols+1, -1, +1, +ncols-1, +ncols, +ncols+1]
    indx_around = [(-1,-1),(-1,0),(-1,+1),(0,-1),(0,+1),(+1,-1),(+1,0),(+1,+1)]  # [(row,col)]

    flattened_map = ''.join(lines)
    len_map = len(flattened_map)

    for pos,item in enumerate(flattened_map):
        if item == '.':
            accessible_rolls.append(0)
            continue
        surrounding_spots = []
        for indx in indx_around:
            rc = (pos//ncols,pos%ncols)
            check_row = rc[0]+indx[0]
            check_col = rc[1]+indx[1]
            this_pos = check_row*ncols + check_col
            # print(f"{pos}: {flattened_map[this_pos]}")
            if (0 <= check_row < nrows) and (0 <= check_col < ncols) and flattened_map[this_pos]=='@':
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
