import sys

LIMITS = {'red': 12, 'green': 13, 'blue': 14}

def read_games(filename):
    with open(filename,'r') as fh:
        lines = [line.rstrip('\n') for line in fh]
    
    valid_games = []
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

    print(sum(valid_games))

def is_game_valid(r):
    reveals = r.split('; ')
    for reveal in reveals:
        colors = reveal.split(', ')
        for c in colors:
            count, color = c.split(' ')
            if int(count) > LIMITS[color]:
                return False
    return True


if __name__ == "__main__":
    file = sys.argv[1]

    read_games(file)
