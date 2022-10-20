file = open(r'C:\Users\Filip Kwapień\PycharmProjects\pythonProject\Mobilo Python\Średniozaawansowany\data.txt')
data = file.read()
file.close()

for line in data.splitlines():
    if line.startswith('ACTION'):
        print(line)
# powyszy przyklad jest zly bo wczytujemy naraz caly plik jakby mial iles GB to bylby problem ponizej lepsze rozwiazanie
print('-'*50)
file = open(r'C:\Users\Filip Kwapień\PycharmProjects\pythonProject\Mobilo Python\Średniozaawansowany\data.txt')

for line in file:
    if line.startswith('ACTION'):
        print(line)
file.close()
print('-'*50)
# inaczej jeszcze rozdzielamy dwukropkiem  w obiekt tuple
file = open(r'C:\Users\Filip Kwapień\PycharmProjects\pythonProject\Mobilo Python\Średniozaawansowany\data.txt')
records = []
for line in file:
    if ':' in line:
        type, action = line.rstrip('\n').split(':',1) # rstrip wywali nam wszystkie entery
        record = (type,action)
        records.append(record)
print(records) # lista skladajaca sie  z tuple

file.close()
print('-'*50)
# piszemy generator
def get_records(filepath):
    print('opening file')
    file = open(r'C:\Users\Filip Kwapień\PycharmProjects\pythonProject\Mobilo Python\Średniozaawansowany\data.txt')
    for line in file:
        type, action = line.rstrip('\n').split(':', 1)  # rstrip wywali nam wszystkie entery
        record = (type, action)
        yield record

    print('closing file')
    file.close()
# tu nie wczytujemy calosci danych tylko wczytujemy po jednym elemecnie wyzej append stworzylo znowu duzy element do wczytania naraz
for record in get_records(r'C:\Users\Filip Kwapień\PycharmProjects\pythonProject\Mobilo Python\Średniozaawansowany\data.txt'):
    print('Type is {} and action is: {}'.format(record[0],record[1]))
