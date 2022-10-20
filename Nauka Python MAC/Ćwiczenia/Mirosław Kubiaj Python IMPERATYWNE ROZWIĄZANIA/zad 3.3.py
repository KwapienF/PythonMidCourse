x = 1
suma = 0
while x <= 12:
    if x % 2 == 0:
        suma += x
        print(x, end = "+")
        x += 1
    else:
        x += 1
print(" =",suma)


print("teraz silnia")
s= int(input("Podaj liczbę: "))
c = 1
silnia = 1
while c <= s:
    silnia *= c
    c+=1
print(silnia)


