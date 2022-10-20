def ciekawostka():
    a = 1
    b = 1
    ile = 0
    for a in range (1, 1000):
        for b in range (1,1000):
            c = a ** 2 + b ** 2
            if 1000 <= c <= 9999:
                if str(a) + str(b) == str(c):
                    ile+= 1
                    print(f" a = {a} i b = {b} daje c = {c}")
                    print("Liczb spełniających tę zależność jest: ", ile)
    print("Koniec obliczeń")

ciekawostka()

# szybsze obliczenia:
for i in range(1000, 10000,1):
    a = i // 100
    b = i % 100
    if a*a + b*b == i:
        print(i)


