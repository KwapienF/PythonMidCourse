for number in range(1,21):  # 3 parametr funkcji range mowi nam o ile ma byc skok zrobiony
    print(number)

for number in range(1,21):
    if number % 2 == 0:
        print('Number %2d is %s' %(number,'even')) # even = parzysta
    else:
        print('Number %2d is %s' % (number, 'odd'))  # odd = nieparzysta
#LAB

string_A = '+---+---+---+---+'
string_B = '|   |   |   |   |'

for i in range(9):
    if i %2 != 0:
        print(string_B)
    else:
        print(string_A)