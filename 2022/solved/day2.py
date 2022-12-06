import sys

#ASSUMED_SCORING_STRATEGY 
partial = {
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

#ACTUAL_SCORING_STRATEGY
full = {
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

def read_strategy(filename):
    with open(filename,'r') as fh:
        lines = [line.rstrip('\n') for line in fh]

    return lines

def strategy_score(strategy,knowledge):
    score = 0
    for game in strategy:
        score += globals()[knowledge][game]
    
    return score

if __name__ == "__main__":
    file = sys.argv[1]
    understanding = sys.argv[2]
    strategy = read_strategy(file)

    end_score = strategy_score(strategy, understanding)
    print(f"The end score would be {end_score}.")

    part1_ans = part2_ans = end_score

    if len(sys.argv) == 4:
        if int(sys.argv[3]) == part1_ans:
            print(f"Answer for part 1 is correct!")
    if len(sys.argv) == 5:
        if int(sys.argv[4]) == part2_ans:
            print(f"Answer for part 2 is correct!")
