import sys
from math import sqrt, ceil, floor
from functools import reduce

def read_document(filename):
    with open(filename,'r') as fh:
        lines = [line.rstrip('\n') for line in fh]
    
    _,timeStr = lines[0].split(':')
    _,distStr = lines[1].split(':')

    # Part 1
    times = [int(time) for time in timeStr.split()]
    distances = [int(dist) for dist in distStr.split()]

    #Part 2
    times = [int(''.join(timeStr.split()))]
    distances = [int(''.join(distStr.split()))]

    num_of_wins = []
    for indx,time in enumerate(times):
        beat = distances[indx]
        discriminant = time**2 - (4*beat)
        zeros = ( ( time - sqrt(discriminant) ) / 2 , ( time + sqrt(discriminant) ) / 2 )
        # print(f"{zeros}")

        edges = [ceil(zeros[0]), floor(zeros[1])]
        # print(f"{edges}")
        if edges[0] == int(zeros[0]):
            edges[0] += 1
        if edges[1] == ceil(zeros[1]):
            edges[1] -= 1
        
        num_of_wins.append(edges[1]-edges[0]+1)

    # print(f"{num_of_wins}")
    ways_to_win = reduce(lambda x, y: x*y, num_of_wins)
    print(f"Multiplying the number of ways you can beat the record we get {ways_to_win}")

    print(f"The number of ways I can win in one long race is {ways_to_win}")

if __name__ == "__main__":
    file = sys.argv[1]

    read_document(file)
