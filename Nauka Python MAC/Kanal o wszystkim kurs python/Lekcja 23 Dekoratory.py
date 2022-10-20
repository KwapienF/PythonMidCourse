def decorator(func):  #argumentem bedzie inna funkcja
    def wrapper():  # wrapper - obwiednia otoczka funka wrappe bedzie opakowywala nam inna funkaj jeszcze inna funkcje
        print("---------")
        func()
        print("---------")
    return wrapper  # bez nawiasow na koncu bo chcemy zwrocic nowa postac funkci wrapper a nie ja wywolywac


# teraz definiujmy funkcje ktora cchemy ozdboic udekorowac wiec ja wysylamy do dekoratora ktory jakas inna funkcja nam ja ozdabia np wrapper
def hello():
    print("Hello World")
hello =  decorator(hello)
hello()
print("xxxxxxxxxxxxxxxxxxxxxx")
@decorator  # jesli jakąś  funckje chcemy udekorowac to szybszy spsoob zamiast jak wyzej przypisywac
def witaj():
    print("Witaj świecie")
witaj()

