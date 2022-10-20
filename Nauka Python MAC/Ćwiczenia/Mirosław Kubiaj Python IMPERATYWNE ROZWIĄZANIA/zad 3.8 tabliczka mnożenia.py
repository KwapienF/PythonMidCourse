i = 1
x = 1
for i in range(1,10):
    for x in range (1,101):
        a = x * i
        print(f"{i} * {x} = {a}", sep = "\n")
    i += 1

print("inny sposób")
n = 10
for wiersze in range(n):
    for kolumny in range(n):
        print((wiersze + 1) * (kolumny +1), "\t", end = "")
    print()
