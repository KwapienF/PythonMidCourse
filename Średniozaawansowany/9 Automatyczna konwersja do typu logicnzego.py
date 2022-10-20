isOK = True
print('Variable isOK: ', isOK, type(isOK))
if isOK:
    print('True')

isOK = '' # napis pusty zostanie zinterpretowany jako FAŁSZ i if si enie wykoan cokolwiek wpsizesz jednak w '' to bedzie wtedy jako TRUE zinterpretowane
print('Variable isOK: ', isOK, type(isOK))
if isOK:
    print('True')

    #napis pusty to FALSZ a nieousty to prawda

isOK = 1 # liczba jakakolwiek nawet ujemna rozna od 0 to TRUE.
print('Variable isOK: ', isOK, type(isOK))
if isOK:
    print('True')
isOK = 0  # zinterpretuj ot jako FALSZ
print('Variable isOK: ', isOK, type(isOK))
if isOK:
    print('True')
# dla pythona jak cos jest to jest TRUE jak nic nie ma to FALSZ
isOK = [1,2,3] #true
print('Variable isOK: ', isOK, type(isOK))
if isOK:
    print('True')
isOK = [] # faslz
print('Variable isOK: ', isOK, type(isOK))
if isOK:
    print('True')
isOK = [0,0,0] # mimo ze zerao to true bo lista nie jest pusta chyab ze odowlay sie do elemntu isOK[0] ti bedzie falsz bo dla 0 jest falsz
print('Variable isOK: ', isOK, type(isOK))
if isOK:
    print('True')

# mozna np sprawdzac tak czy doszlo do bledow jak beda bledy w liscie to wywali true
