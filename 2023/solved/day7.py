import sys
from collections import Counter
from copy import deepcopy

ORDERED = 'AKQJT98765432'
ORDERED_JOKERS = 'AKQT98765432J'

def read_CamelCards(filename):
    with open(filename,'r') as fh:
        lines = [line.rstrip('\n') for line in fh]
    
    camel_cards = {}
    for line in lines:
        cards, rank = line.split()
        camel_cards[cards] = int(rank)

    return camel_cards

def determine_strength(hand):
    cards_in_hand = [card for card in hand]

    counting_cards = Counter(cards_in_hand)

    counts = counting_cards.values()
    if 5 in counts:
        return 'FIVE'   # 'Five of a kind'
    elif 4 in counts:
        return 'FOUR'   # 'Four of a kind'
    elif 3 in counts and 2 in counts:
        return 'FULL'   # 'Full house'
    elif 3 in counts:
        return 'THREE'  # 'Three of a kind'
    elif 2 in counts and Counter(counts)[2] == 2:
        return 'TWO'    # 'Two pair'
    elif 2 in counts:
        return 'ONE'    # 'One pair'
    else:
        return 'HIGH'   # 'High card'

def determine_strength_with_jokers(hand):
    cards_in_hand = [card for card in hand]

    counting_cards = Counter(cards_in_hand)
    counting_cards_without_jokers = deepcopy(counting_cards)
    if 'J' in counting_cards:
        joker_count = counting_cards_without_jokers.pop('J')
    else:
        joker_count = 0
    
    counts = counting_cards_without_jokers.values()
    max_count = max(counting_cards_without_jokers.values()) if counting_cards_without_jokers else 0

    if max_count+joker_count == 5:
        return 'FIVE'

    if max_count+joker_count == 4:
        return 'FOUR'

    if joker_count == 0:
        if 5 in counts:
            return 'FIVE'   # 'Five of a kind'
        elif 4 in counts:
            return 'FOUR'   # 'Four of a kind'
        elif 3 in counts and 2 in counts:
            return 'FULL'   # 'Full house'
        elif 3 in counts:
            return 'THREE'  # 'Three of a kind'
        elif 2 in counts and Counter(counts)[2] == 2:
            return 'TWO'    # 'Two pair'
        elif 2 in counts:
            return 'ONE'    # 'One pair'
        else:
            return 'HIGH'   # 'High card'
    else:
        if max_count+joker_count == 5:
            return 'FIVE'
        elif max_count+joker_count == 4:
            return 'FOUR'
        elif Counter(counts)[2] == 2 and joker_count == 1: # we could asume joker_count==1 is true by logic
            return 'FULL'
        elif  max_count+joker_count == 3:
            return 'THREE'
        # would never get two pairs with joker as that scenario the joker would make three of kind
        elif max_count+joker_count == 2:
            return 'ONE'
        else:
            raise ValueError('Should never get this')

def sort_cards(cards):
    return sorted(cards, key=lambda word: [ORDERED_JOKERS.index(c) for c in word])

if __name__ == "__main__":
    file = sys.argv[1]

    cc = read_CamelCards(file)

    types = [ 'FIVE', 'FOUR', 'FULL', 'THREE', 'TWO', 'ONE', 'HIGH' ]
    types_of_cards = {t:[] for t in types}

    for hand in cc:
        # strength = determine_strength(hand)
        strength = determine_strength_with_jokers(hand)
        types_of_cards[strength].append(hand)
        print(f"{hand}: {strength}")
    
    ranks = []
    rank = len(cc)
    for type in types:
        cards_sorted = sort_cards(types_of_cards[type])
        
        for c in cards_sorted:
            print(f"{cc[c]} {rank}")
            ranks.append(cc[c]*rank)
            rank -= 1

    print(f"The total winnings are {sum(ranks)}")
