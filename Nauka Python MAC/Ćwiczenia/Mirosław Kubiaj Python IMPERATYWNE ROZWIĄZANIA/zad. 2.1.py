# ax + b = c
a = float(input("Podaj liczbę a równiania ax +b = c, a obliczę x: "))

if a == 0:
    print("a nie może być 0")
else:
    b = float(input("Podaj liczbę: "))
    c = float(input("Podaj liczbę: "))
    print("x = ", (c-b)/a)
