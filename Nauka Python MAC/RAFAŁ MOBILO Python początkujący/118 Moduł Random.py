import random
print(random.randint(1,100))
print(random.choice((range(1,100)))) # = random.randrange
print(random.randrange(1,100))
list = [1,2,3,4,5]
random.shuffle(list)
print(list)
countries = [
    'Uruguay',
    'Russia',
    'Saudi Arabia',
    'Egypt',
    'Spain',
    'Portugal',
    'Iran',
    'Morocco',
    'France',
    'Denmark',
    'Peru',
    'Australia',
    'Croatia',
    'Argentina',
    'Nigeria',
    'Iceland',
    'Brazil',
    'Switzerland',
    'Serbia',
    'Costa Rica',
    'Sweden',
    'Mexico',
    'Korea Republic',
    'Germany',
    'Belgium',
    'England',
    'Tunisia',
    'Panama',
    'Colombia',
    'Japan',
    'Senegal',
    'Poland'
    ]
random.shuffle(countries)
groupNumber = 0
for i in range(len(countries)):
    if i % 4 == 0:
        groupNumber +=1
        print("========== Group %d ==========" % (groupNumber))
    print(countries[i])












