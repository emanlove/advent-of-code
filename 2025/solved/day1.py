import sys


def read_rotations_part2(filename):
    with open(filename, 'r') as fh:
        lines = [line.rstrip('\n') for line in fh]

    num_zeros = 0
    this = 50
    for line in lines:
        direction = line[0]
        adjustment = int(line[1:])

        num_zeros += adjustment // 100
        adjustment = adjustment % 100

        if direction == 'L':
            next = this - adjustment
        elif direction == 'R':
            next = this + adjustment

        if (next < 1) or (next > 99):
            num_zeros += 1
            this = next % 100
        else:
            this = next

    return num_zeros

def read_rotations(filename):
    with open(filename, 'r') as fh:
        lines = [line.rstrip('\n') for line in fh]

    num_zeros = 0
    pointer = 50
    for line in lines:
        direction = line[0]
        adjustment = int(line[1:])

        if adjustment == 0:
            print("Adjustment is zero")
            continue

        if direction == 'L':
            # if pointer > adjustment:
            #     pointer -= adjustment
            # if pointer == (adjustment % 100):
            #     num_zeros += 1
            #     num_zeros += adjustment // 100
            # if pointer < (adjustment % 100):
            #     num_zeros += 1
            #     num_zeros += adjustment // 100
            if pointer <= (adjustment % 100):
                if pointer != 0:
                    num_zeros += 1
                num_zeros += adjustment // 100
            # print(f"{pointer} -{adjustment} {num_zeros}")
            pointer -= (adjustment % 100)
            pointer = pointer % 100
            # print(f"{pointer}")

        elif direction == 'R':
            # if (100 - pointer) > adjustment:
            #     pointer += adjustment
            # if (100 - pointer) == (adjustment % 100):
            #     num_zeros += 1
            #     num_zeros += adjustment // 100
            # if (100 - pointer) < (adjustment % 100):
            #     num_zeros += 1
            #     num_zeros += adjustment // 100
            if (100 - pointer) <= (adjustment % 100):
                num_zeros += 1
                num_zeros += adjustment // 100
            # print(f"{pointer} +{adjustment} {num_zeros}")
            # pointer += (adjustment % 100)
            # pointer = pointer % 100
            pointer = (pointer + adjustment) % 100
            if pointer == 0:
                num_zeros += 1
            # print(f"{pointer}")

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

        # num_zeros += abs(pointer // 100)
        # if pointer == 0:
        #         num_zeros -= 1
        # if pointer == 100:
        #         num_zeros += 1
        # pointer = pointer % 100

        # if pointer == 0:
        #     num_zeros -= 1

    return num_zeros


if __name__ == "__main__":
    file = sys.argv[1]

    # zeros = read_rotations(file)
    zeros = read_rotations_part2(file)
    print(f"The number of zeros is {zeros}")
