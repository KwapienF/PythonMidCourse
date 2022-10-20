message1 = ' "Processing file %s' # % tworzy nam w srodku zmienna s pod ktora bedzie mozna cos podstawic
print(message1 % ('file_1.txt'))
message2 = 'File %s has size %d KB' # %d kaze podstawic liczbe %s string
print(message2 %('plik.txt', 1000)) # w nawaisie po kolei co mamy podstawic pod procent czyli %(s,d) etc
message3 = 'File %20s has size %10d KB' # liczba miedzy %  liczba s i % liczba d okresla ile znakow mozna wstawic pod te zmienne i rezerwuje dla nich miejsce mozna wtedy w slupku wyswietlac dane
print(message3 %('qwertyuio', 12341))
print(f'file size has { 110 + 5} KB') # umieszcza int w stringu lub funkcje lub co chcesz
message4 = 'Procesing file {0:s}' # 0 mowi ze wstawiony bedzie tylko 1 parametr string napis dla funckji format
print(message4.format('plik.txt'))
message5 = 'Procesing file {1:s}' # 0 mowi ze wstawiony bedzie  3 z kolei parametr 0 1 2 z wypisanych w nawiasie   funckji format jak nizej
print(message5.format('plik.txt', 'plik2.txt', 'plik3.txt'))
message6 = 'File {0:s} has size {1:d}' # {1:d} oznacza ze bedzie wstawiony na drugi miejscu
print(message6.format('plik.txt', 132))
# zmiana kolejnosci
message7 = 'File {1:s} has size {0:d}' # {1:d} oznacza ze bedzie wstawiony na drugi miejscu
print(message7.format(132,'plik.txt')) # tu nalezy podac w odwrotnej kolejnosci
# LAB
helloMessage = "Hello %s!"
print(helloMessage % 'Kate')
helloMessage2 = "Hello {0:s}!"
print(helloMessage2.format('Kate'))
helloMessage3 = "%s has %d %s"
print(helloMessage3 %('Kate', 1,  "animal"))
helloMessage4 = ("{0:s} has {1:d} {2:s}" )
print(helloMessage4.format('Kate', 1, 'animal'))
line = '%20s costs %6d u"\u20AC" '
print(line %('Ice cream',3))
print(line %('Trip to Venice',119))
print(line %('PIZZA',6))

line2 = '{0:20s} costs {1:6d} u"\u20AC" '
print(line2.format('Ice cream',3))
print(line2.format('Trip to Venice',119))
print(line2.format('PIZZA',6))

print(2400-500-900)
