from random import randint
n= int(input("Podaj ile liczb wylosować: "))
i = 1
lista = []
while i <= n:
    los = randint(0,100)
    lista.append(los)
    i+=1
print(f" Twoje liczby to {lista}")
x = 1
max = max(lista)
min = min(lista)
element = 0
a = lista[element]
for x in range(n-1):
   if n == 2:
       print(f"Maksymlana liczba to {max}, a minimalna to {min}")
       break
   elif lista[element] == max:
       print(f" maks liczba to {lista[element]}")
       element += 1
   elif lista[element] == min:
       print(f" Minimalna liczba to {lista[element]}")
       element += 1
   elif lista[element] == lista[element]:
       element += 1
   else:
       element += 1
   a += lista[element]
b = a/n
print(f"Średnia z wylosowanych liczb wynosi {b}")







