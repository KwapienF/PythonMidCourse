number = [1]
print(number)
for i in range(5):
    newNumber = [1]
    position = 0
    while position < len(number) -1:
        newNumber.append(number[position]+number[position+1])
        position += 1
    newNumber.append(1)
    number = newNumber.copy()
    print(number)


list = [1]
print(list)
for num in range(5):
    i = 0
    list2 = [1]
    while i < len(list)-1:
        list2.append(list[i]+list[i+1])
        i+=1
    list2.append(1)
    list = list2.copy()
    print(list2)