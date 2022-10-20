zmienna = 1
zmienna2 = "Abc"
lista = [1, 2, "c", "d", "e"]  # lista moze przechowac nieskonczenie wiele dowolnych zmiennych z indeskem
print(lista)
print(lista[0]) # odwołujemy sie do elementu pierwszego listy bo liczymy od 0
lista[2] = 3 # zmieniamy element w liście
print(lista)
tekst = "Siema"
print(tekst[3]) # mozemy drukowac dowolny indekst ze zmiennej
print(lista +  [1]) # mozna dolaczyc do listy elementy
print(lista * 3) # wyswietli sie 3 razy pod rzad toc o w liscie
print("Ilość elementów w liście: ", len(lista))  # len length wyswietla ilosc elementow w liscie
b = 0
while b < len(lista) : # można też dac porownanie jest różne !=
    print(lista[b])
    b+=1
lista.append("f")  #kropka to operator który pozwala sie odwołać do elementow zawartych w obiekcie lista append = dołącz
print(lista)
lista.append(["g", "h"])
print(lista) #Powstała lista w liście
print(lista[6][1]) # 6 lelement to lista a drugi nawiast mowi ktory element z tej isty pokazać
lista.insert(3,3) # insert dołącza elemnety w dwolonym miejscu, a append zawze na końcu (3,3) pierwsze 3 mówi w jakim iejscu dołączyc słowo a druga to co wstawiamy
print(lista)
print("ilość wystąpień danego znaku w liście", lista.count(3)) # count liczy ile jest danych elementow w liscie
print("Index", lista.index("f")) # index mowie nam na ktorym miejscu jest wskazany przez nas element wystepujacy jako pierwszy
lista.remove("f") # remove usuwa element z listy
print(lista)
lista2 = [1, 20, 30, -5, 0]
print("min", min(lista2)) # pokazuje najmniejsza liczbe
print(max(lista2))
lista2.sort() # sortuje od min do max elementy w liscie
print(lista2)
lista2.reverse() # odwraca elementy w liście
print(lista2)
lista2.clear() # czysci liste i zostawia pustą
print(lista2)






