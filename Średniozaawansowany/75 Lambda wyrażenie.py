# lambda pozwlaa zapsiac funkce w bardzo prosty sposob

def double(x):
    return x*2

x=10
x = double(x)
print(x)


x = 10
f = lambda x: x*2  # funkcja anonimowa
print(f(x))

def power(x,y):
    return x**y

x = 5
y = 5
print(power(x,y))

f2 = lambda x,y: x**y
print(f2(x,y))

list_numbers = [1,2,3,4,11,14,15,21]
# funkcja filter filtruje nam przyjmuej 2 argiment

def is_odd(x):
    return x % 2 !=0

print(is_odd(7),is_odd(4))

filtered_list = list(filter(is_odd,list_numbers)) # funkcje filter trzeba skonwertowac np do listy i przefiltrowala nam pod katem funkcji na nieparzyste
print(filtered_list)


# krócej

filtered_list_lambda = list(filter(lambda x: x%2 == 0,list_numbers)) # lambda wyrazenie funkcyjne anonimowe bez nazwy
print(filtered_list_lambda)

# dlaczego pythonowcy lubia lambda? bo jest jedna linijka kodu gdzie lacze kilka funkcji:

print(list(filter(lambda x: x%2 != 0,list_numbers)))

def generate_multiply_function(n):
    return lambda x: n*x
null2 = generate_multiply_function(2)
null3 = generate_multiply_function(3)

print(null2(13))
print(null3(8))

# LAB
print('LAB' * 40)

text_list = ['x','xxx','xxxxx','xxxxxxx','']
f = lambda x:  len(x)

print(f('Filip'))
# funkcja map pozwala uruchomic wskazana funkcja wszystkie elementy listy
print(list(map(f,text_list)))
print(list(map(lambda x: len(x),text_list)))


