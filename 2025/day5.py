import sys
from datetime import datetime

def read_fresh_spoiled_list(filename):

    with open(filename, 'r') as fh:
        lines = [line.rstrip('\n') for line in fh]

    fresh_ranges = []
    check_ingredients = []
    for line in lines:
        if '-' in line:
            start,end = line.split('-')
            # fresh_ranges += list(range(int(start),int(end)+1))
            # fresh_ranges += range(int(start),int(end)+1)
            fresh_ranges.append((int(start),int(end)))
        elif line != '':
            check_ingredients.append(int(line))

    return fresh_ranges, check_ingredients

def simplify_sort_fresh_ranges(fresh_ranges):
    mark = datetime.now()
    sorted_fresh_ranges = sorted(fresh_ranges)
    print(f"sorted fresh ranges - elapsed time: {datetime.now()-mark}")
    # print(sorted_fresh_ranges)

    # following assumes list of ranges is sorted
    simplified_fresh_ranges = []
    this = sorted_fresh_ranges[0]
    for indx,next in enumerate(sorted_fresh_ranges[1:]):
        this_start = this[0]; this_end = this[1]
        next_start = next[0]; next_end = next[1]

        if next_start > this_end + 1:
            simplified_fresh_ranges.append(this)
            this = next
            continue
        elif next_end > this_end:
            this = (this_start,next_end)
            continue
        else:
            # next is within the range of this
            # .. so ignore
            continue

    # ?? do I need to close out the list
    if simplified_fresh_ranges[-1] != this:
        simplified_fresh_ranges.append(this)

    # print(f"{simplified_fresh_ranges}")
    return simplified_fresh_ranges

def sort_fresh_from_spoiled(list_of_fresh, check_these):
    # assumes both list_of_fresh (ranges) and check_these ingredients
    # are sorted in increasing order
    num_fresh_ingredients = 0

    list_pntr = 0

    for check_this in check_these:
        increase_index_by = 0
        for subindx, rnge in enumerate(list_of_fresh[list_pntr:]):
            start = rnge[0]; end = rnge[1]
            if check_this < start:
                # this one is before all sorted ranges
                break
            elif start <= check_this <= end:
                # is fresh
                num_fresh_ingredients += 1
                break
            if check_this > end:
                increase_index_by += 1
                continue
        # since we know the ranges are sorted we don't need to
        # check those we know are less than the ingredient we
        # are currently checking
        list_pntr += increase_index_by

    return num_fresh_ingredients


if __name__ == "__main__":
    file = sys.argv[1]

    fresh_list, check_list = read_fresh_spoiled_list(file)
    sorted_fresh_list = simplify_sort_fresh_ranges(fresh_list)
    sorted_check_list = sorted(check_list)
    num_fresh_ingredients = sort_fresh_from_spoiled(sorted_fresh_list, sorted_check_list)
    print(f"The total number of fresh ingredients is {num_fresh_ingredients}")
