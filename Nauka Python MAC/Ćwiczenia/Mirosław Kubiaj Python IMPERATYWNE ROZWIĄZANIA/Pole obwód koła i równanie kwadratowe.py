import math
from math import sqrt as pierwiastek
print(pierwiastek(81))

# r = float(input("podaj promień koła: "))
# pole = math.pi * r * r
# if r >= 0:
#     print (f" Pole koła wynosi {pole}, a obwód koła wynosi {2 * math.pi * r}")
# else:
#     print("Promień nie może być ujemny")


print("podaj współczynniki równani akwadratowego ax^2 + bx + c = 0")
a = float(input("Podaj współczynnika a: "))
b = float(input("Podaj współczynnika b: "))
c = float(input("Podaj współczynnika c: "))

delta = (b ** 2) - (4 * a * c)
if delta > 0:
    x1 = (-b - pierwiastek(delta)) / (2 * a)
    x2 = (-b + pierwiastek(delta)) / (2 * a)
    print("Równanie ma dwa pierwiastki: x1 =  %5.2f"% x1, "oraz x2 = %5.2f"% x2)
elif a == 0 and b == 0 and c > 0:
    print(f"x może być dowloną liczbą, a c = tylko i wyłącznie 0, a nie {c}")
elif a == 0 and b == 0 and c == 0:
    print("x może być dowloną liczbą.")
elif delta == 0:
    x0 = (-1 * b) / (2 * a)
    x0 = round(x0,2)
    print(f"równanie ma jeden pierwiastek x0 = {x0}")
elif delta < 0:
    print(f"Brak rozwiązania delta wyszła ujemna: {delta}")
