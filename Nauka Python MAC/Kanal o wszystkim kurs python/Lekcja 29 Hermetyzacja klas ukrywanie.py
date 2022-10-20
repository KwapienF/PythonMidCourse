class Test:
    _lista = []  # pojedyncze podkresle sprawi ze lista jest  prywatna ale to nie dziala do konca tylko wskauzje aby tego nie modyfikowac
    # można do listy dodac jeszcze podloge aby byly 2 i wtedy bardziej to ochroni od modyfikowania
    def dodaj(self, arg1):
        self._lista.append(arg1)

    def zdejmij(self):
        if len(self._lista) > 0:
            return self._lista.pop(len(self._lista) - 1)    # pop zdejmuje elementy z listy po indeksie
        else:
            return
obj = Test()
obj.dodaj("A")
obj.dodaj("B")
obj.dodaj("C")
print(obj._lista)
print(obj.zdejmij()) # zdjelo osttni argument B
print(obj._lista)
obj._lista.append("X") # chcemy aby bylo prywatne i nie mozna bylo dodawac dolisty poza klasa  elementow
# naprawimy to jednym slowem:
print(obj._lista)