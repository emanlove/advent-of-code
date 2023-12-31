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

def read_contraption (filename):
    with open(filename,'r') as fh:
        lines = [line.rstrip('\n') for line in fh]
    
    flattened = ''.join(lines)

    ncols = len(lines[0])
    nrows = len(lines)

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
        case LEFT:
            pass
            # path = []  # indices of points to the left
            # ignore = ['-']
        case RIGHT:
            pass
            # path = []  # indices of points to the right
            # ignore = ['-']
        case UP:
            pass
            # path = []  # indices of points upward
            # ignore = ['|']
        case DOWN:
            pass
            # path = []  # indices of points downward
            # ignore = ['|']

    for indx,step in enumerate(path):
        if (step in reflectors) and reflectors[step][type] not in ignore:
            traversed = path[:indx+1]
            next_reflector = step
            return next_reflector, traversed  # return next reflector or None if not one AND the tiles traversed            
    traversed = path
    next_reflector = None
    return next_reflector, traversed  # return next reflector or None if not one AND the tiles traversed

def reflect_beam(reflectors, pos, coming_from):
    type = reflectors[pos][TYPE]

    match type:
        case '|':
            match coming_from:
                case LEFT:
                    pass
                case RIGHT:
                    pass
                case _:
                    print(f"!!WARNING!! Should not be approching | ({pos} from {coming_from}")
        case '-':
            match coming_from:
                case UP:
                    pass
                case DOWN:
                    pass
                case _:
                    print(f"!!WARNING!! Should not be approching - ({pos} from {coming_from}")
        case '\':
            match coming_from:
                case LEFT:
                    pass
                case RIGHT:
                    pass
                case UP:
                    pass
                case DOWN:
                    pass
        case '/':
            match coming_from:
                case LEFT:
                    pass
                case RIGHT:
                    pass
                case UP:
                    pass
                case DOWN:
                    pass

    # ?? How and when/where do we remove a beam 

def shine_light(reflectors):

    # trace to initial reflector
    # path = range(ncols)
    find_next_reflector(0,RIGHT)
    reflect_beam()

    # while any beams
    while any(reflectors[pnt][beams] for pnt in reflectors):
        pass

    # count up number of tiles

    print(f"The number of tiles end up being energized is ")


if __name__ == "__main__":
    file = sys.argv[1]

    reflectors = read_contraption(file)
    shine_light(reflectors)
