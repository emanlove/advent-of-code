import sys

def read_tree_map(filename):
    with open(filename,'r') as fh:
        tree_map = [line.rstrip('\n') for line in fh]

    return tree_map

def check_for_trees(tree_map):
    num_rows=len(tree_map)
    num_cols=len(tree_map[0])
    pos_on_slope=[(row,row*3 % num_cols) for row in range(num_rows)]

    return sum(1 for here in pos_on_slope if tree_map[here[0]][here[1]]=='#')

if __name__ == "__main__":
    file = sys.argv[1]
    map = read_tree_map(file)
    trees = check_for_trees(map)

    print(f"The number of tress encountered down the slop is {trees}.")
