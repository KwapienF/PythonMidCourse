myvar = "hello"
myvar2 = myvar + '!!'
print(myvar)
print(myvar2)
print(type(myvar) is type(myvar2))
print(myvar is myvar2)
print(id(myvar), id(myvar2)) # te same ma id bo myvar 2 odnosi sie do jednej zmiennej na ktora jest jedno miejsce w pamieci
myvar2 = myvar2[:-2] # ze zmeinnej marvy2 robimy wszsytkie literki z pomienieciem 2 ostatnich znaków
print(myvar)
print(myvar2)
print(myvar == myvar2) # tutaj czy tak samo wygladaja
print(myvar is myvar2) # ozancza ze sa to dwa rozne obiekty w pameici ale  przypadkowo maja taka sama zawartosc
print(id(myvar), id(myvar2))

# dzieki id mozemy stwierdzic czy dwie zmeinne to te same zmienne czy dwie rozne w pamieci