import sys
from itertools import accumulate

def read_platform(filename):
    with open(filename,'r') as fh:
        lines = [line.rstrip('\n') for line in fh]
    
    platform = []
    nrows = len(lines); ncols = len(lines[0])
    flattened = ''.join(lines)
    for col in range(ncols):
        platform.append(''.join([flattened[col+(r*ncols)] for r in range(nrows)]))

    return platform

def find_weight_per_slice(slice):
    sections = slice.split('#')
    lengths = list(accumulate([len(s) for s in sections]))
    heaviest = len(slice)
    starting_weight = [heaviest]+[heaviest-(l+i+1) for i,l in enumerate(lengths[:-1])]

    section_weights = []
    for sindx,section in enumerate(sections):
        num_rocks = section.count('O')
        start = starting_weight[sindx]
        weight_rocks = range(start,start-num_rocks,-1)
        # print(f"{list(weight_rocks)}")
        section_weights.append(sum(weight_rocks))
    # print(f"{slice}  {starting_weight}  {section_weights}")
    total_weight = sum(section_weights)

    return total_weight

if __name__ == "__main__":
    file = sys.argv[1]

    platform = read_platform(file)
    total_weight = 0
    for beam in platform:
        beam_weight = find_weight_per_slice(beam)
        total_weight += beam_weight

    print(f"The total load on the north support beams is {total_weight}")
