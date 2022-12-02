import sys

ASSUMED_SCORE = {
    'A X': 1 + 3,
    'A Y': 2 + 6,
    'A Z': 3 + 0,
    'B X': 1 + 0,
    'B Y': 2 + 3,
    'B Z': 3 + 6,
    'C X': 1 + 6,
    'C Y': 2 + 0,
    'C Z': 3 + 3,
}

CORRECTED_SCORE = {
    'A X': 3 + 0,
    'A Y': 1 + 3,
    'A Z': 2 + 6,
    'B X': 1 + 0,
    'B Y': 2 + 3,
    'B Z': 3 + 6,
    'C X': 2 + 0,
    'C Y': 3 + 3,
    'C Z': 1 + 6,
}

def read_file(filename):
    with open(filename,'r') as fh:
        lines = [line.rstrip('\n') for line in fh]

    return lines

def strategy_score(strategy):
    score = 0
    for game in strategy:
        score += CORRECTED_SCORE[game]
    
    return score

if __name__ == "__main__":
    file = sys.argv[1]
    data = read_file(file)

    #import pdb;pdb.set_trace()
    end_score = strategy_score(data)
    print(f"The end score would be {end_score}.")

    part1_ans = end_score
    part2_ans = end_score

    if len(sys.argv) == 3:
        if int(sys.argv[2]) == part1_ans:
            print(f"Answer for part 1 is correct!")
    if len(sys.argv) == 4:
        if int(sys.argv[3]) == part2_ans:
            print(f"Answer for part 2 is correct!")
