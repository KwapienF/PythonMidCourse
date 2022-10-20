number = [1]
line = ''
width = 100
height = 10
for n in number:
    line += "%5d" % (n)
    print(line.center(width)) # funkcja wyrownania do środka a w nawiasie na ilu znakach ma byc wycentorwane
for i in range(height):
    newNumber = [1]
    position = 0
    while position < len(number) -1:
        newNumber.append(number[position]+number[position+1])
        position += 1
    newNumber.append(1)
    number = newNumber.copy()

    line = ''
    for n in number:
        line += "%5d" % (n)
    print(line.center(width))
