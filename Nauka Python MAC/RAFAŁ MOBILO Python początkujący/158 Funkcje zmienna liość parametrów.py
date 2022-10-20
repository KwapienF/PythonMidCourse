def DoACtion(action, parameter):
    print('action: ',action)
    print('parameter', parameter)
    return

DoACtion('buy', 'schoes')

# a jak chce wprowadzac ile chce parametrow np dla aki buy nie tylko buty ale tez skarpety itd?

def DoACtion2(action, *parameter): # gwiazdka daje nam tuple kolekcje elementów
    print('action: ',action)
    print('parameter', parameter)
    for element in parameter: # tworzy liste do kupienia
        print('element is ', element)
    return

DoACtion2('buy', 'schoes', 'socks')

def DoACtion3(action, what, **parameter): # gwiazdka daje nam tuple kolekcje elementów # ** stworza nie tuple a SLOWNIK! :) i wtedy bedzie mozna opsiac dla parametru jego podparametry np kup buty czerwone sportowe rozmiar 42 its
    print('action: ',action)
    print( 'what:', what)
    print('parameter', parameter)
    for element in parameter: # tworzy liste do kupienia
        print(element, '=', parameter[element])
    return

DoACtion3('buy', 'schoes', size=42, color = 'red', type = 'casual')