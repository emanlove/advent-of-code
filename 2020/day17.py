import sys

def read_active_cubes(filename):
    active_cubes=[]
    with open(filename,'r') as fh:
        cube_space = [line.rstrip('\n') for line in fh]

    for ycord,yaxis in enumerate(cube_space):
        for xcord,cube in enumerate(yaxis):
            if cube == '#':
                active_cubes.append((xcord,ycord,0))
                
    return active_cubes

def get_space_limits(cubes):
    nDimensions = [dim for cube in cubes for dim in cube]
    xDim = nDimensions[::3]
    yDim = nDimensions[1::3]
    zDim = nDimensions[2::3]
    limits =( (min(xDim),max(xDim)), (min(yDim),max(yDim)), (min(zDim),max(zDim)) )

    return limits

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
        #limits = get_space_limits(active_cubes)
        (xmin,xmax),(ymin,ymax),(zmin,zmax)  = get_space_limits(active_cubes)
        
        for x in range(xmin,xmax+1):
            for y in range(ymin,ymax+1):
                for z in range(zmin,zmax+1):
                    here = (x,y,z)

                    if here in active_cubes:
                        neighbors = get_neighbors(here)
                        numActiveNeighbors = sum(1 for neighbor in neighbors if neighbor in active_cubes)
                        if numActiveNeighbors==2 or numActiveNeighbors==3:
                            next_active.append(here)
                    else:
                        neighbors = get_neighbors(here)
                        numActiveNeighbors = sum(1 for neighbor in neighbors if neighbor in active_cubes)
                        if numActiveNeighbors==3:
                            next_active.append(here)

        active_cubes = next_active

    print(f"The number of active cubes after {cycles} cycles is {len(active_cubes)}")
