colors = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
figures = ['Ace', 'King', 'Queen', 'Jack', '10', '9']

allCards = []
for c in colors:
    for f in figures:
        allCards.append("%s - %s" % (c, f))

print(allCards)

import random

random.shuffle(allCards)
print(allCards)

player1 = []
player2 = []

max = len(allCards)
for i in range(max):
    if i % 2 == 0:
        player1.append(allCards[i])
    else:
        player2.append(allCards[i])

print('-------PLAYER 1--------')
print(player1)

print('-------PLAYER 2--------')
print(player2)

player1 = allCards[:12]
player2 = allCards[12:]

print('-------PLAYER 1--------')
print(player1)

print('-------PLAYER 2--------')
print(player2)    