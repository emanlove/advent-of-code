import sys

def read_sensor_data(filename):
    with open(filename,'r') as fh:
        sensor_data = [line.rstrip('\n') for line in fh]

    return sensor_data

def parse_cords(cord_str):
    x_cord_str,y_cord_str = cord_str.split(', ')
    _,x_str = x_cord_str.split('x=')
    _,y_str = y_cord_str.split('y=')
    x = int(x_str)
    y = int(y_str)

    return (x,y)

def parse_sensor_data(data):
    sensor_pings = []
    for line in data:
        sensor_at,closest_beacon_at = line.split(': ')
        sensor_cords = sensor_at[len('Sensor at '):]
        closest_beacon_cords = closest_beacon_at[len('closest beacon is at '):]

        sensor = parse_cords(sensor_cords)
        beacon = parse_cords(closest_beacon_cords)

        sensor_pings.append((sensor,beacon))

    return sensor_pings

def build_coverage_map(pings):
    """
    Build coverage map ignoring location of beacons which will be subtracted out later

    Coverage map will show by sensor and will need to be flatten out by row later
    """
    map = {}
    for ping in pings:
        Sx = ping[0][0]; Sy = ping[0][1]        
        Bx = ping[1][0]; By = ping[1][1]        
        m_dist = abs(Sx-Bx) + abs(Sy-By)

        y = Sy
        # ...
        if y not in map:
            map[y] = {}

        y_reach = m_dist
        map[y][(Sx,Sy)] = list(range(Sx-y_reach,Sx+y_reach+1))

        for d in range(1,m_dist+1):
            y = Sy + d
            if y not in map:
                map[y] = {}

            y_reach = m_dist-d
            map[y][(Sx,Sy)] = list(range(Sx-y_reach,Sx+y_reach+1))

            y = Sy - d
            # ...
            if y not in map:
                map[y] = {}

            y_reach = m_dist-d
            map[y][(Sx,Sy)] = list(range(Sx-y_reach,Sx+y_reach+1))

    return map

def get_beacons_on_y(pings,y):
    ybeacons_x = []

    for ping in pings:
        Bx = ping[1][0]; By = ping[1][1]        
        if By == y:
            ybeacons_x.append(Bx)

    ybeacons_x_unique = set(ybeacons_x)

    return ybeacons_x_unique

def get_coverage_on_y(y):
    y_coverage = []
    for sensor in y:
        y_coverage += y[sensor]

    y_coverage_unique = set(y_coverage)

    return y_coverage_unique    

if __name__ == "__main__":
    file = sys.argv[1]
    query_y = int(sys.argv[2])

    data = read_sensor_data(file)
    pings = parse_sensor_data(data)
    map = build_coverage_map(pings)

    ybeacons = get_beacons_on_y(pings,query_y)
    ycoverage = get_coverage_on_y(map[query_y])

    num_pos = len(ycoverage - ybeacons)

    print(f"The number of positions a beacon cannot possibly exist is {num_pos}")
    part1_ans = num_pos

    if len(sys.argv) >= 4:
        if int(sys.argv[3]) == part1_ans:
            print(f"Answer for part 1 is correct!")
    if len(sys.argv) == 5:
        if int(sys.argv[4]) == part2_ans:
            print(f"Answer for part 2 is correct!")

