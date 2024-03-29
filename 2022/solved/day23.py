import sys
from collections import Counter

TOTAL_NUM_ROUNDS = 5000

def read_map(filename,cleanup=True):
    elves = {}
    with open(filename,'r') as fh:
        map = [line.rstrip('\n') for line in fh]

    nRows = len(map)
    nCols = len(map[0])

    for rindx in range(nRows):
        for cindx in range(nCols):
            if map[rindx][cindx] == '#':
                # elves[(rindx,cindx)]=cindx + (rindx*nCols)
                elves[(rindx,cindx)]=()

    return elves,nRows,nCols

def hasNW(pnt,elves): return (pnt[0]-1,pnt[1]-1) in elves
def  hasN(pnt,elves): return (pnt[0]-1,pnt[1]  ) in elves
def hasNE(pnt,elves): return (pnt[0]-1,pnt[1]+1) in elves
def  hasW(pnt,elves): return (pnt[0]  ,pnt[1]-1) in elves
def  hasE(pnt,elves): return (pnt[0]  ,pnt[1]+1) in elves
def hasSW(pnt,elves): return (pnt[0]+1,pnt[1]-1) in elves
def  hasS(pnt,elves): return (pnt[0]+1,pnt[1]  ) in elves
def hasSE(pnt,elves): return (pnt[0]+1,pnt[1]+1) in elves

#def moveAtAll(pnt,elves):
def notMove(pnt,elves):
    return not (hasNW(pnt,elves) or hasN(pnt,elves) or hasNE(pnt,elves) or hasW(pnt,elves) or hasE(pnt,elves) or hasSW(pnt,elves) or hasS(pnt,elves) or hasSE(pnt,elves))

def moveN(pnt,elves):
    if not hasNW(pnt,elves) and not hasN(pnt,elves) and not hasNE(pnt,elves):
        return (pnt[0]-1,pnt[1])
    else:
        return ()

def moveS(pnt,elves):
    if not hasSW(pnt,elves) and not hasS(pnt,elves) and not hasSE(pnt,elves):
        return (pnt[0]+1,pnt[1])
    else:
        return ()

def moveW(pnt,elves):
    if not hasNW(pnt,elves) and not hasW(pnt,elves) and not hasSW(pnt,elves):
        return (pnt[0],pnt[1]-1)
    else:
        return ()

def moveE(pnt,elves):
    if not hasNE(pnt,elves) and not hasE(pnt,elves) and not hasSE(pnt,elves):
        return (pnt[0],pnt[1]+1)
    else:
        return ()

def display_map(elves,nRows,nCols):
    points = [['.' for c in range(nCols)] for r in range(nRows)]
    for elf in elves:
        try:
            points[elf[0]][elf[1]] = '#'
        except:
            pass
    map = [''.join(r) for r in points]

    print()
    for row in map:
        print(f"{row}")

def number_of_empty_ground_tiles(elves):
    row_positions = [elf[0] for elf in elves]
    min_row = min(row_positions); max_row = max(row_positions)
    col_positions = [elf[1] for elf in elves]
    min_col = min(col_positions); max_col = max(col_positions)
    rect_rows = max_row-min_row+1; rect_col = max_col-min_col+1
    num_empty_tiles = rect_rows*rect_col - len(elves)

    return num_empty_tiles

if __name__ == "__main__":
    file = sys.argv[1]

    elves,nr,nc = read_map(file)

    move_order = ['moveN', 'moveS', 'moveW', 'moveE']

    for round in range(TOTAL_NUM_ROUNDS):
        for elf in elves:
            # if round==1 and elf==(7,2):
            #     import pdb;pdb.set_trace()

            if notMove(elf,elves):
                elves[elf] = elf
            else:
                for move in move_order:
                    if next:=locals()[move](elf,elves):
                        elves[elf] = next
                        break

        # print(f"{elves}")

        # if all elves move position equal there current position (ie they need not move) we can stop
        if all([True if elf==elves[elf] else False for elf in elves]):
            print(f"Stopping at round {round+1} as all elves need not move")
            break

        # find unique moves and move
        cnt = Counter(elves.values())
        for elf,move_to in elves.items():
            if cnt[move_to] > 1 or elf==move_to:
                elves[elf] = ()  # don't move
        
        for elf in list(elves.keys()):
            if move_to:=elves[elf]:
                elves[move_to] = ()
                del elves[elf]

        # display
        # print(f"\n== End of Round {round+1} ==")
        # display_map(elves,nr,nc)

        # advance move_order
        move_order = move_order[1:] + move_order[:1]

    n_tiles = number_of_empty_ground_tiles(elves)

    print(f"The number of empty ground tiles is {n_tiles}")
    part1_ans = n_tiles

    # print(f"The total number of unique positions the last knot visited is {num_unique_pos_last_knot_visited}")
    # part2_ans = num_unique_pos_last_knot_visited

    if len(sys.argv) >= 3:
        if int(sys.argv[2]) == part1_ans:
            print(f"Answer for part 1 is correct!")
    if len(sys.argv) == 4:
        if int(sys.argv[3]) == part2_ans:
            print(f"Answer for part 2 is correct!")

