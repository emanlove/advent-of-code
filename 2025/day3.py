import sys


def read_battery_banks(filename, num_batteries):

    battery_index_limit = num_batteries - 1
    with open(filename, 'r') as fh:
        lines = [line.rstrip('\n') for line in fh]

    output_joltages = []
    for line in lines:
        battery_bank = [int(b) for b in line]
        start_indx = 0
        len_bank = len(battery_bank)
        joltages_turned_on = []
        for end_indx in range(num_batteries,0,-1):
            battery_max = max(battery_bank[start_indx:len_bank-end_indx+1])
            start_indx = start_indx + battery_bank[start_indx:len_bank-end_indx+1].index(battery_max) + 1
            joltages_turned_on.append(str(battery_max))
        largest_possible_joltage = int(''.join(joltages_turned_on))

        output_joltages.append(largest_possible_joltage)

    return sum(output_joltages)

if __name__ == "__main__":
    file = sys.argv[1]
    num_batteries = int(sys.argv[2])

    total_output_joltage = read_battery_banks(file, num_batteries)
    print(f"The total output joltage is {total_output_joltage}")
