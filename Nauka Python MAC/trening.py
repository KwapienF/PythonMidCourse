import random
N = 5
tablica = [[0 for i in range(N)] for j in range(N)]
for i in range(N):
    for j in range(N):
        liczba = random.randint(1, 9)
        if i == j:
            tablica[i][j] = liczba
        else:
            tablica[i][j] = 0
for i in range(N):
    for j in range(N):
        print(tablica[i][j], " ", end="")  # wyświetla liste
    print()