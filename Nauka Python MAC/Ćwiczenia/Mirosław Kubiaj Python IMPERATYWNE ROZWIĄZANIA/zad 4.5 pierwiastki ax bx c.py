from math import *
def trojmian(a,b,c):
    delta = b**2 - 4*a*c
    if delta > 0 and a != 0:
        x1 = ((-b + sqrt(delta))/(2*a))
        x2 = ((-b - sqrt(delta))/(2*a))
        print("x1 =%5.2f"% x1, "a x2 = %5.2f"% x2)
    elif delta == 0 and a != 0:
        x0 = -b/(2*a)
        print("x0 = %5.2f"% x0)
    elif a == 0:
        x = -c/b
        print("x = %5.2f"% x)
    elif delta < 0:
        print("Delta mniejsza od zera, brak pierwiastków")

def rownanie():
    a = float(input("podaj a: "))
    b = float(input("podaj b: "))
    c = float(input("podaj c: "))
    trojmian(a,b,c)
rownanie()