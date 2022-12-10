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

def move_as_head_moves(h,t):    
    change_in_X = h[0]-t[0]
    change_in_Y = h[1]-t[1]

    MOVE = [
        [ (-1, 1) , (-1, 1) , (0, 1) , (1, 1) , (1, 1) ],
        [ (-1, 1) , ( 0, 0) , (0, 0) , (0, 0) , (1, 1) ],
        [ (-1, 0) , ( 0, 0) , (0, 0) , (0, 0) , (1, 0) ],
        [ (-1,-1) , ( 0, 0) , (0, 0) , (0, 0) , (1,-1) ],
        [ (-1,-1) , (-1,-1) , (0,-1) , (1,-1) , (1,-1) ],
    ]
    # move_x = 1 if change_in_X > 1 else -1 if change_in_X < -1 else 0
    # move_y = 1 if change_in_Y > 1 else -1 if change_in_Y < -1 else 0
    Yrow = list(range(4,-1,-1))
    # tail_change_by = (1 if change_in_X > 1 else 0, 1 if change_in_Y > 1 else 0)
    return MOVE[Yrow[change_in_Y+2]][change_in_X+2]

def tail_follows_along(heads_path):
    tail_visited = [(0,0)]

    for head_pos in heads_path[1:]:
        last_tail_pos = tail_visited[-1]
        # head - tail = gives both distance away but also direction tail needs to go
        change = move_as_head_moves(head_pos,last_tail_pos)
        tail_visited.append(take_step(last_tail_pos,change))

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
    offsetY = [_ for _ in range(maxY,minY-1,-1)]  # grid row diff from display row

    # import pdb;pdb.set_trace()
    for pos in path:
        # print(f"{pos[0]} {offsetY[pos[1]]}")
        default_grid[offsetY[pos[1]]][pos[0]] = '#'
    
    #display start
    default_grid[offsetY[0]][0] = 's'

    pp = pprint.PrettyPrinter()
    pp.pprint(default_grid)

if __name__ == "__main__":
    file = sys.argv[1]

    moves = read_movement(file)
    heads_path = build_heads_path(moves)
    tails_path = tail_follows_along(heads_path)

    # display_spots_visited(tails_path)

    num_unique_pos_tail_visited = len(set(tails_path))
    print(f"The total number of unique positions the tail visited is {num_unique_pos_tail_visited}")
    part1_ans = num_unique_pos_tail_visited

    # import pdb;pdb.set_trace()
    # print(f"The highest tree score is {max_tree_score}")
    # part2_ans = 0

    if len(sys.argv) >= 3:
        if int(sys.argv[2]) == part1_ans:
            print(f"Answer for part 1 is correct!")
    if len(sys.argv) == 4:
        if int(sys.argv[3]) == part2_ans:
            print(f"Answer for part 2 is correct!")

