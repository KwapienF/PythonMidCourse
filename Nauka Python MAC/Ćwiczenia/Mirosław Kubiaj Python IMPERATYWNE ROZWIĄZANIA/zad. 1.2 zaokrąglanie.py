import math

print("pi = %5.3f"% math.pi, ".", sep = "")
pi = round(math.pi, 4)
print(pi)

print("3.123456 = %.3f"% 3.123456)
print(round(3.123456, 3))

print("Pierwiastek kwadratowy z pi do 4 miejsc po przecinku")
a = math.sqrt(math.pi)
print(round(a, 4))
print("a = %1.4f" %a)
print("wynik to : %1.4f" %math.sqrt(math.pi)) #1 to ile pol bedzie przeznacozne na wynik, 4 ile miejsc po przecinku  i % wskauzje jaka liczba ma byc pod to interpretowana
print(f"sqrt(pi) = {math.sqrt(math.pi):.4f}", ".", sep = "")
print(f"inny sposób zapisu: {a:.4f}")

print(f"37/11 bez reszty to {37//11}")
a = 37
b = 11
print("Dla liczb: a = %2i i b = %2i" %(a,b))
print("%2i // %2i = " %(a,b), a//b, ".")
print(f"reszta z dzielenia 37/b = {a % b}")
