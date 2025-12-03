import sys

def retry_part2(filename):
    with open(filename, 'r') as fh:
        lines = [line.rstrip('\n') for line in fh]

    num_zeros = 0
    pointer = 50
    for line in lines:
        direction = line[0]
        adjustment = int(line[1:])

        print(f"{pointer} {direction}{adjustment} {num_zeros}")
        num_of_full_rotations = adjustment // 100
        leftover_adjustment = adjustment % 100

        dist_to_edge = pointer if direction == 'L' else 100 - pointer

        # add in number of full rotations
        num_zeros += num_of_full_rotations

        # if pointer is non zero and adjustment is greater than or equal to distance to edge
        #     then add one more zero
        if pointer and (leftover_adjustment >= dist_to_edge):
            num_zeros += 1
            new_pointer = pointer - leftover_adjustment if direction == 'L' else pointer + leftover_adjustment
        else:
            new_pointer = pointer - leftover_adjustment if direction == 'L' else pointer + leftover_adjustment

        # make sure point is within 0-99
        pointer = new_pointer % 100

    return num_zeros

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
            next = next % 100
            if next > this:
                num_zeros += 1
            elif next == this and this != 0:
                num_zeros += 1
        elif direction == 'R':
            next = this + adjustment
            next = next % 100
            if next < this:
                num_zeros += 1
            elif next == this and this != 0:
                num_zeros += 1
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
    # zeros = read_rotations_part2(file)
    zeros = retry_part2(file)
    print(f"The number of zeros is {zeros}")
