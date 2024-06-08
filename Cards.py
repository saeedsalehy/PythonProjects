import random

# makig cards
SUITS = ["Clubs", "Diamonds", "Hearts", "Spades"]
RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

rank = random.randrange(0, len(RANKS))
suits = random.randrange(0, len(SUITS))

# print(f'{RANKS[rank]} of {SUITS[suits]}')
# print('--------' * 7)
# making deck
deck = []
for rank in RANKS:
    for suit in SUITS:
        card = rank + ' of ' + suit
        deck.append(card)
        # print(card)
# print(deck)
# shuffling cards
n = len(deck)
for i in range(n):
    r = random.randrange(0, i + 1)
    deck[i], deck[r] = deck[r], deck[i]
print(deck)
print(len(deck))
