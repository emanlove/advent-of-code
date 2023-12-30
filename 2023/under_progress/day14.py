import sys
from itertools import accumulate

def read_platform(filename):
    with open(filename,'r') as fh:
        lines = [line.rstrip('\n') for line in fh]
    
    platform = []
    nrows = len(lines); ncols = len(lines[0])
    flattened = ''.join(lines)
    for col in range(ncols):
        platform.append(''.join([flattened[col+(r*ncols)] for r in range(nrows)]))

    return platform

def find_weight_per_slice(slice):
    sections = slice.split('#')
    lengths = list(accumulate([len(s) for s in sections]))
    heaviest = len(slice)
    starting_weight = [heaviest]+[heaviest-(l+i+1) for i,l in enumerate(lengths[:-1])]

    section_weights = []
    for sindx,section in enumerate(sections):
        num_rocks = section.count('O')
        start = starting_weight[sindx]
        weight_rocks = range(start,start-num_rocks,-1)
        # print(f"{list(weight_rocks)}")
        section_weights.append(sum(weight_rocks))
    # print(f"{slice}  {starting_weight}  {section_weights}")
    total_weight = sum(section_weights)

    return total_weight

if __name__ == "__main__":
    file = sys.argv[1]

    platform = read_platform(file)
    total_weight = 0
    for beam in platform:
        beam_weight = find_weight_per_slice(beam)
        total_weight += beam_weight

    print(f"The total load on the north support beams is {total_weight}")

def read_titling_platform(filename):
    with open(filename,'r') as fh:
        lines = [line.rstrip('\n') for line in fh]
    
    nrows = len(lines); ncols = len(lines[0])
    flattened = ''.join(lines)

    # round = [indx for indx,char in enumerate(flattened) if char=='O']
    round = [(indx//ncols,indx%ncols) for indx,char in enumerate(flattened) if char=='O']
    # square = [indx for indx,char in enumerate(flattened) if char=='#']
    square = [(indx//ncols,indx%ncols) for indx,char in enumerate(flattened) if char=='#']

    square_rows = {}
    square_cols = {}
    for indx,char in enumerate(flattened):
        if char=='#':
            row = indx//ncols
            col = indx%ncols
            if row not in square_rows:
                square_rows[row]['ascending'] = [-1, ncols]
            if col not in square_cols:
                square_cols[col]['ascending'] = [-1, nrows]
            square_rows[row].append(col)
            square_cols[col].append(row)
    for r in square_rows:
        square_rows[r]['ascending']=sorted(square_rows[r]['ascending'])
        square_rows[r]['decending']=sorted(square_rows[r]['decending'],reverse=True)
    for c in square_cols:
        square_cols[c]['ascending']=sorted(square_cols[c]['ascending'])
        square_cols[c]['decending']=sorted(square_cols[c]['decending'],reverse=True)
            
    square_rows = {indx//ncols: }
    square += [ends for c in range(ncols) for ends in ((-1,c),(nrows,c)) ]
    square += [ends for r in range(nrows) for ends in ((r,-1),(r,ncols)) ]

    return square, round

def shift(square, round, direction='ascending'):
    shifted = []
    sindx = 0
    while round:
        start = square[sindx]; stop = square[sindx+1]
        # if two square rocks right next to each other
        if stop-start == 1:
            sindx +=1
            continue
        
        count = 0
        for rindex,r in enumerate(round):
            if start<r<stop:
                round.pop(rindx)
                count += 1
        if count:
            offset = +1 if direction='ascending' else -1
            shifted.append(range(start+offset,start+offset+(count*offset),offset))
    return shifted

def tilt_and_shift():
    pass

def cycle():
    # tilt North
    for col in range(nCols):
        col_rocks
        for


def tilt(square, round, tilt):
    new = []
    sindx = 0
    while round:
        start = square[sindx]; stop = square[sindx+1]
        # if two square rocks right next to each other
        # Possible To Do: if number of rocks is equal to the space skip check to see if in??
        if stop-start == 1:
            sindx +=1
            continue
        count = 0
        for rindex,r in enumerate(round):
            if start<r<stop:
                r.pop(rindx)
                count += 1
        if count:
            new.append(range())
    return new


if __name__ == "__main__":
    file = sys.argv[1]

    sqr_rocks,rnd_rocks = read_titling_platform(file)
