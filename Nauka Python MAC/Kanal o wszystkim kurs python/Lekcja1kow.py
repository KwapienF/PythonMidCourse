for i in range(1000, 10000,1):
    a = i // 100
    b = i % 100
    if a*a + b*b == i:
        print(i)
