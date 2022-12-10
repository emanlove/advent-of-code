import sys

def read_treemap(filename):
    with open(filename,'r') as fh:
        trees = [[int(tree) for tree in row.rstrip('\n')] for row in fh]

    return trees

def translated_forest(trees):
    nrows = len(trees)
    ncols = len(trees[0])
    serialized = [t for r in trees for t in r]
    translated = []
    for c in range(ncols):
        translated.append([])
        for r in range(nrows):
            translated[c].append(serialized[c+(r*ncols)])
    return translated

def default_visibility(num_rows, num_cols):
    visibility = [[True for _ in range(num_cols)]]
    for row in range(1,num_rows-1):
        visibility.append([True] + [False for _ in range(num_cols-2)] + [True])
    visibility.append([True for _ in range(num_cols)])

    return visibility

def combine_lr_with_ud(lr,ud):
    lr_serialized = [t for r in lr for t in r]
    ud_serialized = [None for _ in range(len(ud)*len(ud[0]))]
    for r in range(len(ud)):
        for c in range(len(ud[0])):
            ud_serialized[r+(c*len(ud))] = ud[r][c]
    
    lrud = list(zip(lr_serialized,ud_serialized))

    return lrud

def combine_visibility(lr,ud):
    lrud = combine_lr_with_ud(lr,ud)
    visibility = [pair[0] or pair[1] for pair in lrud]

    return visibility

def find_row_wise_visibility(trees):
    tree_vis = default_visibility(len(trees),len(trees[0]))

    for rindx,row in enumerate(trees[1:-1]):
        for tindx,tree in enumerate(row[1:-1]):            
            # print(f"{row[:tindx+1]} {row[tindx+1]} {row[tindx+2:]}   {tree > max(row[:tindx+1])} {tree > max(row[tindx+2:])}")
            tree_vis[rindx+1][tindx+1] = (tree > max(row[:tindx+1])) or (tree > max(row[tindx+2:]))
    
     # print(f"{tree_vis}")
    return tree_vis

def default_scenic_score(num_rows, num_cols):
    scenic_score = [[0 for _ in range(num_cols)]]
    for row in range(1,num_rows-1):
        scenic_score.append([0] + [None for _ in range(num_cols-2)] + [0])
    scenic_score.append([0 for _ in range(num_cols)])

    return scenic_score

def calc_row_wise_scenic_score(trees):
    scenic_score = default_scenic_score(len(trees),len(trees[0]))

    for rindx,row in enumerate(trees[1:-1]):
        for tindx,tree in enumerate(row[1:-1]):
            l_score = score(tree,trees[rindx+1][tindx::-1])
            r_score = score(tree,trees[rindx+1][tindx+2:])
            scenic_score[rindx+1][tindx+1] = l_score * r_score

    return scenic_score

def score(height,trees_in_sight):
    is_blocking = [1 if tree >= height else 0 for tree in trees_in_sight]
    try:
        score = is_blocking.index(1) + 1   # +1 because Python is zero based indexing
    except ValueError:
        score = len(trees_in_sight)
    
    return score

def combine_score(lr,ud):
    lrud = combine_lr_with_ud(lr,ud)
    score = [pair[0] * pair[1] for pair in lrud]

    return score

if __name__ == "__main__":
    file = sys.argv[1]

    trees = read_treemap(file)
    lr_visibility = find_row_wise_visibility(trees)
    flipped = translated_forest(trees)
    ud_visibility = find_row_wise_visibility(flipped)

    tree_visibility = combine_visibility(lr_visibility, ud_visibility)

    total_trees_visible = sum([1 if vis else 0 for vis in tree_visibility])

    # print(f"trees\n{trees}")
    # print(f"flipped\n{flipped}")

    print(f"The total number of trees visible is {total_trees_visible}")
    part1_ans = total_trees_visible

    lr_scored = calc_row_wise_scenic_score(trees)
    ud_scored = calc_row_wise_scenic_score(flipped)

    trees_scored = combine_score(lr_scored, ud_scored)

    max_tree_score = max(trees_scored)
    print(f"The highest tree score is {max_tree_score}")
    part2_ans = max_tree_score

    if len(sys.argv) >= 3:
        if int(sys.argv[2]) == part1_ans:
            print(f"Answer for part 1 is correct!")
    if len(sys.argv) == 4:
        if int(sys.argv[3]) == part2_ans:
            print(f"Answer for part 2 is correct!")

