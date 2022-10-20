#funkcje wywołujemy po przez nawiasy okrągłe

def funkcja_test(): # def to zdefiniuj funkcje nawias okrągły musi byc bo mowi ze to funkcja i to miejsce na argumenty
    print("Funkcja...")

funkcja_test() # wywołujemy funkcja która na cos printuje :)
funkcja_test()
funkcja_test()


def dodaj(x):
    print(x + 1)
dodaj(3)

def dodaj(x, y = 1, z = 0): # ta sama nazwa funkcji nadpisuje poprzednią w innych językach działałyby 2 funkcje w zależnosci ile argumentow sie poda
    print(x + y + z)
dodaj(4) # to dziala bo y jest 1 jak dodamy 2 argumenty funkcja pomienie ze y = 1 i doda 2 podane liczby
dodaj(4, 5)
dodaj(2, 3, 5)

def dodaj2(x, y = 1, z = 0):
    return x + y + z # return zwraca poza funkcje wynik, na zewnątrz
print(dodaj2(2,3)) # return nie pokazuje wyniku trzeba wyprintować
wynik = dodaj2(2, 3, 5)
print(wynik)

def func(z):
    return z * z

zmienna = func # zmienna  funkcje podpisujemy bez nawiasów wtedy w zmiennej definiujemy niewiadomą w nawiasach jak niżejw print
print(zmienna(5))
def func2(f1, x): # f1  pod to progrma wie ze chcemy podlozyc inną funkcję
    return f1(x) * x
print(func2(func, 5))

def silnia(x): # silnia liczona za pomocą funkcji i rekurencji (czyli wewnątrz funkcji wywołujemy ją samą siebie
    if x <= 1:
        return 1
    else:
        return x * silnia(x - 1)
print(silnia(123))




