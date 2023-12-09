import sys
from collections import Counter

ORDERED = 'AKQJT98765432'

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

def sort_cards(cards):
    return sorted(cards, key=lambda word: [ORDERED.index(c) for c in word])

if __name__ == "__main__":
    file = sys.argv[1]

    cc = read_CamelCards(file)

    types = [ 'FIVE', 'FOUR', 'FULL', 'THREE', 'TWO', 'ONE', 'HIGH' ]
    types_of_cards = {t:[] for t in types}

    for hand in cc:
        strength = determine_strength(hand)
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
