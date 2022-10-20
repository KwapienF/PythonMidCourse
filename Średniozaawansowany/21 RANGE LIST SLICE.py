for i in range(1,6,2): # 2 mowi jak obliczac co ile s
    print(i)
for a in range(6,0,-2): # trzeba dac minus by szedl w druga strone
    print(a)

list0 = range(10) # lista nie jest listą jest rangem typ to range a nie lsita
print('list = ',list0,type(list0))
list1 = list(range(10)) # konwertujemy range na liste
print('list = ',list1,type(list))

# slicing czyli wykrojenie krojenie na plasterki na czeci:

print(list1[5:7]) # drukowanie czesci listy np od 5 do konca to[5:]
print(list1[:len(list1)-1]) # do przedostatneigo mozna prosciej jak nizej
print(list1[:-1]) # -1 do przedostatenigo dasz to -2 opusic dwa ostatnei itd
print(list1[:8:2]) # :2 oznacza co drugi element w petli for tez tak mozna ale po przecinku, nie : dwukropku
print(list1[-1:2:-1]) # -1:0 od konca do poczatku i cofamy sie o 1
#odwrocenie listy:
print(list1[-1::-1])
# tworzenie kopii listy za pomocą operatora slice zamist list1.copy() tak aby byla w nowym iejscu pamieci mutable:
list2 = list1[:]
print(list2, id(list2),'\n',list1,id(list1))
print(list1[-2:])
