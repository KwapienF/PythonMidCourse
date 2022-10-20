class Human:  # definujemy klase tka jak np funckje def tutaj calss klasy zaczynamy z wielkiej litery aby pokazac ze jest czyms wiecej
    def __init__(self, name, age):  # tworzymy konstruktor
        self.name = name
        self.age = age #zamiast jak nizej globalnei definiujemy dal calej klasy
    # name = "Philip" # tworzymy zmienna  w klasie klasy pozwalaja nam na przechowywanie zbiorw zmiennych i funkcji
    # kiedy funkcja znajduje sie wewnatrz klasy to nazywamy to METODĄ, klasa moze byc wszystkim jak czlowiek mozna
    # miec na mysli kogokolwiej a obiekt to juz jest konkretny np mama jest obiektem bo wiadomo o kogo konkretnei
    # chodzi teraztworzymy metodą czyli funkcje wewnatrz klasy funkcja to jest to samo co metoda
    def introduce_yourself(self, welcome = "Hi"): # self to taki predefiniowany argument ktory zawsze jest a zaczynamu po przecinku definiowac argimentu
#self jest aliasem słówkiem dostepu do klasy w tym przypadku Human. self pozwala odwolac sie do tego co istnieje wewnatrz danej klasy
       # self.name = "Aneta" # dzieki self mozemy zmienic argument znajdujacy sie w caly obiekcie w calej klasie bez tego imie = aneta by nam nie zmienila zmiennej imie tylko utworzylo nowa zmienna wewnatrz funkcji
        #self mozna zmienc na co sie chce np def introduce_yourself(abc, arg2) i wtecy abc.imie = Aneta
        return welcome + " , my name is " + self.name + " and i'm " + str(self.age) +" years old" # self.age konwertujemy na stringa aby wyswietlio nam w zdaniu
object = Human("Aneta", 36) # tworzymy obiekt korzystajac z gotowego przepisu na wymodelwoanie postaci czlowiek nawiasy okragle sa dla konstruktora
print(object.name)
print(object.introduce_yourself("Witam")) # za argument drugi po self przypisalismy inne powitanie, self nie widac boto jest ukryty argument
object2 = Human("Filo", 32) # tworzymy nowy obiekt gdzie korzystamy z tej klasy i przypiszemy inne imie
#object2.name = "Lecia"
print(object2.introduce_yourself())

