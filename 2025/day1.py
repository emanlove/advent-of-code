import sys

def read_calibration(filename):
    with open(filename, 'r') as fh:
        lines = [line.rstrip('\n') for line in fh]

    digits = []
    for line in lines:
        nums = [c for c in line if ord(c) < 58]
        digit = int(nums[0] + nums[-1])
        digits.append(digit)

    print(sum(digits))


NUMBER_STRINGS = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
                  '1', '2', '3', '4', '5', '6', '7', '8', '9']
NUMBER_DICT = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8',
               'nine': '9',
               '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9'}


def read_rotations(filename):
    with open(filename, 'r') as fh:
        lines = [line.rstrip('\n') for line in fh]

    num_zeros = 0
    pointer = 50
    dial = range(0,99)
    for line in lines:
        direction = line[0]
        adjustment = int(line[1:])

        if direction == 'L':
            pointer -= adjustment
        elif direction == 'R':
            pointer += adjustment
        else:
            print(f"unknown direction {direction}")
        pointer = dial[pointer]

        if pointer == 0:
            num_zeros += 1

    return num_zeros


if __name__ == "__main__":
    file = sys.argv[1]

    zeros = read_rotations(file)
    print(f"The number of zeros is {zeros}")
