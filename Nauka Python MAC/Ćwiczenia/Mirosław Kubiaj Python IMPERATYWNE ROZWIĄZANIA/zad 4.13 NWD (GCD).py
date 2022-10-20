import math
def nwd(x,y):
    if x % y == 0:
        return y
    else:
        return nwd(y,x % y)

def wynik():
        x = int(input("Podaj liczbę dodatnią x: "))
        y = int(input("Podaj liczbę dodatnią y: "))
        print("nwd(",x,",",y,") = ", nwd(x,y), ".", sep = "")
wynik()


print(math.gcd(49,27))