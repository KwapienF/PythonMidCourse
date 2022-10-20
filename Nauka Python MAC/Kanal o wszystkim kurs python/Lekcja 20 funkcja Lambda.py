def funkcja(f, liczba):
    return f(liczba)

print(funkcja(lambda x: x * x, 2))

def kwadrat(x):
    return x * x
print(kwadrat(5))

wynik = lambda x: x * x
print(wynik(6))

wynik = (lambda x: x * x)(6)
print(wynik)

wynik2 = lambda x, y: x* y
print(wynik2(3,4))

wynik2 = (lambda x, y: x* y)(3,4)
print(wynik2)