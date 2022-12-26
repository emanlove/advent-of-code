import sys

MAX = 4000001
# MAX = 21

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

def determine_if_sensor_coverage_includes_y(ping,y):
    Sx = ping[0][0]; Sy = ping[0][1]        
    Bx = ping[1][0]; By = ping[1][1]        
    m_dist = abs(Sx-Bx) + abs(Sy-By)

    empty_range = ()
    y_dist = abs(Sy-y)
    if y_dist <= m_dist:
        if By == y:  # beacon on y
            if Bx < Sx:
                empty_range = (Bx+1,Sx+m_dist-y_dist)
            elif Bx > Sx:
                empty_range = (Sx-m_dist+y_dist,Bx-1)            
        else:
            empty_range = (Sx-m_dist+y_dist,Sx+m_dist-y_dist)
    return empty_range

def simple_range_combination(ranges):
    combined = []
    for r in ranges:
        combined += (list(range(r[0],r[1]+1)))

    return len(set(combined))

def reduce_ranges(ranges):
    ord_ranges = sorted(ranges)
    # import pdb;pdb.set_trace()
    reduced = [(0,0)]
    for ordr in ord_ranges:
        last = reduced[-1]
        if ordr[0] > last[1]:
            # import pdb;pdb.set_trace()
            reduced.append(ordr)
            # also might have found answer
            # print(f"{last[1]}  {ordr[0]}")
            return last[1]+1            
        if ordr[1] > last[1]:
            reduced[-1] = (last[0],ordr[1])
    #     elif

def get_m_dists(pings):
    m_dists = []
    for ping in pings:
        Sx = ping[0][0]; Sy = ping[0][1]        
        Bx = ping[1][0]; By = ping[1][1]        
        m_dist = abs(Sx-Bx) + abs(Sy-By)
        m_dists.append(((Sx,Sy),m_dist))
    
    return m_dists

def build_coverage_set(pings):
    """
    Build coverage map ignoring location of beacons which will be subtracted out later

    Coverage map will show by sensor and will need to be flatten out by row later
    """
    ping_sets = set()
    for indx,ping in enumerate(pings):
        Sx = ping[0][0]; Sy = ping[0][1]        
        Bx = ping[1][0]; By = ping[1][1]        
        m_dist = abs(Sx-Bx) + abs(Sy-By)

        y = Sy
        y_reach = m_dist
        ping_sets |= set(range(Sx-y_reach,Sx+y_reach+1))

        for d in range(1,m_dist+1):
            y = Sy + d
            y_reach = m_dist-d
            ping_sets |= set(range(Sx-y_reach,Sx+y_reach+1))

            y = Sy - d
            y_reach = m_dist-d
            ping_sets |= set(range(Sx-y_reach,Sx+y_reach+1))

    return ping_sets


if __name__ == "__main__":
    file = sys.argv[1]
    query_y = int(sys.argv[2])

    data = read_sensor_data(file)
    pings = parse_sensor_data(data)

    empty_ranges_on_y = []
    for ping in pings:
        range_on_y = determine_if_sensor_coverage_includes_y(ping,query_y)
        if range_on_y:
            empty_ranges_on_y.append(range_on_y)
    
    # map = build_coverage_map(pings)

    # ybeacons = get_beacons_on_y(pings,query_y)
    # ycoverage = get_coverage_on_y(map[query_y])

    # num_pos = len(ycoverage - ybeacons)

    num_pos = simple_range_combination(empty_ranges_on_y)
    print(f"The number of positions a beacon cannot possibly exist is {num_pos}")
    part1_ans = num_pos

    # import pdb;pdb.set_trace()

    for y in range(MAX): 
        empty_ranges_on_y = []
        for ping in pings:
            range_on_y = determine_if_sensor_coverage_includes_y(ping,y)
            if range_on_y:
                empty_ranges_on_y.append(range_on_y)
        found = reduce_ranges(empty_ranges_on_y)
        if found:
            print(f"{y}  {found}")
            print(y+found*4000000)
    # m_dists = get_m_dists(pings)

    # for P in range(MAX**2):
    #     Px = P%MAX
    #     Py = P//MAX

    #     in_range_of_sensor = False
    #     for sensor in m_dists:
    #         Sx = sensor[0][0];Sy = sensor[0][1]
    #         dist = sensor[1]
    #         if abs(Sx-Px) + abs(Sy-Py) <= dist:
    #             in_range_of_sensor = True
    #             break
    #             #found a sesnoer it is in range of and thus no need to continue searching
    #             # in_range_of_sensor.append(True)
    #         # else:
    #         #     in_range_of_sensor.append(False)
        
    #     if not in_range_of_sensor:
    #         # found the point
    #         if MAX != 21:
    #             tuning_frequency_for_distress_beacon = P
    #         else:
    #             tuning_frequency_for_distress_beacon = Py+Px*4000000
            
    #             print(f"The tuning frequency for this distress beacon is {tuning_frequency_for_distress_beacon}")
    #             part1_ans = tuning_frequency_for_distress_beacon

    # covered = build_coverage_set(pings)
    # all_pos = set(range(MAX**2))

    # tuning_frequency_for_distress_beacon = all_pos - covered
    # import pdb;pdb.set_trace()

    if len(sys.argv) >= 4:
        if int(sys.argv[3]) == part1_ans:
            print(f"Answer for part 1 is correct!")
    if len(sys.argv) == 5:
        if int(sys.argv[4]) == part2_ans:
            print(f"Answer for part 2 is correct!")

