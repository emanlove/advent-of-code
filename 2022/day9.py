import sys
import pprint

STEP = {
    'L': (-1, 0),
    'R': ( 1, 0),
    'U': ( 0, 1),
    'D': ( 0,-1)
}

# def take_step(pos,add):
#     return (pos[0]+add[0],pos[1]+add[1])

def take_step(pos,dir):
    if isinstance(dir,str):
        return (pos[0]+STEP[dir][0],pos[1]+STEP[dir][1])
    if isinstance(dir,tuple):
        return (pos[0]+dir[0],pos[1]+dir[1])
    
def read_movement(filename):
    with open(filename,'r') as fh:
        movement = [line.rstrip('\n') for line in fh]

    return movement

def build_heads_path(movements):
    head_visited = [(0,0)]

    for move in movements:
        dir,steps = move.split(' ')
        last_pos = head_visited[-1]
        for _ in range(int(steps)):
            head_visited.append(take_step(last_pos,dir))
            last_pos = head_visited[-1]

    return head_visited

def get_relative_dir_dist(h,t):
    dir = (h[0]-t[0],h[1]-t[1])
    # dist = abs(dir[0]) + abs(dir[1])
    too_far = (abs(dir[0]) > 1) or (abs(dir[1]) > 1)

    return dir,too_far

def tail_follows_along(heads_path):
    tail_visited = [(0,0)]

    for head_pos in heads_path:
        last_tail_pos = tail_visited[-1]
        # head - tail = gives both distance away but also direction tail needs to go
        rel_dir, too_far = get_relative_dir_dist(head_pos,last_tail_pos)
        if too_far:
            tail_visited.append(take_step(last_tail_pos,rel_dir))

    return tail_visited

def build_breadcrumbs(movements):
    tail_visited = [(0,0)]

    for move in movements:
        dir,steps = move.split(' ')

        # movement of tail dependent on both movement, as well as starting relative position

def display_spots_visited(path):
    X = [p[0] for p in path]; Y = [p[1] for p in path]
    minX = min(X); maxX = max(X); minY = min(Y); maxY = max(Y)
    nCols = abs(maxX - minX) + 1; nRows = abs(maxY-minY) + 1
    # default_grid = ['.' * nCols for _ in range(nRows)]
    default_grid = [['.' for _ in range(nCols)] for _ in range(nRows)]
    offsetX = [4, 3, 2, 1, 0]  # grid row diff from display row

    for pos in path:
        # import pdb;pdb.set_trace()
        # print(f"{offsetX[pos[0]]} {pos[1]}")
        default_grid[offsetX[pos[0]]][pos[1]] = '#'
    
    #display start
    default_grid[offsetX[0]][0] = 's'

    pp = pprint.PrettyPrinter()
    pp.pprint(default_grid)

if __name__ == "__main__":
    file = sys.argv[1]

    moves = read_movement(file)
    heads_path = build_heads_path(moves)
    tails_path = tail_follows_along(heads_path)

    display_spots_visited(tails_path)

    num_unique_pos_tail_visited = len(set(tails_path))
    print(f"The total number of unique positions the tail visited is {num_unique_pos_tail_visited}")
    part1_ans = num_unique_pos_tail_visited

    # print(f"The highest tree score is {max_tree_score}")
    # part2_ans = 0

    if len(sys.argv) >= 3:
        if int(sys.argv[2]) == part1_ans:
            print(f"Answer for part 1 is correct!")
    if len(sys.argv) == 4:
        if int(sys.argv[3]) == part2_ans:
            print(f"Answer for part 2 is correct!")

