lista = ["Subskrybuj", "Kanał", "o", "Wszystkim"]
print(lista)
print(len(lista))
lista[1] = lista[1].lower()
lista[3] = lista[3].lower()
print(lista)

i = 0
while i < len(lista):
    print(lista[i])
    i +=1

# pętla obiektowa teraz mamy liste ktora jest obiektem wiec mozemy uzyc tej petli

for x in lista: # deklarujemy nową zmienną w obiekcie lista for bedzie robilo petle tyle razy ile obiekt ma elementow
    print(x)
print(range(10))
print(list(range(10))) # funkcja range buduje nam liste (list) z indeksami od 0 do ilosci podanego elementu
for y in range(10): # dla takiej petli definiujemy ile dokaldne ma zrobi petli
    print(lista) # czyli wydrukuje nam 10 razy liste)
for y in range(10):
    print(y)
    #czyli for robi tyle petli ile jest elementow w danym obiekcie lub tyle ile jej kazemy funkcją range

for z in range(1,11): # liiczba w nawiase z lewej mowi nam od jakiej wartosci ma zacząć a z pawej ile razy petla
    print(z)
for z in range(1,11, 2): # 3 argument w nawiasie mowi co ktory elelemnt ma nam wyswietlac pętla czyli np czy parzyste itd
    print(z)

l = int(input("Podaj liczbę: "))
r = 0
for silnia in range(1,(l+1)):
    print(silnia)