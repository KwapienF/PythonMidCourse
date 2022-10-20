def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def wynik():
    for n in range(0,11):
        fib(n)
        print(fib(n), end = "\t")
wynik()
