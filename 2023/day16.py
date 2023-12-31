import sys

type  = 'type'
left  = 'left'
right = 'right'
up    = 'up'
down  = 'down'
beams = 'beams'

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
            reflectors[coord][type] = tile
            reflectors[coord][left] = False
            reflectors[coord][right] = False
            reflectors[coord][up] = False
            reflectors[coord][down] = False
            reflectors[coord][beams] = []
    return reflectors

def find_next_reflector(reflectors, pos, heading):
    match heading:
        case [left]:
            pass
            # path = []  # indices of points to the left
            # ignore = ['-']
        case [right]:
            pass
            # path = []  # indices of points to the right
            # ignore = ['-']
        case [up]:
            pass
            # path = []  # indices of points upward
            # ignore = ['|']
        case [down]:
            pass
            # path = []  # indices of points downward
            # ignore = ['|']

    for step in path:
        if (step in reflectors) and reflectors[step][type] not in ignore:
            traversed = ...
            next_reflector = step
            return next_reflector, traversed  # return next reflector or None if not one AND the tiles traversed            
    traversed = path
    next_reflector = None
    return next_reflector, traversed  # return next reflector or None if not one AND the tiles traversed

def shine_light(reflectors):

    # trace to initial reflector
    path = range(ncols)

    # while any beams
    while any(reflectors[pnt][beams] for pnt in reflectors):
        pass

    # count up number of tiles

    print(f"The number of tiles end up being energized is ")


if __name__ == "__main__":
    file = sys.argv[1]

    reflectors = read_contraption(file)
    shine_light(reflectors)
