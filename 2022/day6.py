import sys, copy

def read_datastream(filename):
    with open(filename,'r') as fh:
        ds_str = fh.readline().rstrip('\n')

    ds = [c for c in ds_str]

    return ds

def find_start_of_packet_marker(ds):
    for indx,_ in enumerate(ds):
        if len(set(ds[indx:indx+4])) == 4:
            return indx+4   # noting Python is zero based but answer will be one based

if __name__ == "__main__":
    file = sys.argv[1]

    datastream = read_datastream(file)
    pos_marker = find_start_of_packet_marker(datastream)

    print(f"The position of the marker is {pos_marker}")
    part1_ans = pos_marker

    if len(sys.argv) >= 3:
        if int(sys.argv[2]) == part1_ans:
            print(f"Answer for part 1 is correct!")
    if len(sys.argv) == 4:
        if sys.argv[3] == part2_ans:
            print(f"Answer for part 2 is correct!")
