import itertools as it
# policzymy ile bylo typw zdarzen w pliku txt
filepath = r'C:\Users\Filip Kwapień\PycharmProjects\pythonProject\Mobilo Python\Średniozaawansowany\data.txt'
data = []
with open(filepath) as file:
    for line in file:
        element = line.rstrip("\n").split(':')
        d = {'type': element[0], 'action' : element[1]}
        data.append(d)
print(data)
data = sorted(data,key=lambda x: x['type'])
for key, element in it.groupby(data,key = lambda x: x['type']):  # data to jakie dane ma przetworzyc  key to klucz, chcemy pogrupowac ze wzgledu na kolumne ze slownika wiec uzywamy lambda i okreslamy jaka kolumne chcemy wyciagnac
    print('The key is {} and the group is {}'.format(key,len(list(element))))







