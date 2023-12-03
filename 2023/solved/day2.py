import sys
from functools import reduce

LIMITS = {'red': 12, 'green': 13, 'blue': 14}

def read_games(filename):
    with open(filename,'r') as fh:
        lines = [line.rstrip('\n') for line in fh]
    
    valid_games = []
    powers = []
    for line in lines:
        g, r = line.split(': ')
        _,game = g.split('Game ')
        game = int(game)

        # reveals = r.split('; ')
        # for reveal in reveals:
        #     colors = reveal.split(', ')
        #     for c in colors:
        #         count, color = c.split(' ')
        #         if int(count) > LIMITS[color]:

        if is_game_valid(r):
            valid_games.append(game)

        power = minimum(r)
        powers.append(power)
    
    print(sum(valid_games))
    print(f"the sum of the power of these sets is {sum(powers)}")

def is_game_valid(r):
    reveals = r.split('; ')
    for reveal in reveals:
        colors = reveal.split(', ')
        for c in colors:
            count, color = c.split(' ')
            if int(count) > LIMITS[color]:
                return False
    return True

def minimum(r):
    cubes = {'red': [], 'green': [], 'blue': []}
    reveals = r.split('; ')
    powers = []
    for reveal in reveals:
        colors = reveal.split(', ')
        for c in colors:
            count, color = c.split(' ')
            cubes[color].append(int(count))
    fewest_cubes = [max(cubes[c])for c in cubes]
    # print(f"{fewest_cubes}")
    power = reduce(lambda x, y: x*y, fewest_cubes)
    return power

if __name__ == "__main__":
    file = sys.argv[1]

    read_games(file)
