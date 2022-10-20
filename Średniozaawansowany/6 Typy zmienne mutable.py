number = 10
print('Variable number: ', number, id(number))
number += 2
print('Variable number: ', number, id(number)) # winnych jezykach programowanie zmienaicjac wartosc zmiennej zmienia ją i zapsiuje w tym samym miejscu pamieci
# python przy zmianie zmiennej zapisuje ja jako nowa o tej samej nazwie w nowym miejscu pamieci
#immutable = zmienna ktora jest niezmienna

text = 'Africa'
print(text, id(text))
text += ' is hot'
print(text, id(text))

list = [1,2,3]
print(list,id(list))
list.append(4)
print(list,id(list))

# lista jest mutable zmienna ktora mozna zmieniac id zostanie ten sam

list2 = list
print(id(list), id(list2))
list2.append(5)
print(list,id(list))
print(id(list), id(list2))
print(list,list2)

#dodajac cos do listy 2  dodal sie do tez list mimo ze append dotyczyl tylko list2, dlatego ze list i list2 wskazywaly ten sam obszar w pamieci
# aby utworzyc kopie listy i cos na niej podzialalc i wrocic do oryginnaje aby dzialac dalej juz na oryginalnej to trzeba kopie zrobic w wsposob ponizej:
list3 = list.copy()
print(list, list3)
list3.append(6)
print(list, list3) # juz lista 3 ma 6 a list nie ma tej 6 czyli mozna dziala na prawdziwej kopii

# lab
days = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
workdays = days.copy()
workdays.reverse()
del workdays[0:2] # lub workdays.remove('sat') workdays.remove('sun')
workdays.reverse()
print(days,'\n', workdays)
