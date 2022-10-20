def descending_order(num):
    num = str(num)
    n = len(num)
    i = 0
    lista = []
    while i <= (n - 1):
        lista.append(num[i])
        i += 1
    lista.sort()
    lista.reverse()
    return int(("".join(lista)))
print(descending_order(69085))

# zmiana liczby na tekst sortowanie jej cyfr i wyrzucenie ponownie jako posortowanej liczby