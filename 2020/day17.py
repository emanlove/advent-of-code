import sys

def read_active_cubes(filename):
    active_cubes=[]
    with open(filename,'r') as fh:
        cube_space = [line.rstrip('\n') for line in fh]

    for ycord,yaxis in enumerate(cube_space):
        for xcord,cube in enumerate(yaxis):
            if cube == '#':
                active_cubes.append((xcord,ycord,0,0))
                
    return active_cubes

def get_space_limits(cubes):
    nDimensions = [dim for cube in cubes for dim in cube]
    xDim = nDimensions[::4]
    yDim = nDimensions[1::4]
    zDim = nDimensions[2::4]
    wDim = nDimensions[2::4]
    limits =( (min(xDim),max(xDim)), (min(yDim),max(yDim)), (min(zDim),max(zDim)), (min(wDim),max(wDim)) )

    return limits

def get_4D_neighbors(cube):
    neighbors = []
    xD,yD,zD,wD = cube

    for x in range(xD-1,xD+2):
        for y in range(yD-1,yD+2):
            for z in range(zD-1,zD+2):
                for w in range(wD-1,wD+2):
                    neighbors += [(x,y,z,w)]

    # pop out self
    this = neighbors.index(cube)
    neighbors.pop(this)

    return neighbors
    
def get_neighbors(cube):
    neighbors = []
    x,y,z = cube
    
    neighbors += [(x-1,y+1,z-1)] ; neighbors += [(x,y+1,z-1)] ; neighbors += [(x+1,y+1,z-1)]
    neighbors += [(x-1,y  ,z-1)] ; neighbors += [(x,y  ,z-1)] ; neighbors += [(x+1,y  ,z-1)]
    neighbors += [(x-1,y-1,z-1)] ; neighbors += [(x,y-1,z-1)] ; neighbors += [(x+1,y-1,z-1)]

    neighbors += [(x-1,y+1,z)] ; neighbors += [(x,y+1,z)] ; neighbors += [(x+1,y+1,z)]
    neighbors += [(x-1,y  ,z)] ;                            neighbors += [(x+1,y  ,z)]
    neighbors += [(x-1,y-1,z)] ; neighbors += [(x,y-1,z)] ; neighbors += [(x+1,y-1,z)]

    neighbors += [(x-1,y+1,z+1)] ; neighbors += [(x,y+1,z+1)] ; neighbors += [(x+1,y+1,z+1)]
    neighbors += [(x-1,y  ,z+1)] ; neighbors += [(x,y  ,z+1)] ; neighbors += [(x+1,y  ,z+1)]
    neighbors += [(x-1,y-1,z+1)] ; neighbors += [(x,y-1,z+1)] ; neighbors += [(x+1,y-1,z+1)]

    return neighbors

if __name__ == "__main__":
    file = sys.argv[1]
    cycles = int(sys.argv[2])

    active_cubes = read_active_cubes(file)

    for cycle in range(cycles):
        next_active=[]
        (xmin,xmax),(ymin,ymax),(zmin,zmax),(wmin,wmax)  = get_space_limits(active_cubes)
        
        for x in range(xmin-1,xmax+2):
            for y in range(ymin-1,ymax+2):
                for z in range(zmin-1,zmax+2):
                    for w in range(wmin-1,wmax+2):
                        here = (x,y,z,w)

                        if here in active_cubes:
                            neighbors = get_4D_neighbors(here)
                            numActiveNeighbors = sum(1 for neighbor in neighbors if neighbor in active_cubes)
                            if numActiveNeighbors==2 or numActiveNeighbors==3:
                                next_active.append(here)
                        else:
                            neighbors = get_4D_neighbors(here)
                            numActiveNeighbors = sum(1 for neighbor in neighbors if neighbor in active_cubes)
                            if numActiveNeighbors==3:
                                next_active.append(here)

        active_cubes = next_active
        #print(f"The number of active cubes after {cycle} cycles is {len(active_cubes)}")

    print(f"The number of active cubes after {cycles} cycles is {len(active_cubes)}")
