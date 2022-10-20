# exec robi wszystko podobnie jak eval ale eval tylko operacje na zmiennych a exec wszystko nawet typy logiczne  przyrównainia petle itd
var_x = 10
source = 'var_x = 4'
result = exec(source)
print(result) # tu eval wywali blad
print(var_x)

#exec przyjmie wiele linijek tekstu a eval tylko jedna

source2 = '''
for i in range(10):
    print(i)

'''
result2 = exec(source2)
print(result2)