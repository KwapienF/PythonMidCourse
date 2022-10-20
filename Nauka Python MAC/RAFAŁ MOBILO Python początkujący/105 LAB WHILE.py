x = 20730906
x = str(x)
list = []
i = 0
print(len(x))
while i <= (len(x)-1):
    list.append(int(x[i]))
    i +=1
print(list)

sum = 0
for number in list:
    sum += number
print(sum)

# inny sposob
x2 = 20730906
x2 = str(x2)
c = int(len(x2))
x2 = int(x2)
a = 0
sum2 = 0

while a < c:
     num = x2 % 10
     sum2 += num
     a+= 1
     x2 = x2 // 10
print(sum2)

# zad 3
text = '''
United Space Alliance: This company provides major support to NASA for
various projects, such as the space shuttle. One of its projects is to
create Workflow Automation System (WAS), an application designed to
manage NASA and other third-party projects. The setup uses a central
Oracle database as a repository for information. Python was chosen over
languages such as Java and C++ because it provides dynamic typing and
pseudo-code–like syntax and it has an interpreter. The result is that
the application is developed faster, and unit testing each piece is easier.
'''

textList = text.replace('\n', ' ' ).split(' ')
print(textList)
shortWords = 0
longWords = 0
#print(len(textList))
for word in textList:
    if len(word) < 6:
        shortWords += 1
    else:
        longWords += 1
print(shortWords)
print(longWords)
print('---------------------------------------------------')

listOfWords = text.replace('\n', ' ').split(' ')
print(listOfWords)
print(len(listOfWords))
wordLength = 6
i = 0
shortWords = 0
longWords = 0
while i < len(listOfWords):
    if len(listOfWords[i]) > wordLength:
        longWords += 1
    else:
        shortWords += 1

    i += 1
print("Words shorter than ", wordLength, ":", shortWords)
print("Words longer than ", wordLength, ":", longWords)


