print(" - ".join(["a", "b", "c"]))# funkcja join  rozdzielna nam argumenty podane jako lista  stringiem, ktory wpisalismy wczesniej
print("Hello world".replace("Hello", "Cześć")) # podmienia za hello slowo czesc jak dasz zamiast hello d to wstawi czesc za literke d
print("To jest zdanie".startswith("To")) # zwraca nam wartosc ligoczna prawde lub falsz w zalezsnoci czy nasz tekst zaczyna sie od tego co wpiszemy w argument
print("To jest zdanie".endswith("iek")) # czy konczy sie danym ciagiem znaku true or false
print("jes" in "To jest zdanie") # sprawdza czy gdziekolwiek w teksie znajduej si ejakis ciag znakow
# czy j znajduje sie w takim zdaniu? zleci true or fasle
print("To jest zdanie".upper()) # to juz wiesz
print("To jest zdanie".lower())# i to też ;)


print("-------")
lista = [10, 14, 15, 84, 99]

if all([i % 2 == 0 for i in lista]):# all dziala tak ze kazdy z elementow listy musi spenic pdoany warinek aby funkcja all zwrocila true
    print("liczby są w liście parzyste")
else:
    print( "znajdują sie w liśie liczby nieparzyste")

if any([i == 14 for i in lista]):
    print("w liscie jest 14-ka")
else:
    print( "nie ma tej liczby w liscie")

for i in enumerate(lista): # tworzy numeracje od 0 jak iteracja i pokazuej wszystkie argumenty w liscie
    print(i)
# wyswietli krotki, listy w nawiasach kwadratowych a krotki w nawiasach zwyklych listy mozemy edytowac a krotki nie :)
for i in enumerate(lista):
    print(i[0] + 1, "-", i[1]) # to nam wyswietli  juz nie jako krotki a lanuch znakow bez nawiasow, +1 zacznie nuemracje od 1 a nei od zera i mozna jeszcze rozdzileic argumenty podanym argumentem


