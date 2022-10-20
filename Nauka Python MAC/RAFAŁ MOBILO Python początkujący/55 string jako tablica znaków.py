s = "A Python script"
print(type(s))
print(s[0:5]) # wydrukuje 5 znakow  z napisu od 0 do 5 z pominiecie 0 1 2 3 4 A _ P y t
print(s[:8]) # pokaze wszystkie znaki do 8
print(s[8:]) # pokaze wszystkie znaki od 8 do konca
message = 'Document "cv.doc" was printed o printer: XEROX'
print(message)
print(message[message.find(':')+2:])
m = message[message.find('"')+1:]
print(m[:m.find('"')])

print(message[message.find('"')+1:][:message[message.find('"')+1:].find('"')])

