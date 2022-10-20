text = ''
number = 10
condition = True

while condition:
    if len(text) < number:
        text += 'x'
    else:
        condition = False
print(text)