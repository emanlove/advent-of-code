import sys

def read_treemap(filename):
    with open(filename,'r') as fh:
        trees = [[int(tree) for tree in row.rstrip('\n')] for row in fh]

    return trees

def find_row_wise_visibility(trees):
    for row in trees[1:-1]:
        for indx,tree in enumerate(row[1:-1]):
            left_view = row[:indx+1]
            right_view = row[indx:]

if __name__ == "__main__":
    file = sys.argv[1]

    trees = read_treemap(file)

    total = 0
    print(f"The total number of trees visible is {total}")
    part1_ans = total

    # print(f"The ... is {...}")
    # part2_ans = ...

    if len(sys.argv) >= 3:
        if int(sys.argv[2]) == part1_ans:
            print(f"Answer for part 1 is correct!")
    if len(sys.argv) == 4:
        if int(sys.argv[3]) == part2_ans:
            print(f"Answer for part 2 is correct!")

