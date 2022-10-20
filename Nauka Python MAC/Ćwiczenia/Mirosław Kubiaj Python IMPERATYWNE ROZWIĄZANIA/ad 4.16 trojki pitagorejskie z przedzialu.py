def trojka_pitagorjeska(n):
    for a in range(1,n):
        for b in range(a,n): # gdyby dac przedzial od 1,n  to wystapi permutacja tych samych trojek
            for c in range(b,n):
                if a*a + b*b == c*c:
                    print(a,b,c)
def main():
    n = int(input("podaj n: "))
    trojka_pitagorjeska(n)
main()





