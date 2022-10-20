def silnia(n):
        if n < 1:
            return 1
        else:
            return n * silnia(n - 1)
def wynik(n):
    if n < 1:
        return 1
    else:
        return 1/silnia(n) + wynik(n-1)
print(wynik(20))


# prostsza metoda:
def e(n):
    s, m = (1, 1)
    for i in range(1, n):
        m = m * i
        s = s + 1 / m
    return s
print(e(20))


