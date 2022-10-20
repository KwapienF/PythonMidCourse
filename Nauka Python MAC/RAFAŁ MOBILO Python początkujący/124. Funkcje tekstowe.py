line = 'this IS a very STRANGE text.'
print(line.capitalize()) # pomieszany tekst zostanie sprowadzony do poprawnej wersji czyli pierwsza litera duza.
print(line.title()) # kazde slowo od wielkiej litery
print(line.upper()) # or lower wiadomo
print(line.swapcase()) # duza na malą a małą na dużą
print(line.casefold()) # zmienai na male ale bardziej agresywanie np szafeses z niemeickiego zmieni na małe s a lowe nie
print(line.count('e')) # ile w teksie jest literek e
print(line.find('e')) # na ktorym miejsu od lewej jest ltiera e
print(line.rfind('e')) # na ktorym miejsu od PRAWEJ jest ltiera e
print(line.index('e')) # tak ja k find mozna tez rindex od prawej index rozni sie tym ze zwroci blad jak szukamy literki ktorej nie ma a find pokaze -1
print(line.find('p'))


# mozna syzbo tez logicznie znalexc operatorem in
print('e' in line)
print(line.startswith('thi'))
# jak znalexc entery? szukamy '\n'
line3 = """asdsadsd
        sdsdsdsd"""
print(line3)
print(line3.count('\n'))
# moduly string
import string
print(string.ascii_letters) # pokauzje znaki asciii litery
print(string.digits) # wyswietli liczby
print(line.split(' ')) # utworzy liste eodzielna przez space
list = line.split(' ')
# JOIN dolącza nam cos do stringa
a = 'FILIP'.join('FILIP')
print(a)
b = ' '.join(list) # połaczy wszystkie elementy listy spacją
print(b)
print('---'.join(list))

# LAB
poem = '''1.Runą i w łunach spłoną pożarnych 
Krzyże kościołów, krzyże ofiarne 
I w bezpowrotnym zgubi się szlaku 
W lechickiej ziemi Orzeł Polaków. 
2.O, jasne słońce- wodzu Stalinie! 
Niech sława twoja nigdy nie zginie 
Niechaj jak orły powiedzie z gniazda 
Rosja i z Kremla płonąca gwiazda. 
3.Na ziemskim globie flagi czerwone 
Będą na wiatrach grały jak dzwony 
Czerwona Armia i wódz jej Stalin 
Odwiecznych wrogów na zawsze obali! 
4.Zaćmisz się rychło w czarnej godzinie 
Polsko- Twe córy i syny, 
Wiara i każdy krzyż na mogile, 
U stóp am legą w prochu i pyle! '''

line4 = poem.split('\n')
print(line4)
a= 0
b = 8
for i in range (8):
    print(line4[a])
    print(line4[b])
    a += 1
    b += 1
print('-------------------------------------------------')

for d in range(8):
    print(line4[d])
    print(line4[d+8])

