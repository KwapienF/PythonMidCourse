import os
webadresses = []
line = input('Podaj adres www: ')
while line:
    webadresses.append(line)
    line = input('Podaj adres www: ')

dirname = os.getcwd()
filename = input('Podaj nazwe pliku: ')
filename2 = (filename +'.txt')
print('Twój plik to: ', filename2)
filepath = os.path.join(dirname,filename2)
print(filepath)
print(webadresses)
file = open(filepath, 'w')
for adress in webadresses:
    file.write(adress + '\n')

file.close()

# wyszkuj finderem plik stronki :)

zad 2
