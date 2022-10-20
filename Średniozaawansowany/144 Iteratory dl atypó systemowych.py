aTuple = (1,2,3,4,5)

# for x in aTuple:
#     print(x)
# print('-'*50)
# it = iter(aTuple)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

foraList = [1,2,3,4,5] # tak smao mozna jak z krotką  zrobic z niej iterator aby dzialalo next

# teraz zbior
aSet={1,2,(3,4),'another number',3,4,'Something'} # tez jest iterrabel ale nie dzialal next # set to kolejnsco zwraancyh elelemtnow zostanie zmieniona
for x in aSet:
    print(x)

it = iter(aSet)
print(next(it))

with open(r'C:\temp\lines.txt','r') as file: # zawartos cpliku jest iterable a dodatkowo plik tekstowy posiada swoj wlasny iterator czyli file posiada metode iter next
    for line in file:
        print(line)
    while True:
        try:
            print(next(file))
        except StopIteration:
            break


