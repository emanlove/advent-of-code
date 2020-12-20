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

    called_out = {}
    for position,start_num in enumerate(starting_nums[:-1]):
        called_out[start_num] = position

    previous_num = starting_nums[-1]
    for turn in range(len(starting_nums),nthNumber):
        if previous_num in called_out:
            saying = turn - 1 - called_out[previous_num]
            #print(f"{turn-1} - {called_out[previous_num]} : {saying}")
            called_out[previous_num] = turn - 1
        else:
            saying = 0
            called_out[previous_num] = turn - 1

        previous_num = saying
        #print(f"The number said on turn {turn+1} was {previous_num}")

    print(f"The number said on turn {turn+1} was {previous_num}")
