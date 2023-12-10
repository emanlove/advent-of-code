"""
| is a vertical pipe connecting north and south.
- is a horizontal pipe connecting east and west.
L is a 90-degree bend connecting north and east.
J is a 90-degree bend connecting north and west.
7 is a 90-degree bend connecting south and west.
F is a 90-degree bend connecting south and east.
"""
import sys

# LEADING_NORTH = ['|', '7', '']
LEADING_NORTH = {'7':-1, '|':0, 'F':1}
LEADING_EAST  = {'L':-1, '-':0, 'F':1}
LEADING_WEST  = {'J':-1, '-':0, '7':1}
LEADING_SOUTH = {'J':-1, '|':0, 'L':1}

def read_pipes(filename):
    with open(filename,'r') as fh:
        lines = [line.rstrip('\n') for line in fh]

    nCols = len(lines[0])
    for indx,line in enumerate(lines):
        if 'S' in line:
            # start = (line.index('S'),indx)
            start = line.index('S') + (indx * nCols)
            break

    flattened_map = ''.join(lines)

    connections = get_connecting_pipes(flattened_map, start, nCols)
    next = connections[0]
    prev = start
    path = [start,next]
    while flattened_map[next] != 'S':
        connections = get_connecting_pipes(flattened_map, next, nCols)
        connections.pop(connections.index(prev))
        #sanity check
        if len(connections) != 1:
            raise ValueError(f"At this point connections should have length of 1 but does not. {connections}")
        prev = next
        next = connections[0]
        path.append(next)
    
    import pdb;pdb.set_trace()
    print(f"The number of steps farthest from the starting position is ")

def get_connecting_pipes(map, this, nCols):
    connections = []
    
    # Check North
    north_pos = this-nCols
    north = map[north_pos]
    if north in LEADING_NORTH:
        connections.append(north_pos+LEADING_NORTH[north])

    # Check East
    east_pos = this-1
    east = map[east_pos]
    if east in LEADING_EAST:
        connections.append(east_pos + (LEADING_EAST[east]*nCols) )

    # Check West
    west_pos = this+1
    west = map[west_pos]
    if west in LEADING_WEST:
        connections.append(west_pos + (LEADING_WEST[west]*nCols) )
    
    # Check South
    south_pos = this+nCols
    south = map[south_pos]
    if south in LEADING_SOUTH:
        connections.append(south_pos+LEADING_SOUTH[south])

    if len(connections) != 2:
        raise ValueError(f"Number of connection leading out of {this} should be two but was {len(connections)} instead.")
    
    return connections


if __name__ == "__main__":
    file = sys.argv[1]

    read_pipes(file)
