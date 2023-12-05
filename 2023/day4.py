import sys
from functools import reduce

LIMITS = {'red': 12, 'green': 13, 'blue': 14}

def read_cards(filename):
    with open(filename,'r') as fh:
        lines = [line.rstrip('\n') for line in fh]
    
    cards = {}
    points = []
    winning_cards = {}
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

        # winning_cards[card] = [i for i in range(card+1,card+1+num_matchs)]
        won_cards[card] = [i for i in range(card+1,card+1+num_matchs)]

        # make deep copy of winning/won_cards into counting_cards
        # count number of cards remaining in counting_cards (len of keys) and add to total
        # remove any keys with empty lists
        # starting with the back of the list
        #   for any card in values whose list is no longer in the keys add it back in
        #      or if num_matches for that card is zero add in a self reference (so it will be counted on next round)
        #      or for any self referencing cards (ie 5 in 5) pop just one each counting round
        #      or(?) for all cards add it's won_cards to other counting_cards stack poping off that card
        #  .. repeat
    
    print(f"The total worth of points for the cards is {sum(points)}")
    import pdb;pdb.set_trace()

if __name__ == "__main__":
    file = sys.argv[1]

    read_cards(file)
