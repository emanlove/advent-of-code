import sys

# type  = 'type'
# left  = 'left'
# right = 'right'
# up    = 'up'
# down  = 'down'
# beams = 'beams'
TYPE  = 'type'
LEFT  = 'left'
RIGHT = 'right'
UP    = 'up'
DOWN  = 'down'
BEAMS = 'beams'
NCOLS = None
NROWS = None

def read_contraption (filename):
    with open(filename,'r') as fh:
        lines = [line.rstrip('\n') for line in fh]
    
    flattened = ''.join(lines)

    ncols = len(lines[0])
    nrows = len(lines)
    NCOLS = len(lines[0])
    NROWS = len(lines)

    reflectors = {}
    for coord,tile in enumerate(flattened):
        if tile != '.':
            reflectors[coord] = {}
            reflectors[coord][TYPE] = tile
            reflectors[coord][LEFT] = False
            reflectors[coord][RIGHT] = False
            reflectors[coord][UP] = False
            reflectors[coord][DOWN] = False
            reflectors[coord][BEAMS] = []
    return reflectors

def find_next_reflector(reflectors, pos, heading):
    match heading:
        case "left":
            # indices of points to the left
            # range(pos, beginning of this row-1, -1)
            # range(pos-1, (pos//NCOLS)*NCOLS)-1, -1)
            path = range(pos-1, ((pos//NCOLS)*NCOLS)-1, -1)
            ignore = ['-']
        case "right":
            # indices of points to the right
            # range(pos+1, (pos//NCOLS+1)*NCOLS), +1)
            path = range(pos+1, (pos//NCOLS+1)*NCOLS, +1)  # indices of points to the right
            ignore = ['-']
        case "up":
            # indices of points upward
            # range(row above, 0, -num of cols)
            # range(pos-NCOLS, 0, -NCOLS)
            path = range(pos-NCOLS, 0, -NCOLS)  # indices of points upward
            ignore = ['|']
        case "down":
            # indices of points downward
            # range(row below, num of cols, +num of cols)
            # range(pos+NCOLS, NCOLS, +NCOLS)
            path = range(pos+NCOLS, NCOLS, +NCOLS)  # indices of points downward
            ignore = ['|']

    for indx,step in enumerate(path):
        if (step in reflectors) and reflectors[step][type] not in ignore:
            traversed = path[:indx+1]
            next_reflector = step
            # ?? remove beam from reflector (conditional based upon pos in reflector - needed for initial start)
            # remove beam from reflector
            if pos in reflectors:
                beam_indx = reflectors[pos][BEAMS].find(heading)
                reflectors[pos][BEAMS].pop(beam_indx)
            return next_reflector, traversed  # return next reflector or None if not one AND the tiles traversed            
    traversed = path
    next_reflector = None
    # ?? remove beam from reflector (conditional based upon pos in reflector - needed for initial start)
    # remove beam from reflector
    if pos in reflectors:
        beam_indx = reflectors[pos][BEAMS].find(heading)
        reflectors[pos][BEAMS].pop(beam_indx)
    return next_reflector, traversed  # return next reflector or None if not one AND the tiles traversed

def reflect_beam(reflectors, pos, coming_from):
    type = reflectors[pos][TYPE]

    # if beam coming into this reflector has arrived from same direction before
    # then don't reflect back out (as this would be looping the light)
    
    match type:
        case '|':
            match coming_from:
                case "left" | "right":
                    # split up and down
                    pass
                case _:
                    print(f"!!WARNING!! Should not be approching | ({pos}) from {coming_from}")
        case '-':
            match coming_from:
                case "up" | "down":
                    # split left and right
                    pass
                case _:
                    print(f"!!WARNING!! Should not be approching - ({pos}) from {coming_from}")
        case '\':
            match coming_from:
                case "left":
                    # reflect up
                    pass
                case "right":
                    # reflect down
                    pass
                case "up":
                    # reflect left
                    pass
                case "down":
                    # reflect right
                    pass
        case '/':
            match coming_from:
                case "left":
                    # reflect up
                    pass
                case "right":
                    # reflect down
                    pass
                case "up":
                    # reflect right
                    pass
                case "down":
                    # reflect left
                    pass

    # ?? How and when/where do we remove a beam 

def shine_light(reflectors):

    all_tiles_energized = [0]

    # trace to initial reflector
    next_reflector, tiles_traversed = find_next_reflector(reflectors, 0,RIGHT)
    all_tiles_energized.append(tiles_traversed)
    reflect_beam(reflectors, next_reflector, RIGHT)

    # while any beams
    while any(reflectors[pnt][BEAMS] for pnt in reflectors):
        pass

    # count up number of tiles

    print(f"The number of tiles end up being energized is ")


if __name__ == "__main__":
    file = sys.argv[1]

    reflectors = read_contraption(file)
    shine_light(reflectors)
