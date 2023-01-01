import sys

def read_position_grid(filename):
    with open(filename,'r') as fh:
        lines = [line.rstrip('\n') for line in fh]
    
    grid = [[int(pos) for pos in cord.split(',')] for cord in lines]

    return grid

if __name__ == "__main__":
    file = sys.argv[1]

    grid = read_position_grid(file)

    matching_faces = 0
    for cube in grid:
        for another_cube in grid:
            # matching_faces += 1 if ( abs(cube[0]-another_cube[0]) + abs(cube[1]-another_cube[1]) + abs(cube[2]-another_cube[2]) ) == 1 else 0
            if ( abs(cube[0]-another_cube[0]) + abs(cube[1]-another_cube[1]) + abs(cube[2]-another_cube[2]) ) == 1:
                # print(f"{cube}  {another_cube}")
                matching_faces += 1
    
    total_surface_area = len(grid)*6 - matching_faces
    print(f"The answer to part one is {total_surface_area}")
    part1_ans = total_surface_area

    # print(f"The answer to part two is {0}")
    # part2_ans = 0

    if len(sys.argv) >= 3:
        if int(sys.argv[2]) == part1_ans:
            print(f"Answer for part 1 is correct!")
    if len(sys.argv) == 4:
        if int(sys.argv[3]) == part2_ans:
            print(f"Answer for part 2 is correct!")

