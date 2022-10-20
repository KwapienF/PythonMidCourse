# rozpakwoanie kolekcji  np krotki czy listy
a,b = (2,5)  # przypisanie obiektu kolekcji krotki
print(a)
print(b)  # wydrukuje element krotki przypisze sobie do zmiennej, bez zadnych indeksow przypisywania po indeksie itd
c,d = [2,5]
print(c)
print(d)

x = 10
y = 20
x,y = y,x
print("x:", x)
print("y:", y)
# zamiast zamienic te wartosci skomplikowanie tak:
# tmp = x # tymczasowa zapamietanie x
# x = y
# y = tmp

start, *wszystko, koniec = (1, 2, 3, 4, 5, 6, 7) #zmiennych musi byc tyle ile elemnetow w krotce lub liscie chyba zeby dac gwiazdke* wtedy zmienna z gwiazdka wezmie wszystkie ktore sa ponadliczbowe
print(start)
print(wszystko) # z * wiec przyjea wszystkie argumenty nieprzypisane
print(koniec)
