print("Program obliczania silni danej liczby")
silnia = input("Podaj liczbę: ")
x = float(silnia)
y = 1
b = 1
if x < 0:
    print("Nie ma silni z liczby ujemnej")
else:
    while True:
        if 1 > x > 0:
            print("Nie umiem policzyć silni z liczby przecinkowej")
        else:
            c = b
            b = c * y
            c = b
            y += 1
        if y > (x):
            break
    print(f"Silnia podanej liczby wynosi: {c}")
    print("Koniec obliczeń")




