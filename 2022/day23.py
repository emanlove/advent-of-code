import sys

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

    return elves

def isNW(pnt,elves): return (pnt[0]-1,pnt[1]-1) in elves
def  isN(pnt,elves): return (pnt[0]-1,pnt[1]  ) in elves
def isNE(pnt,elves): return (pnt[0]-1,pnt[1]+1) in elves
def  isW(pnt,elves): return (pnt[0]  ,pnt[1]-1) in elves
def  isE(pnt,elves): return (pnt[0]  ,pnt[1]+1) in elves
def isSW(pnt,elves): return (pnt[0]+1,pnt[1]-1) in elves
def  isS(pnt,elves): return (pnt[0]+1,pnt[1]  ) in elves
def isSE(pnt,elves): return (pnt[0]+1,pnt[1]+1) in elves

move_order = ['moveN', 'moveS' 'moveW', 'moveE']

def moveAtAll(pnt,elves):
    return not (isNW or isW or isNE or isW  or isE  or isSW or isS  or isSE)

def moveN(pnt,elves):
    if not isNW(pnt,elves) and not isN(pnt,elves) and not isNE(pnt,elves):
        return (pnt[0]-1,pnt[1])
    else:
        return ()

def moveS(pnt,elves):
    if not isSW(pnt,elves) and not isS(pnt,elves) and not isSE(pnt,elves):
        return (pnt[0]+1,pnt[1])
    else:
        return ()

def moveW(pnt,elves):
    if not isNW(pnt,elves) and not isW(pnt,elves) and not isSW(pnt,elves):
        return (pnt[0],pnt[1]-1)
    else:
        return ()

def moveE(pnt,elves):
    if not isNE(pnt,elves) and not isE(pnt,elves) and not isSE(pnt,elves):
        return (pnt[0],pnt[1]+1)
    else:
        return ()

def display_map(map,nCols):
    rows = [map[x:x+nCols] for x in range(0,len(map),nCols)]
    strings = [''.join(r) for r in rows]
    print("\n".join(strings))

if __name__ == "__main__":
    file = sys.argv[1]

    map  = read_map(file)
    import pdb;pdb.set_trace()
    # display_map(map,nCols)

    # print(f"The shortest path is {sum(total_steps)}")
    # part1_ans = sum(total_steps)

    # print(f"The total number of unique positions the last knot visited is {num_unique_pos_last_knot_visited}")
    # part2_ans = num_unique_pos_last_knot_visited

    if len(sys.argv) >= 3:
        if int(sys.argv[2]) == part1_ans:
            print(f"Answer for part 1 is correct!")
    if len(sys.argv) == 4:
        if int(sys.argv[3]) == part2_ans:
            print(f"Answer for part 2 is correct!")

