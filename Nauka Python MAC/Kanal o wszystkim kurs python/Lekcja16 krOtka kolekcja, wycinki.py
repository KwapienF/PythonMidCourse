# krotka nie krótka!

krotka = (2, 4, 8, 16, 32, 64, 128, "abc")
print(krotka[4])
print(krotka)
# krotka rozni soe od listy tym, ze nie mozna zmieniac wartosci pod indeksem
print("elementów:", krotka.count(1))  # count liczy ile jest takich elementow
print("Index:", krotka.index(64)) # index funkcja zwraca nam na ktorym iejscu znadjuje sie podana liczba
# w liscie mozna modyfikowac zawartosc w krotce nie czyli krotka to wartosc stala niezmienna

print("\nWycinki:")
print(krotka[0:3]) # wyswietli elementy od indeksy 0 do 3 do indeksu 3 czyli wezmie indeksy 0, 1, 2 jest to domkniete z lewej strony z prawej otwarte
print(krotka[3:5])
print(krotka[-2:-5])
 #liczy od tyłu indeksy
print(krotka[0:7:2]) # trzeci element mówi o skoku kolekcji czyli co drugi element wyswietli
print(krotka[0:]) # od 0 do konca indeksu
print(krotka[:4]) #od poczatku samego do wskazaneg indeksu
print(krotka[::-1]) # odwrotnie posortowana krotka od końca do początku

