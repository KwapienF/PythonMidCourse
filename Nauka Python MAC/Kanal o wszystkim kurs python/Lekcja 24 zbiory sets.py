liczby1 = {0, 1, 2, 3, 4, 5}  # zbior tworzy sie w nawiasach klamrowych zbiro czyli set
print(liczby1)

slowa = set(["a", "b", "c"])  # z listy utworz zbiór wyswielti w roznej kolejnosci bo zbiory sa unorderedi nie mozna przypisac im indeksu i wywolywac ich po kolejnosci
print(slowa)

liczby1.add(444)  # kazda funkcjama swoje metody listy appedn ma a zbiory maja add
print(liczby1)
liczby1.remove(0)
print(liczby1)
liczby1.add(5) # nie doda 2 razy tej samej liczby bo zbior zawiera jakies argumenty cos ie nei moga powtarzac w przeciwienstwie do listy
print(liczby1)

print(1 in liczby1) # to zwrocu booleend true or false, sprawdza czy liczba jest w danym zbiorze
print("aba" in slowa)

liczby2 = {3, 4, 5, 6}

print(liczby1 | liczby2)  #| kreska pionowa znaczy lub or oznacza logiczną sume i polaczy nam zbiory,
print(liczby1 & liczby2)  #& iloczyn czyli czesc wspolna pokaze wspolne elementy zbiorw
print(liczby1 - liczby2)  #& odejmowanie zbiorw od siebie. w zbiorach odejmuje zawsze od lewej do prawej czyli usunie ze zbioru 1 elementy zbioru 2
print(liczby1 ^ liczby2)  # ^ to roznica symetryczna czyli odejmuje zbior 2 od 1 i pozniej 1 od 2 i wyswielta sume pozostlaych elementow co w efekcie da nam zbior z usunietymi elementami ktore sie powtarzaly w jednym i grudim
