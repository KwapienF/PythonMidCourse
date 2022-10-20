tab = [8, 2, 1, 9, 5] # deklaracja tablicy
print(tab)

i = 0
while i < len(tab) - 1: #W sortowaniu zawsze petla wykona jeden krok mniej niz liczba argumentow
    j = 0
    while j < len(tab) -1:
        if tab[j]  > tab[j+1]:
            tab[j], tab[j+1] = tab[j+1], tab [j]
        j += 1
    i += 1
    print(tab)

# skrócone działanie
print("-------")
i = 0
while i < len(tab) - 1: #W sortowaniu zawsze petla wykona jeden krok mniej niz liczba argumentow
    j = 0
    while j < len(tab) -1 - i:
        if tab[j]  > tab[j+1]:
            tab[j], tab[j+1] = tab[j+1], tab[j]
        j += 1
    i += 1
    print(tab)

    # jeszcze lepsza optymalizacja

print("-------")
zamieniono = True # zrobienie flagi
i = 0
while i < len(tab) - 1 and zamieniono: #W sortowaniu zawsze petla wykona jeden krok mniej niz liczba argumentow
    j = 0
    zamieniono = False
    while j < len(tab) -1 - i:
        if tab[j]  > tab[j+1]:
            tab[j], tab[j+1] = tab[j+1], tab [j]
            zamieniono = True
        j += 1
    i += 1
    print(tab)