import sys

def read_raw_calories(filename):
    with open(filename,'r') as fh:
        raw_calories = [line.rstrip('\n') for line in fh]

    return raw_calories

def split_calories_into_elves(raw_calories):
    elves_calories = [0]
    indx = 0
    for calorie in raw_calories:
        if calorie == '':
            elves_calories.append(0)
            indx += 1
        else:
            elves_calories[indx] += int(calorie)

    return elves_calories

if __name__ == "__main__":
    file = sys.argv[1]
    raw_calories = read_raw_calories(file)
    elves_calories = split_calories_into_elves(raw_calories)
    elves_calories.sort(reverse=True)
    print(f"The most calories are {max(elves_calories)}.")
    print(f"The total of the top three calories are {sum(elves_calories[:3])}.")
    if len(sys.argv) == 3:
        if int(sys.argv[2]) == max(elves_calories):
            print(f"Answer for part 1 is correct!")
    if len(sys.argv) == 4:
        if int(sys.argv[3]) == sum(elves_calories[:3]):
            print(f"Answer for part 2 is correct!")
