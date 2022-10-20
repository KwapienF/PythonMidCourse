colors = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
figures = [
    {'Figure':'Ace',  'Power':14},
    {'Figure':'King', 'Power':13},
    {'Figure':'Queen','Power':12},
    {'Figure':'Jack', 'Power':11},
    {'Figure':'10',   'Power':10},
    {'Figure':'9',    'Power':9}] # elementami listy figures są słowniki
allCards = []
aCard = {}
i = 0

for c in colors:
    for f in figures:
        aCard = f.copy()
        aCard['Color'] = c
        allCards.append(aCard)

import random
random.shuffle(allCards)
print(allCards)
player1 = []
player2 = []
i = 0
for cards in allCards:
    if i == 0 or i % 2 == 0:
        player1.append(cards)
        i+=1
    else:
        player2.append(cards)
        i+=1
if len(player1) == len(player2):
    print("Utworzono talie graczy.")
random.shuffle(player1)
random.shuffle(player2)
print(player1)
print(player2)
# zamiast dlugiej funkcji if mozna rozdac karty po prostu dodajac elemtny z lsit jak ponizej
#player1 = allCards[:12]
#player2 = allCards[12:]

while len(player2) > 0 and len(player1) > 0:
    card1 = player1.pop(0) # usuwamy pierwsza karte  ponizej ja dodajemy do wygranej talii i od nowa petla znowu wystarczy ze jest 0 bo na 0 wskoczyla druga pozycja wiec nei trzeba tutaj iterowaz za pomoca i
    card2 = player2.pop(0)
    if card1["Power"] == card2["Power"]:
        player1.append(card1)
        player2.append(card2)
        print("remis")
    elif card1["Power"] > card2["Power"]:
        player1.append(card1)
        player1.append(card2)
        print("Player 1's round")
    else:
        player2.append(card1)
        player2.append(card2)
        print("Player 2's round")

if len(player1) > 0:
    print("Player 1 WON!!!")
else:
    print("Player 2 WON!!!")






