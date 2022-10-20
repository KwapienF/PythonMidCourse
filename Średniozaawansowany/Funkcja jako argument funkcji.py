def Bake(what):
    print('Baking ', what)
def Add(what):
    print('Adding ', what)
def Mix(what):
    print('Mixing ', what)

cookbook = [(Add, 'milk'),(Add, 'eggs'), (Add, 'flour'), (Add, 'sugar'), (Mix, 'ingredients'), (Bake, 'cookies')]

for activity,obj in cookbook:
    activity(obj)
# inna metoda za pomoca funkcji
print('-'*50)
def Cook(activity,obj):
    activity(obj)
Cook(Bake,'Brownies')

for a,o in cookbook:
    Cook(a,o)
#LAB
print('LAB '*40)

def double(x):
    return 2 * x
def square(x):
    return x ** 2
def negative(x):
    return -x
def div2(x):
    return x / 2

def generate_values(func,values_list): # funkcja oblicza dla danej listy licz wartosci funkcji
    table = []
    for i in values_list:
        table.append(func(i))
    print(table)

generate_values(double,[1,2,3,4])
print('-'*40)
x_table = list(range(11))

print(generate_values(double, x_table))
print(generate_values(square, x_table))
print(generate_values(negative, x_table))
print(generate_values(div2, x_table))