def BuyMe(prefix = 'Im begging You',what = 'something nice'): # NIE MOZNA DAC PARAMETRU DOMYSLENGO TYLKO DLA PEIRWSZEGO ARGUMENTU MOZE TYLKO WARTOSC DOMYSLNA W POZNIEJSYCH ARGUMENTACH NIGDY PRZED
    print(prefix,what)

BuyMe('Please', 'new cat')

BuyMe(prefix = 'Please buy me', what = 'a car') # jak podasz  nazwe wartosci to nie musisz zachowywac kolejnosci
BuyMe( what = 'a car', prefix = 'Please buy me') # brak kolejnosci i dziala
# omijanie fragmentow
BuyMe('Please') # wtedty pobeirze wartosc domyslną
BuyMe(prefix = 'Please buy me')
BuyMe()
BuyMe(what = 'something sweet')

# LAB
def show_progress(how_many, character = '*',):
    print(character * how_many)

show_progress(5,'%')
show_progress(10)

