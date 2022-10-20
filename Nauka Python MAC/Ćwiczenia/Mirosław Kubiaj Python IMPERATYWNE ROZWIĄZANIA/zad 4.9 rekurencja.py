def main(x):
    if x <= 1:
        return  "Koniec"
    else:
        return main(x-1), "Wywołuje siebie"
print(main(5))


def prosto(x):
    if x <= 5:
        print("wywoluje siebie", x, "raz")
        prosto(x + 1)
prosto(1)

def silnia(n):
    if n < 1:
        return 1
    else:
        return  n * silnia(n-1)

def wynik():
    for n in range(0,11):
        silnia(n)
        print(n,"! =", silnia(n))
wynik()

