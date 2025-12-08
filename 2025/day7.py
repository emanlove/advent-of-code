import sys
import math

def read_diagram_and_tilt(filename):

    with open(filename, 'r') as fh:
        lines = [line.rstrip('\n') for line in fh]

    nrows = len(lines[0])
    titled_diagram = []
    S = None
    untouched_reflectors = []
    for row in range(nrows-1,-1,-1):
        titled_row = [line[row] for line in lines]
        if 'S' in titled_row:
            S = (nrows-1-row,titled_row.index('S'))
        reflectors_in_row = [indx for indx,obj in enumerate(titled_row) if obj == '^']
        if reflectors_in_row:
            untouched_reflectors += [(nrows-1-row,r) for r in reflectors_in_row]
        titled_diagram.append([line[row] for line in lines])

    return S, untouched_reflectors, titled_diagram

def calculate_num_splits(S, tilted_diagram):
    return None

if __name__ == "__main__":
    file = sys.argv[1]

    S, untouched_reflectors, tilted_diagram = read_diagram_and_tilt(file)
    print(f"{S}\n{untouched_reflectors}\n{tilted_diagram}")
    num_splits = calculate_num_splits(S, tilted_diagram)
    print(f"The number of times the beam will split is {num_splits}")
