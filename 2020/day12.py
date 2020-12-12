import sys

COMPASS_ROSE = ['E', 'S', 'W', 'N']

def read_navigation_instrct(filename):
    with open(filename,'r') as fh:
        directions = [line.rstrip('\n') for line in fh]

    return directions

def move(here,waypoint,dist):
    there = [None,None]
    there[0] = here[0] + waypoint[0]*dist
    there[1] = here[1] + waypoint[1]*dist

    return there

def move_waypoint(old_waypoint,direct,dist):
    new_waypoint = old_waypoint
    if direct=='N':
        new_waypoint[1] += dist
    elif direct=='E':
        new_waypoint[0] += dist
    elif direct=='S':
        new_waypoint[1] -= dist
    elif direct=='W':
        new_waypoint[0] -= dist

    return new_waypoint

def rotate_waypoint(old_waypoint,pointing):
    new_waypoint = [None,None]
    if pointing==0:      # 12 O'Clock
        new_waypoint = old_waypoint
    elif pointing==1:    # 3 O'Clock
        new_waypoint[0] =  old_waypoint[1]
        new_waypoint[1] = -old_waypoint[0]
    elif pointing==2:    # 6 O'Clock
        new_waypoint[0] = -old_waypoint[0]
        new_waypoint[1] = -old_waypoint[1]
    elif pointing==3:    # 9 O'Clock
        new_waypoint[0] = -old_waypoint[1]
        new_waypoint[1] =  old_waypoint[0]
    else:
        print(f"Error: Unknown rotation - {pointing}")

    return new_waypoint

if __name__ == "__main__":
    file = sys.argv[1]

    directions = read_navigation_instrct(file)

    waypoint  = [10,1]
    start_pos = [0,0]

    pos = start_pos
    for movement in directions:
        direction = movement[0]
        distance  = int(movement[1:])

        if direction=='L':
            rotate = -int(distance/90) % 4
            waypoint = rotate_waypoint(waypoint,rotate)
        elif direction=='R':
            rotate = int(distance/90) % 4 
            waypoint = rotate_waypoint(waypoint,rotate)
        elif direction=='F':
            pos = move(pos, waypoint, distance)
        elif direction in COMPASS_ROSE:
            waypoint = move_waypoint(waypoint, direction, distance)
        else:
            print(f"ERROR: Unknown direction - {direction}")

    manhattan_distance=abs(pos[0])+abs(pos[1])
    print(f"The current Manhattan Distance from start is {manhattan_distance}")
