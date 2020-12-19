import sys

def read_starting_numbers(filename):
    with open(filename,'r') as fh:
         data = fh.readline()

    numStr = data.rstrip('\n').split(',')
    numbers = [int(n) for n in numStr]

    return numbers

if __name__ == "__main__":
    file = sys.argv[1]
    nthNumber = int(sys.argv[2])

    starting_nums = read_starting_numbers(file)

    import pdb;pdb.set_trace()
    called_out = {}
    for position,start_num in enumerate(starting_nums[:-1]):
        called_out[start_num] = position+1

    previous_num = starting_nums[-1]
    for turn in range(len(starting_nums)+1,nthNumber+1):
        if previous_num in called_out:
            saying = turn - called_out[previous_num] - 1
            called_out[saying] = turn
        else:
            saying = 0
            #called_out[saying] = turn
        previous_num = saying
        print(f"The number said on turn {turn} was {previous_num}")

    print(f"The number said on turn {turn} was {previous_num}")
