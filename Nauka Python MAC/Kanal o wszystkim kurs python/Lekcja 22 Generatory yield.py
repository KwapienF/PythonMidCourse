def gen():
    i = 0
    while i < 5:
        yield i # yield zwraca i i kontynuje dzialanie petli a retrun by wyswietlio i przerwala petle
        i +=1
for i in gen(): # for mozemy uzyc na funkcji ktora ma w sobie yield czyli jest generatorem na innej nie uzyjemy for
    print(i)  # drukuje z petli for
print(list(gen())) #Drugukje z petli while  kazde i pokolei zwracane przez yield. ale ze jest to generator to trzeba w formie lsity to wyswietlic bo daje kilka wynikow


def parzyste(x): # zwroci nam parzyste liczby funckja
    i = 0
    while i <= x:
        if i % 2 == 0:
            yield i
        i += 1
for i in parzyste(16):
    print(i)
print(list(parzyste(16)))


