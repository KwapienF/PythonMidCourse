file = open('/Users/filipkwapien/Documents/PROGRAMOWANIE/Python/tworzenieplikow/plik1.txt','r') # r oznacza read czyli otwieramy plik tylko na odczyt
content = file.read()
print(content)
file.close() # trzeba zawsze kazdy otwarty plik zamknac ale mozna to ominac aby nie zamykac:
with open('/Users/filipkwapien/Documents/PROGRAMOWANIE/Python/tworzenieplikow/plik1.txt','r') as file:
    content2 = file.read()
    print(content)

# instrukcja with nie jest wydajna do duzych plikow, lepiej to zrobic petla odczytujaca linijka po linijce zamaist jak wyzej calego pliku  w całości:
with open('/Users/filipkwapien/Documents/PROGRAMOWANIE/Python/tworzenieplikow/plik1.txt','r') as file:
    for line in file:
        print(line)
        #lub inna forma
file = open('/Users/filipkwapien/Documents/PROGRAMOWANIE/Python/tworzenieplikow/plik1.txt','r')
for line in file:
    print(line)
file.close()
# CZEGO NIE NALEZY ROBIC:

file = open('/Users/filipkwapien/Documents/PROGRAMOWANIE/Python/tworzenieplikow/plik1.txt','r')
for line in file.readlines(): # tutaj znowu readlines przeczyta caly plik
    print(line)
file.close()
#ODCZYT BAJTOW
file = open('/Users/filipkwapien/Documents/PROGRAMOWANIE/Python/tworzenieplikow/plik1.txt','r')
fragment = file.read(10)# oznacza ze przeczyta tylko 10 bajtow tekst
while fragment:
    print(file.tell(),fragment) # tell wskaznik  pokaze nam w ktorym miejscu tekstu sie znajdujemy
    fragment = file.read(10)
file.close()

