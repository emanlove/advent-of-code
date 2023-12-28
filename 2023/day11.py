import sys
import itertools

def read_skydata(filename,scale):
    with open(filename,'r') as fh:
        lines = [line.rstrip('\n') for line in fh]

    empty_rows = []
    empty_cols = []
    nCols = len(lines[0])

    # find empty rows
    for lindx, line in enumerate(lines):
        if '#' not in line:
            empty_rows.append(lindx)
    
    # find empty cols
    for cindx in range(len(lines[0])):
        column = [line[cindx] for line in lines]
        if '#' not in column:
            empty_cols.append(cindx)
    
    # extract galaxies within the sky
    galaxies = {}
    for rindx,row in enumerate(lines):
        for cindx,col in enumerate(row):
            if col == '#':
                abs_indx = cindx + (rindx*nCols)
                # noting that abs_indx is on the NON-EXPANDED universe cordinates 
                # that's ok but maybe we want it in the expanded unirvrse cordinates ..
                r = rindx + shift_by(empty_rows,rindx,scale)
                c = cindx + shift_by(empty_cols,cindx,scale)
                galaxies[abs_indx] = (r,c)
    
    uniq_pairs = list(itertools.combinations(galaxies.keys(), 2))

    distances = [0]
    for pair in uniq_pairs:
        alpha = galaxies[pair[0]]
        beta = galaxies[pair[1]]
        dist = abs(beta[1]-alpha[1]) + abs(beta[0]-alpha[0])
        distances.append(dist)

    print(f"The sum of the lengths of the shortest path between every pair of galaxies"
          f" in a scale of {scale} is {sum(distances)}")

def shift_by(empties, indx, scale):
    return sum([1 for e in empties if indx > e])*scale

if __name__ == "__main__":
    file = sys.argv[1]
    if len(sys.argv)==3:
        scale = int(sys.argv[2])
    else:
        scale = 1
    read_skydata(file,scale)
