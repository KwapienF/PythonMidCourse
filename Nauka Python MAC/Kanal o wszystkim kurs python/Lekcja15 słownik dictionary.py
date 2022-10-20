slownik = {1: "Poniedziałek",2: "Wtorek", 7: "Niedziela"}  #liste w kwadratowych a dictionary w klamrach słownik dane wpisujemy parami  klcuz wartosc klucz wartosc itd
# key: "value"
print(slownik) # do odwoloania sie po indeksie uzywamy juz nawiasow kwadratowych
print(slownik[2])
slownik[3] = "Środa" # tak mozna dodac element do slownika stworzyc indeks i przypisac wartość
slownik[4] = False  # slownik moze posaidac rozne typt  int string lub false true itd czyli boolean typ logiczny
slownik[5] = 5
slownik["a"] = 1  # indeks moze byc rowniez stringiem itd a nie tylko liczbą
print(slownik)
#print(slownik[8]) wygeneruje blad  bo nie ma tego idneksu w slowniku
print(slownik.get(8, "inny dzień")) #funckaj get odajduje indeks ktorych chcesz i jesli go nie ma to  zwraca to co zapiszesz po przecinku
# get jednorazowo w meijsce indeksu wstawi to co chcesz ale nie przypsize tego na stałę
print(slownik.get(7, "inny dzień"))

# wydrukowanie wszystkich elementow słownika jeden pod rugim
print(slownik)
for l in slownik.values(): # petla for iteruje po kluczach domyslnie aby wartosc pokazala trzeba dac metode values() dla kluczy keys()
    print(l)
# druga opcja:
print("Druga opcja")
for l in slownik:
    print(slownik[l])
print("wyswietlenie i klucza i wartosci:")
for k, v in slownik.items():
    print(k, v)

    #usuwanie ze slownika

print(slownik.pop(1))   # funkcja pop usuwa nam indeks podany w nawiasie
print(slownik)  # i tu juz brak poniedzialku