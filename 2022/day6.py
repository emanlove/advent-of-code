import sys

def read_datastream(filename):
    with open(filename,'r') as fh:
        ds_str = fh.readline().rstrip('\n')

    ds = [c for c in ds_str]

    return ds

def find_start_of_packet_marker(ds,size):
    for indx,_ in enumerate(ds):
        if len(set(ds[indx:indx+size])) == size:
            return indx+size   # noting Python is zero based but answer will be one based

if __name__ == "__main__":
    file = sys.argv[1]
    marker_size = int(sys.argv[2])

    datastream = read_datastream(file)
    pos_marker = find_start_of_packet_marker(datastream, marker_size)

    print(f"The position of the marker is {pos_marker}")
    part1_ans = pos_marker

    if len(sys.argv) >= 4:
        if int(sys.argv[3]) == part1_ans:
            print(f"Answer is correct!")
