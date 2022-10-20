def suma(n):
    s = 0
    for i in range (1,n+1):
        s = s + 2 * i - 1
    print(s)

def main():
    n = 100
    suma(n)
main()

