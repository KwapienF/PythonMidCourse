def dzialanie(n):
    s = 1
    for a in range (2,n+1):
        if a % 2 == 0:
            s = s + a
        else:
            s = s - a
    print(s)
def main():
    n = 5
    dzialanie(n)
main()