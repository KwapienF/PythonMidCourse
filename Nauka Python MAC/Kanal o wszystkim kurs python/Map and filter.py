liczby = [2, 10, 24, 13, 7,  9]
 # mapy

def funkcja(x):
    return x * 2

wynik = map(funkcja, liczby)  # ucinamy nawiasy aby nie ograniczyc dzialania funkcji do jednego argumentu
print(list(wynik))

wynik2 = map(lambda x: x * 2, liczby)
print(list(wynik2))


# mapy na kazdym argumencie z listy robia jakis algorytm
# Filtry:

wynik3 = filter(lambda x: x % 2 ==0, liczby)  # filter nie robi nic tylko patrzy czy spelniony jest warunek
print(list(wynik3))