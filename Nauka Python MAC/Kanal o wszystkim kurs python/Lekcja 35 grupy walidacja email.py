import re

# def email():
#     print("Utwórz hasło składajace się conajmniej z 8 znaków, cyfr i jednej dużej litery, bez znaków specjalnych")
#     haslo = input(r"Podaj Hasło: ")
#     if re.search("^[A-Z]{1,}[a-z]+[0-9]+$",haslo):
#         print("Hasło poprawne")
#     else:
#         print("Hasło niepoprawne")
# email()
# uzyejmy grupy aby nie pozwolic na powtarzanie sie słów
wynik = re.match(r"^((?:He)(?P<first>ll)o)( World)+(!|\.)$", "Hello World!") # tworzymy grupy znaków w nawiasach
#  nazywamy grupy komenda ?P<> w nawiasach ostrych nazwe grupy
# mozna uzyc (?:tekst) tworzymy grupe ukrytą, która niemiesza nam indeksów i nie wpływ ana numerowanie indeksów. nie jest indeksowana
# !|\. wykrzyknik lub kropka ma być  backslash aby kropka byla intepretowanan jako kropa zwykla
if wynik:
    print("Dopasowano")
    print(wynik.group())
    print(wynik.group(0)) # idneks zero  drukuje całość
    print(wynik.group(1)) # 1 to nasza grupa zdefiniowananwewnatrz nawiasami
    print(wynik.groups()) # zwraca wszystkie grupy bez podawania indeksu
    print(wynik.group("first"))

else:
    print("Nie dopasowano")


    # walidacja adresu email
if re.match(r"^([A-Za-z0-9]+|[A-Za-z0-9][A-Za-z0-9-\.]+[A-Za-z0-9])@([A-Za-z0-9]+|[A-Za-z0-9][A-Za-z0-9-\.]+[A-Za-z0-9])\.[A-Za-z0-9]+$", "filipalv@o2.pl"):
    print("Dopasowano email")

else:
    print("Nie dopasowano email")



if re.match(r"^(\([0-9]{3,3})\)([ ])[0-9]{3,3}([-])[0-9]{4,4}$", "(123) 456-7890"):
    print("Numer poprawny")
else:
    print("Zły numer")
