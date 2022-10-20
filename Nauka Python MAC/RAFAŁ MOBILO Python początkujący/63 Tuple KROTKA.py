# Tuple to statyczna lista. Tworzy sie je uzywając nawiasow () a nie [] jak w listach.
tax = (94,7,8,23)
print(tax)
# dzialają te same funkcje co w listach tylko ni emożna ich modyfikować jak listy można tylko odczytywac
print(max(tax))
# LIST(...)aby skonwertowac tuple na liste
taxList = list(tax)
print(taxList)
#TUPLE(...) i odwrotnie konwertowanie listy na krotke


# problem

a = 1
b = 10
print(a,b)
temp = a
a = b
b= temp
print(a,b)
#szybicej mozna stworzyc krotke i ja odwrocic
a = 1
b = 10
(a,b) = (b,a)
print(a,b)