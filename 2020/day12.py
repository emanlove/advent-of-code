import sys

COMPASS_ROSE = ['E', 'S', 'W', 'N']
def read_navigation_instrct(filename):
    with open(filename,'r') as fh:
        directions = [line.rstrip('\n') for line in fh]

    return directions

def move(here,direct,dist):
    there = here
    if direct=='N':
        there[1] += dist
    elif direct=='E':
        there[0] += dist
    elif direct=='S':
        there[1] -= dist
    elif direct=='W':
        there[0] -= dist

    return there

if __name__ == "__main__":
    file = sys.argv[1]

    directions = read_navigation_instrct(file)

    current_orientation = 0    # 'E'
    start_pos = [0,0]

    pos = start_pos
    for movement in directions:
        direction = movement[0]
        distance  = int(movement[1:])

        if direction=='L':
            current_orientation = (current_orientation - int(distance/90)) % 4 
        elif direction=='R':
            current_orientation = (current_orientation + int(distance/90)) % 4
        elif direction=='F':
            pos = move(pos, COMPASS_ROSE[current_orientation], distance)
        elif direction in COMPASS_ROSE:
            pos = move(pos, direction, distance)
        else:
            print(f"ERROR: Unknown direction - {direction}")

    manhattan_distance=abs(pos[0])+abs(pos[1])
    print(f"The current Manhattan Distance from start is {manhattan_distance}")
