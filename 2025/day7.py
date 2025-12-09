import sys
import math

def read_diagram_and_tilt(filename):

    with open(filename, 'r') as fh:
        lines = [line.rstrip('\n') for line in fh]

    nrows = len(lines[0])
    titled_diagram = []
    S = None
    untouched_reflectors = []
    for row in range(nrows-1,-1,-1):
        titled_row = [line[row] for line in lines]
        if 'S' in titled_row:
            S = (nrows-1-row,titled_row.index('S'))
        reflectors_in_row = [indx for indx,obj in enumerate(titled_row) if obj == '^']
        if reflectors_in_row:
            untouched_reflectors += [(nrows-1-row,r) for r in reflectors_in_row]
        titled_diagram.append([line[row] for line in lines])

    return S, untouched_reflectors, titled_diagram


def calculate_num_splits(S, untouched_reflectors, tilted_diagram):
    started_beams = [S]

    num_splits = 0
    # while(started_beams):
    debug_while = 25
    while debug_while:
        for beam in started_beams:
            # print(f"{beam}")
            added_beams = []
            removed_beams = []
            # from starting point (beam) check for any reflectors in remaining
            # part of the row
            if '^' not in tilted_diagram[beam[0]][beam[1]:]:
                # todo: might save how far beam went
                # remove this beam
                removed_beams.append(beam)
                # indx = started_beams.index(beam)
                # started_beams.pop(indx)
            else:
                num_splits += 1
                next_reflector = (beam[0], tilted_diagram[beam[0]][beam[1]:].index('^')+beam[1])
                print(f"{next_reflector}")
                print(f"{untouched_reflectors}")
                ref_index = untouched_reflectors.index(next_reflector)
                untouched_reflectors.pop(ref_index)
                new_beams = [(next_reflector[0]-1,next_reflector[1]), (next_reflector[0]+1,next_reflector[1])]
                removed_beams.append(beam)
                for new_beam in new_beams:

                    if new_beam not in started_beams:
                        added_beams.append(new_beam)

        for remove in removed_beams:
            # import pdb;pdb.set_trace()
            try:
                indx = started_beams.index(remove)
                started_beams.pop(indx)
            except ValueError:
                raise Exception(f"Unable to find beam {remove} that needs to be removed.\n{started_beams}")
        for added in added_beams:
            started_beams.append(added)
        debug_while -= 1

    return num_splits

if __name__ == "__main__":
    file = sys.argv[1]

    S, untouched_reflectors, tilted_diagram = read_diagram_and_tilt(file)
    print(f"{S}\n{untouched_reflectors}\n{tilted_diagram}")
    num_splits = calculate_num_splits(S, untouched_reflectors, tilted_diagram)
    print(f"The number of times the beam will split is {num_splits}")
