import sys
from copy import deepcopy

DROP_LINE = 500

def read_scans(filename):
    with open(filename,'r') as fh:
        scans = [line.rstrip('\n') for line in fh]

    return scans

def build_scan_map(scans):
    map = {}

    paths = []
    for scan in scans:
        pairs = scan.split(' -> ')
        points = [(pair.split(','))for pair in pairs]
        cords = [tuple(int(cord) for cord in point) for point in points]
        paths.append(cords)

    end_points_of_paths = [list(zip(path[:-1],path[1:])) for path in paths]

    for path in end_points_of_paths:
        for end_points in path:
            if end_points[0][0] == end_points[1][0]:  # vertical scan line
                col = end_points[0][0]
                min_depth = min([end_points[0][1] , end_points[1][1]])
                max_depth = max([end_points[0][1] , end_points[1][1]])
                if col not in map:
                    map[col] = []
                
                map[col] += range(min_depth,max_depth+1)
            else:                                     # horizontal scan line
                depth = end_points[0][1]
                min_col = min([end_points[0][0] , end_points[1][0]])
                max_col = max([end_points[0][0] , end_points[1][0]])
                for col in range(min_col,max_col):
                    if col not in map:
                        map[col] = []
                    
                    map[col] += [depth]

    # was going to remove possible duplicates but actually don't need to for my solution
    # for scan_line in map:
    #     pass

    return map

def fall_further(depth,col,map):
    # .. doing this one step at a time .. think one might be able to drop it down without
    #    going down one depth at a time. But for now lets explore this as is
    # check below
    if depth+1 not in map[col]:
        return depth+1, col
    elif depth+1 not in map[col-1]:
        return depth+1, col-1
    elif depth+1 not in map[col+1]:
        return depth+1, col+1
    else:
        return None, None


if __name__ == "__main__":
    file = sys.argv[1]

    scans = read_scans(file)
    map = build_scan_map(scans)
    rock_map = deepcopy(map)

    units = 0
    try:        
        while True:
            # initial_depth = min(map[DROP_LINE])-1
            # initial_col = DROP_LINE
            sand_depth = min(map[DROP_LINE])-1
            sand_col = DROP_LINE
            unsettled = True
            while unsettled:
                move_to_depth,move_to_col = fall_further(sand_depth,sand_col,map)
                if move_to_depth is None:
                    map[sand_col] += [sand_depth]
                    unsettled = False
                else:
                    sand_depth = move_to_depth
                    sand_col = move_to_col
            units +=1
            print(f"{units}")

    except KeyError:
        print(f"The units of sand that come to rest before sand starts flowing into the abyss below is {units}")
        part1_ans = units

    if len(sys.argv) >= 3:
        if int(sys.argv[2]) == part1_ans:
            print(f"Answer for part 1 is correct!")
    if len(sys.argv) == 4:
        if int(sys.argv[3]) == part2_ans:
            print(f"Answer for part 2 is correct!")

