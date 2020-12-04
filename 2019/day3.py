import sys

def loadWires(wirefile):
    with open(wirefile,'r') as fh:
        wires = [line.rstrip('\n') for line in fh]

    return wires

def getVerticalHorizontalLines(wire):
    verticals = []
    horizontals = []
    cur_x = 0
    cur_y = 0

    movements = wire.split(',')

    for move in movements:
        direction = move[0]
        distance = int(move[1:])

        if direction=='U':
            nex_y = cur_y + distance
            verticals.append((cur_x,(cur_y,nex_y)))
            cur_y = nex_y
        elif direction=='D':
            nex_y = cur_y - distance
            verticals.append((cur_x,(nex_y,cur_y)))
            cur_y = nex_y
        elif direction=='L':
            nex_x = cur_x - distance
            horizontals.append(((nex_x,cur_x),cur_y))
            cur_x = nex_x
        elif direction=='R':
            nex_x = cur_x + distance
            horizontals.append(((cur_x,nex_x),cur_y))
            cur_x = nex_x
        else:
            print(f"Error - Unkown Direction: {direction}")

    return verticals,horizontals

def doesIntersect(vlineseg,hlineseg):
    if (hlineseg[0][0] < vlineseg[0] < hlineseg[0][1]) and (vlineseg[1][0] < hlineseg[1] < vlineseg[1][1]):
        return (vlineseg[0],hlineseg[1])
    else:
        return (None,None)

def manhattanDistance(vlineseg,hlineseg):
    if (hlineseg[0][0] < vlineseg[0] < hlineseg[0][1]) and (vlineseg[1][0] < hlineseg[1] < vlineseg[1][1]):
        return vlineseg[0]+hlineseg[1]
    else:
        return None

if __name__ == "__main__":
    wirefile = sys.argv[1]

    wires = loadWires(wirefile)

    # knowing we have only two lines
    va,ha = getVerticalHorizontalLines(wires[0])
    vb,hb = getVerticalHorizontalLines(wires[1])

    hbva = [manhattanDistance(v,h) for h in hb for v in va]
    havb = [manhattanDistance(v,h) for h in ha for v in vb]

    closest_dist = min([i for i in hbva if i is not None] + [i for i in havb if i is not None])
    print(f"The minimum Mahattan Dostance to an intersection is {closest_dist}")