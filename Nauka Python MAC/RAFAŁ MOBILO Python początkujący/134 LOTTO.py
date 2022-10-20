import random
myNumbers = []
while len(myNumbers) < 7:
    newNumber = random.randint(1,49)
    if newNumber in myNumbers:
        print("eliminated", newNumber)
        continue

    myNumbers.append(newNumber)
print(myNumbers)