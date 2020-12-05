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
    steps_to_this_segment = 0

    movements = wire.split(',')

    for move in movements:
        direction = move[0]
        distance = int(move[1:])

        if direction=='U':
            nex_y = cur_y + distance
            verticals.append({'x':cur_x,'y':{'min':cur_y,'max':nex_y}, 'steps_to':steps_to_this_segment, 'incoming_end':'min'})
            cur_y = nex_y
        elif direction=='D':
            nex_y = cur_y - distance
            verticals.append({'x':cur_x,'y':{'min':nex_y,'max':cur_y}, 'steps_to':steps_to_this_segment, 'incoming_end':'max'})
            cur_y = nex_y
        elif direction=='L':
            nex_x = cur_x - distance
            horizontals.append({'x':{'min':nex_x,'max':cur_x},'y':cur_y, 'steps_to':steps_to_this_segment, 'incoming_end':'max'})
            cur_x = nex_x
        elif direction=='R':
            nex_x = cur_x + distance
            horizontals.append({'x':{'min':cur_x,'max':nex_x},'y':cur_y, 'steps_to':steps_to_this_segment, 'incoming_end':'min'})
            cur_x = nex_x
        else:
            print(f"Error - Unkown Direction: {direction}")

        steps_to_this_segment += distance

    return verticals,horizontals

def doesIntersect(vlineseg,hlineseg):
    if (hlineseg['x']['min'] < vlineseg['x'] < hlineseg['x']['max']) and (vlineseg['y']['min'] < hlineseg['y'] < vlineseg['y']['max']):
        return (vlineseg['x'],hlineseg['y'])
    else:
        return (None,None)

def manhattanDistance(vlineseg,hlineseg):
    if (hlineseg['x']['min'] < vlineseg['x'] < hlineseg['x']['max']) and (vlineseg['y']['min'] < hlineseg['y'] < vlineseg['y']['max']):
        #print(f"v:{vlineseg} h:{hlineseg}")
        return abs(vlineseg['x'])+abs(hlineseg['y'])
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
    print(f"The minimum Mahattan Distance to an intersection is {closest_dist}")
