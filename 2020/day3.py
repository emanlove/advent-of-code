import sys, math

def read_tree_map(filename):
    with open(filename,'r') as fh:
        tree_map = [line.rstrip('\n') for line in fh]

    return tree_map

def check_for_trees(tree_map, right=3, down=1):
    num_rows=len(tree_map)
    num_cols=len(tree_map[0])
    #pos_on_slope=[(row,row*right % num_cols) for row in range(num_rows)]
    pos_on_slope=[(row,step*right % num_cols) for step,row in enumerate(range(0,num_rows,down))]
    
    return sum(1 for here in pos_on_slope if tree_map[here[0]][here[1]]=='#')

if __name__ == "__main__":
    file = sys.argv[1]
    map = read_tree_map(file)

    # First problem 3 right, 1 down slope
    trees_3_1 = check_for_trees(map)
    print(f"The number of tress encountered down the slop is {trees_3_1}.")

    # Second problem - various slopes
    slopes=[(1,1), (3,1), (5,1), (7,1), (1,2)]

    tree_encountered = []
    for slope in slopes:
        trees = check_for_trees(map,slope[0],slope[1])
        tree_encountered.append(trees)
        
    print(f"Product of trees encounter on various slopes: {math.prod(tree_encountered)}")
