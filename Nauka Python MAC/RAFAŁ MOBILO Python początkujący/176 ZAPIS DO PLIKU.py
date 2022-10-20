filename = '/Users/filipkwapien/Documents/PROGRAMOWANIE/Python/tworzenieplikow/output.txt'
line = 'Europe'
cities = ['London','Baerlin','Paris','Warsaw','Madrid', 'Rome']
file = open(filename, 'w') # w aby write zapisywac za kazdym uruchomienem programu w spowoduje ze bedzie toc owczesniej nadpisywane na nowo. mozna
# dac literke 'a' zamiast 'w' i wtedy bedzie dodawalo do tekstu przy kazdym nowym uruchomieniu programu
file.write(line) # .write() zapisuje do  pliku  mozna tez 'w+' czyli mamy plik do zapisu i do odczytu tylko i mozna dawac 'a+' aby moc zapisywac dodawac i odczytywac
file.write('\n')
#file.writelines(cities) # pozwoli nam dopisac liste do pliku

for line in cities:
    file.write(line + '\n')


file.close()