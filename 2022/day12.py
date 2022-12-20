"""
Some thoughts ...

- Every point if used will only be used once. That is if it were used twice, thus the trail
  would be circling back upon itself, and thus NOT the shortest route.
- Maximum path length is NRows*nCols and the minimum is 25.
- There are step up points where one can olny step up to the next letter. In both th test
  data and in the problem data there are some limits here.
"""

import sys
import copy

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def read_map(filename,cleanup=True):
    with open(filename,'r') as fh:
        map = [line.rstrip('\n') for line in fh]

    serialized_map = [point for point in ''.join(map)]
    nCols = len(map[0])
    nRows = len(map)
    start = serialized_map.index('S')
    end = serialized_map.index('E')
    
    # cleanup map replaing S with a and E with z
    if cleanup:
        serialized_map[start]='a'
        serialized_map[end]='z'

    return serialized_map, nCols, nRows, start, end

def create_movement_maps(map,nCols,nRows):
    # left up right down
    neighbors = []
    allowed_exit_pathway = []
    allowed_entr_pathway = []

    for indx,point in enumerate(map):
        col = indx%nCols
        row = indx//nCols
        left_neighbor_coord  = (col-1,row)
        up_neighbor_coord    = (col  ,row-1)
        right_neighbor_coord = (col+1,row)
        down_neighbor_coord  = (col  ,row+1)
        left_neighbor  = None if (left_neighbor_coord[0] < 0 ) else ( left_neighbor_coord[0] + (left_neighbor_coord[1]*nCols))
        up_neighbor    = None if (up_neighbor_coord[1] < 0 ) else ( up_neighbor_coord[0] + (up_neighbor_coord[1]*nCols))
        right_neighbor = None if (right_neighbor_coord[0] >= nCols ) else ( right_neighbor_coord[0] + (right_neighbor_coord[1]*nCols))
        down_neighbor  = None if (down_neighbor_coord[1]  >= nRows ) else ( down_neighbor_coord[0] + (down_neighbor_coord[1]*nCols))

        neighbors.append([left_neighbor, up_neighbor, right_neighbor, down_neighbor])

        left_exit_pathway  = False if ( (left_neighbor is None)  or (ord(map[left_neighbor])-ord(point)>1)) else True
        up_exit_pathway    = False if ( (up_neighbor is None)    or (ord(map[up_neighbor])-ord(point)>1)) else True
        right_exit_pathway = False if ( (right_neighbor is None) or (ord(map[right_neighbor])-ord(point)>1)) else True
        down_exit_pathway  = False if ( (down_neighbor is None)  or (ord(map[down_neighbor])-ord(point)>1)) else True

        allowed_exit_pathway.append([left_exit_pathway, up_exit_pathway, right_exit_pathway, down_exit_pathway])

        left_entr_pathway  = False if ( (left_neighbor is None)  or (ord(point)-ord(map[left_neighbor])<1)) else True
        up_entr_pathway    = False if ( (up_neighbor is None)    or (ord(point)-ord(map[up_neighbor])<1)) else True
        right_entr_pathway = False if ( (right_neighbor is None) or (ord(point)-ord(map[right_neighbor])<1)) else True
        down_entr_pathway  = False if ( (down_neighbor is None)  or (ord(point)-ord(map[down_neighbor])<1)) else True

        allowed_entr_pathway.append([left_entr_pathway, up_entr_pathway, right_entr_pathway, down_entr_pathway])

    return neighbors,allowed_exit_pathway,allowed_entr_pathway

def step_up_spots(map,neighbors,frm,to):
    step_up_points = []
    for indx,point in enumerate(map):
        if point != to:
            continue
        for n in neighbors[indx]:
            if (n is not None) and map[n]==frm:
                step_up_points.append((indx,n))

    return step_up_points

def display_map(map,nCols):
    rows = [map[x:x+nCols] for x in range(0,len(map),nCols)]
    strings = [''.join(r) for r in rows]
    print("\n".join(strings))

def display_map_level(map,nCols,level):
    for indx,point in enumerate(map):
        if point != level:
            map[indx]='.'
    display_map(map,nCols)    

if __name__ == "__main__":
    file = sys.argv[1]

    map,nCols,nRows,Sindx,Eindx  = read_map(file)
    neighbors,exits,entries = create_movement_maps(map,nCols,nRows)

    letters = [chr(o) for o in range(ord('a'),ord('a')+26)]
    steps = list(zip(letters[:-1],letters[1:]))
    # for step in steps[2:]:  # start with stepping up from c to d
    for step in steps:  # start with stepping up from a to b
        stepping_points = step_up_spots(map,neighbors,step[0],step[1])
        print(f"steps {step}: {stepping_points}")

    # display_map(map,nCols)

    # step_from_b_to_c = step_up_spots(map,neighbors,'b','c')
    # bc_map = copy.deepcopy(map)
    # for step in step_from_b_to_c:
    #     bc_map[step[0]] = bcolors.BOLD + bc_map[step[0]] + bcolors.ENDC
    # display_map(bc_map,nCols)

    display_map_level(map,nCols,'k')

    total_steps = [
        8,              #a-b
        1,              #b-c
        18+9+23+15+8,   #c-d
        1,  #d-e
        10, #e-f
        12, #f-g
        11, #g-h #12r
        10, #h-i #9r
        11, #i-j
        11, #j-k

        ]
    # print(f"The level of monkey business is {monkey_business_level}")
    # part1_ans = monkey_business_level

    # print(f"The total number of unique positions the last knot visited is {num_unique_pos_last_knot_visited}")
    # part2_ans = num_unique_pos_last_knot_visited

    if len(sys.argv) >= 3:
        if int(sys.argv[2]) == part1_ans:
            print(f"Answer for part 1 is correct!")
    if len(sys.argv) == 4:
        if int(sys.argv[3]) == part2_ans:
            print(f"Answer for part 2 is correct!")

