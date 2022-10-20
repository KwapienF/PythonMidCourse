# /Users/filipkwapien/PycharmProjects/pythonProject2/venv/Nauka Python/RAFAŁ MOBILO Python początkujący/stronki.txt
import os
filename = os.path.abspath('stronki.txt')
print(filename)
webadresses = []
file = open(filename, 'r')
for line in file:
    line = line.replace('\n', '')
    webadresses.append(line)
    if line.endswith('.pl'):
        print("Polska strona")
    else:
        print('strona zagraniczna')

file.close()
print(webadresses)