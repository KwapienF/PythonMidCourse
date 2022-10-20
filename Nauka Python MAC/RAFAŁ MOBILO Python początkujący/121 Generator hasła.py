   # gnerator Hasła
# wyswietlenie tabeli ascii
#for i in range (32,127):
 #   print(i,chr(i))
import random
ints = range(33, 127)
print(ints)
password= ''
for i in range(8):
    password += chr(random.choice(ints))
print('password is: ',password)