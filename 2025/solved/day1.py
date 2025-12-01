import sys

def read_rotations(filename):
    with open(filename, 'r') as fh:
        lines = [line.rstrip('\n') for line in fh]

    num_zeros = 0
    pointer = 50
    for line in lines:
        direction = line[0]
        adjustment = int(line[1:])

        if direction == 'L':
            pointer -= adjustment
        elif direction == 'R':
            pointer += adjustment
        else:
            print(f"unknown direction {direction}")

        # pointer = pointer % 100
        # print(f"Dial points to {pointer}")

        # if pointer == 0:
        #     num_zeros += 1
        # if (pointer % 100) == 0:
        #     num_zeros += 1
        # else:
        #     num_zeros += abs(pointer // 100)
        num_zeros += abs(pointer // 100)
        if pointer == 0:
                num_zeros -= 1
        if pointer == 100:
                num_zeros += 1
        pointer = pointer % 100
        # if pointer == 0:
        #     num_zeros -= 1

    return num_zeros


if __name__ == "__main__":
    file = sys.argv[1]

    zeros = read_rotations(file)
    print(f"The number of zeros is {zeros}")
