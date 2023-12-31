import sys

left  = 'left'
right = 'right'
up    = 'up'
down  = 'down'

def read_contraption (filename):
    with open(filename,'r') as fh:
        lines = [line.rstrip('\n') for line in fh]
    
    flattened = ''.join(lines)

    reflectors = {}
    for coord,point in enumerate(flattened):
        if point != '.':
            reflectors[point] = {}
            reflectors[point][left] = False
            reflectors[point][right] = False
            reflectors[point][up] = False
            reflectors[point][down] = False

    return reflectors

def shine_light(reflectors):

    beams = []
    initial_beam = {pos: 0, heading: right}
    beams.append(initial_beam)

    while beams:
        beams=[]
    
    print(f"The number of tiles end up being energized is ")


if __name__ == "__main__":
    file = sys.argv[1]

    reflectors = read_contraption(file)
    shine_light(reflectors)
