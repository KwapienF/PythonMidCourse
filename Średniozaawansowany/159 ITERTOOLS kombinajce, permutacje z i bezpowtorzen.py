import itertools as it

mylist = ['a','b','c','d']

for combination in it.combinations(mylist,3): # commbinations tworzy kombinacje elementow a 3 oznacza ze z 3 elementow ma si eskladac
    print(combination)
print('-'*100)
for p in it.permutations(mylist,3): # permutation pokauzje wszystkie mozliwe zestawienia bez powtórzen
    print(p)
# for pr it.combinations_with_replacement (mylist,3): # nie dziala juz a tu by bylo nawet aaa aab bbb itd
#     print(pr)
# for i in mylist:
#     for x in mylist:
#         for y in mylist:
#             if i != x and i != y and x != y:
#                 print(i,x,y)
#             else:
#                 continue
print('-'*100)

money = [20,20,20,20,10,10,10,5,5,1,1,1,1,1] # na ile sposobw jestesmy w stanie zaplacic 100zł
result = []
for i in range(1,101):
    for combination in it.combinations(money,i):
        if sum(combination) == 100:
            result.append(combination)

result = set(result) # konwertujemy liste na zbiór  zbior rozni sie tym ze elementy w zbiorz enie maja kolejnosci i nie powtarzaja sie

for r in result:
    print(r)
print('-'*100)
money2 = [50,20,10]
for i in range(1,101):
    for combination in it.combinations_with_replacement(money2, i): # o zadzialalo sick!
        if sum(combination) == 100:
            print(combination)

# lab

import itertools as it
import math

notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']

for x in it.permutations(notes, 4):
    print(x)

print("4-notes melody, notes cannot repeat - it is variation without repeating - there are {} possibilities".format(
    math.factorial(len(notes)) / math.factorial(len(notes) - 4)))

input('Press enter')

for x in it.product(notes, repeat=4):
    print(x)

print("4-notes melody - notes can repeat - it is variation with repeating - there are {} possibilities".format(
    pow(len(notes), 4)))

