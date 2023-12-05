import sys
from functools import reduce
from copy import deepcopy

LIMITS = {'red': 12, 'green': 13, 'blue': 14}

def read_cards(filename):
    with open(filename,'r') as fh:
        lines = [line.rstrip('\n') for line in fh]
    
    cards = {}
    points = []
    won_cards = {}
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


    print(f"The total worth of points for the cards is {sum(points)}")

        # # make deep copy of winning/won_cards into counting_cards
        # counting_cards = deepcopy(won_cards)
        # total_cards = 0
        # while counting_cards:
        #     # count number of cards remaining in counting_cards (len of keys) and add to total
        #     total_cards += len(counting_cards.keys())
        #     # remove any keys with empty lists
        #     for card in counting_cards:
        #         if not counting_cards[card]:
        #             counting_cards.pop(card)
            

        # # make deep copy of winning/won_cards into counting_cards
        # # count number of cards remaining in counting_cards (len of keys) and add to total
        # # remove any keys with empty lists
        # # starting with the back of the list
        # #   for any card in values whose list is no longer in the keys add it back in
        # #      or if num_matches for that card is zero add in a self reference (so it will be counted on next round)
        # #      or for any self referencing cards (ie 5 in 5) pop just one each counting round
        # #      or(?) for all cards add it's won_cards to other counting_cards stack poping off that card
        # #  .. repeat
    

    # make to_count list of len(lines) of ones
    num_cards = len(lines)
    to_count = [1] * num_cards
    total_cards = 0
    # while not all zeros
    while (any(to_count)):
        # print(f"{to_count}")
        # count all non zeros and add to total
        # addend = sum([1 for _ in to_count if _>0])
        addend = sum(to_count)
        total_cards += addend
        # for each card in to_count make addition list
        additional = [0] * num_cards
        for indx,multiple in enumerate(to_count):
            card_indx = indx+1
            for add_this_card in won_cards[card_indx]:
                zero_indx = add_this_card-1
                additional[zero_indx] += multiple
            
        # uncount or simply replace???
        to_count = additional

    print(f"The total number of scratchcards I ended up with is {total_cards}")

    # import pdb;pdb.set_trace()

if __name__ == "__main__":
    file = sys.argv[1]

    read_cards(file)
