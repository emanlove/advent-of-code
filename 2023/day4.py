import sys
from functools import reduce

LIMITS = {'red': 12, 'green': 13, 'blue': 14}

def read_cards(filename):
    with open(filename,'r') as fh:
        lines = [line.rstrip('\n') for line in fh]
    
    cards = {}
    points = []
    for line in lines:
        c, n = line.split(': ')
        _,card = c.split('Card ')
        card = int(card)

        winningNumStr,myNumStr = n.split(' | ')
        winning_nums = winningNumStr.split(' ')
        winning_nums = [n for n in winning_nums if n!='']
        my_numbers = myNumStr.split(' ')
        my_numbers = [n for n in my_numbers if n!='']
        matching_numbers = set(winning_nums) & set(my_numbers)
        num_matchs = len(matching_numbers)
        point_value = 2**(num_matchs-1) if num_matchs else 0
        points.append(point_value)

    print(f"The total worth of points for the cards is {sum(points)}")

if __name__ == "__main__":
    file = sys.argv[1]

    read_cards(file)
