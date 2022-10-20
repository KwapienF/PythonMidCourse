# Program sprawdza czy 3 wprowadzone liczby to są trójki pitagorejskie
a = float(input("Podaj liczbę: "))
b = float(input("Podaj liczbę: "))
c = float(input("Podaj liczbę: "))
if (a**2 + b**2) == c**2:
    print(a,b,c,"jest to trójka pitagorejska")
else:
    print("Nie są to trójki pitagorejskie")
