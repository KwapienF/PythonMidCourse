import re # regular expretions wyrazenia regularne

wzor1 = r"banan\nbanan\tbanan"  # row - surowy. ignoruj znaki specjalne jak enter czy tab \n \t itd
wzor = r"banan"
tekst = r"wrozkabananjabłko"

print(re.match(wzor, tekst)) # match sprawdza dopasowanie none bo nie dopasowalo match dopasowuje tekst ktory zaczyna sie od danego wzory jak banan ejst w srodku to match nie znajdzie

if re.match(wzor, tekst):
    print("Dopasowano!")
else:
    print("Nie dopasowano.")
# aby match znalazlo cos w srodku:
if re.match(r".*" + wzor + r".*",  tekst):  # teraz sprawdzi wszedzie w leckji 33 wyjasnienie tych znakow specjalnych
    print("Dopasowano!")
else:
    print("Nie dopasowano.")

if re.search(wzor, tekst): # serach niezaleznie od pozycji szuka wszedzie w tekscie danych slow
    print("Znaleziono")
else:
    print("Nie znaleziono")

print(re.findall(wzor, tekst)) # funkcja findall znajduje wszystkie dopasowania i zwraca w  postacji zwyklej list
print(len((re.findall(wzor, tekst))))

dopasowanie = re.search(wzor, tekst) # robimy teraz obiekt
if dopasowanie:
    print(dopasowanie.group()) # metoda group wskauzje wszystkie grupy ktore udalo sie znalezx
    print(dopasowanie.start()) #metoda start poakzuej gdzie zaczyna sie slowo indeks
    print(dopasowanie.end())  # metoda end pokauzje indeks gdzie dopasowanie sie konczy
    print(dopasowanie.span())  # metoda span zwraca krotke poczatka i konca

tekst2 = re.sub(wzor, r"jagoda", tekst )  # sub sluzy do zamiany banana na jagode w danym tekscie
print(tekst2)