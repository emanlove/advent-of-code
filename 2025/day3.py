import sys


def read_battery_banks(filename):
    with open(filename, 'r') as fh:
        lines = [line.rstrip('\n') for line in fh]

    output_joltages = []
    for line in lines:
        batteries = [int(b) for b in line]
        leading_battery_max = max(batteries[:-1])
        max_leading_battery_index = batteries[:-1].index(leading_battery_max)
        following_battery_max = max(batteries[max_leading_battery_index+1:])
        largest_possible_joltage = int(str(leading_battery_max)+str(following_battery_max))

        output_joltages.append(largest_possible_joltage)

    return sum(output_joltages)


if __name__ == "__main__":
    file = sys.argv[1]

    total_output_joltage = read_battery_banks(file)
    print(f"The total output joltage is {total_output_joltage}")
