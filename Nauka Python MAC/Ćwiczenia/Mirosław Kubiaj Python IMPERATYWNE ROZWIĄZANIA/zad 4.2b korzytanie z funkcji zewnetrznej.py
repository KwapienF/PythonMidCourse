from kalkulator import *
print("wybierz działanie i podaj liczby do jego obliczenia:")
rodzaj = int(input("Podaj 1 dla dodawania 2 dla odejmowania 3 dla mnożenia i 4 dla dzielenia: "))
if rodzaj == 1:
    print(dodawanie(a,b))
elif rodzaj == 2:
    print(minus())
elif rodzaj == 3:
    print(mnoz())
elif rodzaj == 4:
    print(dziel())
else:
    print("Nie ma dzialan")